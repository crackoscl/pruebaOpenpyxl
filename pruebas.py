from openpyxl import Workbook
wb = Workbook()
hoja = wb.active
def columna_a_letra(columna):
    """Convierte un número de columna a su letra correspondiente."""
    letras = []
    while columna > 0:
        columna, resto = divmod(columna - 1, 26)
        letras.append(chr(65 + resto))
    return ''.join(reversed(letras))

fila = 1
num_filas = 20
valor = 1

for i in range(num_filas):
    columna_inicial = num_filas - i
    for j in range(2 * i + 1):
        columna = columna_inicial + j
        letra_columna = columna_a_letra(columna)
        hoja[f'{letra_columna}{fila}'] = valor
        hoja.column_dimensions[letra_columna].width = 4
        valor += 1
    fila += 1
wb.save("prueba.xlsx")
