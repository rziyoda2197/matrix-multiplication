def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matritsalar ko'paytirilishi mumkin emas")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def test_matrix_multiply():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    expected_result = [[19, 22], [43, 50]]
    assert matrix_multiply(A, B) == expected_result

def test_matrix_multiply_invalid():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8], [9, 10]]
    try:
        matrix_multiply(A, B)
        assert False, "ValueError kelishi kerak"
    except ValueError as e:
        assert str(e) == "Matritsalar ko'paytirilishi mumkin emas"
