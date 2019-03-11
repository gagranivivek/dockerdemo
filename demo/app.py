from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
	"https://photos.app.goo.gl/3SxFvGnJx39MAsnWA",
	"https://photos.app.goo.gl/d5hKgYMoDhq3tHD29",
	"https://photos.app.goo.gl/8BxmVFzQvpJVzw5f6",
	"https://photos.app.goo.gl/Z4R7jhTscezuoKfD6"

]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
