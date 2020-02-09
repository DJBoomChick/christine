import urllib.request
import json
import sys


def issnow():
    req = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
    html = req.read()

    j = json.loads(html.decode("utf-8"))
    for x in j:
        print(x,j[x])


def isspass():
    req = urllib.request.urlopen("http://api.open-notify.org/iss-pass.json?lat=43.1420982&lon=-87.9200786")
    html = req.read()
    print("HTML", html)
    j = json.loads(html.decode("utf-8"))
    print("Type", type(j))
    print("J", j)

    for x in j:
        print("Key (x)=", x, "Value (j[x])=", j[x])


def issastros():
    req = urllib.request.urlopen("http://api.open-notify.org/astros.json")
    html = req.read()

    j = json.loads(html.decode("utf-8"))
    for x in j:
        print(x, j[x])


if __name__ == "__main__":
    try:
        option = sys.argv[1]
    except:
        option = "two"
    if option == "one":
        issnow()
    elif option == "two":
        isspass()
    elif option == "three":
        issastros()
