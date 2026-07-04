---
title: "Customer Penetration Testing Policy"
aliases:
  - KB0538598
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538598
kb_number: KB0538598
last_modified: 2026-04-15
---

## Issue

 

### Table of Contents

[Purpose](#purpose)

[Roles & Responsibilities](#roles-and-responsibilities)

[Prior Approval](#prior-approval)

[Scope of Security Testing Activities](#scope-of-testing)

[Finding Submission](#finding-submission)

[Release](#release)

[Resolution](#resolution)

[Related Links](#related-links)

### Purpose

Customers may request to perform, at their own expense, an application penetration test. This document describes the policy which applies to such security testing activities.

This Customer Penetration Testing Policy applies to all ServiceNow customers who perform security testing activities against their ServiceNow instance(s). Customers must understand and adhere to this policy to prevent potential impact to their instance and responsibly report identified security findings to ServiceNow.

Failure to perform testing within the parameters set forth by this Policy may result in ServiceNow taking action to respond to unauthorized activity. Such response may include, but is not limited to, blocking traffic from source IPs, and notifying law enforcement.

The process that accompanies this policy is available here: [NowSupport Link - Customer Penetration Testing Process Overview](/kb?id=kb_article_view&sysparm_article=KB1119943 "NowSupport Link - Customer Penetration Testing Process Overview")

### Roles & Responsibilities

| 
Roles

 | 

Responsibilities

 |
| --- | --- |
| 

ServiceNow Global Security Support Center

 | 

-   Review and approve Customer Penetration Test (CPT) requests
-   Triage submitted Security Findings (SFs)
-   File problem (PRB) records for confirmed findings

 |
| 

ServiceNow Customers

 | 

-   Request authorization to perform a Customer Penetration Test
-   Perform security testing within the scope of allowed activity
-   Report all manually validated security findings

 |

### Prior Approval

#### Scheduling

By default, each individual ServiceNow customer account is provisioned one penetration test per calendar year. Further penetration tests may incur additional cost.

To schedule a penetration test, customers must submit a request to schedule a penetration test.

_Note, penetration tests must be scheduled with a lead time of least seven (7) days from the current date. Once submitted, ServiceNow may adjust the lead time to be sooner, at the customer's request._

#### Authorization

Authorization to perform a Customer Penetration Test must be obtained prior to commencing any security testing activity.

In the event that unauthorized security testing activities are detected, ServiceNow may take action to prevent impact to customer instances. Such action may include, blocking traffic from source IPs, and notifying law enforcement.

### Scope of Security Testing Activities

#### In Scope Activities

The following activities are permitted to be performed during the authorized testing window.

-   Application layer testing of the approved target sub-production instance
-   Static and dynamic analysis of the most up-to-date ServiceNow mobile applications from public stores
-   Use of vulnerability scanning tooling to guide manual testing  
      
    

#### Out of Scope Activities

The following activities are out of scope for all testing activity.

-   Network layer testing. Such testing is strictly prohibited
-   Denial of Service (DoS) testing. Such testing is strictly prohibited.
-   Testing of ancillary components, which includes, without limitation:  
    -   Edge Encryption
    -   Password Reset Desktop App
    -   ODBC Driver
    -   ServiceNow Owned Domains/Assets.
-   Testing Integration Spokes / Connectors and third-party integrations.
    -   Please note, customers are able to test their own personal endpoints; however, since the endpoint is not part of ServiceNow, ServiceNow would not review Security Findings not related to the ServiceNow platform.  
          
        

#### Required Testing Environment

To minimize risk and ensure the security of customer data and operations, penetration testing must be conducted on a sub-production instance  (e.g., development, test, or staging environments). Production instances are not eligible for testing and are intentionally excluded from the Customer Penetration Test (CPT) request form. Testing on a production instance can unintentionally disrupt business processes, cause system instability, or lead to the exposure of sensitive data.

Testing on sub-production instances allow customers to:

-   Safely replicate their production environment for testing
-   Validate findings without impacting end users
-   Apply fixes or remediations before promoting them to production

Only sub-production instances will appear in the CPT submission form. If an instance is not visible, verify that it is a sub-production instance and properly registered.  
  

#### Testing Mobile Applications

The most recent versions of the ServiceNow applications are permitted as in scope for this program. These are available here:

[https://play.google.com/store/apps/details?id=com.servicenow.requestor](https://play.google.com/store/apps/details?id=com.servicenow.requestor)

[https://play.google.com/store/apps/details?id=com.servicenow.fulfiller](https://play.google.com/store/apps/details?id=com.servicenow.fulfiller)

[https://play.google.com/store/apps/details?id=com.servicenow.onboarding](https://play.google.com/store/apps/details?id=com.servicenow.onboarding)

[https://play.google.com/store/apps/details?id=com.servicenow.support](https://play.google.com/store/apps/details?id=com.servicenow.support)

[https://apps.apple.com/us/app/now-mobile/id1469616608](https://apps.apple.com/us/app/now-mobile/id1469616608)

[https://apps.apple.com/us/app/servicenow-agent/id1446951408](https://apps.apple.com/us/app/servicenow-agent/id1446951408)

[https://apps.apple.com/us/app/servicenow-onboarding/id1472486882](https://apps.apple.com/us/app/servicenow-onboarding/id1472486882)

[https://apps.apple.com/us/app/now-support/id1504338471](https://apps.apple.com/us/app/now-support/id1504338471)  
  

The following categories of bugs are out of scope, and will not be accepted:

-   Absence of certificate pinning
-   Lack of obfuscation
-   Root/jailbreak detection when system property is not set
-   Runtime hacking exploits; exploits only possible in a rooted environment
-   Third-party mobile app libraries/SDKs findings that do not show significant impact (including InTune & Blackberry MAM libraries)
-   Sensitive data in URLs/request bodies when protected by TLS
-   Path disclosure in the binary
-   Google Maps, Firebase, and/or Crashlytics hard-coded/recoverable keys in binary
-   Any kind of sensitive data stored within the app's internal/private directory
-   Lack of binary protection control or anti-debugging techniques
-   Crashes due to malformed Intents sent to custom URL schemes or exported Activity/Service/BroadcastReceive (exploiting these for sensitive data leakage is commonly in scope)
-   Snapshot/Clipboard leakage  
      
    

These particular issues have been identified by ServiceNow to either

      a) demonstrate a gap in the customer's mobility management policy or

      b) be commonly found to be of little to no risk.  
  

Finally, when evaluating the ServiceNow mobile app(s), please consider the role of appropriate enterprise mobility management security policies. ServiceNow supports several MDM/MAM vendors which reduce the risk of both managed and bring your own device (BYOD) scenarios through customizable policies. Many issues which include a prerequisite for compromising the app or device are best mitigated through mobility management strategies for the benefit of all mobile apps of interest to the customer.  
  

### Finding Submission

#### Reporting

All valid security issues must be reported via Security Finding (SF) record to ServiceNow no later than 30 days after the conclusion of the testing window.

Scanner-generated findings must be manually reproduced by the customer and evaluated for relevant risk. Scanner-generated findings may be closed if there is no evidence that the finding has been manually reproduced.

Single reports containing multiple findings will not be processed.

Please note, Security Findings constitute ServiceNow’s Confidential Information and are subject to the non-disclosure obligations specified in customers’ applicable agreements with ServiceNow.

## Resolution

ServiceNow will assign an engineer to review and validate findings.

If the reported issue is confirmed by ServiceNow a problem (PRB) record will be opened and associated with the Security Finding record. The status of the PRB will be shared with the customer in the security finding record, as necessary.

If ServiceNow has provided a fix, customers are authorized to perform manual testing to validate the fix.

Customers should not use automated tools during the validation of the fix and complete scans are prohibited during retesting. Usage of automated tools for validation is only permitted if the tool has been configured to run a single test for the specific issue that was fixed. Any finding that is detected by an automated tool after a fix has been supplied must be manually validated by the customer.

## Additional Information

-   [KB0780787](https://support.servicenow.com/kb_view.do?sysparm_article=KB0780787) - Simulated Testing Methods
-   [KB0687724](https://support.servicenow.com/kb_view.do?sysparm_article=KB0687724) - Load Testing - Policy and Procedures
-   [KB1119943](/kb?id=kb_article_view&sysparm_article=KB1119943 "NowSupport Link - Customer Penetration Testing Process Overview") - Customer Penetration Testing Process Overview
