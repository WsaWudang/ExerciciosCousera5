#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro 
#e devolve o maior número primo menor ou igual ao número passado à função


def maior_primo(num):
    while num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            return num
        num -= 1