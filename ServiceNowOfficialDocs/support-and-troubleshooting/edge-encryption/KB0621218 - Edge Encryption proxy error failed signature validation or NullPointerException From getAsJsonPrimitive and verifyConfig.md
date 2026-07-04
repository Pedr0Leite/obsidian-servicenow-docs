---
title: "Edge Encryption proxy error \"failed signature validation\" or NullPointerException From getAsJsonPrimitive and verifyConfigurationSignatures"
aliases:
  - KB0621218
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621218
kb_number: KB0621218
last_modified: 2024-04-07
---

## Edge Encryption proxy error "failed signature validation" or NullPointerException From getAsJsonPrimitive and verifyConfigurationSignatures

  

### Issue

Edge Encryption proxy error "failed signature validation" or NullPointerException From getAsJsonPrimitive and verifyConfigurationSignatures

Problem

* * *

You attempt to start the Edge Encryption Proxy and you see an error similar to this in the logfile $proxy\_installation\_location/logs/edgeencryption.log:

2017-02-03 12:06:44,749 ERROR Error occurred during proxy startup: Failed get edge encryption configuration from the ServiceNow instance: Encryption configuration for field '"change\_request"."short\_description"' failed signature validation. Contact support to restore the encryption configurations.

Or the following NullPointerException which will prevent the proxy from starting:

2017-08-19 09:12:45,327 ERROR Error occured during proxy startup

java.lang.NullPointerException

at com.snc.edgeencryption.util.JsonUtil.getAsJsonPrimitive(JsonUtil.java:44)

at com.snc.edgeencryption.encryption.EncryptedFieldsManager.verifyConfigurationSignatures(EncryptedFieldsManager.java:221)

at com.snc.edgeencryption.encryption.EncryptedFieldsManager.updateEncryptedFields(EncryptedFieldsManager.java:152)

at com.snc.edgeencryption.encryption.EncryptedFieldsManager.readEncryptedFields(EncryptedFieldsManager.java:96)

at com.snc.edgeencryption.CloudEdgeConfigClient.startupPing(CloudEdgeConfigClient.java:202)

at com.snc.edgeencryption.CloudEdgeConfigClient.start(CloudEdgeConfigClient.java:345)

at com.snc.edgeencryption.CloudEdge.start(CloudEdge.java:151)

at com.snc.edgeencryption.Main.main(Main.java:30)

at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)

at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)

at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)

at java.lang.reflect.Method.invoke(Method.java:498)

at org.tanukisoftware.wrapper.WrapperSimpleApp.run(WrapperSimpleApp.java:240)

at java.lang.Thread.run(Thread.java:748)

  

  

This can also be seen for Edge Encryption Rules, as an example from the logfile edgeencryption.log:

  

2019-01-29 23:42:30,433 ERROR Edge Encryption rule : 'CustomJson' does not have a valid signature

2019-01-29 23:42:30,512 ERROR Error in updating sync data manager for Edge Encryption Rules : One or more records failed signature validation. Will not update the proxy until this is resolved.

  

If this is seen for a Rule the same Resolution applies, below just do it for the impacted Rule or Rules.

  

Symptoms

* * *

See the mentioned errors in the edgeencryption.log file.

Cause

* * *

The digital signature check between the proxy and the instance fails. 

  

About the digital signature:

The proxy will look for and validate the signature for all of the Edge Encryption Configurations and Rules, and this must be consistent for the proxy to trust it. 

If there is some untrusted configuration in the proxy it will lock itself. It will run with what it has (encryptions will still be done), but any new rule or configuration will not be applied. The proxy keeps a local copy of the configurations (encryptionconfiguration.json and rules folder).  If there is a validation problem, the trust is broken and the proxy only trusts its local copies until recovery.

Signatures are being validated when loading configurations; deletions are also checked. All proxies must have the same RSA key to perform the validation.

The signature is one of the keys that is added to the keystore.jceks, e.g. it is added using this keytool command:

