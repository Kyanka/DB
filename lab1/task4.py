from lxml import etree
from helpers.config import task3_output, task4_xsl, task4_output

goods = etree.parse(task3_output)
xsl = etree.parse(task4_xsl)

transform = etree.XSLT(xsl)
html = transform(goods)

html.write(task4_output, pretty_print=True, encoding="utf-8")