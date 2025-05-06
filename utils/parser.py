from datetime import datetime


def extract_money_data(json_data):
    try:
        data = json_data["props"]["pageProps"]["money"]["data"]
        raw_currencies = data["monedas"]
        raw_exchange_rates = data["api"]["statistics"]

        currencies = [
            {
                "id": currency.get("id") or currency.get("_id"),
                "name": currency["Nombre"],
                "code": currency["short_show"],
                "flag_code": currency["flag_code"],
                "enabled": currency["enabled"]
            }
            for currency in raw_currencies
        ]

        exchange_rates = [
            {
                "currency_code": code,
                **stats
            }
            for code, stats in raw_exchange_rates.items()
        ]


        merged_data = {
            "currencies": currencies,
            "exchange_rates": exchange_rates,
        }

        return merged_data
    except KeyError:
        raise Exception("No se pudo encontrar la sección de los datos.")
