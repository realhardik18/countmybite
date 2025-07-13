from flask import Flask,request
from datetime import datetime

app=Flask(__name__)
app.secret_key = "countmybite"
from utils import User

@app.route("/")
def home():
    return "welcome"

@app.route("/whatsapp", methods=["POST"])
def bot():
    sender_number=request.values.get('From')
    message_content=request.values.get('Body')
    time_sent=datetime.now().strftime('%d/%m/%Y, %H:%M:%S"')
    user=User(sender_number)
    user.log_message(
        content=message_content,
        from_number=sender_number,
        sent_at=time_sent
    )
    message_data={
        'content':message_content,
        'from':sender_number,
        'sent_at':time_sent
    }
    print(message_data)
    return 'ok'

app.run(port=5000,debug=True)