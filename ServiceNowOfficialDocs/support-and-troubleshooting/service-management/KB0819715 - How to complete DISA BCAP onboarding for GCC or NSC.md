---
title: "How to complete DISA BCAP onboarding for GCC or NSC"
aliases:
  - KB0819715
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0819715
kb_number: KB0819715
last_modified: 2026-02-10
---

## Text

## Overview

The Defense Information Systems Agency (DISA) has approved ServiceNow as an authorized Cloud Service Provider (CSP) for its Government Community Cloud (GCC) IL4 and National Security Cloud (NSC) IL5 environments.  This approval allows Department of Defense (DoD) customers to transport workloads through the DISA Boundary Cloud Access Point (BCAP) service.  

This article is for Mission Owners onboarding cloud workloads to the Government Community Cloud (GCC) or National Security Cloud (NSC).

Per DoD mandate, all mission owners who want to onboard to a CSP authorized at Impact Level 4 (IL4) or higher must connect through a BCAP and submit a Secure Cloud Computing Architecture (SCCA) onboarding request form.

## Before you begin

Before starting the onboarding process, verify that you have access to:

-   Your Information System Security Officer (ISSO), Facility Security Officer (FSO), Authorizing Official (AO), or appropriate authority figure
-   Your agency's standard operating procedures for cloud onboarding
-   SIPRNet access for PPSM submissions
-   Your DoD component sponsor's [PPSM TAG representative](https://dl.dod.cyber.mil/wp-content/uploads/connect/CPG/ConnProcGuide.html#_Service_Representative_Officials) contact information

## Onboarding steps

Complete the following steps to onboard to GCC, NSC, or the DISA BCAP.

#### **Step 1: Obtain an Interim Authority to Connect (IATT).**

You must obtain prior approval or authorization to use ServiceNow GCC (IL4), NSC (IL5), the DISA BCAP, or all three. Consult with your ISSO, FSO, AO, or appropriate authority figure to obtain approval.

#### **Step 2: Complete and submit the System and Network Approval Process (SNAP) form.**

For instructions, see [SNAP Registration Instruction](/kb_view.do?sysparm_article=KB0820847).

#### **Step 3: Obtain a Cloud Permission to Connect (CPTC).**

Follow the DoD Cloud Computing Security Requirements Guide (CCSRG) and your agency's standard operating procedures.

#### **Step 4: Complete and submit the DISA SCCA form.**

This form confirms your Cloud Service Support Provider (CSSP) services. Subscribe to DISA CSSP services or report prearranged CSSP services to the DISA SCCA team within the form.

#### **Step 5: Submit your PPSM request.**

Enter your request into the DISA Ports, Protocols, and Service Management (PPSM) system on SIPRNet. The DISA SCCA team uses this information. For details, see PPSM template and registry requirements in this article.

ServiceNow provides a PPSM workbook template prepopulated with example IP addresses, ports, protocols, and services. To request the DISA Ports, Protocols, and Service Management template, contact ServiceNow.

You must complete the required sections specific to your environment and ServiceNow instances.

#### **Step 6: Configure your allow list** 

Use the DISA Ports, Protocols & Service Management template to add sources, destinations, ports, protocols, or services to meet your unique requirements. Add the following to your allow list:

-   Your ServiceNow instance
-   Now Support GCC (HIWAVE) for GCC customers
-   Now Support NSC (HIFIVE) for NSC customers
-   Any integrations or third-party services not using standard ports, protocols, and services already included in ServiceNow's approved list

Use this information to configure allow lists for inbound and outbound connections within your firewalls and DMZs as needed.

#### Step 7: Register in the PPSM registry

You must register your cloud-based systems and applications in the DoD PPSM Registry on SIPRNet. This requirement applies to:

-   Systems and applications in an Infrastructure as a Service (IaaS) or Platform as a Service (PaaS) Cloud Service Offering (CSO)
-   Software as a Service (SaaS) offerings

Registration must include all ports and services along with their related UDP and TCP IP ports that traverse the DISN.

Consult with your DoD Component's PPSM TAG representative to determine whether you must register your required ports, protocols, and services in the NIPRNet DMZ allow list.

