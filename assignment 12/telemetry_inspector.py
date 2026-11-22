"""
Program: The High-Throughput Telemetry Log Inspector
Author: Tanishka Hira
Date: 27-09-2026
A chunk boundary can occur in the middle of a telemetry record because
chunk_size specifies a number of bytes and is unrelated to line boundaries.
The leftover buffer stores the incomplete part of a line and combines it
with the next chunk. This ensures that only complete records are processed
and prevents split records from being incorrectly treated as malformed.

"""

import os
from typing import Tuple


def process_log_stream(file_path: str, chunk_size: int, /) -> Tuple[int, float]:
    """
    Reads a file in fixed-size byte chunks using a callable iterator.
    Returns total valid record count and running average value.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Target path '{file_path}' not found.")
    if isinstance(chunk_size, bool) or not isinstance(chunk_size, int):
        raise TypeError("chunk_size must be an integer.")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    valid_count = 0
    running_total = 0.0
    sentinel_seen = False
    leftover = b""

    def process_line(raw_line: bytes) -> None:
        """Validate one line and update the enclosing statistics."""
        nonlocal valid_count, running_total, sentinel_seen
        if raw_line.endswith(b"\r"):
            raw_line = raw_line[:-1]
        try:
            line = raw_line.decode("utf-8")
        except UnicodeDecodeError:
            return
        if line == "END_OF_LOG":
            sentinel_seen = True
            return
        fields = line.split(",")
        if len(fields) != 3:
            return
        try:
            value = float(fields[2])
        except ValueError:
            return
        valid_count += 1
        running_total += value

    with open(file_path, "rb") as file_obj:
        for chunk in iter(lambda: file_obj.read(chunk_size), b""):
            leftover += chunk
            *complete_lines, leftover = leftover.split(b"\n")
            for raw_line in complete_lines:
                process_line(raw_line)
        if leftover:
            process_line(leftover)

    if not sentinel_seen:
        print("Warning: END_OF_LOG not found; the file may be truncated.")
    mean_value = running_total / valid_count if valid_count else 0.0
    return valid_count, mean_value


def main() -> None:
    """Create a sample and compare results across eight chunk sizes."""
    sample_lines = [
        "2026-01-01T00:00:01,SENSOR_A,14.5",
        "2026-01-01T00:00:02,SENSOR_B,NaN_READING",
        "2026-01-01T00:00:03,SENSOR_C,",
        "2026-01-01T00:00:04,SENSOR_A,16.2",
        "2026-01-01T00:00:05,MALFORMED_ROW_TOO_FEW_FIELDS",
        "2026-01-01T00:00:06,SENSOR_B,15.0",
        "END_OF_LOG",
    ]
    sample_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "telemetry_sample.csv"
    )
    try:
        with open(sample_path, "x", encoding="utf-8", newline="") as file_obj:
            file_obj.write("\n".join(sample_lines))
    except FileExistsError:
        print(f"Using existing sample: {sample_path}")

    baseline = process_log_stream(sample_path, 1)
    for size in (1, 3, 7, 16, 32, 64, 128, 1000):
        result = process_log_stream(sample_path, size)
        print(f"chunk_size={size:4} -> {result}")
        assert result == baseline, "Results differ across chunk sizes."


if __name__ == "__main__":
    main()
