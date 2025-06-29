def calcular_volume_caixa(comprimento, largura, altura):
  """
  Calcula o volume de uma caixa retangular.

  Args:
    comprimento: O comprimento da caixa em cm.
    largura: A largura da caixa em cm.
    altura: A altura da caixa em cm.

  Returns:
    O volume da caixa em cm³.
  """
  volume = comprimento * largura * altura
  return volume

def main():
  comprimento = 12
  largura = 14
  altura = 20

  volume_caixa = calcular_volume_caixa(comprimento, largura, altura)

  print(f"O volume da caixa é: {volume_caixa} cm³")

if __name__ == "__main__":
  main()