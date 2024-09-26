import requests

cache = {}

def populate_cache_with_rates(currency_code):
    url = f"http://www.floatrates.com/daily/{currency_code.lower()}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return {}

def initialize_cache(currency_rates):
    if 'usd' in currency_rates:
        cache['usd'] = currency_rates['usd']['rate']
    if 'eur' in currency_rates:
        cache['eur'] = currency_rates['eur']['rate']


def convert_currency(source_currency, target_currency, amount):
    if target_currency in cache:
        rate = cache[target_currency]
        return round(amount * rate, 2)
    return None


def main():
    source_currency = input().strip().lower()
    currency_rates = populate_cache_with_rates(source_currency)

    initialize_cache(currency_rates)

    while True:
        target_currency = input().strip().lower()
        if target_currency == '':
            break

        amount_input = input().strip()
        try:
            amount = float(amount_input)
        except ValueError:
            print("Invalid amount.")
            continue

        print("Checking the cache...")

        if target_currency in cache:
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            if target_currency in currency_rates:
                cache[target_currency] = currency_rates[target_currency]['rate']
            else:
                print(f"Currency {target_currency.upper()} not available.")
                continue

        converted_amount = convert_currency(source_currency, target_currency, amount)
        if converted_amount is not None:
            print(f"You received {converted_amount} {target_currency.upper()}.")
        else:
            print("Conversion rate not found.")


if __name__ == '__main__':
    main()
