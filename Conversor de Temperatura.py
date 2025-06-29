def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("--- Conversor de Temperaturas ---")

    while True:
        try:
            temperature = float(input("Digite a temperatura: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a temperatura.")

    while True:
        unit_from = input("Qual a unidade de origem? (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()
        if unit_from in ['C', 'F', 'K']:
            break
        else:
            print("Unidade de origem inválida. Por favor, digite C, F ou K.")

    while True:
        unit_to = input("Qual a unidade para a qual deseja converter? (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()
        if unit_to in ['C', 'F', 'K']:
            break
        else:
            print("Unidade de destino inválida. Por favor, digite C, F ou K.")

    result = None

    if unit_from == 'C':
        if unit_to == 'F':
            result = celsius_to_fahrenheit(temperature)
        elif unit_to == 'K':
            result = celsius_to_kelvin(temperature)
        elif unit_to == 'C':
            result = temperature
    elif unit_from == 'F':
        if unit_to == 'C':
            result = fahrenheit_to_celsius(temperature)
        elif unit_to == 'K':
            result = fahrenheit_to_kelvin(temperature)
        elif unit_to == 'F':
            result = temperature
    elif unit_from == 'K':
        if unit_to == 'C':
            result = kelvin_to_celsius(temperature)
        elif unit_to == 'F':
            result = kelvin_to_fahrenheit(temperature)
        elif unit_to == 'K':
            result = temperature

    if result is not None:
        print(f"\n{temperature:.2f} {unit_from} é igual a {result:.2f} {unit_to}.")
    else:
        print("Ocorreu um erro na conversão. Verifique suas entradas.")

if __name__ == "__main__":
    main()