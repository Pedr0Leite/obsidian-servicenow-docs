---
title: "SAM Pro: What information does the \"Microsoft Dynamics 365 and Power Apps\" direct integration pull from O365?"
aliases:
  - KB1970551
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1970551
kb_number: KB1970551
last_modified: 2026-05-21
---

## SAM Pro: What information does the "Microsoft Dynamics 365 and Power Apps" direct integration pull from O365?

  

### Issue

QUESTION:

We are currently evaluating the "Microsoft Dynamics 365 and Power Apps" direct integration.  
  
The documentation indicates the integration pulls information for the following applications:  
\- Dynamics 365 for Sales (Professional, Premium, Enterprise)  
\- Dynamics 365 for Customer Service (Professional, Enterprise, Enterprise for Government, Professional Attach to Qualifying Dynamics, Sales and Customer Service Enterprise)  
\- Dynamics 365 for Team Members  
\- Microsoft Relationship Sales (MRS)  
  
However, there are no details about \*what\* information the integration pulls from O365. We'd like to know what the data look like when the integration populates the ServiceNow tables upon a successful connection.

### Release

\--

### Cause

\-

### Resolution

Microsoft Dynamics 365 and Power Apps:

  
Summary of how the integration profile works and what happens during the execution process:  
  
Creating an Integration Profile  
\* When a new integration profile is created, scheduled jobs are defined that will execute at specified intervals.  
\* These jobs are responsible for retrieving relevant data from external sources such as the Microsoft portal.  
\* During execution, the integration fetches key details related to subscriptions, users, and products.

  
The primary details collected from the O365 are as below:  
\* Subscription Identifier – Unique ID for each subscription.  
\* Publisher Information – Identifies the software provider (e.g., Microsoft).  
\* User Principal Name  
\* Product Details – Defines the software or service associated with the subscription.  
\* User Details – Includes the User Principal Name (UPN) and possibly the email.  
\* Additional Metadata – Other relevant details from the source system.  
  
Data Association and Correlation  
\* Once the data is collected, it is mapped to the software models.  
\* If a subscription identifier matches an existing record, the system links it to the corresponding software model.  
\* This ensures that the retrieved data aligns correctly with existing records.  
  
Reconciliation Process  
\* After associating the collected data with the software models, the reconciliation process runs.  
\* This step compares the collected subscription and user data against entitlement and licensing records.  
\* The system determines if:  
\* The subscription is compliant (licensed correctly).  
\* The subscription is non-compliant (missing licenses or entitlement issues).  
  
Licensing and Compliance Checks  
\* Based on the reconciled data, the system applies licensing rules.  
\* Entitlement settings dictate whether a product or user is properly licensed.  
\* If discrepancies are found, the system flags subscriptions as non-compliant for further action.
