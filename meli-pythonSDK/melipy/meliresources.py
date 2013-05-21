# -*- coding: utf-8 -*-
'''
@author: Joaquin Orbe 
@email: joaquin_orbe@edsa.com.ar
@twitter: joacOrbe
@web: www.edsa.com.ar   
'''

#############################################
# Mercado Libre resources, from:
# http://developers.mercadolibre.com/API-directory/
#
#
# Example:
#    my_url = USER_DETAILS % {'user_id':123456789}
#############################################

# ***************************************************************************
# Users and Apps
# Under users and apps we will find all the resources relatives to mercadolibre users, applications and scopes

USER_DETAILS = '/users/%(user_id)s'
USERS_DETAILS = '/users'  # params: a comma-separated list of id   i.e.: ids=123,455,789
USER_ADDRESSES = '/users/%(user_id)s/addresses'
USER_PAYMENT_METHODS = '/users/%(user_id)s/accepted_payment_methods'
USER_PAYMENT_METHODS_DETAILS = '/users/%(user_id)s/accepted_payment_methods/%(pay_id)s' # it covers GET PUT DELETE
USER_PAYMENT_TYPES = '/users/%(user_id)s/accepted_payment_types'
USER_PAYMENT_TYPES_DETAILS = '/users/%(user_id)s/accepted_payment_types/%(pay_type)s' # it covers GET PUT DELETE

# ***************************************************************************
# Categories and Listings
# Categories and type of publications.

SITES = '/sites'
SITE_DETAILS = '/sites/%(site_id)s'
SITE_DOMAINS = '/site_domains/%(dom_id)s'
LISTING_TYPES = '/sites/%(site_id)s/listing_types'
LISTING_TYPE_DETAILS = '/sites/%(site_id)s/listing_types/%(list_type)s'
LISTING_EXPOSURES = '/sites/%(site_id)s/listing_exposures'
LISTING_EXPOSURE_DETAILS = '/sites/%(user_id)s/listing_exposures/%(list_exposure)s'
LISTING_PRICES = '/sites/%(site_id)s/listing_prices'
LISTING_PRICE_DETAILS = '/sites/%(site_id)s/listing_prices/%(list_price)s'
CATEGORIES = '/sites/%(site_id)s/categories'
CATEGORY_DETAILS = '/categories/%(categ_id)s'

# ***************************************************************************
# Locations and Currencies
# Resources that gives the regional information, countries, cities and currency.

COUNTRIES = '/countries'
COUNTRY_DETAILS = '/countries/%(country_id)s'
STATE_DETAILS = '/states/%(state_id)s'
CITY_DETAILS = '/cities/%(city_id)s'
CURRENCIES = '/currencies'
CURRENCY_DETAILS = '/currencies/%(curr_id)s'
CURRENCY_CONVERSION = '/currency_conversions/search' # params: from & to. date is optional

# ***************************************************************************
# Items and Searches
# The heart of MercadoLibre API, the resources for managing items and to look for them.

ITEM_DETAILS = '/items/%(item_id)s'    # it covers GET PUT
ITEMS_DETAILS = '/items'   # params: a comma-separated list of id   i.e.: ids=123,455,789
POST_ITEM = '/items'   # POST method
VALIDATE_ITEM = '/items/validate'
SHIP_INFO = '/items/%(item_id)s/shipping/search'
ADD_ITEM_PICTURE = '/items/%(item_id)s/pictures'   # POST method
REMOVE_ITEM_PICTURE = '/items/%(item_id)s/pictures/%(pic_id)s'   # DELETE method
UPD_ITEM_LIST_TYPE = '/items/%(item_id)s/listing_type'   # POST method
ITEM_DESCRIPTION = '/items/%(item_id)s/descriptions'   # it covers GET POST    
UPD_ITEM_DESCRIPTION = '/items/%(item_id)s/descriptions/%(descr_id)s'   # PUT method
ITEM_AVAILABLE_UPGRADES = '/items/%(item_id)s/available_upgrades'
ITEM_RELIST = '/items/%(item_id)s/relist'   # POST method
PICTURE_DETAIL = '/pictures/%(pic_id)s'
SEARCH = '/sites/%(site_id)s/search'
SEARCH_URL = '/sites/%(site_id)s/searchUrl'
HOT_ITEMS = '/sites/%(site_id)s/hot_items/search'
FEATURED_ITEMS = '/items/%(site_id)s/featured_items/%(pool_id)s'

# ***************************************************************************
# Order Management
# The core of the business: the transactions. Using the order resources, can easily access to purchases, give feedback and follow any order.

NEW_ORDER = '/orders'     # POST method
ORDER_DETAIL = '/orders/%(order_id)s'    #  it covers GET   PUT
SEARCH_ORDER = '/orders/search'
ORDER_BILLING_INFO = '/orders/%(order_id)s/billing_info'
PAYMENT_DETAILS = '/payments/%(pay_id)s'    #   it covers GET PUT
NEW_PAYMENT = '/payments'    # POST method
PAYMENT_METHOD = '/payment_methods/%(pay_id)s'
MP_PAYMENT_METHODS = '/sites/%(site_id)s/payment_methods'
MP_PAYMENT_METHOD_DETAILS = '/sites/%(site_id)s/payment_methods/%(pay_id)s'
ORDERS_FEEDBACK = '/orders/%(order_id)s/feedback/'
SELLER_FEEDBACK = '/orders/%(order_id)s/feedback/sale' # it covers GET PUT DELETE
BUYER_FEEDBACK = '/orders/%(order_id)s/feedback/purchase' # it covers GET PUT DELETE

# ***************************************************************************
# Questions
# Ask question, receive answers.

QUESTION = '/questions/%(question_id)s'   # it covers GET DELETE
POST_QUESTION = '/questions/'
SEARCH_QUESTION = '/questions/search'
RECEIVED_QUESTIONS = '/my/received_questions/search'
POST_ANSWER = '/answers/'   # POST method
HIDE_QUESTIONS = '/my/questions/hidden'
