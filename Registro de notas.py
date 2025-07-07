def main():
    """
    Permite ao professor registrar as notas de uma turma, calcula e exibe a média.
    O programa solicita notas até que 'fim' seja digitado. Notas válidas são de 0 a 10.
    Notas inválidas são ignoradas.
    """
    notas = []
    print("Bem-vindo ao sistema de registro de notas!")
    print("Digite as notas dos alunos (de 0 a 10). Digite 'fim' para encerrar.")

    while True:
        entrada = input("Digite a nota: ").strip().lower()

        if entrada == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\n--- Resumo ---")
        print(f"Total de notas registradas: {len(notas)}")
        print(f"A média da turma é: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

if __name__ == "__main__":
    main()