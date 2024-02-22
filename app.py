from pywa import WhatsApp
from flask import Flask
from pywa.types import Message, CallbackButton
# from pywa.filters import  CallbackFilter
import requests
# import mysql.connector


def gpt(uid,text):
    headers={'Content-Type': 'application/json'}
    body = {
        "user_id":uid,
        "prompt":text

    }
    r = requests.post('http://127.0.0.1:5002/chat',headers=headers,json=body)
    print(r)
    ans = r.json()
    print(ans)
    if 'filename' not in ans:
        anss = ans['message']['content']
        return anss
    else:
        return 'hi'

    


flask_app = Flask(__name__)
wa = WhatsApp(
    phone_id='229272100273078',
    token='EAAMJMlCpt8wBOxbO5sGnDSs2SQmyDYsdstRLH4yCQQKJJfO94KDF20kC1LLtg63TpdlLGuZAjkr6QAJyGZAsFLBFFhMi33BEySpP6SaEMdOFe1Nw6It5WXMI55BUbRWpcoCwXh6gEezS9jh0ZApcIMVwYFiHHw3I3nPAiaRkB3TrF9w6a7ZCLytgUtItaeMZAvszb43QkgcBa55FoJvYZD',
    server=flask_app,
    verify_token='asd',
)

@wa.on_message()
def hello(client: WhatsApp, message: Message):
    # message.react('👋')
    print(message)
    uid = message.from_user.wa_id
    msg = message.text
    reply = gpt(uid,msg)
    if type(reply) == str:
        message.reply_text(
            text=reply,
        )
    else:
        message.reply_document(
        "invoice.pdf",
        # document="invoice.pdf",
        body="invoice.pdf"
       
    )
    print('pdf send')

# @wa.on_callback_button(CallbackFilter.data_startswith('id'))
# def click_me(client: WhatsApp, clb: CallbackButton):
#     clb.reply_text('You clicked me!')

flask_app.run(port=5005)  # Run the flask app to start the webhook
