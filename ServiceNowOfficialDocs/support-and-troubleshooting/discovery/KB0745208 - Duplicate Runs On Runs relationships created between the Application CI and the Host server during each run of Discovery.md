---
title: "Duplicate Runs On :: Runs relationships created between the Application CI and the Host server during each run of Discovery"
aliases:
  - KB0745208
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745208
kb_number: KB0745208
last_modified: 2024-04-07
---

## Issue

# Symptoms

During each run of discovery, we observe that duplicate Runs On :: Runs relationships created between the Application CI and the Host server.

# Release

Any

# Cause

1) The duplicate relationships are being created because these Application CI's are orphaned applications.

2) The primary reason on why these applications are considered as Orphaned applications is due to 'Classifier' field being empty on these Applications

3) The below code snippet which is a part of the application dependency mapping script include is responsible for creating these duplicate relationships:   
  
// Handle orphaned apps   
var orphan\_id = orphan\_apps\[mk.cid\];   
if (!orphan\_id)   
orphan\_id = orphan\_apps\[mk.running\_process\];   
if (orphan\_id) {   
rel\_gr.initialize();   
rel\_gr.type = mk.relation\_type;   
rel\_gr.child = parent\_this.ci\_sys\_id;   
rel\_gr.parent = orphan\_id;   
rel\_gr.insert(); -----------------------> The rel records are created by this code   
cl\_info.app = orphan\_id;   
continue;   
} 

4) If there is no process Classifier defined for the Application CI, It is expected to create duplicate relationships

# Resolution

1) Make sure there is a process classifier for the Application CI.

2) If there is no process classifier defined, please create a process classifier for that application CI.

3) Once a process classifier is created, Make sure the Classifier field on the existing application CI are populated with the right Classifier value.

4) Navigate to the discovery\_classy\_proc table and check that there are not discovery\_classy\_proc records with empty "Table" column.

5) Delete the duplicate relationships that have been created and Run discovery. You should no longer observe the relationships being duplicated
