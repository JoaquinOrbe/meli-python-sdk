# -*- coding: utf-8 -*-
'''
@author: Joaquin Orbe 
@email: joaquin_orbe@edsa.com.ar
@twitter: joacOrbe
@web: www.edsa.com.ar   
'''

import requests
from urllib import urlencode

import constants

class MeliCore(object):
    def __init__(self,
                 site_id="MLA",
                 client_id=None,
                 client_secret=None):
        """Main class for Mercado Libre's API.
        
        Keyword arguments:
        site_id -- MercadoLibre site id (default "MLA")
        client_id -- App ID from MercadoLibe App Manager
        client_secret -- App Secret from MercadoLibe App Manager
        """
        self.client_id = client_id
        self.client_secret = client_secret 
        self.site_id = site_id
                
        self.API_PREFIX_URL = constants.API_ROOT_URL
        self.SDK_VERSION = constants.SDK_VERSION
        self.AUTH_URL = constants.AUTH_URL
        self.OAUTH_URL = self.API_PREFIX_URL + constants.OAUTH_URL
        self.access_token = None
        self.refsh_token = None
    
    def set_client(self,client_id,client_secret):
        """Set MercadoLibre credentials from App Manager."""
        self.client_id = client_id
        self.client_secret = client_secret
        
    def set_access_token(self,access_token):
        """For testing purpose."""
        self.access_token = access_token
        
    def logged_client(f):
        """Decorator for User Credentials checking."""
        def inner(self,*args, **kargs):
            if ((self.client_id is not None) and (self.client_secret is not None)):
                return f(self,*args,**kargs)
            else:
                raise Exception, "Cannot authorize if User Credentials are missing."
        return inner
    
    @logged_client
    def get_auth_url(self, redirect_URI):
        """Returns Authorization URL.
        
        Keyword arguments:
        redirect_URL -- redirection URL
        """
        params = {'client_id':self.client_id,'response_type':'code','red_uri':redirect_URI}
        url = self.AUTH_URL  + '?' + urlencode(params)
        return url
    
    @logged_client
    def authorize(self, code, redirect_URI):
        """Authorize user for private resource access.
        
        Keyword arguments:
        code -- Server generated Authorization code
        redirect_URL -- redirection URL
        """
        params = {'grant_type':'authorization_code','client_id':self.client_id,'client_secret':self.client_secret,
              'code':code,'redirect_uri':redirect_URI}
    
        headers = {'Accept': 'application/json',
               'User-Agent':self.SDK_VERSION}
    
        response = requests.post(self.OAUTH_URL,headers=headers,params=urlencode(params))
    
        if response.status_code == requests.codes.ok:
            resp_json = response.json()
            self.access_token = resp_json['access_token']
            if resp_json.has_key('refresh_token'):
                self.refsh_token = resp_json['refresh_token']
            else:
                self.refsh_token = '' # offline_access not set up
        else:
            response.raise_for_status()
    
    @logged_client
    def refresh_token(self):
        """Refresh access_token and refresh_token."""
        if self.refrsh_token != '':
            params = {'grant_type':'refresh_token','client_id':self.client_id,
                  'client_secret':self.client_secret,'refresh_token':self.refresh_token}
        
            headers = {'Accept': 'application/json',
                   'User-Agent':self.SDK_VERSION}
        
            response = requests.post(self.OAUTH_URL,headers=headers,params=urlencode(params))
    
            if response.status_code == requests.codes.ok:
                resp_json = response.json()
                self.access_token = resp_json['access_token']
                self.refsh_token = resp_json['refresh_token']
            else:
                response.raise_for_status()
        else:
            raise Exception, "Offline-Access is not allowed."
            
    def get(self, resource, params=None):
        """Implement HTTP GET method.
        
        Keyword arguments:
        resource -- MercadoLibre resource
        params -- URL parameters
        """
        headers = {'Accept': 'application/json',
                   'User-Agent':self.SDK_VERSION}
        
        if params.has_key('access_token'):
            params['access_token'] = self.access_token
            
        response = requests.get(self.API_PREFIX_URL + resource,headers=headers,params=urlencode(params))
        
        
        if params.has_key('access_token') and (self.refsh_token is not None) and (response.status_code == requests.codes.not_found):
            self.refresh_token()
            params['access_token'] = self.access_token
            response = requests.get(self.API_PREFIX_URL + resource,headers=headers,params=params)
        
        return response.json()
    
    def post(self, resource, params=None, body=None):
        """Implement HTTP POST method.
        
        Keyword arguments:
        resource -- MercadoLibre resource
        params -- URL parameters
        body -- request content
        """
        import json
        
        headers = {'Accept': 'application/json',
                   'Content-Type':'application/json',
                   'User-Agent':self.SDK_VERSION}        

        if params.has_key('access_token'):
            params['access_token'] = self.access_token
                    
        response = requests.post(self.API_PREFIX_URL + resource,headers=headers,params=params,data=json.dumps(body))

        if params.has_key('access_token') and (self.refsh_token is not None) and (response.status_code == requests.codes.not_found):
            self.refresh_token()
            params['access_token'] = self.access_token
            response = requests.post(self.API_PREFIX_URL + resource,headers=headers,params=params,data=json.dumps(body))
        
        return response.json()

    def put(self, resource, params=None, body=None):
        """Implement HTTP PUT method.
        
        Keyword arguments:
        resource -- MercadoLibre resource
        params -- URL parameters
        body -- request content
        """
        import json
        
        headers = {'Accept': 'application/json',
                   'Content-Type':'application/json',
                   'User-Agent':self.SDK_VERSION}        
        
        if params.has_key('access_token'):
            params['access_token'] = self.access_token
                    
        response = requests.put(self.API_PREFIX_URL + resource,headers=headers,params=params,data=json.dumps(body))

        if params.has_key('access_token') and (self.refsh_token is not None) and (response.status_code == requests.codes.not_found):
            self.refresh_token()
            params['access_token'] = self.access_token
            response = requests.post(self.API_PREFIX_URL + resource,headers=headers,params=params,data=json.dumps(body))
        
        return response.json()

    def delete(self, resource, params=None):
        """Implement HTTP DELETE method.
        
        Keyword arguments:
        resource -- MercadoLibre resource
        params -- URL parameters
        """
        headers = {'Accept': 'application/json',
                   'User-Agent':self.SDK_VERSION}
        
        if params.has_key('access_token'):
            params['access_token'] = self.access_token
            
        response = requests.delete(self.API_PREFIX_URL + resource,headers=headers,params=urlencode(params))
        
        if params.has_key('access_token') and (self.refsh_token is not None) and (response.status_code == requests.codes.not_found):
            self.refresh_token()
            params['access_token'] = self.access_token
            response = requests.get(self.API_PREFIX_URL + resource,headers=headers,params=params)
        
        return response.json()
    
    def prepare_attributes(self,attributes):
        """Form a string of all attributes for resource request.
        
        Keyword arguments:
        attributes -- list of attributes
        """
        attrs = ",".join([str(i) for i in attributes])
        return attrs
        
    def query_url(self,
                   resource_part,
                   method,
                   ids=None,
                   params=None,
                   attributes=None,
                   access_token=False,
                   body=None):
        """
        Executes the url query and returns a JSON result.
        
        Keyword arguments:
        resource_part -- MercadoLibre resource -> ie: USER_PAYMENT_METHODS_DETAILS
        ids -- dict of IDs to for the final resource URL -> ie: {'user_id':'21323'}
        params -- dict of params for URL -> ie.{'category':'MLA1042'}
        attributes -- list of attributes for URL -> ie: ['site_id','site_name']
        access_token -- either or not it needs an access token
        method -- method to use in request. Options: GET,POST,PUT,DELETE
        """
        resource = resource_part % ids
        
        if params is not None:
            parameters = params
        else:
            parameters = {}
            
        if attributes is not None:
            parameters['attributes'] = self.prepare_attributes(attributes)        
        if access_token:
            parameters['access_token'] = ''
        
        if method == 'GET':
            return self.get(resource, parameters)
        elif method == 'POST':
            return self.post(resource, parameters, body)
        elif method == 'PUT':
            return self.put(resource, parameters, body)
        elif method == 'DELETE':
            return self.delete(resource, parameters)
           
    def resource_helper(self,resource):
        """
        Return description of the resource.
        For pretty-print, use the result -> json.dumps(resp,indent=4)
        
        Keyword arguments:
        resource -- MercadoLibre resource -> ie: USER_PAYMENT_METHODS_DETAILS 
        """
        url = self.API_PREFIX_URL + resource
        print "URL description: %s" % url
        response = requests.options(url)
        return response.json()
    