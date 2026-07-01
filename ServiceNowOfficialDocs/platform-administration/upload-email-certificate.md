---
title: Upload an email certificate
description: Upload an email certificate to validate a signature for inbound email or encrypt an outbound email or both for secure communication.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/upload-email-certificate.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Setting up S/MIME, Email encryption, Email Administration, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Upload an email certificate

Upload an email certificate to validate a signature for [[ia-inbound-email-il|inbound email]] or encrypt an [[ia-outbound-email-il|outbound email]] or both for secure communication.

## Before you begin

-   To enable signing in the instance, upload the private-public key pair corresponding to the instance email account.
-   To enable encryption in the instance and send encrypted email to a recipient's email address, upload the public key/certificate corresponding to the recipient’s email address.


Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Notification** &gt; **SMIME** &gt; **Email Certificate**.

2.  Select **New**.

3.  Select the attachment icon \[Omitted image "attach-icon.png"\] Alt text: Attachment icon to upload the email certificate.

4.  On the form, fill in the fields.

    |Fields|Descriptions|
    |------|------------|
    |Email|Email address for sending the email.|
    |Expiration notification|Select the check box to enable expiration.|
    |Notify on expiration|Add yourself to be notified before expiration.|
    |Warn in days to expire|Number of days to send the warning prior to the expiration date.|
    |Active|Check box to enable the email certificate.|
    |Key store password|Key password to protect PKCS \#12 file.|
    |Short description|The description for this email certificate.|

5.  Select **Submit**.


## What to do next

Enable[[enable-smime-for-outbound-and-inbound|Enable S/MIME]].

**Parent Topic:**[[smime-for-email-signing-and-encryption|Setting up S/MIME for email]]

**Related topics**  


[Import an S/MIME key pair]()

[Upload a CA certificate]()

[Enable S/MIME]()

## Related

- [[enable-smime-for-outbound-and-inbound|Enable S/MIME]]
- [[smime-for-email-signing-and-encryption|Setting up S/MIME for email]]
- [[ia-inbound-email-il|Inbound email]]
- [[ia-outbound-email-il|Outbound email]]
