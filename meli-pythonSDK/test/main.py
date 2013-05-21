'''
@author: Joaquin Orbe 
@email: joaquin_orbe@edsa.com.ar
@twitter: joacOrbe
@web: www.edsa.com.ar   
'''
import json

from melipy.core import MeliCore
import melipy.meliresources as meliresources

CLIENT_ID = 'your app id'
CLIENT_SECRET = 'your app secret'
USERID = 'user id'
USERSID = 'users id'
CODE = ''
ACCESS_TOKEN = ''

def print_test_message(f):
    def inner(*args,**kargs):
        print 'Enter into %s' % f.__name__
        f(*args,**kargs)
        print 'Leaving %s' % f.__name__
    return inner

@print_test_message        
def test_user(meli):
    user = meli.query_url(resource_part=meliresources.USER_DETAILS,
                          method='GET',
                          ids={'user_id':USERID},
                          attributes=['nickname'])
    print user['nickname']
    
@print_test_message
def test_users_details(meli):
    users = meli.query_url(resource_part=meliresources.USERS_DETAILS,
                          method='GET',
                          params={'ids':USERSID})
    
    for u in users:
        print u['permalink']
           
@print_test_message
def test_user_address(meli):
    addresses = meli.query_url(resource_part=meliresources.USER_ADDRESSES,
                               method='GET',
                               ids={'user_id':USERID},
                               access_token=True)
    print addresses
    
@print_test_message
def test_payment_methods(meli):
    payment_methods = meli.query_url(resource_part=meliresources.USER_PAYMENT_METHODS,
                                     method='GET',
                                     ids={'user_id':USERID},)    
    for p in payment_methods:
        print p['name']
        
@print_test_message
def test_payment_method_details(meli):
    payment_methods = meli.query_url(resource_part=meliresources.USER_PAYMENT_METHODS_DETAILS,
                                     method='GET',
                                     ids={'user_id':USERID,'pay_id':'redlink'})
    print payment_methods['name']
    print payment_methods['max_accreditation_days']

@print_test_message
def test_delete_payment_method(meli):
    payment_methods = meli.query_url(resource_part=meliresources.USER_PAYMENT_METHODS_DETAILS,
                                     method='DELETE',
                                     ids={'user_id':USERID,'pay_id':'redlink'},
                                     access_token=True)
    print payment_methods

@print_test_message
def test_add_payment_method(meli):
    body = {'id':'redlink',
            'name':'RedLink',
            'payment_type_id':'atm',
            'thumbnail':'http://img.mlstatic.com/org-img/MP3/API/logos/redlink.gif',
            'secure_thumbnail':'https://www.mercadopago.com/org-img/MP3/API/logos/redlink.gif'}
    payment_methods = meli.query_url(resource_part=meliresources.USER_PAYMENT_METHODS_DETAILS,
                                     method='PUT',
                                     ids={'user_id':USERID,'pay_id':'redlink'},
                                     access_token=True,
                                     body=body)
    print payment_methods
        
if __name__ == '__main__':
    meli = MeliCore(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)
    #meli.authorize(CODE, redirect_URI="http://www.google.com")
    #meli.set_access_token(ACCESS_TOKEN)
    #test_user(meli)
    #test_payment_methods(meli)
    #test_users_details(meli)
    #test_user_address(meli)
    #test_payment_method_details(meli)
    #test_delete_payment_method(meli)
    #test_add_payment_method(meli)
    #print json.dumps(meli.resource_helper(meliresources.NEW_ORDER),indent=4)
    