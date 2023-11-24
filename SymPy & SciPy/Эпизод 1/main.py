from sympy import symbols, Matrix

Lamda, miu, p = symbols('Lamda miu p')

B = Matrix([[0, 0, 0, -1/p, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1/p, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1/p, 0, 0, 0],
            [-(Lamda + 2 * miu), 0, 0, 0, 0, 0, 0, 0, 0],
            [0, -miu, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -miu, 0, 0, 0, 0, 0, 0],
            [-Lamda, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-Lamda, 0, 0, 0, 0, 0, 0, 0, 0]])

for i, val in enumerate(B.eigenvals()):
    print(f'Собственное значение №{i + 1}: {val}, кратность: {B.eigenvals()[val]}')
