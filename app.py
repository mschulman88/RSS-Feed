from bottle import route, static_file, request, run, get, error
import feedparser
import json


feed = feedparser.parse("http://feeds.videogamer.com/rss/allupdates.xml")


@route('/')
def index():
    return "Welcome to the Welcome Page. " \
           "<a href='/test'>Next page</a>"


@error(404)
def error404(error):
    # return 'Nothing here, sorry'
    return static_file("404.html", root='')


def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()
