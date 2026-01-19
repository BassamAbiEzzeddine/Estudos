quantidade_de_termos = int(
    input("Insira a quantidade de termos de fibonacci que deseja ver: ")
)
f0 = 0
f1 = 1
fn = 0
print("0 1", end=" ")
while quantidade_de_termos != 0:
    fn = f0 + f1
    f0 = f1
    f1 = fn
    print(fn, end=" ")
    quantidade_de_termos = quantidade_de_termos - 1
