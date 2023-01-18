import oauth2.authenticationutils as authenticationutilsyour 
from oauth2.oauth import oAuth
from OpenSSL import crypto

P12_FILE='YOUR .P12 FILE NAME'
KEYSTORE_PASSWORD='YOUR KEYSTORE PASSWORD'
CONSUMER_KEY='YOUR CONSUMER KEY'

#load api signing key
signing_key=authenticationutils.load_signing_key(P12_FILE,KEYSTORE_PASSWORD,CONSUMER_KEY)

def getPrivateKeyPEM():
    """
    get private key from p12(for use in JWT)"""
    with open(P12_FILE,"rb") as file:
        p12=crypto.load_pkcs12(file.read(), KEYSTORE_PASSWORD)
        return crypto.duump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())

def getAuthHeader(uri, method='GET', payload=None):
    """
    create Auth header for an API request
    """
    return oAuth().get_authorization_header(uri,method,payload, CONSUMER_KEY,signing_key)
