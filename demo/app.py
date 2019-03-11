from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
"https://drive.google.com/open?id=1RSXzXfUPxr6kGophTV7jZwmYyYDc7uDX",
"https://drive.google.com/open?id=1vVX0hUBcuJBILQhrkZ7WDufTp7slBh9T",
"https://drive.google.com/open?id=1P1__YGPcl3sSdOBnqenQVvMv8xXjKS4n",
"https://drive.google.com/open?id=19PVegl47Ix193CdoXuCgIO1z60_arOf9"

]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
