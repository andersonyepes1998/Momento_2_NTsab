from Escuderia import Escuderia



escuderias = []
contador = 1
print()
print("*********** INICIO DEL PROGRAMA ***********")
print()
numeroEscuderias = int(input("Digite el numero de escuderias: "))

while contador <= numeroEscuderias:
    escuderia = Escuderia()
    escuderia.nombre = input("digite el nombre de la escuderia: ")
    escuderia.casaMotor = input("digite el nombre del casamotor: ")
    escuderia.pilotoPrincipal.nombre = input("digita el nombre del piloto principal: ")
    escuderia.pilotoSuplente.nombre = input("digita el nombre del piloto suplente: ")
    escuderia.costoAnual = int(input("ingrese los costos anuales: "))

    escuderias.append(escuderia)
    contador = contador + 1

    print("Listado de escuderias y costos")
for escuderia in escuderias:
    print(f"Nombre escuderia : {escuderia.nombre}, Costo anual : {escuderia.costoAnual}")

costoMayor = 0
nombreEscuderiaMasCara = None

for escuderia in escuderias:
    if escuderia.costoAnual > costoMayor:
        costoMayor = escuderia.costoAnual
        nombreEscuderiaMasCara = escuderia.nombre
        print(f"Nombre de la escuderia mas cara: {nombreEscuderiaMasCara}")
        print(f"Costo de la escuderia mas cara: {costoMayor}")