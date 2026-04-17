# -*- coding: utf-8 -*-
import math


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
