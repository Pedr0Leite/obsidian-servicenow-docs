---
title: "HR Case Creation from Record Producer FAQ"
aliases:
  - KB0754916
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754916
kb_number: KB0754916
last_modified: 2026-03-16
---

## Issue

If you have an existing HR Service that you want to make available for employee self-service, you can configure a Record Producer (RP) so that the service appears as an HR Catalog Item by following the steps described on the documentation page [Configure a record producer for an HR service](https://docs.servicenow.com/csh?topicname=configure-hr-record-producer.html&version=latest "Configure a record producer for an HR service").

The key step of submitting an HR Case from a Record Producer is to add the following line in the RP's Script:

new hr\_ActivityUtils().createCaseFromProducer(current, producer, cat\_item.sys\_id);   
  

This article explains its behind-the-scenes logic and what can go wrong.

1. The function "_createCaseFromProducer_" in the **"hr\_ActivityUtils"** Script Include calls the function **"**_createCaseFromProducer_**"** in **"hr\_ServicesUtil"** Script Include,

2\. This calls the "_createCaseFromProducerByService_**"** function. A record Producer must be related to an HR Service for this functionality to work, or the generated case will be created without an HR Service and other mandatory fields. 

3\. This calls the internal function "_\_getProducerQuestions_" which retrieves all the variables and their values from the record producer instance. Note that Script Include "**hr\_CaseUtils**" and "**HRSecurityUtils**" are also being called for this.

4\. Then, the **"**_updateCase_**"** function calls **"**_populateCase_**"** in the "hr\_CaseUtils" Script Include. This calls three internal functions:

5\. Function "_\_setServiceFields_()" sets the following fields with values from the HR Service:

\- hr\_service

\- topic\_detail

\- topic\_category

\- template

6\. Function "_\_setGeneralFields_()" sets the following fields:

\- _subject\_person_ - It creates both the sys\_user and sn\_hr\_core\_profile (if there isn't one already) for the Subject Person. Note that Script Include "**hr\_Profile**" is being called, which internally calls Script Include "**hr\_SysUser**". 

\- _opened\_for_ - If a variable has been mapped to opened\_for, it uses that value; otherwise, it uses the user submitting the case.

\- subject\_person\_job. If a variable has been mapped to subject\_person\_job, it uses that value; otherwise, it creates a new record in sn\_hr\_core\_job and uses that. Note that the Script Include "**hr\_Utils**" is being called.

7\. Function "_\_setCommonFields_()" sets all the other fields, including:

\- _short\_description_ - (in the format "_{HR Service name} case for {Subject Person}_".

\- _description_ - This is populated by the function "_\_getDescriptionFromAnswers_" in the format "_The following fields have been provided:_" followed by the list of provided questions/answers. 

**NOTEs**

As seen above, multiple Script Include records are being called when generating a new HR Case from a Record Producer:

_hr\_ActivityUtils (sys\_id=940b94b10b71320074646f3ef6673a1e)_  
_hr\_ServicesUtil (sys\_id=e0d7bdf79f031200d9011977677fcf15)_  
_hr\_CaseUtils (sys\_id=24c782869f202200d9011977677fcf89)_  
_hr\_Profile (sys\_id=ba5370019f22120047a2d126c42e7000)_  
_hr\_SysUser (sys\_id=365370019f22120047a2d126c42e7000)_  
_hrUtils (sys\_id=f65370019f22120047a2d126c42e7000)_  
_HRSecurityUtils (sys\_id=9c71da339373320092051d1e867ffb42)_

Most of these SIs have their "Caller Access" set to "Caller Restriction". **If any of them have been customized, their related Restricted Caller Access records might have been invalidated**, causing unexpected behaviours. 

Try keeping the above Script Includes up-to-date and, if customizations are needed, make sure to review them and apply them on top of the most recent OOB version after each upgrade.

\*\*\*\*\*

## **Possible Issues**

### 1\. Empty mandatory fields on the generated HR Case

\- If an answer is EMPTY in the question\_answer table, the mapped field on the generated HR Case will also be empty. Make sure that the Values in the question\_answer table are populated as expected. If they aren't, and you are submitting the RP from the Employee Center or Service Portal, ensure that the widgets being used are OOB and on their most recent version (in particular, widget "SC Catalog Item" \[widget-sc-cat-item-v2\]). 

### 2\. Empty HR Service on the generated HR Case

\- Make sure to map the RP to an HR Service as mentioned in the above documentation.

### 3\. The description is showing a sys\_id instead of the original value

\- This might be due to the use of the prefix "ref\_" in the name of a variable of type Reference. Refrain from using variable names prepended with "ref\_"

### 4\. How to remove the "Original Value" from the generated Description field

\- More details on how this function works can be found in [KB0955253 ("Original Value" are getting added in description of HR Case)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955253).

### 5\. Some variables referencing HR Profile \[sn\_hr\_core\_profile\] or User \[sys\_user\] are not listed in the generated Description field

\- If any matching Variables are found in the HR Profile or User tables with no differing information, they are ignored.  
For example, if the RP has a Variable called State and its value is "CA", and the State field on the related HR Profile is also "CA", since their values are the same, the "State" variable will not be added to the Description as it is considered a redundancy (and its value can be found in the HR Profile).

## Resolution

See above.
