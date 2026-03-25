import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select("article.product_pod")

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["Book Name", "Price"])
    
    for book in books:
        name = book.h3.a["title"]
        price = book.select_one(".price_color").text
        
        writer.writerow([name, price])

print("Data saved to books.csv")
