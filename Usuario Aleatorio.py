import requests

def get_random_user():
    """
    Busca um perfil de usuário aleatório da API Random User Generator.
    Retorna um dicionário com os dados do usuário ou None em caso de erro.
    """
    url = "https://api.randomuser.me/api/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para respostas de status HTTP ruins (4xx ou 5xx)
        data = response.json()
        return data['results'][0]
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao conectar à API: {e}")
        return None

def main():
    """
    Função principal que gera e exibe o perfil do usuário.
    """
    print("Gerando um perfil de usuário aleatório...\n")
    user_data = get_random_user()

    if user_data:
        # Extrai as informações relevantes
        name = user_data['name']
        full_name = f"{name['first']} {name['last']}"
        email = user_data['email']
        country = user_data['location']['country']

        # Exibe as informações do usuário
        print("--- Perfil do Usuário ---")
        print(f"Nome: {full_name}")
        print(f"Email: {email}")
        print(f"País: {country}")
        print("-------------------------")
    else:
        print("Não foi possível gerar um perfil de usuário no momento. Por favor, tente novamente mais tarde.")

if __name__ == "__main__":
    main()