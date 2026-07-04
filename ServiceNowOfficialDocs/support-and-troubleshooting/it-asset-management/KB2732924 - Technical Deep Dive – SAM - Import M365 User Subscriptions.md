---
title: "Technical Deep Dive – SAM - Import M365 User Subscriptions"
aliases:
  - KB2732924
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2732924
kb_number: KB2732924
last_modified: 2026-05-10
---

## Technical Deep Dive – SAM - Import M365 User Subscriptions

  

### Summary

This is the ultimate fact sheet for the SAM - Import M365 User Subscriptions job. It breaks down exactly what the code does, the tables it touches, and the hidden rules that decide if a license shows up in ServiceNow or not.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **THE GOAL: WHY DOES THIS JOB RUN?**

The mission is to synchronize your Microsoft 365 license reality with your ServiceNow records.

➔ The Benefit It tells you exactly who has a license so you can find waste and save money.

➔ The Primary Entry Point Scheduled Script Execution: SAM - Import M365 User Subscriptions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **STAGE 1: THE STARTING GATE (REQUIREMENTS)**

Before the job even talks to Microsoft, it checks for two Green Lights.

➔ Green Light 1: The Plugin The system checks if the SaaS License Management plugin \[sn\_sam\_saas\_int\] is active.

➔ Green Light 2: The Success Handshake The code runs the function getProfileGr. It looks at the Software Subscription Profile table \[samp\_sw\_subscription\_profile\]. Condition 1: The profile\_type must be microsoft\_office\_365. Condition 2: The custom\_properties field must contain "validate\_connection":"success".

↳ Fact If a technician didn't click Validate Connection successfully on the profile, the job skips the account entirely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **STAGE 2: THE SAFETY RESET (THE SOFT WIPE)**

To ensure your data is fresh, the system performs a temporary reset.

➔ The Action The script calls deactivateSubscription.

➔ The Table Software Subscription \[samp\_sw\_subscription\].

➔ The Rule Every record currently linked to that profile is set to active = false.

↳ Fact This ensures that if a user was deleted in Microsoft, their record stays inactive in ServiceNow unless the API finds them again in the next step.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **STAGE 3: THE BATCH OF 20 RULE (THE DATA PULL)**

The system asks Microsoft for your users, but it does so in small, safe chunks to avoid crashes.

➔ The Function insertSubscriptions

➔ The 20 Rule The code has a hardcoded limit: var BATCH\_SIZE = 20.

➔ The Process 1 ➔ ServiceNow gets a list of all User emails (UPNs) from Microsoft. 2 ➔ It cuts that list into groups of 20 users. 3 ➔ It asks Microsoft: "What licenses (SKUs) do these 20 people have?" 4 ➔ It repeats this until every user is processed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **STAGE 4: THE GATEKEEPERS (FILTERS AND MATCHING)**

Every license found must pass three Logic Gates before it is saved.

➔ Gate 1: The Dynamics Filter The code checks the dynamicsSubsIdentifiersList. If the license is for Dynamics 365, it is skipped (Dynamics has its own logic path).

➔ Gate 2: The Exclusion Rules The code calls checkifExclusionRulesApplicable. It checks your Software Asset Management exclusion settings. If the User Email or License Name is on your Do Not Import list, the data is ignored.

➔ Gate 3: The User Match The code calls getSysUser to link the license to a real person. It searches the User table \[sys\_user\] for a match using the Microsoft email. If Match ➔ The license is linked to that specific person. If No Match ➔ The user field is set to NULL, but the license info is still saved.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **STAGE 5: THE FINANCIAL SYNC (PURCHASED RIGHTS)**

After the users are imported, the system counts your total Owned licenses.

➔ The Table Purchased Subscription Details \[samp\_purchased\_subscription\_details\].

➔ The Data Points prepaidUnits.enabled ➔ This becomes your Purchased Rights. consumedUnits ➔ This becomes your Assigned Rights.

➔ The Available Calculation The system calculates: Purchased minus Assigned equals Available. If you have used more than you bought, Available is set to 0.

➔ The Software Model Link The script uses getSoftwareModel to link these counts to your Product Models. If it can't find a perfect match for the Microsoft SKU, the Software Model field will be empty.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **STAGE 6: THE FINAL CLEANUP (FINALIZATION)**

Once the list is finished, ServiceNow removes the people who are no longer there.

➔ The Function deleteInactiveSubscription

➔ The Logic The script looks for any record that stayed active = false from Stage 2. These records are permanently deleted because they no longer exist in Microsoft.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **THE TROUBLESHOOTING SCOPE:** 

Here are five scenarios that explain why things might go wrong and how to fix them.

Story 1: 

Customer says the job ran but nothing changed.

➔ You check the Software Subscription Profile and see the custom\_properties field is blank. Because the code only looks for profiles that say success, it treated the account as if it didn't exist. Solution ➔ The customer must click Validate Connection and get a success message.

Story 2: A user has a license in Microsoft, but in ServiceNow, the User field is empty.   
  
➔ This happens because the UPN (email) in Microsoft is john.doe@company.com, but in the ServiceNow User \[sys\_user\] table, his email is j.doe@company.com. The code couldn't find a perfect match, so it created the license but couldn't "handshake" with the user record. Solution ➔ Ensure emails match perfectly between both systems.

Story 3: 

The Forbidden List A specific license, like Microsoft Visio, is missing for everyone.

➔ You look at the Exclusion Rules and find that someone added Visio to the list. The code saw the rule and followed it strictly—it threw all the Visio data in the trash during the import. Solution ➔ Remove the license name from the Exclusion Rules.

Story 4: The Ghost in the Machine 

➔ The job crashed halfway through because something went wrong. Instead of everything showing as Inactive, all licenses stayed Active. This is because the catch block triggered the markSubscriptionActive function. The code decided it was better to show old data than to tell the customer they have zero licenses. Solution ➔ Check the SAM Job Log \[samp\_job\_log\] for a timeout error and run the job again.

Story 5: The Model without a Name

The Purchased Subscription Details table shows 100 licenses, but the Software Model field is blank. The code took the SKU name from Microsoft (like O365\_BUSINESS\_PREMIUM) and looked for it in ServiceNow. It couldn't find a matching Software Model with that exact identifier, so it recorded the numbers but couldn't give it a name. Solution ➔ Create a Software Model and link it to the correct Microsoft SKU identifier.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### **TECHNICAL FACT SHEET (MAPPINGS)**

➜ Target Table Software Subscription \[samp\_sw\_subscription\]

➜ Counts Table Purchased Subscription Details \[samp\_purchased\_subscription\_details\]

➜ Mapping A Microsoft skuPartNumber ➔ subscription\_identifier

➜ Mapping B Microsoft userPrincipalName ➔ user\_principal\_name

➜ Mapping C Microsoft skuId ➔ Stored as JSON in custom\_properties

➜ Logs Errors are written to the SAM Job Log \[samp\_job\_log\] using the SampLogger class.
