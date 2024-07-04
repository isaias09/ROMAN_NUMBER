valors = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def to_roman(n):

    order, d = calc_d_order(n)

    if d <= 3:
        result = d * valors[order]
    elif d == 4:
        result = valors[order] + valors[5*order]
    elif d < 9:
        result = valors[5*order] + (d - 5) * valors[order]
    elif d == 9:
        result = valors[order] + valors[10*order]

    return result


def calc_d_order(n):
    order = 10**(len(str(n))-1)
    d = n//order
    return order, d


def dividir_en_digitos(n: int):
    """
    TODO: evitar que entren numeros mayores de 3999. Lanzar ValueError
    """

    cad = f"{n:04d}"
    # millares = centenas = decenas = unidades = 0

    millares = int(cad[0]) * 1000
    centenas = int(cad[1]) * 100
    decenas = int(cad[2]) * 10
    unidades = int(cad[3]) * 1

    return [millares, centenas, decenas, unidades]


def digitos_a_roman(lista):
    result = ""
    for numero in lista:
        result += to_roman(numero)
    return result


def arabigo_a_romano(n: int):
    lista = dividir_en_digitos(n)
    return digitos_a_roman(lista)

def divide_en_miles(n:int):
    lista = []
    modulo = n % 1000
    paluego = n // 1000
    while paluego >= 1000:
        lista.append(modulo)
        n = paluego
        modulo = n % 1000
        paluego = n // 1000 
    
    if paluego <= 3:
        lista.append(n)
    else:
        lista.append(modulo)
        lista.append(paluego)
    return lista