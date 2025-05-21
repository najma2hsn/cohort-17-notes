"""A small example of web scraping."""

from requests import get
from bs4 import BeautifulSoup
import json

def get_all_frontpage_articles():
    URL = "https://www.bbc.co.uk"

    response = get(URL + "/news")

    raw_page = response.text

    soup = BeautifulSoup(raw_page, features="html.parser")

    articles = []
    for heading in soup.find_all("li", class_="e1gp961v0"):
        url = heading.find("a")["href"]
        if url.startswith("/news"):
            title = heading.find("p").get_text()
            articles.append({
                "title": title,
                "url": URL + url,
                "category": heading.find("span", class_="e4wm5bw1").get_text()
            })

    return articles


if __name__ == "__main__":

    articles = get_all_frontpage_articles()

    article = articles[0]

    response = get(article["url"])

    soup = BeautifulSoup(response.content, features="html.parser")

    article["published"] = soup.find("time")["datetime"]

    print(article)
