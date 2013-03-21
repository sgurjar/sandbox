"""
https://www.oasis-open.org/committees/download.php/13392/wss-v1.1-spec-pr-UsernameTokenProfile-01.htm

<wsse:Password>

    Passwords of type PasswordDigest are defined as being the Base64 [XML-
    Schema] encoded, SHA-1 hash value, of the UTF8 encoded password (or
    equivalent). However, unless this digested password is sent on a secured
    channel or the token is encrypted, the digest offers no real additional
    security over use of wsse:PasswordText.

<wsse:Nonce>

    A nonce is a random value that the sender creates to include in each
    UsernameToken that it sends. effective countermeasure against replay
    attacks.


<wsu:Created>


Password_Digest = Base64 ( SHA-1 ( nonce + created + password ) )

"""

import base64
import hashlib

"""
digest, nonce and created is passed by client

digest is computed as base64( SHA-1 (nonce + created + password ) )

nonce sent by client is base64 encoded

to match the passwd
    server needs to compute (server knows plaintextpasswd)
        
        SHA-1 (base64_decoded(nonce) + created + plaintextpasswd)       ----- (1)

and if base64_decoded digest sent by client matches with the digest computed on 
(1) than auth is successful
"""

digest="nRa1OmFgocTxjb9JSZmYj/uVTiw="

nonce="AsydpwytB5qCDXiOHnBHEg=="
created="2013-03-15T16:34:54.615Z"
password="welcome1"

client_digest_decoded = base64.b64decode(digest).encode('hex')
server_computed_digest = hashlib.sha1(base64.b64decode(nonce)+created+password).hexdigest()

if client_digest_decoded == server_computed_digest:
    print "you are in"
else:
    print "unauthorized access"


