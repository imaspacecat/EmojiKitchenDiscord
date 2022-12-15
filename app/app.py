from flask import Flask, request, render_template, send_file
import json, requests, base64
from PIL import Image
from io import BytesIO


app = Flask(__name__)

# https://www.gstatic.com/android/keyboard/emojikitchen/${potentialDate}/${leftEmoji}/${leftEmoji}_${rightEmoji}.png
url_root = "https://www.gstatic.com/android/keyboard/emojikitchen/"
emoji_url = ""

# {\"leftEmoji\": \"1fa84\", \"rightEmoji\": \"2615\"}
# 20210521


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


# https://stackabuse.com/how-to-get-and-parse-http-post-body-in-flask-json-and-form-data/


f = open(r"C:\\Users\\yotam\\code\\EmojiKitchenThing\\app\\data\\emojiData.json", "r")
data = json.loads(f.read())
# {\"leftEmoji\": \"1fa84\", \"rightEmoji\": \"2615\"}

# print(data)
left = "1fa84"
right = "2615"


@app.route("/", methods=["POST"])
def sendEmoji():
    global left, right
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
        left = data["leftEmoji"]
        right = data["rightEmoji"]
        print("rightEmoji:", data["rightEmoji"])
        print("leftEmoji:", data["leftEmoji"])
        return data
    else:
        return 'Content-Type not supported!'
    

@app.route("/emoji")
def emoji():
    date = 0
    print(left + "|", right + "|")
    for entry in data[left]:
        if entry["leftEmoji"] == left and entry["rightEmoji"] == right:
            date = entry["date"]

    if date == 0:
        for entry in data[right]:
            if entry["leftEmoji"] == left and entry["rightEmoji"] == right:
                date = entry["date"]
    emoji_url = url_root + str(date) + "/u" + left + "/u" + left + "_u" + right + ".png"
    
    response = requests.get(emoji_url)
    img = Image.open(BytesIO(response.content))
    img = img.convert('RGBA')
    img.thumbnail((50, 50))
    img.save("static/emoji.png")
    # return send_file("emoji.png", mimetype='image/gif')
    return render_template("index.html")