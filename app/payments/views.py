from django.shortcuts import render
from fintoc import Fintoc
import random
# Create your views here.
from django.shortcuts import render
from config.settings import SK_FINTOC, PK_FINTOC

def payments(request):
    price = random.randint(100,10000)
    fintoc_client = Fintoc(SK_FINTOC)
    


    payment_intent = fintoc_client.payment_intents.create(
        currency="CLP",
        amount=price,
        recipient_account={
            "holder_id": "111111111",
            "number": "123123123",
            "type": "checking_account",
            "institution_id": "cl_banco_de_chile",
        }
    )



    context = {
        'holderType':'individual',
        'product':'payments',
        'publicKey':PK_FINTOC,
        'webhookUrl':'	https://webhook.site/48283ac6-bc27-44ae-a021-197536c720ff',
        'country':'cl',
        'widgetToken':payment_intent.widget_token,
        'price': price
    }

    return render(request, "payments.html", context=context)