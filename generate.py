def generate(numRows):
    triangle = [1]
    for n in range(1, numRows):
        new_row = [1]
        for i in range(n):
            if i == 0:
                continue
            p = triangle[n-1][i-1] + triangle[n-1][i]
            new_row.append(p)
        new_row.append(1)
        triangle.append(new_row)
    return triangle

print(generate(5))
print(generate(1))
