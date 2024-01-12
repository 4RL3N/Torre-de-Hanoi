def func_torre_hanoi(n, A, C, B):
    if n == 1:
        print(f"Mova o disco 1 de {A} para a {C}")
        return
    func_torre_hanoi(n-1, A, B, C)
    print(f"Mova o disco {n} de {A} para a {C}")
    func_torre_hanoi(n-1, B, C, A)

print("Insira a quantidade de discos")
n = int(input())

func_torre_hanoi(n, "Torre A", "Torre C", "Torre B")
print("Concluído!")