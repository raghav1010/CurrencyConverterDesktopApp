import logging

import eel
import requests

from constants import XCHANGE_BASE_URL

eel.init('web')


def fetch_xchange_rates(base_cur, req_cur):
    url = XCHANGE_BASE_URL + '?base=' + base_cur + '&symbols=' + req_cur
    try:
        response = requests.get(url)
    except Exception as exc:
        logging.info('Something went wrong while fetching xchange rates: {}'.format(str(exc)))
        return None
    return response


def format_xchange_response(response):
    if not response.ok:
        return None
    response_json = response.json()
    print("response_json: {}".format(response_json))
    currency_rate = response_json.get('rates', {})
    return currency_rate


@eel.expose
def convert_currency_amount(amount, base_cur, req_cur):
    xchange_response = fetch_xchange_rates(base_cur, req_cur)
    if not xchange_response:
        return 100

    xchange_rates = format_xchange_response(xchange_response)
    if not xchange_rates:
        return 100

    converted_amount = int(amount) * xchange_rates[req_cur]
    return converted_amount


eel.start('currency.html', size=(600, 600))
