# MercadoLibre's Python SDK

Python SDK for MercadoLibre's Platform.


NOTE: we DO NOT have any rights on Mercado Libre trademark. This work is just to contribute to the Open Source community using public MeLi APIs.

## How do I install it?

    1) Download or clone repository 
       https://github.com/joacoRamone/meli-python-sdk.git
    2) cd meli-pythonSDK
    3) python setup.py install

NOTE: it requires requests>=1.1.0

## Design considerations

This module has two main components:
* core.py -> http methods (GET,POST,PUT,DELETE,Authorization)
* meliresources.py -> Mercado Libre resources from http://developers.mercadolibre.com/API-directory/

## How do I use it?

### Create an instance of MeliCore class
 
```python
CLIENT_ID = 'your app id'
CLIENT_SECRET = 'your app secret'

meli = MeliCore(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
```

You can create an instance of MeliCore without client credentials, but on this case you'll be not allowed to call resources where access token is required.

### Authorization

meli-python-sdk provides the server side authorization using OAuth2. For more details see http://developers.mercadolibre.com/authentication-and-authorization/

Step 1: Obtain a code

```python
auth_url = meli.get_auth_url("your_redirect_URI")
```

If the user grants your application the requested data permission the OAuth Dialog will redirect the user's browser to the URL you specified in the redirect_url together with an authorization code. This redirect uses the HTTP 302 status code. The URL will look like this:

    http://YOUR_URL?code=SERVER_GENERATED_AUTHORIZATION_CODE

Step 2: Exchange the code for a token

By using this code you can perform the next step: app authentication.

```python
meli.authorize(SERVER_GENERATED_AUTHORIZATION_CODE, redirect_URI="your_redirect_URI")
```

### Calling resources

All calls to MELi resources are executed by generic query_url() method. This returns a JSONobject. Some examples:

#### GET method

```python
categories = meli.query_url(resource_part=meliresources.CATEGORY_DETAILS,
                                    method='GET',
                                    ids={'categ_id':category},
                                    attributes=['name','children_categories'])
print categories
```

#### POST method

```python
# add new description example
item_id = 'item id'
body = {'text':'new description'}
result = meli.query_url(resource_part=meliresources.ITEM_DESCRIPTION,
                                    method='POST',
                                    ids={'item_id':item_id},
                                    access_token=True,  # we need the access token for data update
                                    body=body)
print result
```

#### PUT method

```python
# add one payment method
USERID = 'user id'
body = {'id':'redlink',
        'name':'RedLink',
        'payment_type_id':'atm',
        'thumbnail':'http://img.mlstatic.com/org-img/MP3/API/logos/redlink.gif',
        'secure_thumbnail':'https://www.mercadopago.com/org-img/MP3/API/logos/redlink.gif'}
result = meli.query_url(resource_part=meliresources.USER_PAYMENT_METHODS_DETAILS,
                                 method='PUT',
                                 ids={'user_id':USERID,'pay_id':'redlink'},
                                 access_token=True,  # we need the access token for data update
                                 body=body)
print result
```

#### DELETE method

```python
# remove one payment method
USERID = 'user id'
result = meli.query_url(resource_part=meliresources.USER_PAYMENT_METHODS_DETAILS,
                                     method='DELETE',
                                     ids={'user_id':USERID,'pay_id':'redlink'},
                                     access_token=True)  # we need the access token for data update
print result
```

## Contribution

Feel free to get the code and play around with it. Any contribution is fully appreciated.

## Contact

* Joaquin Orbe
* e-mail: joaquin_orbe (at) edsa (dot) com (dot) ar
* Twitter: @joacOrbe
* web: http://www.edsa.com.ar
    
## License

See LICENSE.txt
 