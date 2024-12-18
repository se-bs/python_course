#crear un programa que dibuje triangulos con el numero 1
#el usuario debe poner cuantas filas tiene el triangulo 
def generar_triangulo(filas):
    """
    Genera un triángulo de unos con la cantidad de filas especificada.

    Args:
        filas (int): Número de filas del triángulo.

    Returns:
        None
    """

    for i in range(1, filas + 1):
        print("te quiero." * i)

# Solicitar al usuario el número de filas
num_filas = int(input("Ingrese el número de filas del triángulo: "))

# Generar el triángulo
generar_triangulo(num_filas)