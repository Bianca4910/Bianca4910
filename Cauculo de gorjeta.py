def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
  """
  Calcula o valor da gorjeta a ser deixada em um restaurante.

  Args:
    valor_conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta desejada (por exemplo, 15 para 15%).

  Returns:
    float: O valor da gorjeta a ser deixada.
  """
  if valor_conta < 0 or porcentagem_gorjeta < 0:
    raise ValueError("O valor da conta e a porcentagem da gorjeta não podem ser negativos.")
  
  gorjeta = valor_conta * (porcentagem_gorjeta / 100)
  return gorjeta

def main():
  try:
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada (%): "))

    gorjeta_calculada = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    valor_total_com_gorjeta = valor_conta + gorjeta_calculada

    print(f"\nValor da gorjeta: R$ {gorjeta_calculada:.2f}")
    print(f"Valor total a pagar (conta + gorjeta): R$ {valor_total_com_gorjeta:.2f}")
  except ValueError as e:
    print(f"Erro: {e}. Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
  main()