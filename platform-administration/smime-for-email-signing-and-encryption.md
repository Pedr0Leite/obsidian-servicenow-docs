---
title: Setting up S/MIME for email
description: S/MIME is a protocol for sending digitally signed and encrypted emails to ensure the confidentiality, authenticity and integrity.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/smime-for-email-signing-and-encryption.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Email encryption, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Setting up S/MIME for email

S/MIME is a protocol for sending digitally signed and encrypted emails to ensure the confidentiality, authenticity and integrity.

## Set up S/MIME for outbound mails \(signing and encryption\)

You can use S/MIME for outbound mails for the following purposes:

-   Digital signature
-   Encryption
-   Digital signature and encryption

To set up S/MIME, the admin must have the following:

-   email\_account\_admin and sn\_kmf.cryptographic\_manager roles
-   Key pair \(private key and public key\)
-   CA certificate
-   Email certificate

Upload the instance email account key pair and email certificates, and enable outbound S/MIME properties. For more information, see [[enable-smime-for-outbound-and-inbound|Enable S/MIME]].

If there are multiple recipients and some of the recipients do not have valid certificates, the email will be sent only to recipients with a valid certificate.

## Set up S/MIME for inbound mails \(sign verification and decryption\)

S/MIME for inbound mails can be used for the following:

-   Signature verification
-   Decryption
-   Signature verification and decryption

For information about enabling inbound S/MIME properties, see [Enable S/MIME](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/enable-smime-for-outbound-and-inbound.md).

If the system fails to decrypt a message, no inbound actions will run on the email and it is moved to the received-ignored status.

To set up the system to ignore inbound signed emails if the signature cannot be verified or is invalid, admins can create the **email.inbound.smime.ignore\_unverified\_emails** and set it to true.

For more information about key management and cryprographic module, see [Key Management Framework Reference](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-security/understanding-kmf.md).

-   **[[import-smime-key-pair|Import an S/MIME key pair]]**  
Import an S/MIME key pair consisting of the private key and certificate to sign outbound emails or decrypt emails.
-   **[[upload-ca-certificate|Upload a CA certificate]]**  
Upload a digital CA \(Certificate Authority\) certificate to validate email certificates for secure communication.
-   **[[upload-email-certificate|Upload an email certificate]]**  
Upload an email certificate to validate a signature for [[ia-inbound-email-il|inbound email]] or encrypt an [[ia-outbound-email-il|outbound email]] or both for secure communication.
-   **[Enable S/MIME](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/enable-smime-for-outbound-and-inbound.md)**  
Configure S/MIME settings for inbound and outbound email.

**Parent Topic:**[[smime-inbound-outbound-mails|Email encryption - S/MIME protocol]]

**Related topics**  


[Activate S/MIME Email]()

## Related

- [[enable-smime-for-outbound-and-inbound|Enable S/MIME]]
- [[import-smime-key-pair|Import an S/MIME key pair]]
- [[upload-ca-certificate|Upload a CA certificate]]
- [[upload-email-certificate|Upload an email certificate]]
- [[smime-inbound-outbound-mails|Email encryption - S/MIME protocol]]
- [[ia-inbound-email-il|Inbound email]]
- [[ia-outbound-email-il|Outbound email]]
