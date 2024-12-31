def generate_report(inventory_data, forecast):
    print("\n--- Relatório de Inventário ---")
    for item, stock in inventory_data.items():
        print(f"{item}: Estoque Atual: {stock}, Previsão de Demanda: {forecast[item]}")
    print("\nRelatório gerado com sucesso!")
