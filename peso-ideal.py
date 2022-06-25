sexo = input("Digite o sexo, Masculino 'M' Feminino 'F': ")

if sexo == 'M':
    alturaM = float(input("Digite sua altura: "))
    pesoIdealMasculino = (72.7 * alturaM) - 58
    print("Seu peso ideal é: ", pesoIdealMasculino)

else:
    alturaF = float(input("Digite sua altura: "))
    pesoIdealFeminino = (62.1 * alturaF) - 44.7
    print("Seu peso ideal é: ", pesoIdealFeminino)







