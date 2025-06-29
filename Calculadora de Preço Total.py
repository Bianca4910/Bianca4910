def main():
    # Informações do produto
    nome_produto = "Cadeira Infantil"
    preco_unitario = 12.40
    quantidade = 3

    # Calcula o preço total
    preco_total = preco_unitario * quantidade

    # Exibe todas as informações e o resultado final
    print(f"Produto: {nome_produto}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"---")
    print(f"Preço total da compra: R$ {preco_total:.2f}")

if __name__ == "__main__":
    main()