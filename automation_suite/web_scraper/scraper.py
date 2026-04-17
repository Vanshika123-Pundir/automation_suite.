import requests
from bs4 import BeautifulSoup

class WebScraper:

    def __init__(self, url):
        self.url = url

    def scrape_titles(self):
        try:
            response = requests.get(self.url)

            if response.status_code != 200:
                print("❌ Website access failed")
                return

            soup = BeautifulSoup(response.text, "html.parser")

            titles = soup.find_all("span", class_="titleline")

            print("\n📰 Latest Titles:\n")

            for i, title in enumerate(titles, start=1):
                print(f"{i}. {title.text}")

        except Exception as e:
            print("❌ Error:", e)