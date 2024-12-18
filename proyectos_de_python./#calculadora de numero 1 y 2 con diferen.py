#calculadora de numero "1" y "2" con diferentes operaciones
print("hola usuario podras identificar las diferentes operaciones que usamos")
print("usaremos numero de 1 a 9 tu eligue la operacion que quieres")
print("usaremos suma resta y multiplicacion")
print("eligue uno de los simbolos que son")
print("suma(+) resta(-) multiplicacion(x) division(/)")
operacion = input("eligue una operacion(+,-,x,/):")
numero1 = int(input("introduce tu primer numero"))
numero2 = int(input("introduce tu segundo numero"))
if operacion == '+':
    resultado = numero1 + numero2
    print(f"el resultado de {numero1} + {numero2} es {resultado} ")
if operacion == '-':
    resultado = numero1 - numero2
    print(f"el resultado de {numero1} - {numero2} es {resultado} ")
if operacion == 'x':
    resultado = numero1 * numero2
    print(f"el resultado de {numero1} x {numero2} es {resultado} ")
if operacion == '/':
    resultado = numero1 / numero2
    print(f"el resultado de {numero1} / {numero2} es {resultado}" )
#operacion = empezar_de_nuevo = 0
#input("si quieres empezar denuevo presiona" 0)09l