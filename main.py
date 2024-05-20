import json

def load_data():
    """
    Função para carregar os dados do arquivo JSON.
    
    Retorna:
        dict: Dados carregados do arquivo JSON.
    """
    # Abre o arquivo 'superhero.json' em modo de leitura
    with open('superhero.json', 'r') as file:
        # Carrega os dados do arquivo JSON em um dicionário
        data = json.load(file)
    # Retorna os dados carregados
    return data

def list_members(data):
    """
    Função para listar os membros do esquadrão de super-heróis.
    
    Argumentos:
        data (dict): Dados do esquadrão de super-heróis.
    """
    # Imprime o cabeçalho
    print("Members of Super Hero Squad:")
    # Itera sobre os membros do esquadrão
    for member in data["members"]:
        # Imprime os detalhes de cada membro
        print(f"Name: {member['name']}")
        print(f"Age: {member['age']}")
        print(f"Secret Identity: {member['secretIdentity']}")
        print("Powers:")
        # Itera sobre os poderes de cada membro
        for power in member['powers']:
            print(f"- {power}")
        print()

def main():
    """
    Função principal do programa.
    """
    # Carrega os dados do arquivo JSON
    data = load_data()
    # Lista os membros do esquadrão de super-heróis
    list_members(data)

if __name__ == "__main__":
    # Chama a função principal quando o script é executado
    main()
