import requests
from bs4 import BeautifulSoup

url = "https://fashionunited.ru/novostee/moda"

try:
    response = requests.get(url)
    response.raise_for_status()
    bs = BeautifulSoup(response.text, 'lxml')
    statements = bs.find_all('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-lg-3 e10gwzwj0 css-4cgb18')

    for statement in statements:
        print(statement)
        p2_element = statement.find('p2')
        h_element = statement.find('h')

        if p2_element is not None:
            p2_text = p2_element.text
        else:
            p2_text = "N/A"  # Set a default value if the element is not found

        if h_element is not None:
            h_text = h_element.text
        else:
            h_text = "N/A"  # Set a default value for the header

        print(f"Pair: {p2_text} - {h_text}")

except requests.RequestException as e:
    print(f"Error fetching content: {e}")
