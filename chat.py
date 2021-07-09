from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    msg_recebida = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    respondido = False

    if 'oi' in msg_recebida:
        msg.body("Oi!!!")
        respondido = True

    elif "tchau" in msg_recebida:
        msg.body("Tchauuu!!!")
        respondido = True      
    
    if not respondido:
        msg.body("Nao entendi! ")

    return str(resp)


if __name__ == '__main__':
    app.run()