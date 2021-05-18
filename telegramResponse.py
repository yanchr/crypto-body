def simple_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("/showavailablecoins"):
        message = "btc, eth, bnb, uni, vet, iota, btt, icx, ada, dot, doge, xrp"
        return


    if user_message.find("/btc") != -1:
        user_message = user_message.replace("/btc", "")
        return user_message

    return "Who the fuck is that guy"