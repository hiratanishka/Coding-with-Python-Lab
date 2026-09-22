"""
Coding for AI - Problem Set 9
Name: Tanishka Hira
Enrollment No: A26MTAI0001
Assignment: The Automated Meta-Package Inspector

Why use a property setter?
A check performed only inside __init__ validates target_path once, when the
object is created. A property setter validates the value every time the
attribute is assigned. Therefore, even if target_path is changed later, the
new value must still pass the same existence check before it is stored.
"""

import ast
import os
import re


class SourceAuditor:

    def __init__(self, target_path: str, /) -> None:
        self.target_path = target_path

    @property
    def target_path(self) -> str:
        return self._target_path

    @target_path.setter
    def target_path(self, value: str) -> None:
        if not os.path.exists(value):
            raise FileNotFoundError(
                f"Target path '{value}' does not exist."
            )

        self._target_path = value

    def audit_module_structure(
        self,
        file_contents: str,
        /,
        *,
        max_line_length: int = 79
    ) -> dict:
        """
        Parse source code and check the specified style rules.

        Returns a dictionary containing:
        - spacing_violations
        - line_length_violations
        - trailing_whitespace_violations
        - colon_spacing_violations
        """

        tree = ast.parse(file_contents)

        spacing_violations = []
        line_length_violations = []
        trailing_whitespace_violations = []
        colon_spacing_violations = []

        # ------------------------------------------------------------
        # Requirement 1: AST-based top-level function spacing
        # ------------------------------------------------------------

        top_level_functions = [
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
        ]

        for previous, current in zip(
            top_level_functions,
            top_level_functions[1:]
        ):
            previous_end = previous.end_lineno

            if current.decorator_list:
                current_start = current.decorator_list[0].lineno
            else:
                current_start = current.lineno

            blank_lines = current_start - previous_end - 1

            if blank_lines < 2:
                spacing_violations.append(current.name)

        # ------------------------------------------------------------
        # Requirement 2(i): Line length
        # ------------------------------------------------------------

        lines = file_contents.splitlines()

        for line_number, line in enumerate(lines, start=1):
            if len(line) > max_line_length:
                line_length_violations.append(line_number)

        # ------------------------------------------------------------
        # Requirement 2(ii): Trailing whitespace
        # ------------------------------------------------------------

        for line_number, line in enumerate(lines, start=1):

            # Ignore whitespace-only blank lines.
            if line.strip() and re.search(r"[ \t]+$", line):
                trailing_whitespace_violations.append(
                    line_number
                )

        # ------------------------------------------------------------
        # Requirement 2(iii): Type-annotation colon spacing
        # ------------------------------------------------------------

        def check_annotation_colon(
            annotation_node,
            line_number
        ):
            """Check that an annotation colon is followed by a space."""

            line = lines[line_number - 1]

            annotation_column = annotation_node.col_offset

            colon_position = line.rfind(
                ":",
                0,
                annotation_column
            )

            if colon_position == -1:
                return

            if (
                colon_position + 1 < len(line)
                and not line[colon_position + 1].isspace()
            ):
                colon_spacing_violations.append(
                    line_number
                )

        # Function argument annotations
        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                arguments = []

                arguments.extend(node.args.posonlyargs)
                arguments.extend(node.args.args)
                arguments.extend(node.args.kwonlyargs)

                if node.args.vararg is not None:
                    arguments.append(
                        node.args.vararg
                    )

                if node.args.kwarg is not None:
                    arguments.append(
                        node.args.kwarg
                    )

                for argument in arguments:

                    if argument.annotation is not None:
                        check_annotation_colon(
                            argument.annotation,
                            argument.annotation.lineno
                        )

            # Variable annotation:
            # value:str = "hello"
            elif isinstance(node, ast.AnnAssign):

                if node.annotation is not None:
                    check_annotation_colon(
                        node.annotation,
                        node.annotation.lineno
                    )

        # Remove duplicate line numbers.
        colon_spacing_violations = list(
            dict.fromkeys(
                colon_spacing_violations
            )
        )

        return {
            "spacing_violations":
                spacing_violations,

            "line_length_violations":
                line_length_violations,

            "trailing_whitespace_violations":
                trailing_whitespace_violations,

            "colon_spacing_violations":
                colon_spacing_violations,
        }

    # ------------------------------------------------------------
    # Requirement 3: Manifest and Distribution Validator
    # ------------------------------------------------------------

    def verify_sdist_layout(
        self,
        directory_path: str,
        /
    ) -> bool:
        """
        Verify the source-distribution package layout.

        Directory must contain:
        1. setup.py
        2. README.txt
        3. At least one module listed in py_modules
           that exists as a .py file.
        """

        if not os.path.isdir(directory_path):
            return False

        setup_path = os.path.join(
            directory_path,
            "setup.py"
        )

        readme_path = os.path.join(
            directory_path,
            "README.txt"
        )

        if not os.path.isfile(setup_path):
            return False

        if not os.path.isfile(readme_path):
            return False

        try:

            with open(
                setup_path,
                encoding="utf-8"
            ) as file:

                setup_contents = file.read()

            tree = ast.parse(
                setup_contents
            )

        except (OSError, SyntaxError):
            return False

        py_modules = []

        # Find:
        # setup(..., py_modules=["vsearch"])

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if (
                    isinstance(node.func, ast.Name)
                    and node.func.id == "setup"
                ):

                    for keyword in node.keywords:

                        if keyword.arg == "py_modules":

                            try:

                                modules = ast.literal_eval(
                                    keyword.value
                                )

                                if isinstance(modules, list):

                                    py_modules.extend(
                                        module
                                        for module in modules
                                        if isinstance(
                                            module,
                                            str
                                        )
                                    )

                            except (
                                ValueError,
                                TypeError
                            ):
                                return False

        if not py_modules:
            return False

        # At least one listed module must exist.
        for module_name in py_modules:

            module_path = os.path.join(
                directory_path,
                module_name + ".py"
            )

            if os.path.isfile(module_path):
                return True

        return False

# ------------------------------------------------------------
# Requirement 4: Self-Test
# ------------------------------------------------------------

if __name__ == "__main__":
    assert not SourceAuditor(
        __file__
    ).audit_module_structure(
        open(
            __file__,
            encoding="utf-8"
        ).read()
    )["spacing_violations"], (
        "Self-audit failed: spacing violations found."
    )

    print(
        "Self-audit passed: no top-level function spacing violations."
    )
