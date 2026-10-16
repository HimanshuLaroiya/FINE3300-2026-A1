
import pandas as pd 

All_Exchange_Rate_Data = pd.read_csv("BankofCanadaExchangeRate.2026.csv")

class ExchangeRate: 
    def __init__ (self, amount, currency, exchange_rate_data): 
        self.amount = amount 
        self.currency = currency 
        self.exchange_rate_data = exchange_rate_data

    def Convert(self): 
        Rate_Row = self.exchange_rate_data[self.exchange_rate_data["Date"] == '2025-01-01']
        Exchange_Rate = Rate_Row["FXAUSDCAD"].values[0]
        
        if self.currency == 'CAD': 
            USD_Value = self.amount / Exchange_Rate
            return USD_Value
        
        elif self.currency == "USD" : 
            CAD_Value = self.amount * Exchange_Rate
            return CAD_Value 
        
        else:
             return 'Enter Valid Currency '
        
Amount_Input = float(input('Enter Amount: '))
Currency_Input = input ('Enter USD or CAD As the Currency: ').upper()

User_Input = ExchangeRate (Amount_Input, Currency_Input, All_Exchange_Rate_Data) 
Conversion = User_Input.Convert()

if isinstance(Conversion, (int, float)):
    if Currency_Input == "CAD":
        print (f"Your converted amount is: ${Conversion:.2f} USD")

    elif Currency_Input == "USD":
        print(f"Your converted amount is: ${Conversion:.2f} CAD")

else: 
    print(Conversion) 





