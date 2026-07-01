---
aliases:
  - "How to replace usage of GlideEncrypter in Legacy W"
tags:
  - encryption
  - glide-encrypter
  - kmf
  - workflow
  - orchestration
  - security
---

# How to replace usage of GlideEncrypter in Legacy Workflow/Orchestration

### **Summary**

You might be using GlideEncrypter in a server-side script to encrypt values passed to Orchestration activities with an 'Encrypted' type input variable.

Due to 3DES deprecation affecting GlideEncypter (more information available in [KB1320986](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1320986)), you will need to replace all usage of GlideEncypter with secure alternatives before upgrading to the Zurich release.

The suggestions in the KB don't cover the specific crypto operation that Legacy Workflow expects for 'Encrypted' type input variables and you may see an error similar to 'Input variable Password is not Password2 type' after following along with the examples provided.

Please follow the instructions below to create a KMF module to be used for 'Symmetric Wrapping' and replace your usages of GlideEncrypter with KMFCryptoOperation (operationName = 'SYMMETRIC_WRAPPING').

### **Release**

All releases starting from Vancouver Patch 1

### **Instructions**

1. Create a cryptographic module (sys_kmf_crypto_module)
    ◦ Here we've used the Module name 'orchestration_crypt' (full name = global.orchestration_crypt), this is important to note as it is used in step #6.
    ◦ Docs: [Create a cryptographic module](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/create-cryptographic-module.html)
    ◦ Our example uses a 'track' default access policy, if you've selected a 'reject' policy you may get failures in the workflow ('Input variable Password is not Password2 type'). You'll need to create an access policy if you decide to use 'reject'. [Create a module access policy](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/create-module-access-policy.html)
    ◦ 
2. Create a cryptographic specification for the module with Crypto purpose = 'Symmetric Key Wrapping/Unwrapping'
    ◦ Docs: [Create a cryptographic specification](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/create-crypto-spec.html) 
    ◦ 
3. Press 'Next' and configure the Lifecycle Definition for the specification.
    ◦ We've used the default values, if you're looking to change the configuration here please review the documentation. Docs: [Configure key lifecycle states](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/configure-key-lifecycle-states.html)
4. Press 'Next' again and you'll be taken to the key generation screen. Click the 'Generate key' link and a key will be generated, you'll be redirected to the cryptographic module form.
    ◦ Docs: [Generate a ServiceNow cryptographic key](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/generate_sn_key.html)
5. If your cryptographic module is still in the 'Draft' state, move it to 'Published' and save.
    ◦ 
6. Replace your usages of GlideEncrypter with the following code

`var password = 'Example123!';

// old method (GlideEncrypter)

var encr = new GlideEncrypter();
workflow.scratchpad.encrypted_password = encr.encrypt(password);

// new method (KMFCryptoOperation). Note: "global.orchestration_crypt" is the name of the cryptographic module created in step #1, replace it if needed.

var encr = new sn_kmf_ns.KMFCryptoOperation("global.orchestration_crypt","SYMMETRIC_WRAPPING").withAlgorithm("AES").withInputFormat("KMFNONE");
workflow.scratchpad.encrypted_password = encr.doOperation(password);`

1. 1. Create a cryptographic module (sys_kmf_crypto_module)
    - ◦ Here we've used the Module name 'orchestration_crypt' (full name = global.orchestration_crypt), this is important to note as it is used in step #6.
    - ◦ Docs: [Create a cryptographic module](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/create-cryptographic-module.html)
    - ◦ Our example uses a 'track' default access policy, if you've selected a 'reject' policy you may get failures in the workflow ('Input variable Password is not Password2 type'). You'll need to create an access policy if you decide to use 'reject'. [Create a module access policy](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/create-module-access-policy.html)
    - ◦
        
        [](https://support.servicenow.com/sys_attachment.do?sys_id=542eb8b947bf5e50b7832920326d43a4)
        
- 
- 
- 
- 
    
    [](https://support.servicenow.com/sys_attachment.do?sys_id=542eb8b947bf5e50b7832920326d43a4)
    

[](https://support.servicenow.com/sys_attachment.do?sys_id=542eb8b947bf5e50b7832920326d43a4)

1. 2. Create a cryptographic specification for the module with Crypto purpose = 'Symmetric Key Wrapping/Unwrapping'
    - ◦ Docs: [Create a cryptographic specification](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/create-crypto-spec.html)
    - ◦
        
        [](https://support.servicenow.com/sys_attachment.do?sys_id=902eb8b947bf5e50b7832920326d43a7)
        
- 
- 
    
    [](https://support.servicenow.com/sys_attachment.do?sys_id=902eb8b947bf5e50b7832920326d43a7)
    

[](https://support.servicenow.com/sys_attachment.do?sys_id=902eb8b947bf5e50b7832920326d43a7)

1. 3. Press 'Next' and configure the Lifecycle Definition for the specification.
    - ◦ We've used the default values, if you're looking to change the configuration here please review the documentation. Docs: [Configure key lifecycle states](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/configure-key-lifecycle-states.html)
- 
1. 4. Press 'Next' again and you'll be taken to the key generation screen. Click the 'Generate key' link and a key will be generated, you'll be redirected to the cryptographic module form.
    - ◦ Docs: [Generate a ServiceNow cryptographic key](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/key-management-framework/task/generate_sn_key.html)
- 
1. 5. If your cryptographic module is still in the 'Draft' state, move it to 'Published' and save.
    - ◦
        
        [](https://support.servicenow.com/sys_attachment.do?sys_id=a42eb8b947bf5e50b7832920326d43a9)
        
- 
    
    [](https://support.servicenow.com/sys_attachment.do?sys_id=a42eb8b947bf5e50b7832920326d43a9)
    

[](https://support.servicenow.com/sys_attachment.do?sys_id=a42eb8b947bf5e50b7832920326d43a9)

1. 6. Replace your usages of GlideEncrypter with the following code
    
    ```jsx
    var password = 'Example123!';
    
    // old method (GlideEncrypter)
    
    var encr = new GlideEncrypter();
    workflow.scratchpad.encrypted_password = encr.encrypt(password);
    
    // new method (KMFCryptoOperation). Note: "global.orchestration_crypt" is the name of the cryptographic module created in step #1, replace it if needed.
    
    var encr = new sn_kmf_ns.KMFCryptoOperation("global.orchestration_crypt","SYMMETRIC_WRAPPING").withAlgorithm("AES").withInputFormat("KMFNONE");
    workflow.scratchpad.encrypted_password = encr.doOperation(password);
    ```

## Related

- [[Security & ACL]]
- [[Alternative Encryption Products to GlideEncrypter]]
- [[Enabling Report View ACLs]]
- [[Comparing ServiceNow encryption solutions]]