from flask import Flask, render_template
import random

app = Flask(__name__)

# list of Leh Ladaakh
images = [
"https://drive.google.com/file/d/19PVegl47Ix193CdoXuCgIO1z60_arOf9/view?usp=sharing"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
