tamanhoArea = int(input("Digite o tamanho da area a ser pintada: "))
lataDetinta = 18
totaldeLitros = tamanhoArea / 3
totalDeLatas = totaldeLitros / lataDetinta
valorLataDeTinta = float(80)
precoTotal = valorLataDeTinta * totalDeLatas

print(" - Tamanho da area a ser pintada: ", tamanhoArea, "m²", "\n", f"- Quantidade de latas para pintar toda a area: {totalDeLatas:.2f} "
      , "\n", f"- Valor da unidade/lata de tinta: R$ {valorLataDeTinta:.2f}", "\n", f"- Preço total das latas de "
                                                                                    f"tinta: R$ {precoTotal:.2f}")
