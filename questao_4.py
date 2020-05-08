"""
Dados n inteiros não negativos representando um mapa de elevação onde a largura de cada barra é 1,
calcule quanta água é capaz de reter após a chuva.

EXEMPLO
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


def calcula_agua(entrada):
    num_total = len(entrada)

    if num_total == 0:
        return 0

    total_agua = 0

    while sum(entrada) != 0:

        lado_esquerdo = 0
        lado_direito = 0

        for i in range(0, num_total):
            if entrada[i] != 0:
                if lado_esquerdo == 0:
                    lado_esquerdo = i
                else:
                    lado_direito = i
                    total_agua += lado_direito - lado_esquerdo - 1
                    lado_esquerdo = i

        for i in range(0, num_total):
            if entrada[i] != 0:
                entrada[i] = entrada[i] - 1

    print(entrada)

    return total_agua


def main():
    entrada = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(calcula_agua(entrada))


main()
