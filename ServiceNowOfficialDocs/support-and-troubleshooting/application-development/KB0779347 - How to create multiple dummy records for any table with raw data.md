---
title: "How to create multiple dummy records for any table with raw data"
aliases:
  - KB0779347
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779347
kb_number: KB0779347
last_modified: 2025-01-03
---

## How to create multiple dummy records for any table with raw data

  

### Summary

This document explains how to create multiple dummy records on any table for testing your code, workflow, or functionalities.

### Instructions

GO to System Definition -> Scripts - Background in your instance and run the following script. Modify the script to your requirements before running.

**var count = 0;**  
**var number = NUMBER\_OF\_RECORDS; //Enter the number of records to be create here**

  
**while (count< number) {**  
**var rec = new GlideRecord('NAME\_OF\_THE\_TABLE'); //Enter the name of the table here**  
**rec.initialize();**  
**rec.insert();**  
**count++;**  
**}**
