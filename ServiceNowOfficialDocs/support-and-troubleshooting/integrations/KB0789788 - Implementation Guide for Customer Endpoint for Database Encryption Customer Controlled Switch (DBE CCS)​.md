---
title: "Implementation Guide for Customer Endpoint for Database Encryption Customer Controlled Switch (DBE CCS)​"
aliases:
  - KB0789788
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789788
kb_number: KB0789788
last_modified: 2025-02-19
---

## Text

# Summary

Since the customer retains the customer supplied Key Encryption Key (KEK) when CCS is chosen, the customer needs to periodically provide that secret key to their ServiceNow database instance, so the encrypted data can be accessed.

The customer provides the secret to ServiceNow via its CCS Customer Endpoint. The CCS Customer Endpoint is an HTTPS service that responds to a simple GET request for a customer's proprietary key, with a "wrapped" version of said key.  This Endpoint will be polled regularly by ServiceNow, typically every 15 minutes.

### Recent Process Change for new CCS Instances

As of November 2024, there is a change in how an instance is CCS enabled. The customer must implement the CCS endpoint _before_ creating a CCS instance. (Before November, the customer would implement the endpoint after the instance was created as a Database Encryption (also referred to as Tablespace Encryption or TSE) instance, and the instance would be "reconverged" as a CCS instance only after the customer had set up the endpoint with its secret key.

**Warning:** this change is particularly relevant to the situation where the customer has submitted a case on their production CCS instance for Customer Support for assistance, and Customer Support requests permission to create a sub-production copy to troubleshoot the problem. Since the copy will also be a CCS instance, the customer must set up the endpoint for that instance and have it validated prior to agreeing to the copy. Otherwise the copy will fail due to the secret key being unavailable.

Since CCS is used by only a few customers, most Customer Support staff will be unfamiliar with this prerequisite. So the customer will need to warn Customer Support of this requirement, and should refer the internal document KB0870210 (Onboarding Information for CCS) to them.

### Partner-provided Customer Endpoint

Typically a customer will work with a ServiceNow Technology Partner, Fortanix or Llave.io. These partners have implemented the Customer Endpoint on customer's behalf, so the CCS customer need not undertake the endpoint implementation on their own. The Fortanix integration document is here: [Using Fortanix Data Security Manager with ServiceNow](https://urldefense.com/v3/__https://support.fortanix.com/hc/en-us/articles/4404181731732-Using-Fortanix-Data-Security-Manager-with-ServiceNow__;!!N4vogdjhuJM!STkawly0BYc4MAy-gjV9M8Qd6LVwFhCaZP631J9bDpzcZ8A7svZDiZJR7gLX4iBcxLfHerQ$ "Using Fortanix Data Security Manager with ServiceNow") and you can reach Llave.io at [https://www.llave.io/](https://www.llave.io/ "https://www.llave.io/").

### Self Implemented Customer Endpoint

Legacy CCS customers have internally implemented their Customer Endpoint based on the specification contained herein.

In addition to this specification, ServiceNow can provide our reference implementation of Customer Endpoint (written in Java and Spring Boot); the customer can use the reference implementation as a basis for developing their own proprietary application customized for their needs. One can request it at email: [dev-customer-controlled-switch](mailto:dev-customer-controlled-switch@servicenow.onmicrosoft.com "dev-customer-controlled-switch").  The reference implementation is not enterprise ready; the customer would typically use it as a starting point for their proprietary development.

# Customer Endpoint Specification

Request: HTTPS Get, version TLS 1.2

Endpoint: `https://<host>/kek/<instance>/<key_id>`

Instance must be identical to the first component of the ServiceNow instance host. For example, if the instance host is 'ccsdemo.service-now.com' then the instance is 'ccsdemo'.

Key id is an integer representing the chain of customer secret key rotations. In other words, 1 is the key id of the first secret key, 2 the second etc. At this time key rotation is not supported. Thus key id should always be 1.

HTTP Header: Name: X-DB-Certificate, Value: The ServiceNow customer database instance X-509 public certificate, encoded as bytes based on ASN.1 DER scheme, and then encoding those bytes as a string using base64 encoding.

Request Example: `[https://ccs-rest.democorp.com/kek/ccsdemo/1](https://ccs-rest.democorp.com/kek/ccsdemo/1 "https://ccs-rest.democorp.com/kek/ccsdemo/1")`

Header: X-DB-Certificate: MIIFOjCCAyKgAwIBAgIUHEbGRBgSFOI2sSsUY8AvwOEoswEwDQYJKoZIhvcNAQELBQAwgZMxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJDQTEUMBIGA1UEBwwLU2FudGEgQ2xhcmExGTAXBgNVBAoMEFNlcnZpY2VOb3csIEluYy4xHTAbBgNVBAsMFFNlY3VyaXR5IEVuZ2luZWVyaW5nMScwJQYDVQQDDB5TZXJ2aWNlTm93IFRTRUNTSyBSb290IENBIC0gRzEwHhcNMjUwMjE5MjMwMDM4WhcNMjcwMjE5MjMwMDM3WjCBiDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExFDASBgNVBAcMC1NhbnRhIENsYXJhMRkwFwYDVQQKDBBTZXJ2aWNlTm93LCBJbmMuMR0wGwYDVQQLDBRTZWN1cml0eSBFbmdpbmVlcmluZzEUMBIGA1UEAwwLdHNlX2Njc2RlbW8wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCsKv563Fa+OhBuGsBsLql50OvPGNF5/AnYOWpQbyArOXa7oLrp7TJC6NeWWrvKcEgo81SFosc7kxMHGE29xZX/y0O8TgjtlFT1PcWktuicLstT6LaOdtRHp1U97oBQePVvlj0kBlSa1pKzvLH1xFtp0FkjvZJNe2JyosRWOGGdP88s3bV10SDBJduYfgczU8kxI4acLcB8uEAfN1h4oqqXDXVFMy5dhssQKKkAVFywTt+zTzFsN4d4TAmFEbzKPlwAQJNzLUyhJ2S5IN1TJTCZBHnUhwvFt+RyVaPRX/ZnHYpRKIq60siX0yAJPT7YWrNiaqbSyu0NJRqHd1rO7nMXAgMBAAGjgY4wgYswDAYDVR0TAQH/BAIwADAfBgNVHSMEGDAWgBTJl/sM0OMe56+EhHdbCcr150wNQzAWBgNVHREEDzANggt0c2VfY2NzZGVtbzATBgNVHSUEDDAKBggrBgEFBQcDAjAdBgNVHQ4EFgQUsKiDsKIgOYZAl6fXFcIDA33/70gwDgYDVR0PAQH/BAQDAgOIMA0GCSqGSIb3DQEBCwUAA4ICAQCHuhaqbe2Jy8yhnsFVrjX+svQzKorQnDlYJJmQ557XlMoPFeQva9sFXl9oG+Vm7JyobkyJ2iBPJtyXS4/21OvRAKPTLq9/Km7dBIBOLAp5ZEiLi/8Ap0t1qFyn0/pPyRYeIhF6nDm6A8vxuOVxefAnNQjuNdpbG8bWp5eW034Lv4xFFz4chM2V2XATiFhcpEKTJAkezYeWbdET5rugjpKNnNFWA351xlrpy61QbjdNtG4F1qBPBI67cMZH1LlPMaD0RURTzJCsRCmS7xYMXVDdyb6sEUlJSo1Uh4QqFuGh2H38vdImb2mPRyl2YuvMh7bNKLrljQd6QeJWZxfJshqvXyEuvfH8Q1izQp09CCAjnY4fu5B0jnmWv5a/L9IrWqROo45PfVqyoOGI+UMpkpR813UGSylj7oPamE/NqVXa1dPPLKPjRJfwkSJbD7MTUC2jGfqLc3uQAqzpWQ3jGQXvboFCG3MmI0bw9CnzgRgH6IiyFX7xTNSytMR23GE+jSznstAOR+u175Upqs+VjLa4mpwtIMAe+7kad8gx7txYSN8huijoJBiPJm0LuJdoieJsdF17bHC/XseoSKtKRYx0thWo1krt4V6wtm18rxoMFxyLUnw5CMRmAaYF+KgaV5sox40VKUV0XxnRMi69SIURJBqp45XZhs+5TUiXmKp5lw==

Note: that header value above is the actual header value to use in client requests to the endpoint for the instance ccsdemo. It is the double encoding (as specified above) of the database certificate for the ccsdemo instance. That database certificate is attached to this article, and you can use it in client calls for QA testing of your endpoint.  If for some reason you need to test your endpoint for a different instance name, please open a case requesting the corresponding database certificate from customer support.

## Response (Success)

HTTP Status: 200

Content Type: JSON

The wrappedKey is the customer's secret key, encrypted as detailed in the "Operation Logic" section below

Body:

`{"keyId":1,`

`"validUntil":"<yyyy-MM-DDThh:mm:ss.sssZ>",`

`"wrappedKey":``"``<base64(rsa_public_encrypt(kek))>"`

`}`

Body Example: 

{

  "keyId": 1, 

  "validUntil": "2021-12-31T00:00:00Z", 

  "wrappedKey": "XaAenWmlWhdkhklzYSwDzrWUiE3JnhUAMD1HvNOjUqq7IZ8tmrUURkAsv4cgFF4a7gLLbxDmFlaG/M4j+gXMPlvJieMQfOquZ0o+QhbV8ujTzleCAeFCAfXVRgHjkh7mDFbdmIFWT/NC5epMIc9cQEb0UF4OC0sbW4xAegq9ZDHWKtkzlK/xMTHkhyhW4oPUXuDmA92FagHJlFAe86nHhK9Fy8v4mpiwofssUIG5QyhLpEwBuZggsZo/MKLTkTkJEiiIdwpLN/JL3NbVczGIskUpAS92EwM8HvnjumGfJNlpHb4TBsw9N0cFGWsGn0dsG5N+iQmunTTYn95Xzk01Q==" 

} 

## Response (Bad Request)

HTTP Status: 400   

When The URI does not match the /kek/<instance>/<key\_id> pattern 

Content Type: JSON 

Body :  

{"error": "<message>"} 

Response Example: 

{"error": "The operation is not supported"} 

## Response (Not Authorized)

HTTP Status: 401   

When X-DB-Certificate is invalid as detailed in the "Operation Logic" section below

Body :  

{"error": "<message>"}  

Body Example: 

{"error": "The Database certificate is invalid, reason: expired validity date"}

## Response (Not Found)

HTTP Status: 404   

Expected when the instance name is not known by the endpoint, or the keyId is not known by the endpoint.

Body :  

{"error": "<message>"}  

Body Examples: 

{"error": "The requested instance doesn't match the expected instance: requestedInstance=vvsdemo"}

{"error": "The keyId=5 is invalid"}

## Response (Server Error)

HTTP Status: 500   

Operation failed for some reason, other than user error 

Body :  

{"error": "<message>"} 

Response Example: 

{"error": "There was a system error. Please contact Acme corp IT support.  Quote error id E666687 when contacting support"} 

# Operation Logic

## Customer Secret Key

The Customer Endpoint must have read access to the customer's secret key (KEK), which must have the following characteristics: 

-   Key can't be changed (because there is no rotation support at this time)
-   Key must be 64 hexadecimal characters.  Generally, this means generating a random 32 bytes (or 256 bits) and expressing it in hexadecimal. 

## Database Certificate Validation

The database Certificate in the header must fulfill the following:

-   It must be parsable as an X-509 certificate
-   The Common Name (CN) attribute must equal "tse\_<instance >" where <instance > is the name of the instance for which a key is being requested.  For example, if your instance is ccsdemo.service-now.com, the CN must be tse\_ccsdemo.  
-   The database certificate must be issued and signed by either of the ServiceNow root certificates (attached to this article as 'snc-db-encrypt.ca.pem.txt' and 'snc-db-ejbca-root.pem.txt').
-   The database certificate expiration date must be in the future.  It is ServiceNow's responsibility to provide a newer certificate in requests, before the older certificate expires.

## Process for Encrypting the Customer Secret Key 

-   Extract the Public Key from the Database certificate that was passed in the HTTPS header 
-   Use that public key to encrypt the customer secret key, using the padding algorithm referred to by OpenSSL as PKCS1\_OAEP\_PADDING.  In Java, using Castle's encryption library, this padding algorithm is identified as "RSA/NONE/OAEPWithSHA-1AndMGF1Padding". The encrypted result will be a byte array. 
-   Base64 encode that encrypted byte array as a string. That string must be returned as the wrappedKey in the JSON response body. This encryption ensures that the customer secret key can only be decrypted by the customer's ServiceNow instance database, which alone has the private key. 
-   The validUntil timestamp in the response body must follow the ISO8601 timestamp format, expressed in the Zulu time zone with a z at the end of the timestamp. The validUntil timestamp is the time after which ServiceNow must shut down the database on your instance. Your customer endpoint must always specify a future timestamp on each response to the periodic key poll, to signify that the database should remain running.  If the validUntil time returned is in the past, then database must be shut down immediately. Consider using a date calculated from today, such as seven days from today. 

## Reference Java Code Snippet 

class RSAPublicKeyWrapper {   private final PublicKey publicKey;   RSAPublicKeyWrapper(HttpServletRequest request) throws Exception {      byte\[\] x509EncodedCertificate = Base64._getDecoder_().decode(request.getHeader("X-DB-Certificate"));      CertificateFactory certFactory = CertificateFactory._getInstance_("X.509");      InputStream in = new ByteArrayInputStream(x509EncodedCertificate);      X509Certificate cert = (X509Certificate)certFactory.generateCertificate(in);      X509EncodedKeySpec spec = new X509EncodedKeySpec(cert.getPublicKey().getEncoded());      KeyFactory keyFactory = KeyFactory._getInstance_("RSA");  
      this.publicKey \= keyFactory.generatePublic(spec);   }   byte\[\] wrap(String proprietaryKey) {      try {         return getCipher(Cipher._ENCRYPT\_MODE_).doFinal(proprietaryKey.getBytes());      } catch (Exception e) {         throw new RuntimeException(e);      }  
   }   private Cipher getCipher(int mode) throws Exception {

      // This example relies on the presence of the BouncyCastle encryption library

      Cipher cipher = Cipher.getInstance("RSA/NONE/OAEPWithSHA-1AndMGF1Padding", "BC");      cipher.init(mode, publicKey);  
      return cipher;   }  
}

# Optional Features

Some customers implement features that are not part of the customer endpoint specification, but don't prevent it functioning correctly.

## Allow Lists

As an extra layer of security, some customers restrict endpoint access to a defined set of IP addresses. When this is done, the following global IP ranges (owned and operated exclusively by ServiceNow ) must be included in that set:  
37.98.232.0/21  
103.23.64.0/22  
149.96.0.0/16  
199.91.136.0/21  
148.139.0.0/16
