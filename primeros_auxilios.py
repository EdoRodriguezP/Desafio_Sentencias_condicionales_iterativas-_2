import sys 


def cuestionario_ayuda():
    print()
    print("Primeros Auxilios")
    
    while True:
        
        print("\n¿El paciente responde a estimulos?")
        print("\nMarque numero de opcion")
        print("1.- SI")
        print("2.- NO")
        opcion  = input("Ingresa la opcion: ")
    
        if opcion == "1":
            print("\n****--Valorar la necesidad de llevarlo al hospital mas cercano--*****\n")
            sys.exit(0)
        else:
            print("\n****--Abrir via Aerea--****")
            
        while True:
        
            print("\n¿El paciente respira?")
            print("\nMarque numero de opcion")
            print("1.- SI")
            print("2.- NO")
            opcion_2 = input("Ingresa la opcion: ")
        
            if opcion_2 == "1":
                print("\n****--Permitirle posicion de suficiente ventilacion--****\n")
                sys.exit(0)
            else:
                print("\n****--Administrarle 5 ventilaciones y llamar a la ambulancia--****")
            
            while True:
                
                print("\n¿Tiene signos de Vida?")
                print("\nMarque numero de opcion")
                print("1.- SI")
                print("2.- NO")
        
                opcion_3 = input("Ingresa la opcion: ")
        
                if opcion_3 == "1":
                    print("\n****--Reevaluar a la espera de la ambulancia--****")
                else:
                    print("\n****--Administrar compresiones toraxicas hasta que llegue la ambulancia--****")
                while True:
                
                    print("\n¿Llego la ambulancia?")
                    print("\nMarque numero de opcion")
                    print("1.- SI")
                    print("2.- NO")
        
                    opcion_4 = input("Ingresa la opcion: ")
        
                    if opcion_4 == "1":
                        sys.exit(0)
                    elif opcion_4 == "2":
                        break
        
        
    

if __name__ == "__main__":      # Para que este código solo se ejecute cuando el script es el programa principal
        cuestionario_ayuda() 






    