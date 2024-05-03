def add_integers(A, B):
    max_digits = max(len(A), len(B))
    result = [0] * (max_digits + 1)
    carry = 0

    for i in range(max_digits):
        digit_A = A[-(i + 1)] if i < len(A) else 0
        digit_B = B[-(i + 1)] if i < len(B) else 0

        _sum = digit_A + digit_B + carry
        result[max_digits - i] = _sum % 10
        carry = _sum // 10

    if carry > 0:
        result[0] = carry

    return result

# Example usage:
A = [1, 3, 2]
B = [1, 0]

result = add_integers(A, B)
print("Sum:", result)

