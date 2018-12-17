from bottle import route, static_file, request, run, get, error
import feedparser
import json
from time import time


feed = feedparser.parse("http://feeds.videogamer.com/rss/allupdates.xml")
title1 = feed["entries"][0]["title"]
links1 = feed["entries"][0]["link"]

title_list = [title for title in feed["entries"]]
print(title1)

articles = [
    {"title": title1 , "link": links1}
]

@route('/')
def index():
    return static_file("index.html", root='')


@route('/static/css/style.css')
def css():
    return static_file("style.css", root='static/css')


@route('/static/js/logic.js')
def js():
    return static_file("logic.js", root='static/js')


@route('/headlines', method='GET')
def get_headlines():
    return json.dumps(articles)


@route('/images/<filename:re:.*\.(jpg|png)>', method='GET')
def images(filename):
    return static_file(filename, root='static/images')


@error(404)
def error404(error):
    return static_file("404.html", root='')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
