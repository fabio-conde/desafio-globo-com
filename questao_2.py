"""
Um bracket é considerado qualquer um dos seguintes caracteres: (, ), {, },
[ ou ].

Dois brackets são considerados um par combinado se o bracket de
abertura (isto é, (, [ou {) ocorre à esquerda de um bracket de fechamento
(ou seja,),] ou} do mesmo tipo exato. Existem três tipos de pares de
brackets : [ ], { } e ( ).

Um par de brackets correspondente não é balanceado se o de abertura e
o de fechamento não corresponderem entre si. Por exemplo, { [ ( ] ) } não
é balanceado porque o conteúdo entre {e} não é balanceado. O primeiro
bracket inclui o de abertura, (, e o segundo inclui um bracket de
fechamento desbalanceado,].

Dado sequencias de caracteres, determine se cada sequência de brackets
é balanceada. Se uma string estiver balanceada, retorne SIM. Caso
contrário, retorne NAO.


EXEMPLO
{[()]} SIM
{[(])} NAO
{{[[(())]]}} SIM
"""


def brackets(entrada):
    abertura = tuple('({[')
    fechamento = tuple(')}]')
    mapping = dict(zip(abertura, fechamento))
    queue = []

    for caracter in entrada:
        if caracter in abertura:
            queue.append(mapping[caracter])
        elif caracter in fechamento:
            if not queue or caracter != queue.pop():
                return False
    return not queue


def main():
    input_string = "({}[]())"

    if brackets(input_string):
        print(input_string, "SIM")
    else:
        print(input_string, "NAO")


main()
