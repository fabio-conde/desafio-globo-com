"""
Digamos que você tenha um array para o qual o elemento i é o preço de uma determinada ação no dia i.

Se você tivesse permissão para concluir no máximo uma transação (ou seja, comprar uma e vender uma ação), crie
um algoritmo para encontrar o lucro máximo.

Note que você não pode vender uma ação antes de comprar.


EXEMPLO
Input: [7,1,5,3,6,4]
Output: 5 (Comprou no dia 2 (preço igual a 1) e vendeu no dia 5 (preço igual a 6), lucro foi de 6 – 1 = 5

Input: [7,6,4,3,1]
Output: 0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)
"""


def calcula_diferenca(nums):
    num_total = len(nums)

    maior_diferenca = 0
    dia_compra = 0
    valor_compra = 0
    dia_venda = 0
    valor_venda = 0

    for i in range(0, num_total):
        for j in range(i + 1, num_total):
            if nums[j] - nums[i] > maior_diferenca:
                dia_compra = i
                valor_compra = nums[i]
                dia_venda = j
                valor_venda = nums[j]
                maior_diferenca = nums[j] - nums[i]

    return maior_diferenca, dia_compra, valor_compra, dia_venda, valor_venda


def main():
    entrada = [10, 110, 11, 10, 1]

    maior_diferenca, dia_compra, valor_compra, dia_venda, valor_venda = calcula_diferenca(entrada)

    if maior_diferenca == 0:
        print("0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)")
    else:
        print(f"{maior_diferenca} (Comprou no dia {dia_compra} (preço igual a {valor_compra}) e vendeu no dia {dia_venda}"
              f" (preço igual a {valor_venda}), lucro foi de {valor_venda} – {valor_compra} = {maior_diferenca}")


main()

