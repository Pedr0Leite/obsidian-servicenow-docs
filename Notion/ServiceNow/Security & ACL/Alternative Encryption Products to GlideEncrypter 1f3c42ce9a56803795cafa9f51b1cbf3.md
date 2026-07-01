---
aliases:
  - "Alternative Encryption Products to GlideEncrypter"
tags:
  - encryption
  - glide-encrypter
  - kmf
  - security
  - deprecation
---

# Alternative Encryption Products to GlideEncrypter

Other interesting scripts:

https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1745905

https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1320986

https://www.servicenow.com/docs/bundle/yokohama-platform-security/page/administer/encryption/concept/explore-kmf.html

**GlideEncrypter Deprecation**

The GlideEncrypter API uses the three-key Triple Data Encryption Standard (3DES) to secure data. The National Institute of Standards and Technology (NIST)[https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf) has recommended against using this standard to encrypt data after 2023 (See [NIST 800-131A Rev 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-131Ar2.pdf)).

Using the GlideEncrypter API in the Now Platform won’t be permitted in the Zurich release. Admins should consider migrating away from the GlideEncrypter API beginning in Xanadu release to take advantage of the newer, more secure encryption standards.

ServiceNow will automatically replace any use of GlideEncrypter in scripts created by ServiceNow, but you must change any scripts you have created, or any ServiceNow created scripts that you have modified.

**Alternatives to GlideEncrypter**

ServiceNow provides the GlideElement API and the Key Management Framework as alternatives to GlideEncrypter.

**GlideElement API**

