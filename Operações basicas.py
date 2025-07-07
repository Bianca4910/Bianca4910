def main():
    """
    Função principal da calculadora.
    Solicita dois números e uma operação, realiza o cálculo
    e trata erros de entrada.
    """
    while True:
        try:
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str)

            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str)

            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Erro: Operação inválida. Use +, -, * ou /.")

            print(f"O resultado da operação é: {resultado}")
            break  # Encerra o programa após uma operação bem-sucedida

        except ValueError as e:
            print(f"Erro de entrada: {e}. Por favor, tente novamente.")
        except ZeroDivisionError as e:
            print(f"{e}. Por favor, tente novamente.")
        except Exception as e:
            print(f"Um erro inesperado ocorreu: {e}. Por favor, tente novamente.")

if __name__ == "__main__":
    main()