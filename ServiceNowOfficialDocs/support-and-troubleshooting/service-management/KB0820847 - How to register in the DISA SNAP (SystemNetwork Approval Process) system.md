---
title: "How to register in the DISA SNAP (System/Network Approval Process) system "
aliases:
  - KB0820847
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0820847
kb_number: KB0820847
last_modified: 2026-01-08
---

## Text

**Overview**

This article is for Mission Owners who are onboarding their cloud workloads to GCC or NSC and provides instructions for completing the System and Network Approval Process (SNAP) registration, which is Step 2 of the DISA BCAP onboarding process for GCC or NSC. For the complete onboarding process, see [How to complete DISA BCAP onboarding for GCC or NSC](/kb?id=kb_article_view&sysparm_article=KB0819715).  
  
**Note**: The instructions in this article may change without prior notice from the DoD or DISA. If you encounter any issues with these steps, contact the Connection Approval Office at [disa.meade.re.mbx.ucao@mail.mil](https://mailto:disa.meade.re.mbx.ucao@mail.mil/ "https://mailto:disa.meade.re.mbx.ucao@mail.mil/") 

### About the Connection Approval Office

The DISA Connection Approval Office (CAO) maintains the information repository for exceptions to DISN policy on behalf of DoD CIO. The CAO also receives requests for DISN services that may involve a higher level of risk to the DISN than the CAO is authorized to accept. These requests are referred to the Defense Security/Cybersecurity Authorization Working Group (DSAWG). The CAO works with the DoD CIO to review and approve or deny requests for exception to DISN policy. 

**Important:** The SNAP Registration process is manage by the DISA CAO, not ServiceNow. ServiceNow has communicated with the DISA CAO to gather information to populate this article. Contact the DISA CAO with questions about the registration process. 

DISA CAO contact: [disa.meade.re.mbx.ucao@mail.mil](mailto:disa.meade.re.mbx.ucao@mail.mil).

### Account Registration Steps

**Create a SNAP account**

You (the Mission Owner) must have a registered SNAP account before you can submit a Connection Approval Process (CAP) package. 

1.  Go to SNAP: [https://snap.dod.mil/gcap/home.do](https://snap.dod.mil/gcap/home.do)
2.  Download and complete the DD2875 form. The form is customized for SNAP or SGS requirements.
3.  In Section 13 of the DD2875, specify that you need access to Mission Owners (Cloud IT Project).
4.  Specify the type of role you require:
    -   User
    -   Organization
    -   Global Read Only
5.  Upload your completed and signed DD2875 form through SNAP or SGS.
6.  Complete your user profile in SNAP.

**Register your connection in SNAP**

1.  Sign in to SNAP for unclassified connections: [https://snap.dod.mil/gcap/home.do](https://snap.dod.mil/gcap/home.do)
2.  Hover over **CLOUD**, then hover over **Cloud - Information Technology Projects (C-ITPs)**, then select **Register a new C-ITP**.
3.  Complete all required fields in the NIPR Registration form. Sections with a locked icon are reserved for CAO Analyst use.

**Cloud services information**

Complete the following fields in the Cloud Services Information section.

Section 1.1: Select the CSP-CSO being used for this C-ITP

-   Select ServiceNow.

Section 1.2: Is the C-ITP a NSS?

-   You must determine if your instance is a National Security System (NSS).

Section 1.3: Impact Level

-   Select the appropriate impact level:
    -   IL4 for GCC
    -   IL5 for NSC

**Connection information** 

Complete the following fields in the Connection Information section.

Section 2.1: PPSM Registration ID

-   Enter your PPSM Registration ID. If you do not know your PPSM TAG representative, review the Allow List Cheat Sheet (attached) and contact the PPSM office.

Section 2.2: Allow List Registration ID

-   Enter your Allow List Registration ID.

Section 2.3: Select the Cloud Access Point you will use

-   Select DISA Enterprise.

Section 2.4: IP Address

-   Enter your ServiceNow instance IP address.

Section 2.5: Type of Authorization

-   Select your authorization type: RMF or DIACAP.

Section 2.6: Is there an Exception to Policy associated with this C-ITP?

-   Select the appropriate response.

**Attachments**

Upload the following documents in the Attachments section. 

<table style="border-collapse: collapse; width: 100.039%;" border="1"><colgroup><col style="width: 8.44821%;"><col style="width: 40.6952%;"><col style="width: 50.8054%;"></colgroup><tbody><tr><td><strong>Section</strong></td><td><strong>Document</strong></td><td><strong>Notes</strong></td></tr><tr><td>3.1</td><td>Authorization Decision Document (ADD) or ATO</td><td>Your AO must provide an ATO or IATT. You can use the ServiceNow PA for inheritable controls.</td></tr><tr><td>3.2</td><td>Topology</td><td>Template provided in DISN CPG.</td></tr><tr><td>3.3</td><td>Consent to Monitor (CTM) memo</td><td>Your responsibility. Example can be provided on request.</td></tr><tr><td>3.4</td><td>Plan of Action and Milestones (POA&amp;M)</td><td>ServiceNow ARC team can provide.</td></tr><tr><td>3.5</td><td>Scorecard or Security Assessment Report (SAR)</td><td>DISA or ServiceNow can provide.</td></tr><tr><td>3.6</td><td>System Identification Profile (SIP) or System Security Plan (SSP)</td><td>ServiceNow ARC team can provide the SSP.</td></tr><tr><td>3.7</td><td>NSS Exception to Policy (Waiver) Approval</td><td>If applicable.</td></tr><tr><td>3.8</td><td>CSSP Agreement</td><td>Required</td></tr></tbody></table>

**Submit your registration**

After you complete all sections, at the bottom of the screen, select **Submit**.  

**Important:** Submit your CAP package at least 30 days before your desired connection date for new connections, or at least 30 days before your existing ATC or IATC expiration date to ensure service continuity. 

**Note:** The instructions in this article may change without prior notice from the DoD or DISA. If you encounter any issues with these steps, contact the Connection Approval Office at [disa.meade.re.mbx.ucao@mail.mil](https://mailto:disa.meade.re.mbx.ucao@mail.mil/ "https://mailto:disa.meade.re.mbx.ucao@mail.mil/") 

### CAP package documentation requirements

**DoD Component Connections to the DISN**

Your CAP package must include the following documentation: 

<table style="border-style: solid; height: 210px;" cellspacing="0" cellpadding="0"><tbody><tr style="border-style: solid;"><td style="width: 325px; height: 35px;" valign="top"><p><span style="font-size: 12pt;"><strong>DoD RMF&nbsp;</strong></span></p></td><td style="width: 263px; height: 35px;" valign="top"><p><span style="font-size: 12pt;"><strong>DIACAP&nbsp;</strong></span></p></td></tr><tr style="border-style: solid;"><td style="width: 325px; height: 35px;" valign="top"><p><span style="font-size: 12pt;">Authorization Decision Document (ADD) signed by the AO&nbsp;</span></p></td><td style="width: 263px; height: 35px;" valign="top"><p><span style="font-size: 12pt;">ATO or ATO with conditions signed by the DAA&nbsp;</span></p></td></tr><tr style="border-style: solid;"><td style="width: 325px; height: 35px;" valign="top"><p><span style="font-size: 12pt;">Security Assessment Report (SAR)&nbsp;</span></p></td><td style="width: 263px; height: 35px;" valign="top"><p><span style="font-size: 12pt;">DIACAP Scorecard&nbsp;</span></p></td></tr><tr style="border-style: solid;"><td style="width: 325px; height: 35px;" valign="top"><p><span style="font-size: 12pt;">Security Plan (SP)&nbsp;</span></p></td><td style="width: 263px; height: 35px;" valign="top"><p><span style="font-size: 12pt;">System Identification Profile (SIP)&nbsp;</span></p></td></tr><tr style="border-style: solid;"><td style="width: 325px; height: 35px;" valign="top"><p><span style="font-size: 12pt;">POA&amp;M&nbsp;</span></p></td><td style="width: 263px; height: 35px;" valign="top"><p><span style="font-size: 12pt;">IT Security POA&amp;M&nbsp;</span></p></td></tr></tbody></table>

**Mission Partner Connections to the DISN** 

If you are a Mission Partner, your CAP package must include the following documentation. DoD Sponsors and Mission Partners must keep information in SNAP up to date.

Required documents:

-   ATO or ATO with conditions signed by the AO or DAA
-   As appropriate, RMF Documentation or DIACAP Executive Package (DIACAP Scorecard), in accordance with DoDI 8510.01, DoD 5220.22-M, NISPOM, NIST 800-37, ICD 503 documentation, or equivalent
-   Statement of Residual Risk
-   Detailed Topology Diagram
-   DoD Sponsor Validation Letter (Appendix B) or Revalidation Letter (Appendix C)
-   DoD CIO Memo validating the mission requirement for a new Mission Partner connection to DISN
-   Consent to Monitor memo (the DoD Sponsor is responsible for signing the CTM)
-   AO or DAA Appointment Letter

**Sponsor responsibilities**

The DoD Sponsor must validate the Mission Partner's need for access to the DISN. The DoD Sponsor and Mission Partner must understand and agree to their responsibilities as stated in the DoD CIO Sponsor Memorandum: _Responsibilities of DoD Components Sponsoring Mission Partner Connections to DISN-Provided Transport Infrastructure_. This agreement may be documented in an MOA, MOU, or contract.

**Downloadable PDFs**

[DISA CAP KB0819715](sys_attachment.do?sys_id=dc24c1d647fdfe94b7832920326d43fd "DISA CAP KB0819715")

[SNAP Registration KB0820847](sys_attachment.do?sys_id=282405d647fdfe94b7832920326d4377 "SNAP Registration KB0820847")

[Whitelist Cheat Sheet](sys_attachment.do?sys_id=282405d647fdfe94b7832920326d437f "Whitelist Cheat Sheet")
