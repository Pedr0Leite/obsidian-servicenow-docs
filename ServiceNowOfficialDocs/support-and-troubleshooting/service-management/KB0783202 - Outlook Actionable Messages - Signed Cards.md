---
title: "Outlook Actionable Messages - Signed Cards"
aliases:
  - KB0783202
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783202
kb_number: KB0783202
last_modified: 2024-04-07
---

## Issue

For customers whose environments do not support Sender Policy Framework (SPF)/DomainKeys Identified Mail (DKIM) email verification, you must implement signed cards for sender verification. Refer [https://docs.microsoft.com/en-us/outlook/actionable-messages/security-requirements#signed-card-payloads](https://docs.microsoft.com/en-us/outlook/actionable-messages/security-requirements#signed-card-payloads) for more details.

**Signed Cards Implementation**

1\. For implementing signed cards, you should register as a new service in the [Microsoft website](https://aka.ms/publishoam "Microsoft website") setting the scope as Organization. Follow the onboarding instructions provided at [https://docs.microsoft.com/en-us/outlook/actionable-messages/security-requirements#signed-card-payloads](https://docs.microsoft.com/en-us/outlook/actionable-messages/security-requirements#signed-card-payloads). Specify the provider ID value in the sn\_ms\_oam.outlookactionable.originator property.

2\. Follow the instructions at [https://docs.servicenow.com/csh?topicname=JWT-Bearer-token-support.html&version=latest#configure-JWT-signing-key](https://docs.servicenow.com/csh?topicname=JWT-Bearer-token-support.html&version=latest#configure-JWT-signing-key) to create a new JWT Provider using your X.509 certificate.

3\. Specify the JWT Provider ID value created above in sn\_ms\_oam.jwt\_provider\_id property

4\. Use the following email scripts in the Message HTML field of your approval or survey emails.

**Survey:**

${mail\_script:include\_signed\_survey\_actionable}

**Approval:**

${mail\_script:include\_signed\_approval\_actionable}

**Note:** Signed Cards are only supported for notifications of Content type HTML only.
