from mpesa import keys
from mpesa import access_token
from mpesa import utils

import requests


class Lipa_na_mpesa():
    """Lipa_na_mpesa class initiates the online payment."""

    def __init__(self):
        self.my_access_token = access_token.generate_access_token()
        self.decoded_password = utils.decode_password()
        self.formatted_time = utils.format_date()
        self.phone_number = keys.phone_number
        self.business_shortcode = keys.business_shortcode

    def pay(self,amount):
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization":"Bearer %s"%self.my_access_token}
        request = {
            "BusinessShortCode": self.business_shortcode,
            "Password": self.decoded_password,
            "Timestamp": self.formatted_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": str(amount),
            "PartyA": self.phone_number,
            "PartyB": self.business_shortcode,
            "PhoneNumber": self.phone_number,
            "CallBackURL": "https://bestchick01.herokuapp.com/",
            "AccountReference": "12345678",
            "TransactionDesc": "Pay Testing Fees",
        }
        response = requests.post(api_url, json=request, headers = headers)
        return response

        def change_phone_number(self,phone_no):
            self.phone_number = phone_no

lnp = Lipa_na_mpesa()
lnp.pay(10)
