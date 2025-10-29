from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Твой Telegram Bot
BOT_TOKEN = "7752486636:AAExMvL7ReohDs3ssh_PqV_6583SEYCULxI"
CHAT_ID = "7752486636"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    text = f"📩 Новое сообщение!\nИмя: {name}\nEmail: {email}\nСообщение:\n{message}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    try:
        response = requests.post(url, data={"chat_id": CHAT_ID, "text": text})
        if response.status_code == 200:
            return "✅ Сообщение отправлено!"
        else:
            return f"❌ Ошибка отправки: {response.text}"
    except Exception as e:
        return f"❌ Ошибка: {e}"

if __name__ == "__main__":
    app.run(debug=True)




