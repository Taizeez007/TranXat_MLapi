import requests
import json
from api_key_utils import getAuthHeader

def responder():

     BASE_URL ="https://sandox.api.mastercard.com/openapis"

     uri=f'{ BASE_URL}/notification/transactions'

     CARD_REF="card reference from consent flow"

     trans=json.dumps(
       {
        "cardhoderAmount":9.99,
        "cardholderCurrency":"NGN",
        "cardReference":CARD_REF,
        "cardLastNumbers":2323,
        "merchandiseName":"NCC"
       }
    )
     authHeader=getAuthHeader(uri,method='POST', payload=trans)

     headerdict={
       'Authorization':authHeader,
       'Content-Type':'application/json'
    }


     response=requests.post(uri, headers=headerdict, data=trans)

     print(f'response={response.status_code}')