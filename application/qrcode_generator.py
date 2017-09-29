import csv
import json
import qrcode
import requests

from application import app


def generate_qrcode(inputText):
    with app.app_context():

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

def generate_qrcode_batch_csv(inputFile):

    with app.app_context():

        with open(inputFile) as csvfile:
            reader = csv.reader(csvfile)
            data = []
            master = []  # to store tuples of both

            for inputRow in reader:
                app.logger.info(inputRow)
                img = qrcode.make(inputRow)
                img.save('uploads/stub.png')

                album = None
                image_path = 'uploads/stub.png'
                clientId = 'F5a0da0ee22b6b9' # Please get your own ClientId from imgur

                url = "https://api.imgur.com/3/image"
                payload = {'image': open(image_path, 'rb').read(), 'type': 'file'}
                headers = {'authorization': 'Client-ID ' + clientId}  # notice the space after Client-ID, concat

                response = requests.request("POST", url, data=payload, headers=headers) # post image anonymously to imgur

                # return json.dumps(response.text)

                temp_obj = json.loads(response.text) # json encode response again since it's a string
                app.logger.info(temp_obj)
                responseURL = temp_obj["data"]["link"]

                for x, y in zip(inputRow, responseURL):
                    master.append({x: y})

            app.logger.info(json.dumps({'data': master}, indent=3))

    return json.dumps({'data': master}, indent=3)

        # return responseURL


