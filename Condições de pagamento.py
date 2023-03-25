preco_etiqueta = float(input("Digite o preço normal de etiqueta do produto: "))
condicao_pagamento = int(input("Digite o código da condição de pagamento (1-4): "))

if condicao_pagamento == 1:
    preco_final = preco_etiqueta * 0.9
elif condicao_pagamento == 2:
    preco_final = preco_etiqueta * 0.85
elif condicao_pagamento == 3:
    preco_final = preco_etiqueta
elif condicao_pagamento == 4:
    preco_final = preco_etiqueta * 1.1
else:
    print("Codigo de condição de pagamento inválido. Por favor, tente novamente.")
    exit()

print(f"Preço final a pagar: R$ {preco_final:.2f}")
