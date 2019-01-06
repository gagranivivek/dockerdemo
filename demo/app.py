from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
"https://cdn.pixabay.com/photo/2013/07/25/13/01/stones-167089_960_720.jpg",
"https://cdn.pixabay.com/photo/2014/12/15/17/16/pier-569314_960_720.jpg"

]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")