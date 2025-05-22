import sys
import getpass
from string import ascii_lowercase


def fuerza_bruta():
    password = getpass.getpass("Ingresa tu contraseña : ").lower()
    
    intentos = 0
    contraseña_encontrada = []
    
    for letra in password:
        for letra_prueba in ascii_lowercase:
            intentos += 1
            if letra_prueba == letra:
                contraseña_encontrada.append(letra_prueba)
                break
            
    print(f"\nLa contraseña fue encontrada en {intentos} intentos. ")
    print(f"\nContraseña adivinada: {''.join(contraseña_encontrada)}")

if __name__ == "__main__":
    fuerza_bruta()
            
        
            

