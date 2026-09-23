import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Website accessed successfully!\n")

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print("Books found:\n")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        print("Title:", title)
        print("Price:", price)
        print("-" * 40)

else:
    print("Failed to access the website.")
    print("Status code:", response.status_code)