[PPSM TAG representative](/kb#_Service_Representative_Officials)

[DISN Connection Guide](https://dl.dod.cyber.mil/wp-content/uploads/connect/CPG/ConnProcGuide.html)

### After onboarding: Access compliance authorization packages  

After you complete onboarding, you can access Compliance Authorization Packages from Now Support.

To access GCC compliance documents:

1.  Sign in to Now Support GCC (HIWAVE).
2.  Review the [GCC Compliance Authorization article.](https://hiwave.servicenowservices.com/kb?id=kb_article_view&sysparm_article=KB20003165) 

To access NSC compliance documents:

1.  Sign in to Now Support NSC (HIFIVE).
2.  Review the [NSC Compliance Authorization article.](https://hifive.servicenowcloud.mil/kb?id=kb_article_view&sysparm_article=KB80002686)

Available documents include:

-   System Security Plan (SSP)
-   Control Implementation Summary (CIS) Workbook and Customer Responsibility Matrix (CRM)
-   DoD Provisional Authorization (PA) Memo
-   FedRAMP Provisional Authority to Operate (P-ATO) Letter (GCC only)
-   Monthly Continuous Monitoring (ConMon) Reports
-   Plan of Action and Milestones (POA&M)
-   Security Assessment Plan (SAP)
-   Security Assessment Report (SAR)
-   PPSM Spreadsheet

**Note:** If you are currently in FedRAMP High, you can initiate migration to GCC (IL4) or NSC (IL5) in parallel during onboarding. 

### **How do public internet users access GCC or NSC instances through NIPRNet (protected by IAPs)?** 

User traffic must originate within NIPRNet boundaries. This is a prerequisite for accessing ServiceNow GCC (IL4) or NSC (IL5) instances through the DISA BCAP.

The DoD Network Information Center (NIC) controls the NIPRNet. Your responsibilities include:

-   Provisioning access to the NIPRNet on behalf of your users
-   Adding IP addresses to the NIPRNet allow list for your users

Internet Access Points (IAPs) are edge gateways into the NIPRNET. The DoD NIC controls these gateways. To allow your public internet users access through IAP gateways, **your agency must coordinate with the DoD NIC for approval**. This requirement applies to both GCC (IL4) and NSC (IL5) environments.  

According to the Defense Information Systems Network (DISN) Connection Guide:

-   If your enclave, network, or application requires information to traverse both the NIPRNet and the internet, you may need to register this with the NIPRNet Demilitarized Zone (DMZ) allow list. 
-   This registration ensures the DISN IAPs are configured to permit the information flow between the NIPRNet and the internet. 
-   Consult your DoD component sponsor's [PPSM TAG representative](https://dl.dod.cyber.mil/wp-content/uploads/connect/CPG/ConnProcGuide.html#_Service_Representative_Officials) to determine whether you must register your required ports, protocols, and services in the NIPRNet DMZ allow list. 

For more information, see the [DISN Connection Guide](https://dl.dod.cyber.mil/wp-content/uploads/connect/CPG/ConnProcGuide.html). 

**Important**: ServiceNow cannot assist with DoD allow list approvals for either environment. 

## Contact information

#### **DoD NIC (for NIPRNet and IAP access)**

-   **NIPRNet email:** [disa.columbus.ns.mbx.hostmaster-dod-nic@mail.mil](mailto:disa.columbus.ns.mbx.hostmaster-dod-nic@mail.mil)
-   **NIPRNet email (distribution list):** [disa.columbus.ns.list.hostmaster-dod-nic-dl@mail.mil](mailto:disa.columbus.ns.list.hostmaster-dod-nic-dl@mail.mil)
-   **SIPRNet email:** [disa.columbus.ns.mbx.hostmaster-dod-nic@mail.smil.mil](mailto:disa.columbus.ns.mbx.hostmaster-dod-nic@mail.smil.mil)
-   **Phone:** CML 1-844-DISA-HLP (347-2457) Select the option for Infrastructure Support. 
-   **Website:** [https://www.nic.mil](https://www.nic.mil) (NIPRNet, CAC required)

The 24/7 Global Service Desk (GSD) initiates a ticket for DoD NIC Registration   
Support assistance. DoD NIC Registration Support available 24/7

#### **PPSM Secretariat (for PPSM submissions)**

-   Phone: 301-225-2904
-   DSN: 312-375-2904
-   Unclassified email: [dod.ppsm@mail.mil](mailto:dod.ppsm@mail.mil)
-   Classified email: [disa.meade.ns.mbx.ppsm@mail.smil.mil](mailto:disa.meade.ns.mbx.ppsm@mail.smil.mil)

#### **NIPRNet DMZ allow list resources**

-   Allow list portal: [https://niprdmzwhitelist.csd.disa.smil.mil/home.aspx](https://niprdmzwhitelist.csd.disa.smil.mil/home.aspx)
-   Current allow list: [https://niprdmzwhitelist.csd.disa.smil.mil/whitelist.aspx](https://niprdmzwhitelist.csd.disa.smil.mil/whitelist.aspx)
-   DoD Component DMZ allow list points of contact: [https://niprdmzwhitelist.csd.disa.smil.mil/POCList.aspx](https://niprdmzwhitelist.csd.disa.smil.mil/POCList.aspx) 

![](/sys_attachment.do?sys_id=8dfa8520474f361c77b5ab29736d4300)
