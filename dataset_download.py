from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from requests.api import get


def get_links():
    html = requests.get('https://datasets.imdbws.com/').text
    soup = BeautifulSoup(html, "html.parser")
    hrefs = soup.find_all('a', href=True)

    links = [link['href'] for link in hrefs if link['href'].endswith('.gz')]
    return links


def download_url(links, chunk_size=128):

    for url in links:
        file_name = url.split('/')[-1]
        print(f'{file_name} is downloading...')
        r = requests.get(url, stream=True)
        with open(file_name, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)


def main():
    links = get_links()
    download_url(links)


if __name__ == '__main__':
    main()
