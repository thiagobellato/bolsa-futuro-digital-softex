custo_ingresso = 10
ingressos_vendidos = 500
valor_bruto = custo_ingresso * ingressos_vendidos
taxa = 0.1
valor_liquido = valor_bruto - (valor_bruto * taxa)

print(
    f"Custo do ingresso: R${custo_ingresso}\n"
    f"Ingressos vendidos: {ingressos_vendidos}\n"
    f"Valor bruto: R${valor_bruto}\n"
    f"Taxa: {taxa * 100}%\n"
    f"Valor líquido: R${valor_liquido}"
)
