def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
# Implement your solution here
    intervals.sort(key=lambda x: x[0])
    merge = [intervals[0]]
    for a, b in intervals:
        for i, (c, d) in enumerate(merge):
            if ((c >= a and c <= b) and d > b):
                merge[i] = (a, d)
                break
            elif ((c >= a and c <= b) and d <= b):
                break
            elif (c < a and (d >= a and d <= b)):
                merge[i] = (c, b)
                break
            elif (c < a and d > b):
                merge[i] = (c, d)
                break
            # If no overlaps with every element:
            elif (i == len(merge) - 1):
                merge.append((a, b))
            else: continue
    return merge

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
        try:
            result = merge_intervals(input_data)
            print(f"Test Case {i + 1}: ", "Passed" if result == expected_output else f"Failed - Got {result}, Expected {expected_output}")
        except Exception as e:
            print(f"Test Case {i + 1}: Error occurred: {e}")


if __name__ == "__main__":
    main()
