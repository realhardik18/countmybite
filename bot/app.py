from flask import Flask,request

app=Flask(__name__)
app.secret_key = "countmybite"

@app.route("/")
def home():
    return "welcome"

@app.route("/whatsapp", methods=["POST"])
def bot():
    sender_number=request.values.get('From')
    print(sender_number)
    return 'ok'

app.run(port=5000,debug=True)