# Gestión de Notas 
# ---------------------------------------------------------------------
# Este programa maneja el registro de estudiantes, cálculo de promedios,
# mostrar aprobados/reprobados y generar un informe. 

# Se usa una lista de diccionarios para almacenar todos los datos de cada estudiante.
# Cada estudiante tiene: nombre, documento, asignatura y una lista de 3 notas.

# Lista donde se guardan todos los estudiantes
# Tipo: list (lista)
# Cada usuario o estudiante se agregara como diccionario para colocarlo en la lista volviendola lista de diccionarios
# Ejemplo: {"nombre":"Ana", "documento":12345, "asignatura":"Matemáticas", "notas":[4.0,3.5,4.2]} Asi quedaria un ejemplo
estudiantes = []

# Variable de control para el menú principal 
# Tipo: int (entero)
# Mientras sea diferente de 6, el programa seguirá corriendo de lo contrario pues el programa dejara de correr y no seguira el bucle
opcion = 0

# Bucle principal del programa es el que inicia el menu siempre que el usuario escoja una opcion del 1 al 5 volvera a este menu
while opcion != 6:
    # Menú principal que se muestra al usuario
    print("\n     SISTEMA GESTIÓN DE NOTAS\n")
    print(" 1. Registrar Estudiante")
    print(" 2. Mostrar lista estudiantes")
    print(" 3. Calcular promedios")
    print(" 4. Mostrar aprobados y reprobados")
    print(" 5. Generar informe de resultados")
    print(" 6. Salir\n")

    # Se le pide al usuario escoger una opción
    # int() convierte el texto ingresado en número entero asi la persona no escoje una palabra y si o si escoja un numero 
    opcion = int(input("Ingrese una opción: "))

    # ---------------- OPCIÓN 1: REGISTRAR ESTUDIANTE ----------------
    if opcion == 1: #Se usa una condicion que dice "si el usuario escoje la opcion 1 se ejecutara esta parte del programa "
        # Variable para controlar si el usuario quiere seguir registrando
        continuar = "si"
        while continuar == "si":
            # Se pide el nombre (str = cadena de texto)
            nombre = input("Ingrese nombre del estudiante: ")

            # Se pide el documento (int = número entero)
            documento = int(input("Ingrese documento del estudiante: "))

            # Se pide la asignatura (str = cadena de texto)
            asignatura = input("Ingrese asignatura del estudiante: ")

            # Se piden tres notas (float = número decimal)
            nota1 = float(input("Ingrese nota 1: "))
            nota2 = float(input("Ingrese nota 2: "))
            nota3 = float(input("Ingrese nota 3: "))

            # Se crea un diccionario para guardar todos los datos juntos
            estudiante = {
                "nombre": nombre,          # clave 'nombre' con valor str
                "documento": documento,    # clave 'documento' con valor int
                "asignatura": asignatura,  # clave 'asignatura' con valor str
                "notas": [nota1, nota2, nota3] # clave 'notas' con valor list de floats
            }

            # Se agrega el diccionario a la lista principal
            estudiantes.append(estudiante)
            print("Estudiante registrado con éxito")

            # Se pregunta si quiere registrar otro estudiante
            continuar = input("¿Quieres ingresar otro estudiante? (si/no): ").lower()

    # ---------------- OPCIÓN 2: MOSTRAR LISTA DE ESTUDIANTES ----------------
    elif opcion == 2:
        # Si no hay estudiantes registrados
        if len(estudiantes) == 0:
            print("\nNo se encuentran estudiantes registrados.\n")
        else:
            print("\n    LISTA DE ESTUDIANTES\n")
            i = 0 # Variable entera que sirve como contador en el bucle
            # Recorremos toda la lista de estudiantes
            while i < len(estudiantes):
                est = estudiantes[i] # Diccionario de un estudiante en la posición i
                print(f"Nombre: {est['nombre']} | Documento: {est['documento']} | Asignatura: {est['asignatura']}")
                i += 1 # Incremento del contador para pasar al siguiente estudiante

    # ---------------- OPCIÓN 3: CALCULAR PROMEDIOS ----------------
    elif opcion == 3:
        # Si no hay datos para calcular 
        if len(estudiantes) == 0:
            print("\nNo hay datos para calcular.\n")
        else: # De lo contrario empezaria los datos del promedio de los estudiantes
            print("\n    PROMEDIOS DE ESTUDIANTES\n")
            i = 0
            while i < len(estudiantes): 
                notas = estudiantes[i]["notas"] # Lista de 3 floats
                # Fórmula de promedio ponderado: 30%, 30%, 40%
                promedio = notas[0]*0.30 + notas[1]*0.30 + notas[2]*0.40
                print(f"{estudiantes[i]['nombre']} - Promedio: {promedio:.2f}")
                i += 1

      # ---------------- OPCIÓN 4: MOSTRAR APROBADOS Y REPROBADOS ----------------
    elif opcion == 4:
        # Primero revisamos si la lista de estudiantes está vacía
        # len(estudiantes) devuelve la cantidad de estudiantes registrados
        if len(estudiantes) == 0:
            print("\nNo hay estudiantes para calcular.\n")
        else:
            # Si hay al menos un estudiante, mostramos el título de esta sección
            print("\n    REPROBADOS Y APROBADOS\n")

            # Creamos un contador i que empieza en 0
            # Este contador nos permitirá recorrer la lista estudiante por estudiante
            i = 0

            # Mientras i sea menor que la cantidad de estudiantes, seguimos en el bucle
            while i < len(estudiantes):
                # Guardamos en la variable notas la lista de 3 notas del estudiante actual
                # Esto lo hacemos accediendo a la clave "notas" dentro del diccionario del estudiante
                notas = estudiantes[i]["notas"]

                # Calculamos el promedio ponderado (con porcentajes):
                # nota1 * 30% + nota2 * 30% + nota3 * 40%
                promedio = notas[0]*0.30 + notas[1]*0.30 + notas[2]*0.40

                # Verificamos si el promedio es mayor o igual a 3.0
                # Si es así, significa que el estudiante aprobó
                if promedio >= 3.0:
                    # Imprimimos el nombre, el promedio con 2 decimales y la palabra "Aprobado"
                    print(f"{estudiantes[i]['nombre']} - {promedio:.2f} - Aprobado")
                else:
                    # Si no cumple la condición anterior, automáticamente es "Reprobado"
                    print(f"{estudiantes[i]['nombre']} - {promedio:.2f} - Reprobado")

                # Incrementamos el contador en +1 para pasar al siguiente estudiante
                i += 1

    # ---------------- OPCIÓN 5: GENERAR INFORME FINAL ----------------
    elif opcion == 5:
        if len(estudiantes) == 0:
            print("\nNo se encuentran datos registrados de estudiantes.\n")
        else:
            total = len(estudiantes) # cantidad total de estudiantes
            aprobados = 0            # contador de aprobados
            reprobados = 0           # contador de reprobados
            suma_promedios = 0.0     # acumulador de todos los promedios (float)

            print("\nInforme final de los estudiantes:\n")
            i = 0
            while i < len(estudiantes):
                notas = estudiantes[i]["notas"]
                promedio = notas[0]*0.30 + notas[1]*0.30 + notas[2]*0.40
                if promedio >= 3.0:
                    estado = "Aprobado"
                    aprobados += 1
                else:
                    estado = "Reprobado"
                    reprobados += 1
                suma_promedios += promedio
                print(f"El estudiante {estudiantes[i]['nombre']} ({estudiantes[i]['asignatura']}) - Promedio: {promedio:.2f} -> {estado}")
                i += 1

            promedio_general = suma_promedios / total

            print("\n--- Resumen ---")
            print(f"Total estudiantes: {total}")
            print(f"Aprobados: {aprobados}")
            print(f"Reprobados: {reprobados}")
            print(f"Promedio general de la clase: {promedio_general:.2f}\n")

    # ---------------- OPCIÓN 6: SALIR ----------------
    elif opcion == 6:
        confirmacion = input("Ingresa (SALIR) para salir totalmente o (VOLVER) para reiniciar el programa: ").lower()
        if confirmacion == "salir":
            print("HAS SALIDO TOTALMENTE DEL PROGRAMA")
        else:
            # Si el usuario escribe VOLVER, reiniciamos la variable opcion a 0
            opcion = 0

                    
                   

            
