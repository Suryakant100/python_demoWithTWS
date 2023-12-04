import requests
from twilio_conn import send_whatsapp_text,client


# url = "https://quotes.rest/qod?language=en"
# headers = {
#     'accept': 'application/json',
#     'Authorization': 'Bearer NPqPjRKqqIMc2cgGCT4UMy2g2SXVfai3Q5tOcuHz'
# }
# response = requests.get(url, headers=headers)
# data=response.json()
# print(data)
# print(data["contents"]['quotes'][0]['quote'])
# quote = data['contents']['quotes'][0]['quote']
# print(quote)

# Function to get quotes of the day
def get_quotes_of_day(category):
    url = "https://quotes.rest/qod?language=en&category={}".format(category)
    headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer NPqPjRKqqIMc2cgGCT4UMy2g2SXVfai3Q5tOcuHz'
     }
    response = requests.get(url, headers=headers)
    data=response.json()
    status=response.status_code
    quote=""
    match status:
        case 200:
            quote = data['contents']['quotes'][0]['quote']
        case 400:
            quote = data['error']['message'] 
        case 429:
            quote = data['message'] 
        case _:
            quote = "Sorry, could not get the the quote"
    return quote

quote=get_quotes_of_day(category="inspire")
# print(quote)
send_whatsapp_text(client,quote)

# Example
"""
data_dict={
  "success": {
    "total": 1
  },
  "contents": {
    "quotes": [
      {
        "quote": "Do not worry if you have built your castles in the air. They are where they should be. Now put the foundations under them.",
        "length": "122",
        "author": "Henry David Thoreau",
        "tags": [
          "dreams",
          "inspire",
          "worry"
        ],
        "category": "inspire",
        "date": "2016-11-21",
        "title": "Inspiring Quote of the day",
        "background": "https://theysaidso.com/img/bgs/man_on_the_mountain.jpg",
        "id": "mYpH8syTM8rf8KFORoAJmQeF"
      }
    ]
  }
}

print(data_dict['contents']['quotes'][0]['quote'])
"""