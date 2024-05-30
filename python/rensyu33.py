#親クラスの定義
class Car():
    def __init__(self) -> None:
        self.gasoline = 40.0
    
    def refuel(self):
        self.gasoline += 10.0

#サブクラスの定義
class HybridCar(Car):
    def __init__(self) -> None:
        super().__init__()
        self.battery = 90.0

    def charge(self):
        self.battery += 10.0

#TeslaCarクラスの定義
class TeslaCar(HybridCar):
    def __init__(self) -> None:
        super().__init__()
        self.price = 1000

    def run(self):
        self.battery -= 10

tesla = TeslaCar()
tesla.run()
tesla.run()
tesla.run()
tesla.run()
print(tesla.battery) 