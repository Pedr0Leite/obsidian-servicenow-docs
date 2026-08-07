---
title: "Customization support in MultiSSOv2"
aliases:
  - KB0778203
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778203
kb_number: KB0778203
last_modified: 2025-01-03
---

## Customization support in MultiSSOv2

  

### Summary

Excess customization can build up technical debt and lengthen your upgrade cycle, inhibiting your ability to take advantage of new features. Evaluate demands for customization very carefully and only resort to customization where there is clear business value and no alternative to satisfying demand. Before you plan to go for customizations, please review [customization best practices for ServiceNow.](https://www.servicenow.com/success/playbook/innovate-at-scale.html#resources "customization best practices for ServiceNow")

Coming to MultiSSO, before you plan to modify the scripts please check if the same functionality can be achieved by configurations in the identity provider record. Some of the features which were not supported in previous releases or used to require customizations are now supported out-of-the-box (OOTB). Some examples are:

1.  HTTP-POST redirect binding
2.  IDP initiated single logout (SLO) (Rome release onwards)

In the MultiSSOv1 version, modifications used to be made in the SAML2\_update1 and MultiSSO\_SAML2\_update1 script includes for customizations. Making changes to these OOTB scripts, used to create upgrade challenges. As ServiceNow upgrades will not overwrite customizations you have made but will mark them as skipped records in the ServiceNow Upgrade Monitor. To make sure they’re successfully ported to the upgraded instance, manual intervention was required for handling the skipped changes.  
  
To avoid these upgrade challenges, In the MultiSSOv2 version, we are changing the way customizations in OOTB implementation are supported.  
This KB provides a basic idea, how existing or new customizations can be incorporated in the MultiSSOv2 version.  
  
  
  

### Release

These instructions are valid for the MultiSSOv2 version, which is available in the New York release onwards. 

### Instructions

In order to reduce some of the upgrade challenges, core single sign-on script includes are made read-only for customers in MultiSSOv2. Additional script includes are provided specifically for applying customizations. These custom scripts extend the core scripts. Methods available in these read-only core script-includes can be overridden in the corresponding custom scripts. Extension points and supporting methods are also provided in the OOTB scripts to support various customization use cases.  
  
Note: ServiceNow will not make modifications to these custom scripts provided for customization purposes.**  
  
Mapping of the script includes and Installation exits in MultiSSOv2 and MultiSSOv2**

<table class="MsoTableGrid" style="border-collapse: collapse; border: none; height: 256px;" border="1" width="941" cellspacing="0" cellpadding="0"><tbody><tr><td style="width: 96.2656px; border: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-family: verdana, geneva;"><strong><span style="font-size: 8.0pt; color: #4472c4;">Feature</span></strong></span></p></td><td style="width: 100.266px; border-top: 1pt solid windowtext; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-image: initial; border-left: none; padding: 0cm 5.4pt;" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-family: verdana, geneva;"><strong><span style="font-size: 8.0pt; color: #4472c4;">Type</span></strong></span></p></td><td style="width: 226.578px; border-top: 1pt solid windowtext; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-image: initial; border-left: none; padding: 0cm 5.4pt;" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-family: verdana, geneva;"><span style="color: #4472c4;"><span style="font-size: 10.6667px;"><strong>Script to modify for&nbsp;<br>Customization</strong></span></span><strong style="font-size: 12pt;"><span style="font-size: 8.0pt; color: #4472c4;">&nbsp;in v1</span></strong></span></p></td><td style="width: 213.547px; border-top: 1pt solid windowtext; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-image: initial; border-left: none; padding: 0cm 5.4pt;" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-family: verdana, geneva;"><strong><span style="font-size: 8.0pt; color: #4472c4;">Read-only scripts with&nbsp;<br>OOTB Implementation in MultiSSOv2 version</span></strong></span></p></td><td style="width: 224.594px; border-top: 1pt solid windowtext; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-image: initial; border-left: none; padding: 0cm 5.4pt;" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-family: verdana, geneva;"><span style="color: #4472c4;"><span style="font-size: 10.6667px;"><strong>Script to override the OOTB implementation for<br>Customization</strong></span></span><strong style="font-size: 12pt;"><span style="font-size: 8.0pt; color: #4472c4;"> in MultiSSOv2</span></strong></span></p></td></tr><tr><td style="width: 96.2656px; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 0cm 5.4pt;" rowspan="4" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-size: 8pt; font-family: verdana, geneva;">MultiSSO</span></p></td><td style="width: 100.266px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" rowspan="2" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-size: 8pt; font-family: verdana, geneva;">Script Include</span></p></td><td style="width: 226.578px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: red; font-family: verdana, geneva;">SAML2_update1</span></p></td><td style="width: 213.547px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">SAML2_internal</span></p></td><td style="width: 224.594px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">S</span><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">AML2_custom</span></strong></p></td></tr><tr><td style="width: 226.578px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: red; font-family: verdana, geneva;">MultiSSO_SAML2_Update1</span></p></td><td style="width: 213.547px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">MultiSSOv2_SAML2_internal</span></p></td><td style="width: 224.594px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">MultiSSOv2_SAML2_custom</span></strong></p></td></tr><tr><td style="width: 100.266px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" rowspan="2" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-size: 8pt; font-family: verdana, geneva;">Installation Exit</span></p></td><td style="width: 226.578px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: red; font-family: verdana, geneva;">MultiSSO</span></p></td><td style="width: 213.547px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">&nbsp;</span></p></td><td style="width: 224.594px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">MultiSSOv2</span></strong></p></td></tr><tr><td style="width: 226.578px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: red; font-family: verdana, geneva;">MultiSSOLogout</span></p></td><td style="width: 213.547px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">&nbsp;</span></p></td><td style="width: 224.594px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">MultiSSOLogoutv2</span></strong></p></td></tr><tr><td style="width: 96.2656px; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 0cm 5.4pt;" rowspan="2" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-size: 8pt; font-family: verdana, geneva;">E-signature</span></p></td><td style="width: 100.266px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" rowspan="2" valign="top"><p style="text-align: center; margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;" align="center"><span style="font-size: 8pt; font-family: verdana, geneva;">Script Include</span></p></td><td style="width: 226.578px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: red; font-family: verdana, geneva;">ESignatureUtils</span></p></td><td style="width: 213.547px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">&nbsp;</span></p></td><td style="width: 224.594px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">ESignatureUtils</span></strong></p></td></tr><tr><td style="width: 226.578px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: red; font-family: verdana, geneva;">SAML2_update1_esig</span></p></td><td style="width: 213.547px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">&nbsp;</span></p></td><td style="width: 224.594px; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0cm 5.4pt;" valign="top"><p style="margin: 0cm 0cm 0.0001pt; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8pt; color: #385623; font-family: verdana, geneva;">SAML2_custom_esig</span></strong></p></td></tr></tbody></table>

While migrating existing customizations from the MultiSSOv1 version to MultiSSOv2, customers can override the OOTB behavior in custom scripts.

For example:

in MultiSSOv1, if the customizations were done in a particular method in the SAML2\_update1 script include, the corresponding method will be available in SAML2\_internal script include in the MultiSSOv2. The same method can be overridden in the SAML2\_custom script include for customization.

Similarly, if the customizations in MultiSSOv1 were in the MultiSSO\_SAML2\_Update1 script include, In MultiSSOv2 corresponding OOTB implementation is available in the MultiSSOv2\_SAML2\_internal script includes.  The same method can be overridden in the MultiSSOv2\_SAML2\_custom script include for customizations. The same is applicable for SAML2\_update1\_esig to SAML2\_custom\_esig script includes.

Overview of methods available in SMAL2\_internal

**OOTB Authentication options for override Authn request options.**

1.  _forceAuthn_

to set the forceAuthn in AuthnRequest

2.  _isPassive_

to set the AuthnRequest as passive in the script

3.  _assertionConsumerServiceURL_

to set the assertion consumer service URL in the script while building custom Authn Request

4.  _assertionConsumerServiceIndex_

to set the assertion consumer service index in the script while building custom Authn Request

5.  _providerName_

to set the provider name in the script while building custom Authn Request

6.  _skipNavFrame_

if the customer wants to render specific URLs or patterns without the navigation frame(for Portals etc), they can set skip a frame option. While generating relay state, nav\_to will not be added to the URL and the page will be rendered without the navigation frame_._

7.  _deepLink_

if the customer wants to set a custom deep link or starting page for specific URLs or patterns, they can set this parameter. End-user will always be redirected to that deep-link post successful login.

Example script for overriding _getAuthnOptions_ method available in SAML2\_internal script include in SAML2\_custom script include. These examples are only for demonstration purposes. Please test your customizations thoroughly before applying those in the production instances.

```
getAuthnOptions : function() {

                                    var authGenerationOptions = {};

                                    if(this.isTestSAMLConnection()){

                                                      authGenerationOptions.forceAuthn = true;  

                                    }

                                    return authGenerationOptions;

},
```

Override in SAML2\_custom like the example below

```
gs.include("PrototypeServer");

var SAML2_custom = Class.create();

SAML2_custom.prototype = Object.extend(new SAML2_internal(), {

                  initialize:function() {

                                    SAML2_internal.prototype.initialize.call(this);

                  },

                 

    getAuthnOptions : function() {

                                    var authGenerationOptions = {};

                                    if(this.isTestSAMLConnection())    {

                                                      authGenerationOptions.forceAuthn = true;  

                                   }

                                    //Customization for forceAuthn

           authGenerationOptions.forceAuthn = true;

                                    return authGenerationOptions;

                            },

 

                  type: 'SAML2_custom'

});
```

**OOB  Method available for customising SAML response validation**

Response validation options (true/false) available to support customizations.

1.  skip\_responseissuer\_check
2.  skip\_assertionissuer\_check
3.  skip\_audiencerestriction\_check
4.  skip\_onetimeuse\_check
5.  skip\_proxyrestriction\_check
6.  skip\_inresponseto\_check
7.  skip\_sessionindex\_check
8.  skip\_unknown\_attribute\_check
9.  support\_httppost\_login\_only

getValidationOptions:

 This method is to support customizations in SAML response validation.

Method available in SAML2\_internal

```
getValidationOptions : function() {

                                    var responseValidationOptions = {};

                                    return responseValidationOptions;

},
```

Override in SAML2\_custom like the example below.

```
gs.include("PrototypeServer");

var SAML2_custom = Class.create();

SAML2_custom.prototype = Object.extend(new SAML2_internal(), {

                  initialize:function() {

                                    SAML2_internal.prototype.initialize.call(this);

                  },

                 

                  getValidationOptions : function() {

                                    var responseValidationOptions = {};

                                    responseValidationOptions. skip_sessionindex_check=true;

                                    return responseValidationOptions;

                  },

 

                  type: 'SAML2_custom'

});

 
```

**Customizing AuthN request**

customizeAuthnRequest:

    if the Authn request customization cannot be achieved through the options available in getAuthnOptions method, customized Authn request can be build using GlideXML API and set the modified request using this method.

Method available in SAML2\_internal

```
customizeAuthnRequest: function (xmlAuthnRequestElement) {

                                    return;

                  },
```

Override in SAML2\_custom like the example below.

example script:  create a scope using request DOM

```
customizeAuthnRequest: function () {

                  //Customization through Request DOM Element

                  var xmlAuthnRequestElement = this.glidesaml2api.getGeneratedReqElemDOM();

                  var parentNameSpace = xmlAuthnRequestElement.getPrefix();

                  var scopingElement = GlideXMLUtil.newElement(xmlAuthnRequestElement, parentNameSpace + ":Scoping");

                  var idpListElement = GlideXMLUtil.newElement(scopingElement, parentNameSpace + ":IDPList");

                  var idpEntryElement = GlideXMLUtil.newElement(idpListElement, parentNameSpace + ":IDPEntry");

                  idpEntryElement.setAttribute('Name', 'uia.no');

                  idpEntryElement.setAttribute('ProviderID', this.getSSORecord().getValue('idp'));

                  this.glidesaml2api.setCustomizedReqElemDOM(xmlAuthnRequestElement); //this is mandatory if the DOM is customized

}
```

**Customizing Logout request**

customizeLogoutRequest: customize the logout request similar to the above example using GlideXML API and set the modified request using this method. The below example adds two extra attributes (NameQualifier and SPNameQualifier) to the NameID node which is obtained from an already built logout request element.

```
customizeLogoutRequest: function() {
       var xmlRequestElement = this.glidesaml2api.getGeneratedReqElemDOM();
       var nodeList = xmlRequestElement.getChildNodes();
       var nameidElement = null;
       for (var i = 0; i < nodeList.getLength(); i++) {
             if ("saml2:NameID".equalsIgnoreCase(nodeList.item(i).getNodeName())) {
                   nameidElement = nodeList.item(i);
                   break;
             }
       }

       if (nameidElement != null) {
             nameidElement.setAttribute("NameQualifier", "TEST VALUE");
             nameidElement.setAttribute("SPNameQualifier", "ANOTHER TEST VALUE");
       }
       this.glidesaml2api.setCustomizedReqElemDOM(xmlRequestElement);

}
```

`   `

### Related Links

Related resources

-   [Steps to migrate from MultiSSOv1 to MultiSSOv2](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0756504 "Steps to migrate from MultiSSOv1 to MultiSSOv2")
-   [Customization best practices for ServiceNow](https://www.servicenow.com/success/playbook/innovate-at-scale.html#resources "Customization best practices for ServiceNow")
-   [Upgrade quickly and maintain platform health](https://www.servicenow.com/success/instance-upgrades.html "Upgrade quickly and maintain platform health")
