salarioHora = float(input("Quanto você ganha por hora? : "))

horaMes = float(input("Quantas horas trabalhou no mês? :"))

salarioBruto = salarioHora * horaMes

umPorCentoSalarioBruto = salarioBruto / 100

impostodeRenda = umPorCentoSalarioBruto * 11

inss =  umPorCentoSalarioBruto * 8

sindicato = umPorCentoSalarioBruto * 5

descontos = impostodeRenda + inss + sindicato

salarioLiquido = salarioBruto - descontos

print("Salário Bruto: R$ ", salarioBruto, "\n", "Desconto de IR: R$ ",impostodeRenda,
       "\n", "Desconto INSS: R$ ", inss, "\n", "Desconto sindicato: R$ ", sindicato, "\n",
      "Total de Impostos: R$ ", descontos, "\n", "Salário Liquido: R$ ", salarioLiquido )





