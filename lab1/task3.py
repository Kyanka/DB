from lxml import etree
from helpers.htmlHelper import get_html
from helpers.config import task3_url, goods_quantity, task3_output

page = ''
goods_html = []
goods_price_html = []

#all goods characteristics
names = []
images = []
prices = []

for i in range(2):
    url = task3_url + str(i+1) + "/"
    page = get_html(url)
    goods_html += page.xpath("//div[@class='center_block']")
    goods_price_html += page.xpath("//div[@class='right_block']")

goods_html = goods_html[:goods_quantity]
goods_price_html = goods_price_html[:goods_quantity]

for good in goods_html:
    name_good = good.xpath(".//h3/a/text()")[0]
    names.append(name_good)

    image_url_good = good.xpath(".//img/@src")[0]
    images.append(image_url_good)

for good in goods_price_html:
    price_good = good.xpath(".//div[@class='content_price']/span/text()")[0]
    prices.append(price_good)

root = etree.Element('data')

for i in range(goods_quantity):
    data = etree.SubElement(root, 'good')

    name = etree.SubElement(data, 'name')
    name.text = names[i]

    price = etree.SubElement(data, 'price')
    price.text = prices[i]

    image_url = etree.SubElement(data, 'image')
    image_url.text = images[i]

tree = etree.ElementTree(root)
tree.write(task3_output, pretty_print=True, xml_declaration=True, encoding="utf-8")


