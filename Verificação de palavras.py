import re

def is_palindrome(text):
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    Args:
        text (str): A palavra ou frase a ser verificada.

    Returns:
        bool: True se for um palíndromo, False caso contrário.
    """
    # Remove caracteres não alfanuméricos e converte para minúsculas
    processed_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return processed_text == processed_text[::-1]

def main():
    phrases = [
        "A base do teto desaba.",
        "O lobo ama o bolo.",
        "Madam, I'm Adam",
        "Hello, World!",
        "Racecar",
        "Was it a car or a cat I saw?"
    ]

    for phrase in phrases:
        if is_palindrome(phrase):
            print(f"'{phrase}' é um palíndromo? Sim")
        else:
            print(f"'{phrase}' é um palíndromo? Não")

if __name__ == "__main__":
    main()