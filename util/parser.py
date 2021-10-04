import urllib.request
from bs4 import BeautifulSoup


def check_price_title(article: int):
    page = urllib.request.urlopen(f'https://www.wildberries.ru/catalog/{article}/detail.aspx')
    scr = page.read()
    soup = BeautifulSoup(scr, 'lxml')
    title = soup.title.string  # Название товара
    price = soup.find('meta', itemprop='price')  # получаем цену
    brand = soup.find('meta', itemprop='brand')  # получаем Брэнд
    order_count = 0
    for st in list(soup.find_all('script')):  # Вытаскиваем кусок в котором есть ssrModel
        if 'ssrModel' in str(st):
            temp = str(st).split(':')
            for d in temp:
                if 'ordersCount' in d: 
                    index = temp.index(d)
                    if str(article) in temp[index]:
                        temp[index+1].split(',')
                        order_count = temp[index+1].split(',')[0]
    print(title)
    print(price.get('content'))
    print(brand.get('content'))
    print(order_count)
