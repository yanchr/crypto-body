from binance.client import Client
import config

def simple_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("/showcoins"):
        message = "btc, eth, bnb, uni, vet, iota, btt, icx, ada, dot, doge, xrp"
        return message


    if user_message.find("/btc") != -1:
        user_message = user_message.replace("/btc", "")
        return user_message

    if user_message.find("/showvalue") != -1:
        user_message = user_message.replace("/showvalue ", "")
        client = Client(config.BINANCE_API_KEY, config.BINANCE_SECRET_API_KEY)
        crypto_price = client.get_symbol_ticker(symbol=user_message.upper())
        print("test3")
        roundedPrice = str(round(float(crypto_price.get('price')), 2))
        print("test4")
        return roundedPrice

    return "Who the fuck is that guy"