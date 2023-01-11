from hmac_prodamus import HmacProdamus

API_SECRET = 'API_SECRET_HERE'

query_dict = {
    'order_id': 'ORDER_ID',
    'customer_phone': 'CUSTOMER_PHONE',
    'customer_email': 'CUSTOMER_EMAIL',
    'products': [
        {
            'name': 'PRODUCT NAME',
            'price': 100,
            'quantity': '1',
            'tax': {
                'tax_type': 0,
                'tax_sum': 0,
            },
            'paymentMethod': 1,
            'paymentObject': 4,
        }
    ],
    'do': 'link',
    'urlReturn': 'RETURN_URL',
    'urlSuccess': 'SUCCESS_URL',
    'urlNotification': 'NOTIFICATION_URL',
}

signature = HmacProdamus.create(API_SECRET, query_dict)
verify = HmacProdamus.verify(API_SECRET, query_dict, signature)

print(f'Signature is: {signature}, verifying: {verify}')
