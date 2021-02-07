def tribonacci(signature, n):
    n1 = signature[0]
    n2 = signature[1]
    n3 = signature[2]

    if n <= 3:
        return(signature[:n])
    for i in range(0, n-3):
            sum = n1 + n2 + n3
            n1, n2 = n2, n3
            n3 = sum
            signature.append(n3)
    return(signature)

print(tribonacci([1, 1, 1], 10))

#Test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
#Test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])