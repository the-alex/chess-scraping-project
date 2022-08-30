#!/usr/bin/env python3
"""
The goal of this file is to scrape a single

- [ ] Fetch a forum post
- [ ] Transform fetched response into a row of a CSV
- [ ] write `post url -> csv row` function

"""

from bs4 import BeautifulSoup
import requests
from pprint import pprint

# URL exmaple
# https://www.chess.com/forum/view/general/the-spine-opening
# Post example
# <div id="comment-somedums" class="comment-post-component vote-parent">

def fetch_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def find_posts(soup, post_class_string="comment-post-component"):
    # divs_containing_post_content = soup.findAll('div', {'class': post_class_string})
    return soup.findAll('div', {'class': post_class_string})

def parse_post(post):
    """parse a single html post object into record."""
    comment = post.find('div', {'class': "comment-post-body-component"})

    return list(filter(lambda c: c, map(lambda s: s.text.strip(), comment.children)))

def main():
    """Fetch a forum post, write the content to file."""
    url = "https://www.chess.com/forum/view/general/the-spine-opening"
    soup = fetch_soup(url)
    posts = find_posts(soup)

    pprint({
        # "name of thread": get_thread_name(posts),
        "number of posts": len(posts),
        "posts": [parse_post(p) for p in posts]
    })

    # for el in find_posts(soup):
    #     print("--------------------------------------------------------------------------------")
    #     print(el.prettify())
    # print(find_posts(soup))


if __name__ == '__main__':
    main()
