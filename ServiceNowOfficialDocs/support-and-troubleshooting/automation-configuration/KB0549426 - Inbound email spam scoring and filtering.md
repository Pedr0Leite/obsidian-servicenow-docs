---
title: "Inbound email spam scoring and filtering"
aliases:
  - KB0549426
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549426
kb_number: KB0549426
last_modified: 2026-03-20
---

## Issue

### How does spam scoring work?

Every message sent through ServiceNow email servers is assessed for the likelihood of being spam. Based on the scoring assessment, ServiceNow adds headers to each message that can be used for filtering within the customer instance using the Email Filters plugin. For more information, see [Email Filters](https://docs.servicenow.com/csh?topicname=c_EmailFilters.html&version=latest).

The two main requirements for spam scoring are:

-   Performance: Scoring of messages should not delay or impact mail delivery
-   Accuracy: Messages should be scored accurately so that they can be properly filtered within the instance

**NOTE: If an instance uses a private email server, this article is not applicable.**

### How do I filter spam with the Email Filters plugin?

Within the Email Filters module, there is a **SPAM Assassin** filter or a **Move spam to junk folder** filter. Update the filter conditions in order to enable filtering on the spam headers. Either one or both of the following headers may appear in an email:

X-ServiceNow-Spam-Flag:YES

X-ServiceNow-Virus:INFECTED

The filter condition should, therefore, include an OR condition for both of those headers.

After an email is moved to the Junk mailbox, no inbound actions are run against the email.

Administrators can also create their own filters. Navigate to **System Mailboxes > Administration > Filters** to view the module.

### Example spam score headers

Headers from a message with a low spam score (for example, not spam):

X-ServiceNow-Spam-Flag:NO  
X-ServiceNow-Spam-Score:1.428  
X-ServiceNow-Spam-Level:\*  
X-ServiceNow-Spam-Status:No, score=1.428 tagged\_above=0 required=6.2 

Headers from a message with a high spam score:

X-ServiceNow-Spam-Flag:YES  
X-ServiceNow-Spam-Score:999  
X-ServiceNow-Spam-Level:\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
X-ServiceNow-Spam-Status:Yes, score=999 tagged\_above=0 required=6.2 

Headers from a message with a virus-infected attachment:

X-ServiceNow-Virus:INFECTED, message contains virus: Eicar-Test-Signature 

While other spam-related headers may be present in an email, ServiceNow discourages filtering on headers other than X-ServiceNow-Spam-Flag and X-ServiceNow-Virus:INFECTED in your Email Filters. Any additional headers and their contents may change over time, breaking your spam handling in your instance.

### How do I filter spam without the Email Filters plugin?

Although it is recommended to activate the Email Filters plugin, at times this may not be an option (Express instances). When the Email Filters plugin is not active, email properties are used for filtering emails. For spam filtering, the property: 'glide.pop3.ignore\_headers' is used and will be populated with the following comma-separated values: X-ServiceNow-Spam-Flag:YES,X-ServiceNow-Virus:INFECTED. If an email has either of these values in the header, the type will be set to 'received-ignored' and the email moved to the Junk mailbox. The error string of the email record will have a message "Ignoring inbound email with subject <subject> or userEmail <sending email address>."

An administrator can disable filtering by removing these values from the property.

### Do messages with potentially malicious attachments get scored?

Yes, the header **X-ServiceNow-Virus:INFECTED** indicates that one or more malicious attachments are present in an email.

To help anyone looking at the email to note the anomaly, the ServiceNow mail servers also insert the text "\*\*\* INFECTED \*\*\*" in the email subject line. This text is intended to alert someone reading the email of the anomaly. Any automatic filtering should rely on the headers.

### An email is missing - did spam scoring block it from my instance?

No. Email is never filtered, blocked, or quarantined from the instance as part of spam scoring. It is only scored and then sent on to the instance. All filtering is done within the instance with the Email Filters plugin. If an email is missing, administrators should search the Junk mailbox for the email. The best way to search for a missing email is to get the message-ID from the sender of the email and to search the entire email table with an indexed search. Searching both message-id and Type (received or received-ignored), with no date time constraint, your filter will look like:

example: message\_id=<20130219220111.3B45A1A131C@bulk.service-now.com>^type=received^ORtype=received-ignored

See [KB0563560 - Missing email in an instance](https://support.servicenow.com/kb_view.do?sysparm_article=KB0563560) for more information on locating a missing email.

### An email is delayed - did spam scoring delay my email from being delivered to the instance?

No. The spam scoring architecture has fail-safes in place to prevent any delay and to prevent impact to mail delivery. ServiceNow prioritizes delivery; therefore if scoring introduces unacceptable delay, ServiceNow temporarily disables scoring in order to ensure maximum performance and delivery.

### I do not like the spam scores - what can I do?

ServiceNow will continually improve spam scoring, but cannot accommodate individual suggestions on the scoring algorithm. If the spam scoring is not working as required for your company, turn off any filtering of the scored emails within the Email Filters on the instance.

Note that as of 6/29/2017, SPF checks now factor more heavily into a mail's spam score. In order to be flagged as spam, a message must have an aggregate score of 6.2 or higher. A soft SPF failure (SPF\_SOFTFAIL) will add 3.5 to the score, whereas a hard SPF failure (SPF\_FAIL) will add 4.0 to the score. It is recommended to check and ensure that your company's SPF records are correct and up-to-date, or some messages may be inadvertently marked as spam.

### My organization/customer is sending emails to my instance and they are marked as spam - what can I do?

You may configure Email Filters to create custom filters to allow-list the emails from your organization/customer/partner so that they are not marked as spam. Please note that the following will skip the Email Filter for any email that contains the example domain. For a more granular approach, you may write a condition script to parse the headers and check for different parameters.

![configure Email Filters to create allow-list ](/sys_attachment.do?sys_id=895e20f847fb329430fba325126d43f0 " configure Email Filters to create allow-list ")

You may also decide to turn off any filtering of the scored emails within the Email Filters on the instance.

Alternatively, you may analyze the spam score details in the email headers and you may remedy the reasons why the email has been scored as spam. You can see the reasons for the spam score in the X-ServiceNow-Spam-Status header. Here is an example:

X-ServiceNow-Spam-Status:No, score=6.8 tagged\_above=-999 required=6.2  
tests=\[BAYES\_00=-1.9, DKIM\_INVALID=0.1, DKIM\_SIGNED=0.1,  
HEADER\_FROM\_DIFFERENT\_DOMAINS=0.001, HTML\_FONT\_LOW\_CONTRAST=0.001,  
HTML\_MESSAGE=0.001, MISSING\_MIMEOLE=1.899, NORDNS\_LOW\_CONTRAST=1.274,  
RCVD\_IN\_BL\_SPAMCOP\_NET=1.347, RCVD\_IN\_SBL\_CSS=3.335, RDNS\_NONE=0.793\]

These are SpamAssassin rules. Please refer to SpamAssassin documentation on how to remedy individual rules and consult with your email administrators on which actions to take.

### I do not want spam scoring - how can I turn it off?

Spam scoring is automatic for email sent through the ServiceNow email infrastructure. If you do not want spam scoring, turn off any filtering of the scored emails within the Email Filters on the instance.

## Resolution

## Additional Information

[Email filters](https://www.servicenow.com/docs/r/platform-administration/c_EmailFilters.html "Email filters")

[Incoming emails with infected attachments are not marked as SPAM](https://support.servicenow.com/kb_view.do?sysparm_article=KB0788052 "Incoming emails with infected attachments are not marked as SPAM")

[Malicious email attachments fail to get extracted from the email log causing some files that are present in Phish emails to not get copied into security incidents](https://support.servicenow.com/kb_view.do?sysparm_article=KB1377392 "Malicious email attachments fail to get extracted from the email log causing some files that are present in Phish emails to not get copied into security incidents")
