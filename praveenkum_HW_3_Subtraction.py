def subtract_integers(A, B):
    max_digits = max(len(A), len(B))
    result = [0] * max_digits
    borrow = 0

    for i in range(max_digits):
        digit_A = A[-(i + 1)] if i < len(A) else 0
        digit_B = B[-(i + 1)] if i < len(B) else 0

        diff = digit_A - digit_B - borrow

        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0

        result[max_digits - i - 1] = diff

    return result

# Example usage:
A = [1, 0, 0]
B = [1, 0 ]

result = subtract_integers(A, B)
print("Difference:", result)