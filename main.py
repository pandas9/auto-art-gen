import random

import operator
import math
import matplotlib.pyplot as plt

from samila import GenerativeImage, Projection, VALID_COLORS

import os
import sys

class Generate:
    def __init__(self, num_pieces, bg_color="black"):
        projections = [ Projection.POLAR, Projection.AITOFF, Projection.LAMBERT, Projection.MOLLWEIDE ]
        func = self.algo_functions()

        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(f'{self.dir_path}/output', exist_ok=True)

        for i in range(num_pieces):
            self.g = GenerativeImage(func, func)
            self.g.generate()
            self.g.plot(color=random.choice(VALID_COLORS), bgcolor=bg_color, projection=random.choice(projections))
            self.save(i +1)

    def f_pow(self, a, b):
        try:
            return a ** b
        except:
            return a * b

    def algo_functions(self):
        math_funcs = [
            math.cos,
            math.sin,
            math.tan,
            math.asinh,
            math.cosh,
            math.sinh,
            math.tanh,
            abs
        ]

        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '**': self.f_pow
        }

        def func(x, y):
            result = random.uniform(-3,3)
            for n in range(0, random.randint(3, 9)):
                if n == 0:
                    result = operators[random.choice(list(operators.keys()))](
                        random.choice(math_funcs)(result),
                        random.choice([x, y])
                    )
                else:
                    result = operators[random.choice(list(operators.keys()))](
                        random.choice(math_funcs)(random.choice([x, y])),
                        random.choice([x, y, result])
                    )

            return result

        return func

    def save(self, filename):
        self.g.save_data(file_adr=f'{self.dir_path}/output/{filename}.json')
        plt.savefig(f'{self.dir_path}/output/{filename}.png')

if __name__ == '__main__':
    Generate(num_pieces=300)
