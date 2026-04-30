# Projeto de Testes - Assistente de Código

Repositório contendo exemplos de código Python para testes e validação de funcionalidades de um assistente de programação.

## 📁 Estrutura do Projeto

```
teste-assistent-code/
├── debug.py              # Script de cálculo de compras com impostos e descontos
├── num_primos.py         # Verificação de números primos
├── refatoracao.py        # Cálculo de estatísticas
├── explicacao-debug.md   # Documentação do script de debug
├── explicacao_num_primo.md    # Documentação do algoritmo de primos
└── explicacao_refatoracao.md  # Documentação da refatoração
```

## 🚀 Scripts Disponíveis

### 1. debug.py - Sistema de Compras

Script interativo que calcula o total de uma compra com:
- Múltiplos itens (quantidade × preço)
- Imposto de 10%
- Cupom de desconto percentual
- Exibição formatada do recibo

**Como executar:**
```bash
python debug.py
```

**Exemplo de uso:**
```
Qual é seu nome? João
Quantidade do item 1: 2
Preço do item 1? 50.00
Quantidade do item 2: 1
Preço do item 2? 30.00
Quantidade do item 3: 3
Preço do item 3? 20.00
Você tem um cupom de desconto? (Digite o percentual ou 0): 5
```

---

### 2. num_primos.py - Verificador de Primos

Função `is_prime(n)` que verifica se um número é primo utilizando o algoritmo de trial division otimizado com salto de 6.

**Características:**
- Validação de entrada (inteiros apenas)
- Tratamento de edge cases (n < 2, booleanos)
- Otimização usando `math.isqrt()` para limite do loop
- Complexidade O(√n)

**Como executar:**
```bash
python num_primos.py
```

**Exemplo de uso:**
```
Digite um número inteiro para verificar se é primo: 17
O número 17 é PRIMO.
```

---

### 3. refatoracao.py - Estatísticas

Função `compute_statistics(values)` que calcula:
- Total (soma de todos os valores)
- Média aritmética
- Valor máximo
- Valor mínimo

**Como executar:**
```bash
python refatoracao.py
```

**Saída esperada:**
```
Total: 346
Average: 34.60
Maximum: 89
Minimum: 2
```

---

## 📋 Requisitos

- Python 3.6+
- Módulo `math` (biblioteca padrão)

## 📝 Licença

Este projeto é para fins educacionais e de teste.