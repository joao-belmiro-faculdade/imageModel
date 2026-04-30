cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
# Multiplica quantidade pelo preço unitário de cada item
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

# Soma todos os totais para obter o subtotal antes de impostos
subtotal = total_item1 + total_item2 + total_item3
# Aplica alíquota de 10% de imposto sobre o subtotal
imposto = subtotal * 0.10

# DESCONTO
# O usuário informa o percentual de desconto (0 se não tiver cupom)
# O desconto é calculado sobre o subtotal, antes do imposto
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
# Fórmula: subtotal + imposto - desconto
# O imposto incide sobre o valor original (antes do desconto) conforme legislação
total = subtotal + imposto - desconto

# EXIBIÇÃO
# Formata a saída com linhas de separação para melhor visualização
# Usa 31 caracteres para manter alinhamento adequado dos valores monetários
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Mostra desconto apenas se for maior que zero
# Evita exibir linha desnecessária quando não há cupom aplicado
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
# Arredonda o total para 2 casas decimais antes de formatar
# Garante precisão monetária correta
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)