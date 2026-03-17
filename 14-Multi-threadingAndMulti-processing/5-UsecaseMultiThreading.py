"""
Real-World example: MultiThreading for I/O-bound Tasks
Scenario: Web Scraping
Web Scraping often involves making numerous network requests to fetch web pages.
These tasks are I/O-bound beacuse they spend a lot of time waiting for responses from servers.
MultiThreading can significantly improve the performance by allowing multiple web pages to be
fetched concurrently
"""

"""
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/

"""

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://python.langchain.com/v0.2/docs/introduction/",
    "https://python.langchain.com/v0.2/docs/concepts/",
    "https://python.langchain.com/v0.2/docs/tutorials/",
]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"Fetched {len(soup.text)} characters from {url}")


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")


"""
Most useful BeautifulSoup commands (cheat sheet)
| Task          | Code                        |
| ------------- | --------------------------- |
| Find element  | `soup.find()`               |
| Find all      | `soup.find_all()`           |
| By class      | `soup.find(class_="class")` |
| By id         | `soup.find(id="id")`        |
| Get text      | `.text`                     |
| Get attribute | `.get("href")`              |

"""
