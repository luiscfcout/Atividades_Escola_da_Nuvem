"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais."""

distancia = 300
combustivel = 25

consumo = distancia/combustivel

print ("Distância percorrida: 300 km")
print("Combustível gasto: 25 litros")

print(f"A média de consumo é de: {consumo:.2f} km/l")