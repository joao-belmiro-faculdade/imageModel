# Refatoração de `refatoracao.py`

Este arquivo documenta a refatoração aplicada ao código original para melhorar legibilidade, nomenclatura e estrutura.

## Código original

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

## Refatoração aplicada

- Renomeei a função para `compute_statistics` para deixar claro o propósito: calcular estatísticas de uma lista de valores.
- Usei `values` como nome do parâmetro em vez de `l`, pois é mais descritivo e evita confusão com o número 1 ou letra i.
- Adicionei uma verificação de entrada vazia com `if not values:` para tratar o caso em que a lista não tem elementos.
- Substituí o cálculo manual de soma e busca de mínimo/máximo pelos built-ins `sum()`, `max()` e `min()` para tornar o código mais curto e mais eficiente.
- Separei a lógica de processamento em uma função e o código de execução em um bloco protegido por `if __name__ == "__main__":`, permitindo que o arquivo seja importado como módulo sem executar a parte principal automaticamente.
- Usei nomes de variáveis claros: `total`, `average`, `maximum`, `minimum`.
- Formatei a saída com `print(f"Average: {average:.2f}")` para mostrar a média com duas casas decimais.

## Resultado final em `refatoracao.py`

```python
def compute_statistics(values):
    """Calculate total, average, maximum, and minimum for a list of numbers."""
    if not values:
        raise ValueError("The list of values must not be empty.")

    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)

    return total, average, maximum, minimum


if __name__ == "__main__":
    numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = compute_statistics(numbers)

    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
```
