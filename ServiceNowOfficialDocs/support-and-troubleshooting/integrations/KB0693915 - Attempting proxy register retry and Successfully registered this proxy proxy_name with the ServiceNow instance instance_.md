---
title: "\"Attempting proxy register retry\" and \"Successfully registered this proxy \"<proxy_name>\" with the ServiceNow instance \"<instance_hostname>:443\"\" Repeat in edgeencryption.log"
aliases:
  - KB0693915
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693915
kb_number: KB0693915
last_modified: 2024-04-07
---

## "Attempting proxy register retry" and "Successfully registered this proxy "" with the ServiceNow instance ":443"" Repeat in edgeencryption.log

  

### Issue

# Symptoms

* * *

You startup and Edge Proxy and in the UI the Status remains in "Registering"

The edgeencryption.log shows the following which repeats constantly:

...

2018-07-30 06:16:37,710 INFO  Attempting proxy register retry #88

2018-07-30 06:16:38,068 INFO  Successfully registered this proxy "Edge\_Proxy\_London1" with the ServiceNow instance "test1.service-now.com:443"

2018-07-30 06:16:43,069 INFO  Attempting proxy register retry #89

2018-07-30 06:16:43,416 INFO  Successfully registered this proxy "Edge\_Proxy\_London1" with the ServiceNow instance "test1.service-now.com:443"

2018-07-30 06:16:48,417 INFO  Attempting proxy register retry #90

2018-07-30 06:16:48,771 INFO  Successfully registered this proxy "Edge\_Proxy\_London1" with the ServiceNow instance "test1.service-now.com:443"

2018-07-30 06:16:53,774 INFO  Attempting proxy register retry #91

2018-07-30 06:16:54,114 INFO  Successfully registered this proxy "Edge\_Proxy\_London1" with the ServiceNow instance "test1.service-now.com:443"

2018-07-30 06:16:59,114 INFO  Attempting proxy register retry #92

2018-07-30 06:16:59,471 INFO  Successfully registered this proxy "Edge\_Proxy\_London1" with the ServiceNow instance "test1.service-now.com:443"

...

# Release

* * *

This could apply to any release.

# Cause

* * *

There may be different causes for these repeating registering messages:

(1) Check the node logs to see if this is a cipher text mismatch, in this case the following was seen in the node logs:

2018-07-30 06:14:22 (573) Edge Encryption-thread-6 719BDCB2136B9300A5BA73304244B061 txid=9aecdcf2136b SEVERE \*\*\* ERROR \*\*\* sn\_edge\_encryption (EdgeProxy\_Processor): Validation of encryption key : aes128:-1 has failed. Expected cipher text was : 77eQ77eR77eSYWVzMTI477es77eTZml4ZWTvt6zvt5Qx77es77etUVVWVFh6RTJYMko1ZEdWelgybDJYdz09cUdqcUZlVUFwekNCbUdsR0M4b0VOakFFYklRbHFQVElvVUdFR0RZMWE2WUdkbE1IbkktalFhbGxKTldHbVJyZe+3ru+3rw== . But recieved cipher text : 77eQ77eR77eSYWVzMTI477es77eTZml4ZWTvt6zvt5Qx77es77etUVVWVFh6RTJYMko1ZEdWelgybDJYdz09N2ZKeDJGdlRraGhJNjVCMjZ6em41R0xraEdNVUhMSk1Zb1Flbnp3dVh3V1AtbjRpdFNYWlpKQkozUlZZSVBNVe+3ru+3rw==  

This shows that the keystore used by the proxy has an encryption key with the Key alias of aes128 that has a cipher text of:

77eQ77eR77eSYWVzMTI477es77eTZml4ZWTvt6zvt5Qx77es77etUVVWVFh6RTJYMko1ZEdWelgybDJYdz09N2ZKeDJGdlRraGhJNjVCMjZ6em41R0xraEdNVUhMSk1Zb1Flbnp3dVh3V1AtbjRpdFNYWlpKQkozUlZZSVBNVe+3ru+3rw==

But on the instance there is an Encryption Key that exists that has the same Key alias (aes128), but has a different Cipher text, in this case:

77eQ77eR77eSYWVzMTI477es77eTZml4ZWTvt6zvt5Qx77es77etUVVWVFh6RTJYMko1ZEdWelgybDJYdz09cUdqcUZlVUFwekNCbUdsR0M4b0VOakFFYklRbHFQVElvVUdFR0RZMWE2WUdkbE1IbkktalFhbGxKTldHbVJyZe+3ru+3rw==

This mismatch in Cipher text values is why the proxy registration does not happen.

(2) Another reason is that the encryption keys did not match in the keystore file vs the edgeencryption.properties file vs the Encryption Keys defined in the UI (Encryption Key Configuration -> Set Up Keys) - this could be due to a typo in the key alias name, this includes using mismatching cases since the alias is case sensitive.  A mismatch in any of the three places (keystore file, edgeencryption.properties file, Encryption Keys defined in the UI) can cause this error

# Resolution

* * *

(1) For Cause (1) - Changing or deleting the encryption key may have impact on existing encrypted data.  For example if you have data encrypted with a certain key you will never be able to unencrypt that data if that key is gone.  So you need to be very careful before taking any action.

If you need to keep that encryption key for data that has already been encrypted you could update the encryption key in the proxy's keystore to match the one that is defined on the instance for the key alias aes128 which will eliminate the mismatch and will allow the proxy to register.

If the key is irrelevant it could be deleted from the instance, but note that customers cannot delete keys, this can only be done by ServiceNow maint users with read write access in the "ServiceNow Edge Encryption" Application.

If you switch to that application you can delete the key or keys from Scripts Background using one of these scripts:

Script to delete a key with a specific key\_alias name:

var gr = new GlideRecord('sys\_encryption\_key');

gr.query('key\_alias', 'KEY\_ALIAS\_NAME');

while (gr.next()) {

gr.deleteRecord();

}

Script to delete all the keys:

var gr = new GlideRecord('sys\_encryption\_key');

gr.query();

while (gr.next()) {

gr.deleteRecord();

}

Then you can create a new encryption key in the UI specifying the Key alias aes128 

The Cipher text value of the key will be updated on the instance when the proxy registers so there will not longer be a mismatch and the proxy will Resister without issue.

(2) For Cause (2) - Be sure that the key alias is defined correctly in all three places:

(a) Check the name of the encryption key alias in the keystore file using the keytool command example from below, note that the alias is case sensitive:

keytool -list -keystore keystore.jceks -storepass <password> -storetype jceks -v

...

...

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Alias name: sb128v1  
Creation date: Dec 21, 2018   
Entry type: SecretKeyEntry

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

...

...

(b) In this case the key alias is sb1128v1, make sure that if your edgeencryption.properties file has these two properties defined that they refer to the correct key alias name, again this is also case sensitive:

edgeencryption.encrypter.key.2 = sb128v1  
and  
edgeencryption.encrypter.default.key128 = sb128v1

(c) Lastly in the UI at Encryption Key Configuration -> Set Up Keys the Key alias must also match, again this is case sensitive and in this case must be:

sb128v1
