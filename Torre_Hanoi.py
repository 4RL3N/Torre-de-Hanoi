#funcao principal
def func_torre_hanoi(n, A, C, B):
    #condicao de parada da recursao
    if n == 1:
        print(f"Mova o disco 1 de {A} para a {C}")
        return
    #move os discos da torre "A" para a torre "B" utilizando a torre "C" como auxiliar
    func_torre_hanoi(n-1, A, B, C)
    print(f"Mova o disco {n} de {A} para a {C}")
    #move os discos da torre "B" para a torre "C" utilizando a torre "A" como auxiliar
    func_torre_hanoi(n-1, B, C, A)

print("Insira a quantidade de discos")
n_discos = int(input())

func_torre_hanoi(n_discos, "Torre A", "Torre C", "Torre B")
print("Concluído!")