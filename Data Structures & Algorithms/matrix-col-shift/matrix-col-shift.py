Matrix = list[list[int]]

def mat_col_shift(mat: Matrix) -> int:
    """Returns minimum number of moves necessary to get ones in the same row"""
    one_positions = []

    for row in mat:
        for col, value in enumerate(row):
            if value == 1:
                one_positions.append(col)
                break

    if not one_positions:
        return 0

    one_positions.sort()
    median = one_positions[len(one_positions) // 2]
    return sum(abs(col - median) for col in one_positions)



if __name__ == "__main__":
    test_cases = [
        (
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            2,
        ),
        (
            [[0, 1, 0], [1, 0, 0], [0, 0, 1]],
            2,
        ),
        (
            [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
            2,
        ),
        (
            [[1], [1], [1]],
            0,
        ),
    ]

    for i, (mat, expected) in enumerate(test_cases, start=1):
        result = mat_col_shift(mat)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"

    print("All test cases passed.")
    
