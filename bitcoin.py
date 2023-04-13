import sys


API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    try:
        bitcoins = float(sys.argv[1])
    except (IndexError, ValueError):
        print("Error: please enter a valid number of Bitcoins")
        sys.exit(1)
    
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        price = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        total_cost = bitcoins * price
        print(f"{bitcoins} Bitcoins = ${total_cost:.4f}")
    except (requests.RequestException, ValueError, KeyError):
        print("Error: unable to get current Bitcoin price")
        sys.exit(1)


if __name__ == "__main__":
    main()
