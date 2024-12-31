import random

class DemandPredictor:
    def predict_demand(self, inventory_data):
        print("Prevendo demandas futuras...")
        return {item: max(0, stock - random.randint(20, 50)) for item, stock in inventory_data.items()}
