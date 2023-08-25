import requests

URL = 'https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple'

def main():

    data = requests.get(URL).json()

main()