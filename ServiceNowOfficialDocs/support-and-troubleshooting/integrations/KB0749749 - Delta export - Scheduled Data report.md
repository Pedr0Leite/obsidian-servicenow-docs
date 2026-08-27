---
title: "Delta export - Scheduled Data report"
aliases:
  - KB0749749
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749749
kb_number: KB0749749
last_modified: 2024-04-07
---

## Issue

# Question :

What happens when we enable Delta Export in the Scheduled Export ?

# Details :

When a Scheduled Data Export is created with Delta Export as checked, it works as below:

\->**Test1** - Schedule export of Incident table with 6 records 

**Result** : It exports all the 6 records of the incident table 

![](sys_attachment.do?sys_id=adcae0e6db42b450e515c22305961949)

\->**Test2** - Schedule export of the same  Incident table with no changes in the records

**Result** : Still the export set gets executed but the attachment do not contain any records 

![](sys_attachment.do?sys_id=e5cae0e6db42b450e515c2230596194f)

\->**Test3** - Create a new record on the incident table i.e not the incident table has 7 records in total.

Now ,Schedule export of Incident table with 7 records.

**Result** : It exports only 1 record that is recently created.

![](sys_attachment.do?sys_id=edcae0e6db42b450e515c22305961954)

 **Note :**

\->Delta Export is based on the below fields : 

![](sys_attachment.do?sys_id=f5cae0e6db42b450e515c2230596195a)

\-> We can check the Export history - 'Delta Export Status' column  which contains the comment about the data that is being exported :

eg : Export includes only records updated on or after 2019-05-28 04:36:46

![](sys_attachment.do?sys_id=fdcae0e6db42b450e515c2230596195f)

# Versions :

Applicable for all the versions.
