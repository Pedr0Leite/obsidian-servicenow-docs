---
title: "Knowledge v3 menus appear after upgrade"
aliases:
  - KB0584107
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0584107
kb_number: KB0584107
last_modified: 2024-04-07
---

## Issue

Disabling Knowledge v3 Menus That Appear After an Upgrade  

  
  

# Overview

* * *

Starting with the Fuji release, the Knowledge application was significantly modified (updated from v2 to v3), and a new set of menu items were added. During the first update from v2 to v3, the new menu items (v3 menus) are disabled by default. We expect that during the upgrade, the admins will update the menu options to disable the v2 items and enable the v3 items. The product documentation topic [Migrating Knowledge Functionality](https://docs.servicenow.com/csh?topicname=r_KMv3KnowFunctMigrate.html&version=latest) discusses scripts provided to assist in this process.

If for some reason, the v3 menus were not enabled during the first upgrade and another upgrade is applied (from Fuji to Geneva or to another patch within the same release), the v3 menus are enabled by the automated changes. This article describes how to disable v3 menu items in such a scenario.

# Process to disable v3 menu items

* * *

Prerequisites:

-   The user executing the script should have the **admin** and **security\_admin** roles.
    
-   Make sure before executing the script you have the elevated privileges for security\_admin enabled.
    
    ![](sys_attachment.do?sys_id=9a6efc22db0ab450e515c22305961910)
    

To disable the v3 menu items:

1.  Navigate to **Scripts** > **Background**.
2.  Copy the script provided below and past it into the editor.
3.  Click **Run script** in scope **global**.

Background script to execute:

```
disableKnowledgeV3Menus();
function disableKnowledgeV3Menus(){
  var DEFAULT_KNOWLEDGE_BASE = "dfc19531bf2021003f07e2c1ac0739ab";
  var KNOWLEDGE3_KNOWLEDGE_MODULE_IDS = [
  "9e390143ff0021009b20ffffffffff38",//Homepage
  "2c26bae8ff0221009b20ffffffffffed",//My Knowledge 
  "d78ed921ff4221009b20ffffffffffdf",//Create new
  "bf69ee02ff003100a822ffffffffff8f",//Unpublished
  "2bb842a1ff4221009b20ffffffffff30",//Published
  "e89a46a1ff4221009b20fffffffffff7",//Retired
  "9047f282ff003100a822ffffffffff85",//Knowledge Bases
  "5b0a06a1ff4221009b20ffffffffff0a",//Feedback
  "ec5ec7a3ff0131009b20ffffffffff77",//Flagged Articles
  "2180b621ff0131009b20ffffffffffc5",//All
  "24c15fa3ff0131009b20ffffffffffc8",//Ratings
  "b8bf8221ff0221009b20ffffffffff24",//Search Log
  "24905a21ff0221009b20ffffffffffed",//Overview
  "e1a859b2ef722100438236caa5c0fb24",//Knowledge Analysis
  "f8e0ab0b0a0a0a6f0007309affffffff",//Submissions
  "f77c90ddc0a8001500890435ffffffff",//Open Submissions
  "2a519a21ff0221009b20ffffffffffe7",//Administration
  "59731713ff2121009b20ffffffffff4b",//User Criteria
  "b4bfe262ff1031009b20ffffffffff19",//Navigation Add-ons
  "5ab45261ff0221009b20ffffffffff23",//Properties
  "99755261ff0221009b20ffffffffff4f" //Messages
  ];
  
  for (var i = 0; i < KNOWLEDGE3_KNOWLEDGE_MODULE_IDS.length; i++){ 
     hideModules(KNOWLEDGE3_KNOWLEDGE_MODULE_IDS[i]); 
  } 
} 

function hideModules(moduleID){
  var module = newGlideRecord('sys_app_module'); 
  if (module.get(moduleID)) {
     module.active = false; module.update(); 
  } 
}
```
