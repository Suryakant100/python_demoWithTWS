from twilio.rest import Client
# from config import auth_token,account_sid,phone_number
account_sid = 'AC04dca23dd640ca87068b062ccc2b42aa'
auth_token = '26bc6d43e0a278d70181ddc0af840d16'
phone_number='+919521421694'

def get_twilio_connection(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    return client

client = get_twilio_connection(account_sid, auth_token)

def send_whatsapp_text(client, quote):
    """
    Send a WhatsApp text message using the Twilio API.

    Parameters:
        client (Client): Twilio client object.
        quote (str): Text message to be sent.
        to_phone_number (str): Receiver's phone number.

    Returns:
        str: Twilio message SID.
    """
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=quote,
        to=phone_number
    )
    return message.sid


# print(client)





