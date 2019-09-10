import base64
from datetime import datetime
from mpesa import keys


def format_date():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    return formatted_time

def decode_password():
    formatted_time = format_date()
    data_to_encode = keys.business_shortcode+keys.lipa_na_mpesa_passkey+formatted_time
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode("utf-8")

    return decoded_password
