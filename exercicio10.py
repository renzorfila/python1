print ("Renzo Trigo Orfila\n1051392421006\n")

placadevideo= float(input("Valor da placa de vídeo: R$"))
processador= float(input("Valor do processador: R$"))
placamae= float(input("Valor da placa-mãe: R$"))
ram= float(input("Valor da memória RAM: R$"))
fonte= float(input("Valor da fonte: R$"))
total= (placadevideo)+(processador)+(placamae)+(ram)+(fonte)

print(f"Total a ser pago: {total}")
pagamento= float(input("Total a pagar: R$"))

print(f"O troco recebido pelo pagamento é de: R$ {pagamento-total}")
