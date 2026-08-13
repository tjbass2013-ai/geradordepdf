# modulo para calculo de modificador de atributos

def modCalc(atributo):
    modificador = 0
    if atributo == 1:
        modificador = -5
    else:
        modificador = (atributo - 10) // 2
    
    return modificador
