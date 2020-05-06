"""
Dado um array de números inteiros, retorne os
índices dos dois números de forma que eles se
somem a um alvo específico.

Você pode assumir que cada entrada teria
exatamente uma solução, e você não pode usar o
mesmo elemento duas vezes.

EXEMPLO

Dado nums = [2, 7, 11, 15], alvo = 9,
Como nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def soma_alvo(nums, alvo):
    resultado = []

    num_total = len(nums)

    for i in range(0, num_total):
        for j in range(i + 1, num_total):
            if nums[i] != nums[j]:
                if int(nums[i]) + int(nums[j]) == alvo:
                    resultado.append([i, j])

    return resultado


def main():
    entrada = [2, 7, 11, 15]
    alvo = 9
    print(soma_alvo(entrada, alvo))


main()
