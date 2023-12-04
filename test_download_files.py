import requests
from selene import query
from selene.support.shared import browser


def test_download_pdf():
    browser.open("https://filesamples.com/formats/pdf")
    download_url = browser.element('[class="btn btn-blue col-span-3 md:col-span-1"]').get(query.attribute("href"))

    content = requests.get(url=download_url).content
    with open("tmp/pdf_file.pdf", 'wb') as file:
        file.write(content)


def test_download_xlsx():
    browser.open("https://filesamples.com/formats/xlsx")
    download_url = browser.element('[class="btn btn-blue col-span-3 md:col-span-1"]').get(
        query.attribute("href"))

    content = requests.get(url=download_url).content
    with open("tmp/xlsx_file.xlsx", 'wb') as file:
        file.write(content)


def test_download_csv():
    browser.open("https://filesamples.com/formats/csv")
    download_url = browser.element('[class="btn btn-blue col-span-3 md:col-span-1"]').get(
        query.attribute("href"))

    content = requests.get(url=download_url).content
    with open("tmp/csv_file.csv", 'wb') as file:
        file.write(content)
