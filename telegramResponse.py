from binance.client import Client
import config

def simple_responses(input_text):
    user_message = str(input_text).lower()

    if user_message == "/showcoins":
        message = "btc, eth, bnb, uni, vet, iota, btt, icx, ada, dot, doge, xrp"
        return message


    if user_message.find("/btc") != -1:
        user_message = user_message.replace("/btc", "")
        return user_message

    if user_message.find("/show") != -1:
        user_message = user_message.replace("/show ", "")
        client = Client(config.BINANCE_API_KEY, config.BINANCE_SECRET_API_KEY)
        crypto_price = client.get_symbol_ticker(symbol=user_message.upper() + "USDT")
        roundedPrice = str(round(float(crypto_price.get('price')), 2))
        return roundedPrice + "$"

    if user_message in ("/exit"):
        exit()
        return ''

    if user_message.find("/setalert") != -1:
        user_message = user_message.replace("/setalert ", "")
        messages = user_message.split()
        client = Client(config.BINANCE_API_KEY, config.BINANCE_SECRET_API_KEY)
        crypto_price = client.get_symbol_ticker(symbol=messages[0].upper() + "USDT")
        roundedPrice = round(float(crypto_price.get('price')), 2)
        way = 'test'
        print(roundedPrice)
        print(messages[1])
        way = ('under', 'over') [roundedPrice >= float(messages[1])]
        return messages[0] + ' is ' + way + ' your number'

    return "Who the fuck is that guy"