# ------------ PREGUNTAS QUE PUEDEN SALIR --------------#
# ¿POR QUE USAMOS EN LA OPCION 1 UN WHILE CONTINUAR == "SI"?
# 
# POR QUE SI USAMOS WHILE TRUE ESTARIA EN UN BUCLE INFINITO DE AGREGAR UNA PERSONA O UN ESTUDIANTE ASI NUNCA TERMINARIA DE REGISTRAR 

# ¿POR QUE EN LA OPCION 1 USAMOS AL FINAL .LOWER?
# 
# EL PUNTO LOWER SIRVE PARA VOLVER TODO MINUSCULA EN EL CASO QUE LA PERSONA AL COLOCAR LA OPCION "SI" EN MAYUSCULA EL PROGRAMA LO LEERA COMO "si"

# ¿POR QUE USAMOS LEN EN LA OPCION 2?

# EL LEN SIRVE PARA QUE EL PROGRAMA AL LEER UN DATO LO PASE A NUMERO UN EJEMPLO SERIA QUE LEA NOMBRE DOCUMENTO Y ASIGNATURA LO QUE EL RECOREERIA CON LEN SERIA 3 DATOS OSEA LOS PASA A NUMEROS VE DATO POR DATO Y LOS PASA A NUMEROS POR ESO SI LOS DATOS SON IGUAL A 0 NO HAY ESTUDIANTES Y SIN SON  DIFERENTE A 0 SI HAY ESTUDIANTES Y EMPIEZA EL SEGUNDO BUCLE

# ¿ QUE ES i EN LA OPCION 2?

# ES UN CONTADOR QUE SIRVE PARA COLOCARLE AUTOMATICAMENTE UN ORDEN AL  ESTUDIANTE POR DECIRLO ASI DEL ESTUDIANTE POR EJEMPLO SI HAY 3 ESTUDIANTES LO QUE HARIA EL CONTADOR ES COLOCARLE UN ORDEN A LOS ESTUDIANTES

# ¿ QUE ES .2f EN LA OPCION 3?
                
# ES LA CANTIDAD DE DECIMALES QUE QUIERE QUE COLOQUES EN EL CODIGO POR EJEMPLO ACA ESTAMOS DICIENDO QUE AL PROMEDIO LO APROXIME Y COLOQUE 2 DECIMALES             


        













































