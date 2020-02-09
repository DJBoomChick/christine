from flask import Flask
app = Flask (__name__)

Filey = open(file="C:\\Users\\christine\\Documents\\Tech Immersion\\Christine M. Nault Resume Web.htm", mode='r')
webstring = Filey.read()

@app.route('/')
def hello_world():
    return webstring

#@app.route('/admin)
#def iDontLikeYou():
#   return "You don't belong here"

if __name__ == '__main__':
    app.run()