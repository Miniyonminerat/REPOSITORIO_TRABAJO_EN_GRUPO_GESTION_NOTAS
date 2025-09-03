Consejo sobre el código

Actualmente manejas dos listas paralelas (estudiantes_lista y notas). Esto funciona, pero puede generar errores porque depende de que siempre tengan 
la misma longitud y el mismo orden.

Una mejora sería usar un diccionario o una lista de diccionarios, donde cada estudiante tenga sus propios datos y notas en una sola estructura.
Eso hace que sea más claro, más legible y más fácil de mantener.

Ejemplo con lista de diccionarios
estudiantes = []  # aquí guardamos cada estudiante como un diccionario

# Registrar estudiante
nombre = input("Ingrese nombre del estudiante: ")
documento = int(input("Ingrese documento del estudiante: "))
asignatura = input("Ingrese asignatura del estudiante: ")

nota_1 = float(input("Ingrese nota 1: "))
nota_2 = float(input("Ingrese nota 2: "))
nota_3 = float(input("Ingrese nota 3: "))

# guardamos todo junto en un solo diccionario
estudiante = {
    "nombre": nombre,
    "documento": documento,
    "asignatura": asignatura,
    "notas": [nota_1, nota_2, nota_3]
}

estudiantes.append(estudiante)
print("✅ Estudiante registrado con éxito")

# Calcular promedio
for est in estudiantes:
    notas = est["notas"]
    promedio = notas[0]*0.30 + notas[1]*0.30 + notas[2]*0.40
    print(f"{est['nombre']} - Promedio: {promedio}")
