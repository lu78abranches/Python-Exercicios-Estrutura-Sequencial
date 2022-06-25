quiloPeixe = int(input("Digite o quilo do peixe pescado: "))
excessoDePeso = quiloPeixe - 50
multaExcessoDePeso = excessoDePeso * 4.0

if ( quiloPeixe <= 50):
    print("Quilo do Peixe: ",quiloPeixe,"\n","Voce nao foi multado")
else:
    print("Quilo do Peixe:", quiloPeixe,"\n","Voce foi multado no valor de: R$ ", multaExcessoDePeso )