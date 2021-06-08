import requests
from lxml import html, etree


def get_html(url: str):
    headers = {'Content-Type': 'text/html'}
    response = requests.get(url, headers=headers)
    return html.fromstring(response.text)


def get_links(page: any, links_quantity: int):
    links = page.xpath('//a/@href')
    valid_links = list(filter(lambda link: 'uartlib.org' in link, links))
    return valid_links[:links_quantity]


def get_text_elements(page: any):
    texts = []
    elements = page.xpath('body//*[not(self::script or self::style or self::img)]/text()')
    for element in elements:
        text = element.strip('\n\t\r ')
        if len(text):
            texts.append(text)
    return texts


def get_tree(page: any, quantity: int):
    root = etree.Element('data')
    for i in range(quantity):
        current_page = page[i]

        page_element = etree.SubElement(root, 'page')
        page_element.set('url', current_page.link)

        text_fragment = etree.SubElement(page_element, 'fragment')
        text_fragment.set('type', 'text')
        text_elements = get_text_elements(current_page.page)
        # get text
        for element in text_elements:
            text = etree.SubElement(text_fragment, 'text')
            text.text = element

        image_fragment = etree.SubElement(page_element, 'fragment')
        image_fragment.set('type', 'image')
        image_elements = current_page.page.xpath('body//img/@src')
        # get img
        for element in image_elements:
            image = etree.SubElement(image_fragment, 'image')
            image.text = element

    tree = etree.ElementTree(root)
    return tree
