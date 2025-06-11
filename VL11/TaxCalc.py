class TaxCalculator: 
    def __init__(self, vat: float = 0.19):
        self.vat = vat
    
    def to_net(self, price: float) -> float:
        return price / (1.0 + self.vat)

    def to_gross(self, price: float) -> float: 
        return (1.0 + self.vat) * price

class EURTaxCalculator(TaxCalculator):
    def __init__(self, vat: float = 0.19):
        super().__init__(vat=vat)

    def to_net(self, price):
        return f"{super().to_net(price)} EUR" 
    
    def to_gross(self, price):
        return f"{super().to_gross(price)} EUR"

if __name__ == "__main__":
    calc = TaxCalculator()
    print(calc.to_gross(100))
    print(calc.to_net(238))

    print("--------------")
    calc = EURTaxCalculator(vat = 0.20)
    print(calc.to_gross(100))
    print(calc.to_net(238))