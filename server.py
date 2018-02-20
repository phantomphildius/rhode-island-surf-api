from flask import Flask
from flask import Response
from flask import request
import requests
import os
app = Flask(__name__)


@app.route('/forecast', methods=['GET'])
def fetch_surf_data():
    json = requests.get(build_request(request))

    return Response(
        json.text,
        status=json.status_code,
        content_type=json.headers['content-type']
    )


def build_request(request):
    api = os.environ['MAGIC_SEAWEED_API_KEY']
    fields = request.args['fields']
    spot_id = request.args['spot_id']
    url = 'https://magicseaweed.com/api/{}/forecast/?units=us&spot_id={}&fields={}'
    return url.format(api, spot_id, fields)


if __name__ == "__main__":
    app.run()
