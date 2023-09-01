num = int(input("Informe um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10 
m = num // 1000 % 10
print(f" A unidade é {u} \n A dezena é {d} \n A centena é {c} \n O milhar é {m}" )