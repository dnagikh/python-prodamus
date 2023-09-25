# Prodamus hash verifier (HMAC)

Generate and verify Prodamus hash.

https://help.prodamus.ru/payform/integracii/rest-api/instrukcii-dlya-samostoyatelnaya-integracii-servisov#kak-prinyat-uvedomlenie-ob-uspeshnoi-oplate

## Installation
    
    pip install prodamuspy

## Usage

Init object:

    prodamus = prodamuspy.PyProdamus(API_TOKEN)

Parse query string to a dictionary:

    bodyDict = prodamus.parse(body)

Create signature:

    checkSign = prodamus.sign(bodyDict)

Verify signature:

    signIsGood = prodamus.verify(bodyDict, receivedSign)
    if signIsGood:
        print("Signature is awesome")
    else:
        print("Signature is incorrect")

## Copyright

Copyright 2023 [Max Arnold, Daniil Nagikh], all rights reserved.

This software is released under the MIT License.

A huge thank to https://github.com/max-arnold