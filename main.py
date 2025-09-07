from Hajime import *

app = Hajime()

@app.route("/")
def main(environ):
    return "hello to Hajime!"

app.launch()