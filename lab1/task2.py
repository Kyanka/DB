from lxml import etree
import statistics
from helpers.config import task1_output

tree = etree.parse(task1_output)
text_fragments = tree.xpath("//page/fragment[@type='text']")
average = int(statistics.mean(list(map(lambda fragment: fragment.xpath('count(./text)'), text_fragments))))
print(f'Average quantity of text fragments: {average}')


