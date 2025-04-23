def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []

    # Sort intervals based on the start value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_start, last_end = merged[-1]
        current_start, current_end = current

        if current_start <= last_end:
            # Overlap → merge
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append(current)

    return merged

def main():
    test_cases = [
    ([(1, 3), (2, 6), (8, 10), (15, 18)], [(1, 6), (8, 10), (15, 18)]),
    ([(1, 4), (4, 5)], [(1, 5)]),
    ([(5, 10), (1, 3), (2, 6), (15, 18)], [(1, 10), (15,18)]),
    ([(1, 2), (3, 4), (5, 6)], [(1, 2), (3, 4), (5, 6)]),
    ([(1, 10), (2, 3), (4, 8), (11, 12)], [(1, 10), (11,12)]),
    ([(-5, 0), (-3, 2), (1, 6), (8, 10), (9, 12)], [(-5, 6), (8, 12)]),
    ]
    for i, (input_data, expected_output) in enumerate(test_cases):
        result = merge_intervals(input_data)
        print(f"Test Case {i + 1}: ", "Passed" if result == expected_output else f"Failed - Got {result}, Expected {expected_output}")


if __name__ == "__main__":
    main()