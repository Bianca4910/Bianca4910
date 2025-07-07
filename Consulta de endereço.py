import requests

def get_random_user_profile():
    """
    Busca um perfil de usuário aleatório da API Random User Generator.
    """
    url = "https://api.randomuser.me/?nat=br"  # Adicionei ?nat=br para usuários brasileiros
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        data = response.json()
        user_info = data['results'][0]  # Pega o primeiro usuário da lista de resultados
        return user_info
    else:
        print(f"Erro ao buscar o perfil do usuário: {response.status_code}")
        return None

def main():
    """
    Função principal para gerar e exibir o perfil do usuário.
    """
    print("Gerando um perfil de usuário aleatório...\n")
    user_profile = get_random_user_profile()

    if user_profile:
        name = user_profile['name']
        email = user_profile['email']
        country = user_profile['location']['country']

        # Exibe as informações do usuário
        print(f"--- Perfil de Usuário Aleatório ---")
        print(f"Nome: {name['first']} {name['last']}")
        print(f"Email: {email}")
        print(f"País: {country}")
        print(f"-----------------------------------\n")
    else:
        print("Não foi possível gerar um perfil de usuário no momento. Tente novamente mais tarde.")

if __name__ == "__main__":
    main()