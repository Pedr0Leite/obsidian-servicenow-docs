---
title: "Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance"
aliases:
  - KB0696002
tags:
  - servicenow
  - support-kb
  - mutual-authentication
  - ssl
  - certificates
  - web-services
  - REST
  - SOAP
  - integration
  - security
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696002
kb_number: KB0696002
last_modified: 2026-03-04
---

## Configure Outbound Mutual Authentication (calling 3rd party Web Services) in ServiceNow Instance

  

### Issue

Mutual authentication establishes trust by exchanging SSL (Secure Socket Layer) certificates.

Before connecting to a server, the client requests an SSL certificate. The server responds by requesting that the client send its own certificate. Both respond by validating the certificates and sending acknowledgments before initiating an HTTPS connection.

This article outlines the steps required to set up mutual authentication. Please note that the customer will create and own the ServiceNow instance certificates used for mutual authentication.

Observe that this feature only enables mutual authentication on **outbound https connections**.

### Release

Madrid and newer

### Resolution

The following steps can be executed to set up mutual authentication:

First, the ServiceNow side is set up and shared with the 3rd party

#### A) Creating the Key Store

In this step, you will create a keystore file containing the private and public keys that will be used by ServiceNow side mutual authentication.

The ServiceNow instance will use the public key certificate as authentication with the 3rd party web server.

1.  Generate a new Java keystore and key pair (keyool -genkey command).
2.  Generate a CSR (Certificate Signing Request) for the existing Java keystore (keytool -certreq command).  
    -   Use your own domain for this certificate request.
3.  Import a root or intermediate certificates from the certificate authority into the Java keystore (keytool -import -trustcacerts command).
4.  Import the signed primary certificate returned by your CA authority into the Java keystore (keytool -import -trustcacerts command).

**Notes:**

-   The CA authority may provide you specific instructions about what to include in the certificate request.
-   Keep record of your Keystore password and certificate alias.

#### B) Setting up the Key Store record in ServiceNow.

Role required: **admin**

1.  In **System Definition > Certificates** page, click **New** and set the following fields:  
    -   Enter a Name
    -   Set Type = **Java Key Store**
    -   Set the key store to **Active**
    -   Provide a Key store password (the one used to create the keystore).
2.  Attach the keystore file created in step (A) into the record.
3.  Click **Submit** to create the Java Key Store entry.

#### C) Create a protocol profile

Role required: **admin**

1.  Navigate to **System Security > Protocol Profiles**.
2.  2\. Click **New**.  
    -   Enter a unique name to identify this protocol, such as myhttps ( this name cannot be http).
    -   Enter the protocol communication port (443 for SSL).
    -   Select the Keystore Record created on B) above.
3.  Save the record.

#### D) Share the new keystore's public key with your 3rd party web service provider.

This is the authentication certificate used by ServiceNow.

1.  Using the Java "**keytool -export**" command, export the public key from your recently created keystore file into a DER or PEM format certificate file.
2.  Share this file with your 3rd Party web service provider

As the next step, we will load the 3rd party's PEM/DER certificate into our certificates table, so that the certificate can be verified by the mutual auth process:

#### E) Specifying a Trusted Server Certificate.

This step will import into ServiceNow trust store a public certificate provided by your 3rd party web service. This is the authentication certificate used by your 3rd party.

Role required: **admin**

1.  Navigate to **System Definition > Certificates**.
2.  Click **New** and provide:  
    -   A record a name
    -   Set the Type field to be "Trust Store Cert".
    -   If the certificate provided by the 3rd party is in PEM format, set the Format field to PEM and paste the PEM string into the PEM Certificate field on the record.
    -   If the certificate provided by the 3rd party is in DER format, set the Format field to DER and just attach the certificate file to the record.
3.  Click on **Submit**.

Now that everything is set up correctly, we can enable mutual authentication

#### F) Enable mutual authentication

Role required: **web\_service\_admin** or **admin**

1.  Navigate to **System Web Services > SOAP Message** or **System Web Services > REST Message**.
2.  Select a message record.
3.  Select the **Use mutual authentication** check box.
4.  In the **Protocol profile** field, select a protocol profile configured on D) above for mutual authentication.
5.  Click **Update**.

Test your web service, the Mutual Authentication should allow the web service to complete the call. 

-   If you get error "unsupported protocol" when testing the web service request, ensure that you used the -trustcacerts import option in step A and that the resulting alias is of type "TrustedCertEntry"

### Related Links

Documents used to outline the solution:

-   [Setting up mutual authentication](https://docs.servicenow.com/csh?topicname=c_MutualAuthentication.html&version=latest)
-   [Outbound web services mutual authentication](https://docs.servicenow.com/csh?topicname=c_OutboundWebServicesMutualAuth.html&version=latest)
-   [Create a protocol profile](https://docs.servicenow.com/csh?topicname=t_CreateAProtocolProfile.html&version=latest)
-   [Enable mutual authentication](https://docs.servicenow.com/csh?topicname=t_EnableMutualAuth.html&version=latest)

## Related

- [[KB0691876 - Mutual Authentication Overview]]
- [[KB0696599 - Debugging Mutual Authentication]]
- [[KB0720035 - Error calling Scoped Outbound REST message]]
- [[t_ConfigureRESTMsgBasicAuth]]
