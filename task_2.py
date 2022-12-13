# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами (получить кортеж):

# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

import random


def squre_def(A, B, C) -> tuple:
    print(f'коэффициент А={A}\n'
        f'коэффициент B={B}\n'
        f'коэффициент C={C}')
    D = B ** 2 - 4 * A * C
    print(f'Дискриминант= {D}')
    if D > 0:
        x1 = (-B + D ** 0.5) / (2 * A)
        x2 = (-B - D ** 0.5) / (2 * A)
        print(f'Корень x1= {x1}')
        print(f'Корень x2= {x2}')
        return (x1, x2)
    elif D == 0:
        x = -B / (2 * A)
        print(f'Корень x={x}')
        return (x,)
    return 'Корней нет'


print(squre_def(A=random.randint(1, 15),
    B=random.randint(1, 15),
    C=random.randint(1, 15)))