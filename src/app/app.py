from __future__ import absolute_import

class App:
    @staticmethod
    def add(a,b):
        return a+b

    def resta(a,b):
        return a-b

    def multiplicacion(a,b):
        return a*b

    def division(a,b):
        return a/b

    # 1. Verifica si una lista contiene un número primo
    def contiene_numero_primo(lista):
        def es_primo(num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        return any(es_primo(num) for num in lista)

    # 2. Cuenta los números pares en un rango dado
    def contar_pares(inicio, fin):
        return len([num for num in range(inicio, fin + 1) if num % 2 == 0])

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    def maximo_multiplo(lista, multiplo):
        multiplos = [num for num in lista if num % multiplo == 0]
        return max(multiplos) if multiplos else None

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
    def es_palindromo(palabra):
        return palabra == palabra[::-1]

    # 5. Calcula la suma de los primeros n números impares
    def suma_primeros_impares(n):
        return sum([i for i in range(1, 2 * n, 2)])

    # 6. Verifica si todos los elementos de una lista son únicos
    def elementos_unicos(lista):
        return len(lista) == len(set(lista))


    # 7. Calcula el factorial de un número sin usar recursión
    def calcular_factorial(numero):
        """
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """
        pass

    # 8. Cuenta la cantidad de vocales en una cadena
    def contar_vocales(cadena):
        """
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
        pass

    # 9. Encuentra el segundo número mayor en una lista
    def segundo_mayor(lista):
        """
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
        pass

    # 10. Calcula la serie de Fibonacci hasta n términos
    def fibonacci(n):
        """
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
        pass
