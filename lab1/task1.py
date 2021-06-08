from page import Page
from helpers.htmlHelper import get_html, get_links, get_tree
from helpers.config import task1_url, pages_quantity, task1_output

link_iterator = 0
pages = [
    Page(task1_url, '')
]

while len(pages) < pages_quantity:
    try:
        current_link = pages[link_iterator].link
        current_page = get_html(current_link)
        pages[link_iterator].set_page(current_page)
        links_to_parse_quantity = pages_quantity - len(pages)
        links = get_links(current_page, links_to_parse_quantity)
        for link in links:
            page = Page(link, get_html(link))
            pages.append(page)
        link_iterator += 1
    except Exception as e:
        print(e)
        break

tree = get_tree(pages, pages_quantity)
tree.write(task1_output, pretty_print=True, xml_declaration=True, encoding="utf-8")
