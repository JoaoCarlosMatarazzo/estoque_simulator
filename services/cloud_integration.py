import json

class CloudServiceSimulator:
    """
    Classe para simular uma integração com um serviço de computação em nuvem.
    """

    def __init__(self, cloud_storage_path):
        """
        Inicializa o simulador com o caminho do arquivo que simula o armazenamento na nuvem.

        :param cloud_storage_path: Caminho para o arquivo local que representa o armazenamento na nuvem.
        """
        self.cloud_storage_path = cloud_storage_path

    def upload_data(self, data):
        """
        Simula o upload de dados para o serviço de nuvem.

        :param data: Dados a serem enviados (geralmente um dicionário ou lista).
        """
        try:
            with open(self.cloud_storage_path, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Dados enviados para a nuvem simulada em {self.cloud_storage_path}.")
        except Exception as e:
            print(f"Erro ao enviar dados para a nuvem: {e}")

    def download_data(self):
        """
        Simula o download de dados do serviço de nuvem.

        :return: Dados baixados como um dicionário ou lista.
        """
        try:
            with open(self.cloud_storage_path, 'r') as file:
                data = json.load(file)
            print(f"Dados baixados da nuvem simulada de {self.cloud_storage_path}.")
            return data
        except FileNotFoundError:
            print(f"Arquivo {self.cloud_storage_path} não encontrado. Nenhum dado disponível.")
            return {}
        except Exception as e:
            print(f"Erro ao baixar dados da nuvem: {e}")
            return {}

# Exemplo de uso:
if __name__ == "__main__":
    cloud_service = CloudServiceSimulator("cloud_storage.json")

    # Simular upload de dados
    inventory_data = {
        "Produto A": 100,
        "Produto B": 200,
        "Produto C": 150
    }
    cloud_service.upload_data(inventory_data)

    # Simular download de dados
    downloaded_data = cloud_service.download_data()
    print("Dados baixados:", downloaded_data)
