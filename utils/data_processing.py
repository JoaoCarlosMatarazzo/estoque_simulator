import pandas as pd

def load_inventory_data(json_file_path):
    """
    Carrega os dados de inventário a partir de um arquivo JSON.

    :param json_file_path: Caminho do arquivo JSON contendo os dados do inventário.
    :return: Um DataFrame do Pandas com os dados do inventário.
    """
    try:
        data = pd.read_json(json_file_path)
        print(f"Dados de inventário carregados com sucesso de {json_file_path}.")
        return data
    except Exception as e:
        print(f"Erro ao carregar dados de inventário: {e}")
        return pd.DataFrame()

def save_inventory_data(data, json_file_path):
    """
    Salva os dados de inventário em um arquivo JSON.

    :param data: DataFrame contendo os dados do inventário.
    :param json_file_path: Caminho do arquivo JSON para salvar os dados.
    """
    try:
        data.to_json(json_file_path, orient='records', indent=4)
        print(f"Dados de inventário salvos com sucesso em {json_file_path}.")
    except Exception as e:
        print(f"Erro ao salvar dados de inventário: {e}")

def calculate_inventory_summary(data):
    """
    Calcula um resumo estatístico básico do inventário.

    :param data: DataFrame contendo os dados do inventário.
    :return: Um dicionário com informações como estoque médio, mínimo e máximo.
    """
    try:
        summary = {
            "Total Items": len(data),
            "Average Stock": data['stock'].mean(),
            "Min Stock": data['stock'].min(),
            "Max Stock": data['stock'].max()
        }
        return summary
    except KeyError as e:
        print(f"Erro: a coluna esperada não foi encontrada - {e}")
        return {}
