import requests
from bs4 import BeautifulSoup
import csv


URL = "https://www.kivano.kg/noutbuki?brands=acer-apple"
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "accept": "*/*",
}
LINK = "https://www.kivano.kg"
CSV_FILE = "laptop.csv"

def get_html(url, headers):
    response = requests.get(URL, headers=HEADERS)
    return response

def get_content_from_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    items = soup.findAll("div", class_="item product_listbox oh")
    laptops = []
    for item in items:
        laptops.append(
            {
                "title": item.find("div", class_="listbox_title oh").get_text().replace("\n", ""),
                "description": item.find("div", class_="product_text pull-left").get_text().replace("\n", ""),
                "price": item.find("div", class_="listbox_price text-center").get_text().replace("\n", ""),
                "img": LINK + item.find("img").get("src"),
            }
        )
    return laptops

def save_data(laptops: list) -> None:
    with open(CSV_FILE, "w") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["Title", "Description", "Price", "Img"])
        for laptop in laptops:
            writer.writerow([laptop["title"], laptop["description"], laptop["price"], laptop["img"]])



def get_result_parse():
    html = get_html(URL, HEADERS)
    if html.status_code == 200:
        laptops = get_content_from_html(html.text)
        save_data(laptops)
        return laptops

print(get_result_parse())


# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://cars.kg/offers/?vendor=57fa24ee2860c45a2a2c0905"
# URL_NBKR = "https://www.nbkr.kg/index.jsp?lang=RUS"
# HEADERS = {
#     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/106.0.0.0 Safari/537.36",
#     "accept": "*/*",
# }
#
#
# def get_html_nbkr(url, headers):
#     response = requests.get(URL_NBKR, headers=HEADERS)
#     return response
#
#
# html_nbkr = get_html_nbkr(URL_NBKR, HEADERS)
# soup_nbkr = BeautifulSoup(html_nbkr.text, "html.parser")
# exrate_all = soup_nbkr.find_all("td", class_="exrate")
# exrate = []
# for currency in exrate_all:
#     exrate.append(float(currency.get_text().replace("", "").replace(",", ".")))
#
#
# def get_html(url, headers):
#     response = requests.get(URL, headers=HEADERS)
#     return response
#
#
# def get_content_from_html(html_text):
#     soup = BeautifulSoup(html_text, "html.parser")
#     items = soup.find_all("a", class_="catalog-list-item")
#     mers = []
#     for item in items:
#         mers.append(
#             {
#                 "title": item.find("span", class_="catalog-item-caption").get_text().replace("", ""),
#                 "description": item.find("span", class_="catalog-item-descr").get_text().replace("\n", ""),
#                 "usage": item.find("span", class_="catalog-item-mileage").get_text().replace("", ""),
#                 "price": item.find("span", class_="catalog-item-price").get_text().replace("", ""),
#                 "price_som": str(round(int(item.find("span", class_="catalog-item-price").get_text().replace("", "")
#                                            [0:-2]) * exrate[1])) + " som",
#                 "image": item.find("img").get("src"),
#
#             }
#         )
#     for i in mers:
#         for key, value in i.items():
#             print(key, ":", value)
#
#
# def get_result_parse():
#     html = get_html(URL, HEADERS)
#     if html.status_code == 200:
#         get_content_from_html(html.text)
#
#
# get_result_parse()
