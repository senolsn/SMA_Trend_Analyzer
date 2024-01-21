import pandas as pd
import yfinance as yf
from tabulate import tabulate
from colorama import Fore, Style

def trend_analysis(symbol, moving_averages):
    stock = yf.Ticker(symbol)
    historical_data = stock.history(period="1y")

    ma_dict = {ma: historical_data['Close'].rolling(window=ma).mean() for ma in moving_averages}
    current_price = historical_data['Close'].iloc[-1]

    df = pd.DataFrame(index=["MA"], columns=moving_averages)
    df.index.name = symbol.split(".")[0]

    for ma, values in ma_dict.items():
        ma_value = values.iloc[-1]
        trend_symbol = "+" if current_price > ma_value else "-" if current_price < ma_value else "N/A"

        if trend_symbol == "+":
            colored_symbol = f"{Fore.GREEN}{trend_symbol}{Style.RESET_ALL}"
        elif trend_symbol == "-":
            colored_symbol = f"{Fore.RED}{trend_symbol}{Style.RESET_ALL}"
        else:
            colored_symbol = trend_symbol

        df[ma] = colored_symbol

    return df

user_input = input("Lütfen bir hisse senedi girin (Örneğin, AKBNK):")

symbol = f"{user_input}.IS"

check_moving_averages = [5, 9, 12, 15, 18, 21, 26, 50, 100, 200]

result = trend_analysis(symbol, check_moving_averages)

print(tabulate(result, headers='keys', tablefmt='fancy_grid', stralign="center"))