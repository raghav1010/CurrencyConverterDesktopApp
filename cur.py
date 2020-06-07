import io
import pyqrcode
from base64 import b64encode
import eel
import requests
eel.init('web')


@eel.expose
def dll(dt,f,to):
    base_url = 'https://api.exchangeratesapi.io/latest'
    url = base_url + '?base=' + f + '&symbols=' + to
    response = requests.get(url)
    if (response.ok is False):
        return "invalid request"
    else:
        data = response.json()
        total = int(dt)*data['rates'][to]
        return total



eel.start('currency.html', size=(600, 600))