/java/jre/bin/keytool –genkey -alias rsa\_key -keyalg rsa –keystore keystore/keystore.jceks -storetype jceks -storepass changeme

  

Edge proxy uses asymmetric keys to ‘sign’ configurations, rules, etc.

All base system rules are signed with a ServiceNow private key. The corresponding public key is in the keystore that ships with the edge proxy.  Proxies need the ServiceNow public key.

All user-generated rules and configurations should be signed with a different asymmetric key present in their keystore.

The signature key setup is done in the edgeencryption.properties file:

-   edgeencryption.proxy.signature.keystore.path = keystore/keystore.jceks
-   edgeencryption.proxy.signature.keystore.password = <password>
-   edgeencryption.proxy.signature.keystore.keyalias = rsa\_key

Resolution

* * *

(1) Stop one proxy edit the $proxy\_installation\_location/conf/edgeencryption.properties file, adding these two properties:

edgeencryption.proxy.skip.config.validate = true  
edgeencryption.proxy.signature.verify = false

When the proxy is started this tells it to ignore the signature mismatches.

  

(2) Start this proxy, make sure it starts ok.

  

(3) Repeat steps (1) and (2) for all of the other proxies one by one.

  

(4) Now in the case of the "failed signature validation" or "Edge Encryption Rules : One or more records failed signature validation." errors, log back into the instance via the proxy URL and modify the configuration or configurations or rule or rules that show in the error from the log.  Edit in the form editor to fix the signatures.  In this example this is the error:

2017-02-03 12:06:44,749 ERROR Error occured during proxy startup: Failed get edge encryption configuration from the ServiceNow instance: Encryption configuration for field '"change\_request"."short\_description"' failed signature validation. Contact support to restore the encryption configurations.

Or this error for a Rule:

2019-01-29 23:42:30,433 ERROR Edge Encryption rule : 'CustomJson' does not have a valid signature  
2019-01-29 23:42:30,512 ERROR Error in updating sync data manager for Edge Encryption Rules : One or more records failed signature validation. Will not update the proxy until this is resolved.

To fix the "failed signature validation" error for a configuration, navigate to Edge Encryption Configuration > Encryption Configurations > All. You must do this from the form view for each record individually, not from the list view multi-select -> Select the Configuration for Table = change request and Column = short\_description. You can correct this simply by checking or unchecking the Active box, saving, then putting it back to the original value and saving it again. For a Rule go to Edge Encryption Configuration > Rules > All. You must do this from the form view for each record individually, not from the list view multi-select -> Select the Rule with the failing signature by name and check or uncheck the Active box, saving, then putting it back to the original value and saving it again.  This will synchronize the signature between the instance and the proxy.

  

(5) Stop one proxy.

  

(6) Edit the $proxy\_installation\_location/conf/edgeencryption.properties file, removing these two properties:

edgeencryption.proxy.skip.config.validate = true  
edgeencryption.proxy.signature.verify = false

  

(7) Delete all of the files contained in the $proxy\_installation\_location/cache directory.

  

(8) Start this proxy, make sure it starts ok.  The proxy should start without issue since now the signature issues have been resolved.

  

(9) Repeat steps (5) through (8) for all of the other proxies one by one.

  

  

NOTE: If the issue is not resolved by the steps above check that the script include EdgeEncryptedFields\_Processor is set to use the latest version provided by any upgrades done.  Starting in Kingston the signature was updated to make it more secure.  The proxy is using a new logic to sign that relies on more fields from the configurations and rules than before.  It expects the instance to send those new fields when the proxy asks for all of the configurations and rules.  If the proxy is running on a Kingston or above version and the instance has a pre-Kingston version of the EdgeEncryptedFields\_Processor script include contact ServiceNow support to have the latest version of the EdgeEncryptedFields\_Processor script include active on the instance.

Support must make this change by a change request since the script include is part of the "ServiceNow Edge Encryption" Application which is private and cannot be modified without maintenance access to the instance.
