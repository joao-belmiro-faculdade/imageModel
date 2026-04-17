# Explicação do código `num_primo.py`

Este documento explica de forma didática como o script `num_primo.py` funciona. O objetivo do código é verificar se um número é primo e testar essa verificação.

---

## 1. O que é um número primo?

Um número primo é um inteiro maior que 1 que só pode ser dividido por 1 e por ele mesmo, sem deixar resto.

Exemplos:
- `2` é primo
- `3` é primo
- `4` não é primo porque 4 = 2 × 2
- `5` é primo

---

## 2. Função `is_prime(n)`

A função `is_prime` recebe um valor `n` e retorna `True` se `n` for primo ou `False` caso contrário.

```python
def is_prime(n):
    """Retorna True se n for primo, False caso contrario."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limite = math.isqrt(n)
    for i in range(5, limite + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
```

### Passo a passo da função

1. `if not isinstance(n, int) or isinstance(n, bool) or n < 2:`
   - Verifica se `n` não é um número inteiro, se é `True` ou `False`, ou se é menor que 2.
   - Retorna `False` nesses casos, porque apenas inteiros maiores que 1 podem ser primos.

2. `if n in (2, 3):`
   - Confirma que 2 e 3 são primos.
   - Retorna `True` imediatamente para esses casos.

3. `if n % 2 == 0 or n % 3 == 0:`
   - Elimina números pares e múltiplos de 3 rapidamente.
   - Retorna `False` para esses casos.

4. `limite = math.isqrt(n)`
   - Calcula a raiz quadrada inteira de `n`.
   - Não é necessário testar divisores maiores que a raiz quadrada.

5. `for i in range(5, limite + 1, 6):`
   - Testa apenas valores do tipo `6k - 1` e `6k + 1`, que são os únicos candidatos a divisor além de 2 e 3.
   - Isso deixa a verificação mais rápida.

6. `if n % i == 0 or n % (i + 2) == 0:`
   - Verifica se `n` é divisível por algum desses candidatos.
   - Se for, `n` não é primo.

7. `return True`
   - Se nenhum divisor é encontrado até o limite, `n` é primo.

---

## 3. Bloco de execução principal

O bloco abaixo é executado apenas quando o arquivo é rodado diretamente pelo Python.

```python
if __name__ == "__main__":
    entrada = input("Digite um número inteiro para verificar se é primo: ").strip()
    try:
        valor = int(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
    else:
        if is_prime(valor):
            print(f"O número {valor} é PRIMO.")
        else:
            print(f"O número {valor} NÃO É PRIMO.")
```

### O que esse bloco faz

- Solicita que o usuário digite um número inteiro.
- Converte a entrada para inteiro usando `int()`.
- Exibe uma mensagem de erro se a entrada não for um número inteiro válido.
- Se a conversão for bem-sucedida, chama `is_prime(valor)`.
- Imprime se o número é `PRIMO` ou `NÃO É PRIMO`.

---

## 4. Observações

- O código é eficiente porque testa apenas divisores ímpares depois de filtrar os casos triviais.
- Se o número não for inteiro ou for menor que 2, ele já retorna `False` imediatamente.
- A função `math.isqrt` ajuda a limitar os testes até a raiz quadrada de `n`, reduzindo a quantidade de verificações.

---

## 5. Resultado esperado

Quando você executar o script, ele deve pedir que você digite um número inteiro. Em seguida, ele irá mostrar uma mensagem dizendo se o número informado é `PRIMO` ou `NÃO É PRIMO`.

Exemplo de saída:

```
Digite um número inteiro para verificar se é primo: 17
O número 17 é PRIMO.
```
