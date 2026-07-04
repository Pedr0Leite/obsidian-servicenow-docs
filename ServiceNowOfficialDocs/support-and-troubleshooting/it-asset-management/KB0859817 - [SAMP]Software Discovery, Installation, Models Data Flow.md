---
title: "[SAMP]Software Discovery, Installation, Models  Data Flow"
aliases:
  - KB0859817
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0859817
kb_number: KB0859817
last_modified: 2024-04-08
---

## \[SAMP\]Software Discovery, Installation, Models Data Flow

  

## Overview

Servicenow Discovery, when used in Conjunction with Software Asset Management (SAM) Professional, enables to automatically Discover, Normalize and Reconcile the Software Products, Models, Entitlements and Allocations to quickly identify the Software License Position.  

## Process

1.  Discovery runs installed package probe and populates "cmdb\_ci\_spkg" related list for CI Data.
2.  Related ListReconcilation eventually calls CMDBSoftwareHelper which checks to see if the SAM plugin is installed. If it is, initialize target table to "cmdb\_sam\_sw\_install". Else reconcile on "cmdb\_ci\_spkg" table.  
    
3.  "Sync Installed Software" Business and "Sync Installed Software" Pattern Pre/Post steps.  
      
    -   **Note**: SCCM Import. If SAM is installed then use Transform map that targets "cmdb\_sam\_sw\_install". Else use Transform Map that targets "cmdb\_ci\_spkg"  
          
        
4.  Create Update Installation Record, As it finds the installation record, Discovery populates the Data to the "cmdb\_sam\_sw\_install" with detailed information of the product.  
      
    -   **ProdID**: Unique ID of the Product Assigned by the Manufacturer
    -   **Installation Location**: Path Under Which the Software is installed.
    -   **Install Date**: Date that Software Installed.
    -   **Revision**: Revision of the Software 
    -   **Instance Key**: Unique ID for the Installation of the Software, automatically generated when the Software installed
    -   **Installed On**: Hardware the Software is installed.
    -   **Uninstall String**: Identifier used to Uninstall the Software
    -   **ISO Serial Number**: ISO Number of the Software   
          
        -   **Note**: Along with all the above, a primary key is built using "Publisher" "Display Name" "Version"  
              
                                        ![](sys_attachment.do?sys_id=261bf8c5db80f8d066e0a345ca96190b)  
              
              
            
5.  Software Installations are the most basic component used to determine how many software rights are in use within an environment.
6.  When the ServiceNow Discovery or any of the integrated tools (Import Sets) executes, the cmdb\_sam\_sw\_install table gets populated. Accordingly, the Software discovery models get created by considering the fields   
       
    -   Discovered Publisher 
    -   Discovered Product 
    -   Discovered Version  
          
        
7.  It may not be a case where the discovered published and the normalized publisher value would be the same. In cases, it is expected to be different as it depends on the Normalization mappings/names/companies and several other influencing factors.
8.  The "Create a Software Normalization" Business Rule on the Software Installations table both inserts a Software installation record and either link that record to an existing Discovery Model, or creates a new Discovery Model and normalizes the Discovery Model using values from the ServiceNow SAM Content Library.
9.  The normalized Software Discovery Models, they are linked to the Software Model by the Discovery Map, using PPN Library content not only automates the process of creating the Software Model it also auto-creates a Discovery Map that identifies the Publisher, Product, Version/Edition, Platform and Language that are associated with the Software Model.
10.  This map is also linked with the appropriate Software Discovery Models so that it can be used during the calculation of license positions  
       
     -   Purchased rights (Entitlements are linked to the Software Model)
     -   Consumed rights (Software Discovery Models) are reconciled correctly.  
           
         
11.  Note that there could be multiple Software Discovery Models associated with one Software Model.  
     
12.  A Software Discovery Model is automatically created for each software installation that has the same discovered publisher, product and version.
13.  Software installations that have the same publisher, product and version are aggregated into the same Software Discovery Model.
14.  Ideally, the software installs becomes the base for creating software discovery models

## Normalization 

Refer: [Software Normalization Deep Dive](/kb_view.do?sysparm_article=KB0859819 "Software Normalization Deep Dive")
