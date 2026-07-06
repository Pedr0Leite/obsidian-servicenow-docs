---
title: "Global search keywords do not return results in a cloned instance and users get ambiguous message"
aliases:
  - KB0815204
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815204
kb_number: KB0815204
last_modified: 2024-04-08
---

## Global search keywords do not return results in a cloned instance and users get ambiguous message

  

### Issue

When searching a keyword in one of the tables, the user gets the error "Your text query contained only common words or ambiguous wildcards, please refine your search and try again". In the cloned instance, there will be more stop words in 'ts\_index\_stop' compared to the source instance.

### Cause

This is because when an instance is cloned, the text index will be generated and the stop words will be added to the 'ts\_index\_stop' table based on the Auto Threshold set for a table in the Text index. Since the text index for the entire data of the cloned instance is generated within a short period, more stop words will be inserted to the table 'ts\_index\_stop'. For this reason, stop words will be different and the users would see different behavior in the cloned instance and the source instance even though the data is the same.
