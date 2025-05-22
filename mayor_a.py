import sys

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

def filtro_ventas(setpoint):
    meses = {}
    for mes, valor in ventas.item():
        if valor > setpoint:
            meses[mes] = valor
    return meses

if __name__ == "__main__":      # Para que este código solo se ejecute cuando el script es el programa principal
    if len(sys.argv) != 2:      # Lista de argumentos pasados por consola / verifica si se ingresaron 2 argumentos
        print("\nUso: python mayor_a.py 'setpoint'")  # si datos no son correctos entra en el bloque imprimiendo instrucciones
        sys.exit(1)             # Termina el programa con un código de error 1

    try:                         # Manejo de errores
        setpoint = int(sys.argv[1])
    except ValueError:
        print("\nArgumento inválido: El peso y la altura deben ser valores numéricos\n")
        sys.exit(1)                # Termina el programa con un código de error 1

    resultado = filtro_ventas
    print(f"\nTu jugaste: {resultado}")
    