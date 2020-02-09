from flask import Flask
import urllib.request
import json
import sys

app = Flask (__name__)

Filey = open(file="C:\\Users\\christine\\Documents\\Tech Immersion\\Christine M. Nault Resume Web XKCD.htm", mode='r')
webstring = Filey.read()


@app.route('/')
def hello_world():
    return webstring


@app.route('/xkcd')
def xkcd():
    req = urllib.request.urlopen("http://xkcd.com/info.0.json")
    html = req.read()

    j = json.loads( html.decode("utf-8"))
    imgsrc = "<img src='{}'>".format( j['img'] )
    return imgsrc

#@app.route('/admin)
#def iDontLikeYou():
#   return "You don't belong here"

if __name__ == '__main__':
    app.run()