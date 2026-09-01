'''
Assignment - Calibration synthesizer
Name - Tanishka Hira
Date - 31.08.2026
'''


calibration_feed = [
    [201, 6.0, 9.5, "IGNORE", 4.0],
    [],
    [202, 11.2, "FAULT", 7.8, 5.5],
    [203, 14.0, 3.5, 8.25],
    [204, 2.75, "HALT", 6.0]
]

feed_cursor = 0

total_valid_readings = 0
global_max = None
global_min = None
total_checksum = 0.0

emergency_stop = False


'''---Walrus-Controlled Outer Loop---'''

while (current_slice := calibration_feed[feed_cursor:feed_cursor + 1]):

    batch = current_slice[0]

    '''---Empty batch check---'''

    if not batch:
        print("Batch", feed_cursor, "is EMPTY. Proceeding.")
        feed_cursor += 1
        continue

    calibration_id = batch[0]

    print("Evaluating Batch", feed_cursor,
          "(ID:", calibration_id, ") ...")

    '''---Manually calculate batch length---'''

    reading_count = 0

    for x in batch:
        reading_count += 1

    '''---Batch-specific variables---'''

    batch_sum = 0.0

    '''---Manual Backward Traversal---'''

    for i in range(1, reading_count):

        target_index = reading_count - i
        reading = batch[target_index]

        if reading == "IGNORE":
            print("Signal IGNORE encountered at Batch", calibration_id)
            continue

        if reading == "FAULT":
            print("Signal FAULT detected. Suppressing batch", calibration_id)
            break

        if reading == "HALT":
            print("Signal HALT detected. Executing emergency protocol.")
            emergency_stop = True
            break

        batch_sum += reading
        total_valid_readings += 1

        '''---Global Maximum---'''

        if global_max is None:
            global_max = reading
        elif reading > global_max:
            global_max = reading

        '''---Global Minimum---'''

        if global_min is None:
            global_min = reading
        elif reading < global_min:
            global_min = reading

    else:

        if calibration_id % 2 == 0:
            batch_sum = batch_sum * 1.5
        else:
            batch_sum = batch_sum * 0.8

        total_checksum += batch_sum

    if emergency_stop:
        break

    feed_cursor += 1


print()
print("========================================")
print("CALIBRATION COMPLETE : EMERGENCY TERMINATION")
print("========================================")
print("Total Valid Readings Processed :", total_valid_readings)
print("Global Calibration Checksum :", total_checksum)
print("Maximum Reading Encountered :", global_max)
print("Minimum Reading Encountered :", global_min)
