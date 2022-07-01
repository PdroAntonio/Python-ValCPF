cpf_final = '16899535009'
cpf = cpf_final[:-2]
ac = 0

while len(cpf) < 10:
    for i, r in enumerate(range(10, 2, -1)):
        x = int(cpf[i]) * r
        ac += x

    f = 11 - (ac % 11)

    if f > 9:
       cpf += '0'
       ac == 0
    else:
        cpf += str(f)
        ac == 0

for i, r in enumerate(range(11, 2, -1)):  # Minha solução
    x = int(cpf[i]) * r
    ac += x

f = 11 - (ac % 11)

if f > 9:
    cpf += '0'
else:
    cpf += str(f)

if cpf == cpf_final:
    print(cpf_final)
else:
    print('cpf invalido')
