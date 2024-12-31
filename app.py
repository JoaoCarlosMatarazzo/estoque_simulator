from components.rfid_simulator import RFIDSensor
from models.demand_forecast import DemandPredictor
from utils.report_generator import generate_report

def main():
    print("Bem-vindo ao Sistema Inteligente de Gerenciamento de Inventário")

    # Inicialização dos sensores
    sensor = RFIDSensor()
    inventory_data = sensor.simulate_readings()

    # Previsão de demanda
    predictor = DemandPredictor()
    forecast = predictor.predict_demand(inventory_data)

    # Gerar relatório
    generate_report(inventory_data, forecast)

if __name__ == "__main__":
    main()
