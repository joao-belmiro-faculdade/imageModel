# -*- coding: utf-8 -*-
import math


def is_prime(n):
    """Verifica se um número é primo.

    Determina se o número inteiro fornecido é primo usando o algoritmo
    de trial division otimizado com salto de 6.

    Args:
        n: O número inteiro a ser verificado. Deve ser um inteiro maior
            ou igual a 2.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        TypeError: Se n for um booleano.
        ValueError: Não é levantada explicitamente, mas a função
            retorna False para valores menores que 2.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
    """
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
