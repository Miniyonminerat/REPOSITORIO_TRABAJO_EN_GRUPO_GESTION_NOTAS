#-------------------- GESTION DE NOTAS --------------------#

estudiantes_lista= [] #Creamos una lista para guardar los datos de los estudiantes

notas= [] #Creamos otra lista para guarfar las notas de los estudiantes


Escoger= 0 #Creamos una condicion para que el while pueda entrar


while Escoger != 6: #Usamos while para que cada vez que termine de el proceso que se escogio vuelva al menu de inicio se uso != si el numero es diferente a 6 inicia el bucle se cumple la funcion pero si al escoger las opciones el escoje 6 no se cumple la funcion y el bucle termina 

    print("     SISTEMA GESTION DE NOTAS\n 1. Registrar Estudiante\n 2. Mostrar lista estudiante\n 3. Calcular promedios\n 4. Mostrar aprobados y reprobados\n 5 Generar informe de resultados\n 6 Salir ") # Creamos el menu de inicio que vera el usuario apenas ejecute el codigo con saltos de lineas para facilitar la escritura del codigo y la agilidez 

    Escoger= int(input("Ingrese una opcion: ")) # se le pide al usuario colocar una opcion que este en el menu en el caso de colocar otra opcion saldra error

    # Comenzamos con el registro de estudiantes la opcion 1 

    if Escoger == 1: # si la opcion es igual a 

        while True: # Se crea un bucle infinito 

            nombre= input("Ingrese nombre del estudiante que registrara: ") 

            documento= int(input("Ingrese documento del estudiante: "))

            asignatura= input("Ingrese asignatura del estudiante: ")
             # Se crean variables para pedirle al usuario nombre documento y asignatura aqui se usan 2 clases input y int
            estudiantes_lista.append((nombre,documento,asignatura)) # Se mete todo ala lista de el estudiante usarndo el .append que es un metodo en python 
            nota_1= float(input("Ingrese nota 1 del estudiante: "))
            nota_2= float(input("Ingrese nota 2 del estudiante: "))
            nota_3= float(input("Ingrese nota 3 del estudiante: "))# Se pide 3 notas al usuario para agregarlos a una lista float int y input son clases aqui se usa en todo solo 2 clases float y input
            notas.append ([nota_1,nota_2,nota_3])# se agregan a otra lista aparte de el estudiante y 

            print("El estudiante a sido registrado con exito") # Si el estudiante se registra correctamente al usuario se le imprimira esto si comete un error en lo que se pide le saldra error antes de llegar aca

            otro= input("¿Quieres ingresar otro estudiante? (si/no): ") # se crea una vaiable  para preguntarle al usuario si quiere agregar otro estudiante para que no tenga que hacer el proceso de volver al menu y escoger 1 aqui mismo se le dice si quiere continuar o no

            if otro.lower() != "si": # se usa condicional if aqui por que este if es una condicion independientes osea que este if no depende del de arriba si no que este es aparte 
                
                break # y si el usuario coloca "si " no cumple la condicion y repetiria el bucle y pediria datos denuevo por que se le esta diciendo SI LA VARIABLE OTRO SE CAMIA A MINUSCULA Y ES DIFERENTE A SI SE ROMPE 
    elif Escoger == 2:
        if len(estudiantes_lista)== 0: #en esta parte  si no se encuentran valores en la lista  dara el mensaje de abajo 
            print("\n No se encunetran estudintes registrados por el momento \n ")
        else:

            print("    LISTA ESTUDIANTE ")
            i=0
            while i < len(estudiantes_lista):

                llama=estudiantes_lista[i] #llama a la lista y el i cual de todas por ejemplo si i = 2 entonces llama la lista 2 y lo que haya dentro de esta ya que estan anidadas  

                print(f"estudiante - {llama[0]} documento - {llama[1]} asignatura - {llama[2]}") #con lo anterior los [] despues del "llama" indica la posicion que llama dentro de la lista 

                i+=1
                print() #deja un espacio para que no queden todos amontonados (estetica)
                
                
    elif Escoger == 3: #si selecciona la opcion 3 se hara el siguiente proceso 
        if len(estudiantes_lista) == 0: #verifica si hay un estudiante  agregado 

            print("No hay datos para calcular.\n")

        else:

            print("    PROMEDIO ESTUDIANTE")
            i = 0 #en esta la "i" va agragando notas a su variable 

            while i < len(estudiantes_lista): #mientras esta "i" sea menor al numero de estunadies en la lista se hara el siguiente proceso

                nota_1, nota_2, nota_3 = notas[i] # las nota 1 , 2 , 3 se agregan con el "i" a la lista de notas

                promedio= (nota_1 * 0.30 ) + (nota_2 * 0.30) + (nota_3 * 0.40)  #operacion para sacar el promedio
                print (f"{estudiantes_lista[i][0]} - Promedio: {promedio}") #se muestra el nombre del estudinate seguido del promedio")

                i+=1

                print()


    elif Escoger == 4:  # si la opción seleccionada es 4, se entra a mostrar aprobados y reprobados

        if len(estudiantes_lista) == 0:  # verifica si no hay estudiantes registrados
            print("\nNo hay estudiantes para calcular\n")  # mensaje si la lista está vacía

        else:
            print("\n    REPROBADOS Y APROBADOS\n")  # título de la sección

            i = 0  # inicializa el índice para recorrer las listas paralelas (estudiantes_lista y notas)
            
            while i < len(estudiantes_lista):  # recorre mientras 'i' sea menor al número de estudiantes
                
                # toma las tres notas del estudiante 'i' desde la lista 'notas'
                nota_1, nota_2, nota_3 = notas[i]
                
                # calcula el promedio ponderado: 30% nota 1, 30% nota 2, 40% nota 3
                promedio = (nota_1 * 0.30) + (nota_2 * 0.30) + (nota_3 * 0.40)
                
                if promedio >= 3.0:  # condición de aprobación: promedio mayor o igual a 3.0
                    # imprime: Nombre - Promedio - Aprobado
                    print(f"{estudiantes_lista[i][0]} - {promedio} - Aprobado\n")
                else:
                    # imprime: Nombre - Promedio - Reprobado
                    # (corrección: quitar el operador '-' entre cadenas y usar un único f-string)
                    print(f"{estudiantes_lista[i][0]} - {promedio} - Reprobado\n")
                    
                i += 1  # avanza al siguiente estudiante
                
                
    elif Escoger ==5:
        if len(estudiantes_lista)==0: #si en la variable de estudiantes no se encuentran valores mostra el mensaje 

            print("\n No se encuentran datos registrados de estudiantes \n porfavor ingrese datos de estudiantes ")
        else:
            print("\n Informe final de los estudiantes")
            i=0
            while i< len(estudiantes_lista):
                nota_1, nota_2, nota_3 = notas[i] # las nota 1 , 2 , 3 se agregan con el "i" a la lista de notas 
                promedio= (nota_1*0.30) + (nota_2*0.30) + (nota_3*0.40) #operacion para sacar el promedio
                if promedio >=3.0: #si se cumple la condicion y el promedio es mayor o igual a 3.0 entonces dira aprobo 
                    print(f"el estudiante - {estudiantes_lista[i][0]} aprobo la materian con un {promedio}")
                else: #de lo contrario si el promedio es menor a 3.0 dira que no aprovo 
                    print(f"el estudiante {estudiantes_lista[i][0]} reprobo con un {promedio}")
                i+=1
                
    elif Escoger == 6: #si la opcion escogida es 6 entra en este bloque
        confirmacion2=input("Ingresa (SALIR) para salir totalmente o (VOLVER) para reiniciar el programa: ").lower () 
        # aquí se le pide al usuario que confirme si quiere salir del programa totalmente o volver al menú principal
        # .lower() convierte todo lo que escriba el usuario en minúsculas, así no importa si escribe "SALIR", "salir" o "Salir"

        if confirmacion2 == "salir": # se evalúa si la respuesta del usuario fue "salir"
            print("HAS SALIDO TOTALMENTE DEL PROGRAMA") # si la condición se cumple se imprime el mensaje de salida
            # como la condición del while es while Escoger != 6, al haber elegido 6 ya no se repite el bucle
            # entonces el programa termina completamente
       
                    
                   

            
                
                
            


        













































