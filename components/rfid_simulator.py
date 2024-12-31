import random

class RFIDSensor:
    def __init__(self):
        self.items = ["Produto A", "Produto B", "Produto C"]

    def simulate_readings(self):
        print("Simulando leituras de sensores RFID...")
        return {item: random.randint(50, 200) for item in self.items}
