import qrcode
import json
import requests
from imgurpython import ImgurClient
# from .form import QRForm # import QRForm class from form like in views.py
from application import app


def generate_qrcode(inputText):
    with app.app_context():

        # form = QRForm()
        # inputText = form.qrtext.data

        img = qrcode.make(inputText)
        img.save('qrcode.png')

        album = None
        image_path = 'qrcode.png'
        clientId = 'F5a0da0ee22b6b9' # Please get your own ClientId from imgur

        url = "https://api.imgur.com/3/image"
        payload = {'image': open(image_path, 'rb').read(), 'type': 'file'}
        headers = {'authorization': 'Client-ID ' + clientId}  # notice the space after Client-ID, concat

        response = requests.request("POST", url, data=payload, headers=headers) # post image anonymously to imgur

        # return json.dumps(response.text)

        temp_obj = json.loads(response.text) # json encode response again since it's a string
        app.logger.info(temp_obj)
        responseURL = temp_obj["data"]["link"]

        return responseURL



