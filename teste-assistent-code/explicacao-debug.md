# Explicação dos Erros e Correções em `debug.py`

Este documento detalha os erros identificados no código original e as correções aplicadas.

---

## Erros Identificados

### 1. String sem aspas (Linha 4)

**Código original:**
```python
item1 = float(input(Preço do item 1? ))
```

**Problema:** A mensagem do `input()` estava sem aspas, causando erro de sintaxe.

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

---

### 2. Tipo de dado incorreto para desconto (Linha 17)

**Código original:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

**Problema:** O `input()` retorna uma string, mas estava sendo usado diretamente em operações matemáticas sem converter para número.

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

---

### 3. F-string incompleta (Linha 31)

**Código original:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Problema:** Faltava o prefixo `f` antes das aspas para ativar a formatação de string.

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

### 4. Indentação incorreta (Linhas 36-37)

**Código original:**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Problema:** O comando `print` dentro do `if` não estava indentado, o que causaria erro de indentação.

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## Resumo das Correções

| Erro | Linha | Tipo | Descrição |
|------|-------|------|-----------|
| 1 | 4 | Sintaxe | String sem aspas |
| 2 | 17 | Tipo | Falta de conversão para float |
| 3 | 31 | Sintaxe | F-string incompleta |
| 4 | 36-37 | Indentação | Bloco if sem indentação |

---

## Observações

- Sempre use `float()` ou `int()` ao converter entradas do usuário para operações matemáticas.
- Mantenha consistência na indentação para evitar erros de bloco.
- Use f-strings completas (com o prefixo `f`) para formatação de saída.