The GlideElement API provides a number of convenient script methods for dealing with fields and their values. There are examples using GlideElement in the next section, but you can see complete details on this API at [GlideElement](https://docs.servicenow.com/csh?topicname=c_GlideElementAPI.html&version=latest).

**Key Management Framework (KMF)**

The Key Management Framework (KMF) API/UX lets you fully customize and manage how cryptographic operations are performed on your instance. KMF provides a secure and comprehensive interface, for instance-side cryptographic key management services. In addition to the examples in the next section, you can see details about KMF in [Exploring the Key Management Framework](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/key-management-framework/concept/understanding-kmf.html).

For a brief overview of the Key Management Framework, and how it can help you manage cryptographic operations, see [What Is the Key Management Framework](https://support.servicenow.com/nav_to.do?uri=%2Fkb%3Fid%3Dkb_article_view%26sysparm_article%3DKB1702587).

**Alternatives with examples:**

Use the following table to see common uses of GlideEncrypter methods, and alternatives you can use to replace them. If you want to test some of these methods on your instance prior to updating your scripts, see the testing script section later in this document.

| **Decryption for password2 values** |  |
| --- | --- |
| Example | //Example of password decryption using GlideEncrypter 
var decryptedPwd = new GlideEncrypter().decrypt(gr.password); |
| Alternative | Use getDecryptedValue() API of the Password2 field. 
Sample code:
var decryptedPwd = gr.password2field.getDecryptedValue(); 
Note: getDecryptedValue’s cross-scope access policy doesn’t allow cross-scope calls. Decryption can only be done within the same scope as the data. 

NOTE: This is not applicable for System Properties of type Password2.
The password2 properties are decrypted when they are loaded by system from DB. Hence explicit decryption is not required.
Sample to fetch value from password2 type system property:
var g = GlideProperties.get("name-of-your-property"); 
gs.print(g); |
| Availability | Vancouver Patch 1 |

| **Encryption for password2 values** |  |
| --- | --- |
| Example | //encrypt password value
var encryptedPassword = new GlideEncrypter().encrypt(clearTextValue); 
//set the encrypted value to password field 
gr.setValue("password", encryptedPassword ); 
//insert or update 
gr.insert(); |
| Alternative | Use GlideElement.setDisplayValue() 
gr.password.setDisplayValue(clearTextValue);
gr.insert(); |
| Availability | Vancouver Patch 1 |

| **Encrypt or decrypt non-password2 data** |  |
| --- | --- |
| Example | //encrypt value 
var encryptedValue = new GlideEncrypter().encrypt(value); 
//set the encrypted value to non-password2 field 
gr.setValue("column", encryptedValue); |
| Alternative | Use the [KMFCryptoOperation API](https://docs.servicenow.com/bundle/xanadu-api-reference/page/app-store/dev_portal/API_reference/KMFCryptoOperationBoth/concept/KMFCryptoOperationBothAPI.html) to perform symmetric data encryption or decryption 
//encrypt 
var encryptOp = new sn_kmf_ns.KMFCryptoOperation("< module_name >", "SYMMETRIC_ENCRYPTION") .withInputFormat("KMFNone"); 
var encryptedText = encryptOp.doOperation(clear_text); 
 
 //decrypt  
var encryptOp = new sn_kmf_ns.KMFCryptoOperation("< module_name>", "SYMMETRIC_DECRYPTION") .withOutputFormat("KMFNone"); 
var clear_text = encryptOp.doOperation(<encrypted_text>);
 
To support decryption of both KMF encrypted values and GlideEncrypter encrypted values, use KMF_GLIDE_ENCRYPTER_FORMATTED input format decorator.   
var encryptOp = new sn_kmf_ns.KMFCryptoOperation("<module_name>", "SYMMETRIC_DECRYPTION") .withInputFormat("KMF_GLIDE_ENCRYPTER_FORMATTED")
.withOutputFormat("KMFNone"); 
var clear_text = encryptOp.doOperation(<encrypted_text>); 
 
Note:
These operations require a KMF module that supports SYMMETRIC_ENCRYPTION, SYMMETRIC_DECRYPTION and also tracks/allows the Decryptions. If you do not have a module that matches these criteria, you can [create a new KMF module](https://docs.servicenow.com/csh?topicname=create-cryptographic-module.html&version=latest) and use that in the code as an input parameter for module name. 
If you also need to transfer this data to a different instance and need it to be decrypted there, then you also need to maintain the module and keys in both the source and target instances. You can do this by configuring [KMF key exchange](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/key-management-framework/task/configure-key-exchange.html). |
| Availability | Vancouver Patch 1 |

| **Encrypt or decrypt parameters for MID Server communication** |  |
| --- | --- |
| Example | //encrypt value   
var encrypter = new GlideEncrypter();
var encryptedValue = encrypter.encrypt(value);  
//decrypt value for modifying before sending to MID Server
var decryptedValue = encrypter.decrypt(encryptedValue) + " forMidServerComm"; 
//Encrypt the modified value.
var changedValue = encrypter.encrypt(decryptedValue); 
//ReEncrypt value for transport to MID Server.
var reEncryptValueForMid = encrypter.reencryptForAutomation(changedValue); 
OR 
//ReEncrypt as param value for transport to MID Server.
var reEncryptValueForMid = encrypter.reencryptParamForAutomation(changedValue); |
| Alternative | //encrypt value   
var encrypter = new sn_kmf_ns.KMFCryptoOperation("< moduleName >", "SYMMETRIC_ENCRYPTION") .withInputFormat("KMFNone");
var encryptedValue = encrypter.doOperation(value); 
 
//decrypt value for modifying before sending to MID Server
var decrypter = new sn_kmf_ns.KMFCryptoOperation("< moduleName >", "SYMMETRIC_DECRYPTION") .withOutputFormat("KMFNone")
var decryptedValue = decrypter.doOperation(encryptedValue) + " forMidServerComm"; 
//Encrypt value for transport to MID Server.
var encryptValueForMid = new GlideAutomationEncrypter().encrypt(decryptedValue); 
OR 
//Encrypt as param value for transport to MID Server.
var encryptParamValueForMid = SNC.ParameterEncrypter.encrypt(decryptedValue); 
 
Note:
These operations require a KMF module that supports SYMMETRIC_ENCRYPTION, SYMMETRIC_DECRYPTION and also tracks/allows the Decryptions. If you do not have a module that matches these criteria, you can [create a new KMF module](https://docs.servicenow.com/csh?topicname=create-cryptographic-module.html&version=latest) and use that in the code as an input parameter for module name. |
| Availability | Vancouver Patch 1 |

| **Encrypt or decrypt parameters or payload transferred** |  |
| --- | --- |
| Example | Transferring encrypted data between instances via XML export/import, update sets and web-service calls. |
| Alternative | Use KMFCryptoOperation to perform symmetric data encryption/decryption with the key resource exchanged to target instances ([KMFkey exchange](https://docs.servicenow.com/csh?topicname=configure-key-exchange.html&version=latest))  
To support decryption of both KMF encrypted values and glide encrypted values, use KMF_GLIDE_ENCRYPTER_FORMATTED input format decorator. |
| Availability | Vancouver Patch 1 |

| **Encrypt or decrypt parameters or payload transferred using custom keys** |  |
| --- | --- |
| Example | var encryptedValue = new GlideEncrypter("<custom_key>").encrypt(value); |
| Alternative | Avoid using hardcoded custom keys because they present security risks. Instead, consider using KMF for your key management and encryption needs, which can manage keys for the whole lifecycle.
For details on Key Import & Decryption of Externally Encrypted Data, see [KB1699673](https://support.servicenow.com/nav_to.do?uri=%2Fkb%3Fid%3Dkb_article_view%26sysparm_article%3DKB1699673). |
| Availability | Tokyo |

**Using Cryptographic operations in flow actions using Integration Hub.**

If you are using decryption in flow actions within Integration Hub, you can find details on how to replace GlideEncrypter in these flows in [KB1700626](https://support.servicenow.com/nav_to.do?uri=%2Fkb%3Fid%3Dkb_article_view%26sysparm_article%3DKB1700626).

**Deprecation Steps**

Find GlideEncrypter usage on your instance

To find customer modified scripts that use GlideEncrypter API on your instance, navigate to All > Instance Scan > Suites, and open and run the GlideEncrypter suite. See full details on using this suite in [Prepare your instance for GlideEncrypter deprecation](https://docs.servicenow.com/csh?topicname=check-3des.html&version=latest).

***NOTE*:** This scan tool has been further updated and required to re-run when instance is upgraded to Vancouver Patch 9 and above OR Washington DC Patch 3 and above OR Xanadu and above releases

NOTE: If time-outs are observed on execution of the Scan Suite, then

a)  It is recommended to increase the scan time-out ([Scan Check timeout system property](https://docs.servicenow.com/csh?topicname=hs-create-new-heath-check-timeout.html&version=latest)) value temporarily to 20000 and

b)  It is recommended to run each Test Check independently and analyze the findings as defined below.

If Test Checks are timing out even after the above steps then please contact Customer Support.

**Analyze the findings**

- If there are no findings, then no further action is required.
- If there are any findings:
    - If a finding is found in a customer created or modified record, update the scripts using the proposed alternatives in the Alternatives with examples section earlier in this document.
    - If a finding is found to be an OOB record, then ServiceNow will address them in Yokohama release and no action is required.
    - If the findings are related to workflow engine, refer to [KB1700626](https://support.servicenow.com/nav_to.do?uri=%2Fkb%3Fid%3Dkb_article_view%26sysparm_article%3DKB1700626).

**Test**

Execute any scripts you have modified to ensure that they are working as expected.

**Test Script**

Before you make changes to your scripts, you can use the following example script to verify the functionality of the Key Management Framework’s alternatives to GlideEncrypter.  You can run this example script in the Scripts - Background page.

1. Logon to your instance and navigate to All > System Definition > Scripts -Background
2. In the Run Script box, enter the code example listed below.
3. To execute a script, select Global in the “in scope” list, then select the Run Script button.

1. 1. Logon to your instance and navigate to All > System Definition > Scripts -Background
2. 2. In the Run Script box, enter the code example listed below.
3. 3. To execute a script, select Global in the “in scope” list, then select the Run Script button.

[](https://support.servicenow.com/sys_attachment.do?sys_id=ecd4daef931692d0101833527cba1013)

**Self-made module test**

Use this example script to verify an encryption and decryption operation runs as expected on your instance.

NOTE: global.glide_encrypter_test_no_parent is not an OOTB module it is created for this test example purpose only.

```jsx
//encrypt
var encryptOp = new sn_kmf_ns.KMFCryptoOperation("global.glide_encrypter_test_no_parent", "SYMMETRIC_ENCRYPTION").withInputFormat("KMFNone");
var encryptedText = encryptOp.doOperation("password12345");
gs.info(encryptedText);

//decrypt
var decryptOp = new sn_kmf_ns.KMFCryptoOperation("global.glide_encrypter_test_no_parent", "SYMMETRIC_DECRYPTION").withOutputFormat("KMFNone");
var clear_text = decryptOp.doOperation(encryptedText);
gs.info(clear_text);
```

**FAQ:**

**1. Am seeing a lot of sys_variblae_value records in my instance scan results for GlideEncrypter, they do not belong to any custom code we added?**    If the script you are referring to is shipped by Servicenow, servicenow will take care of it. You can ignore that file.**2. Am seeing a lot of sys_variblae_value records in my instance scan results for GlideEncrypter, and they belong to workflows that are not published. What action item do i have for these?**  The instance scan looksup into all references and provides an overview to customers. If the finding in sys_variable_value belongs to particular work flow that is in Draft, it is possible that you may publish it in future, you have to address it appropriately before you publish it.If the scan finding is referring to a workflow that has a newer version, you can ignore that finding. You only need to address the findings relevant to active or draft workflows. you can confidently ignore other findings.

**3. I fixed the scan results and published a new version for my workflows, but i keep seeing the old references whenever i scan**

The instance scan lookup into all references and provides an overview to customers. If there are some files that you have already addressed in a new version of the activity or flow or a script, you can ignore the findings from those old versions of the records.

## Related

- [[Security & ACL]]
- [[How to replace usage of GlideEncrypter in Legacy W]]
- [[Comparing ServiceNow encryption solutions]]
- [[Enabling Report View ACLs]]