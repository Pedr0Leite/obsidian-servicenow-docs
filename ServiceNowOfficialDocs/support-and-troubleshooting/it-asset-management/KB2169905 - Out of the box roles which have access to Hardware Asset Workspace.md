---
title: "Out of the box roles which have access to Hardware Asset Workspace"
aliases:
  - KB2169905
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2169905
kb_number: KB2169905
last_modified: 2025-07-09
---

## Out of the box roles which have access to Hardware Asset Workspace

  

### Summary

Below are the out-of-the-box roles that have access to the **'Hardware Asset Workspace'**:

-   inventory\_admin
-   Procurement\_user
-   inventory\_user
-   model\_manger
-   contract\_manager
-   itil
-   sam\_admin
-   asset
-   catalog\_manager
-   ham\_admin
-   sam\_user
-   catalog\_admin
-   sam

**inventory\_admin :**  
User with this role has access to create, edit, manage, and delete Stockrooms.  
**Procurement\_user :**  
A user with this role has access to create Purchase Orders, view Transfer orders and etc  
**inventory\_user :**  
A user with this role has access to stock information.  
**model\_manger :**  
A user with this role has access to create, modify, and delete base model \[cmdb\_model\] records.  
**contract\_manager :**   
User with this role has access to create, edit, and delete contracts through the Contract Management application.  
**ITIL :**  
User with this role has access to open, update, close incidents, problems, changes, and configuration management items.  
**sam\_admin :**  
This is the fully fledged role to work on any of the functionalities that SAM offers.  
**asset :**  
This role allows you to create, edit, manage, and delete the hardware and consumables.  
**catalog\_manager :**  
Users with this role can view and assign catalog editors to their categories. They can also create, modify, and publish items within their categories.  
**ham\_admin :**  
This role will work or be visible only when you have the HAM Application installed in an environment. To access all HAM features  
**sam\_user :**   
This role will work or be visible only when you have the HAM Application installed in an environment.  
**catalog\_admin :**  
It allows you to create, edit, and manage the Service Catalogues.  
**sam :**  
This role grants a user access to the software asset management feature included with Asset Management. Different roles (sam\_admin, sam\_user and sam\_developer) are required to use the Software Asset Management application.  
  
  
  
There are 8 sections in the hardware Asset workspace excluding the home page.   
1\. Asset Analytics  
2\. Inventory  
3\. Asset estate  
4\. Model Management  
5\. Procurement  
6\. Contract Management  
7\. Success Portal  
8\. Asset operations  
  
![](/sys_attachment.do?sys_id=aca277b693e2ae14def533527cba10aa)

### Access Notes:  
  
**1\. Asset Analytics:**              Role Required: asset  
**2\. Success Portal**  
           Role Required: asset  
**3\. Inventory Management**

Below are the tabs shown under inventory section:  
![](/sys_attachment.do?sys_id=ec688f7293e66e14def533527cba10d8)  
  
Listed below are the tables associated with each section, along with their corresponding access control details (ACLs):  
  
**All Stockrooms**

-   Table: `alm_stockroom`
    -   Read Roles: All users
    -   Write Roles: `inventory_admin`
    -   Create Roles: `inventory_admin`
    -   Delete Roles: `inventory_admin`

### Asset Audits

-   Table: `sn_hamp_asset_audit`
    -   Read Roles: `asset`, `inventory_user`, `sn_eam.enterprise_asset_technician`
    -   Write Roles: `asset`, `inventory_user`
    -   Create Roles: `asset`, `inventory_user`
    -   Delete Roles: `inventory_admin`

**Disposal Orders**

-   Table: `sn_hamp_hardware_disposal`
    -   Read Roles: `asset`
    -   Write Roles: `asset`
    -   Create Roles: `asset`
    -   Delete Roles: `asset`

**Loaner Asset Orders**

-   Table: `sn_hamp_loaner_asset_order`
    -   Read Roles: `itil` (and if loaner order is assigned to the user), `inventory_user`
    -   Write Roles: `itil` (and if loaner order is assigned to the user), `inventory_user`
    -   Create Roles: nobody
    -   Delete Roles: `admin`

### RMA Orders

-   Table: `sn_hamp_rma_request`
    -   Read Roles: `asset`, `inventory_user`
    -   Write Roles: `asset`, `inventory_user`
    -   Create Roles: `asset`, `inventory_user`
    -   Delete Roles: nobody

### RMA Line Items

-   Table: `sn_hamp_rma_request_line`
    -   Read Roles: `asset`, `itil`, `inventory_user`
    -   Write Roles: `asset`, `itil`, `inventory_user`
    -   Create Roles: `asset`, `itil`, `inventory_user`
    -   Delete Roles: nobody

### Transfer Orders

-   Table: `alm_transfer_order`
    -   Read Roles: `procurement_user`, `asset`, `inventory_user`
    -   Write Roles: `inventory_user`
    -   Create Roles: `inventory_user`
    -   Delete Roles: `inventory_user` (if transfer order is in draft state), `inventory_admin`

### Donation Orders

-   Table: `sn_itam_common_donation_order` _(HAM required to perform CRUD operations)_
    -   Read Roles: `asset`
    -   Write Roles: `asset`
    -   Create Roles: `asset`
    -   Delete Roles: nobody

### Repair Orders

-   Table: `sn_itam_common_repair_order`
    -   Read Roles: `inventory_user`
    -   Write Roles: `asset`
    -   Create Roles: `asset`
    -   Delete Roles: `admin`

### Asset Attestation

-   Table: `sn_itam_common_asset_attestation`
    -   Read Roles: `asset`, `inventory_admin`
    -   Write Roles: `asset`, `inventory_admin`
    -   Create Roles: `asset`, `inventory_admin`
    -   Delete Roles: `asset`

  
  
  

 **4. Asset estate:**Below are the tabs shown under Asset estate section:  
![](/sys_attachment.do?sys_id=f3b94f7693e66e14def533527cba10d6)  
  
Listed below are the tables associated with each section, along with their corresponding access control details (ACLs):

###   
All/Other Assets

-   Table: `alm_asset`
    -   Read Roles: All users 
    -   Write Roles: `asset`
    -   Create Roles: `asset`
    -   Delete Roles: `asset`

### Hardware Assets

-   Table: `alm_hardware`
    -   Read Roles: All users 
    -   Write Roles: `asset`
    -   Create Roles: `asset`
    -   Delete Roles: `asset`

### Consumable Assets

-   Table: `alm_consumable`
    -   Read Roles: All users 
    -   Write Roles: `asset`
    -   Create Roles: `asset`
    -   Delete Roles: `asset`

### Software Licenses

-   Table: `alm_license`
    -   Read Roles: All users 
    -   Write Roles: `sam`
    -   Create Roles: `sam`
    -   Delete Roles: `sam`

**Bundle Assets**

-   Table: `alm_bundle`
    -   Read Roles: All users 
    -   Write Roles: `asset`
    -   Create Roles: `asset`
    -   Delete Roles: `asset`

### Pallets (HAM required)

-   Table: `alm_pallet`
    -   Read Roles: All users 
    -   Write Roles: `asset`
    -   Create Roles: `asset`
    -   Delete Roles: `asset`

### Asset Tasks

-   Table: `asset_task`
    -   Read Roles: `procurement_user`, `itil`, `inventory_user`, `asset`, `sn_request_write`
    -   Write Roles: `asset`, `itil`, `inventory_user`
    -   Create Roles: `admin`
    -   Delete Roles: `ham_admin`, `admin`

  
**5\. Model Management:  
  
**Below are the tabs shown under Model Management section:  
  
![](/sys_attachment.do?sys_id=de8ac73a93e66e14def533527cba10a9)  
  
Listed below are the tables associated with each section, along with their corresponding access control details (ACLs):

### All/Contract Models

-   Table: `cmdb_model`
    -   Read Roles: All users 
    -   Write Roles: `model_manager`
    -   Create Roles: `model_manager`
    -   Delete Roles: `model_manager`

### Hardware Models

-   Table: `cmdb_hardware_product_model`
    -   Read Roles: All users 
    -   Write Roles: `model_manager`
    -   Create Roles: `model_manager`
    -   Delete Roles: `model_manager`

### Consumable Models

-   Table: `cmdb_consumable_product_model`
    -   Read Roles: All users 
    -   Write Roles: `model_manager`
    -   Create Roles: `model_manager`
    -   Delete Roles: `model_manager`

### Contract Models

-   Table: `cmdb_contract_product_model`
    -   Read Roles: `contract_manager`, `model_manager`
    -   Write Roles: `model_manager`
    -   Create Roles: `model_manager`
    -   Delete Roles: `model_manager`

### Software Models

-   Table: `cmdb_software_product_model`
    -   Read Roles: All users 
    -   Write Roles: `model_manager`
    -   Create Roles: `model_manager`
    -   Delete Roles: `model_manager`

  
  
**6\. Procurement  
  
**Below are the tabs shown under Procurement section:  
  
![](/sys_attachment.do?sys_id=f52bc3ba93e66e14def533527cba101f)  
  
Listed below are the tables associated with each section, along with their corresponding access control details (ACLs):

### Requests

-   Table: `sc_request`
    -   Read Roles: `sn_request_read`, `catalog`, `itil`, `asset`, `sn_request_write`, `procurement_user`, `sn_request_approver_read` (if approver)
    -   Write Roles: `sn_request_write`, `catalog_admin`, `itil`, `catalog`
    -   Create Roles: `catalog_admin`
    -   Delete Roles: `catalog_admin`

### Items

-   Table: `sc_req_item`
    -   Read Roles: `sn_request_approver_read` (if approver), `sn_request_read`, `atf_test_admin`, `atf_test_designer`, `itil`, `sn_request_write`, `procurement_user`, `asset`
    -   Write Roles: `sn_request_write`, `itil`, `sn_request_comments_write`
    -   Create Roles: `catalog_admin`
    -   Delete Roles: `itil_admin`

### Tasks

-   Table: `sc_task`
    -   Read Roles: `procurement_user`, `sn_request_read`, `sn_request_write`, `itil`, `catalog`, `asset`
    -   Write Roles: `sn_request_write`, `procurement_user`, `itil`, `asset`
    -   Create Roles: `catalog_admin`
    -   Delete Roles: `itil_admin`

### Purchase Orders

-   Table: `proc_po`
    -   Read Roles: `procurement_user`, `inventory_admin`, `contract_manager`, `asset`
    -   Write Roles: `procurement_user`, `asset`
    -   Create Roles: `procurement_user`, `asset`
    -   Delete Roles: `procurement_user`, `asset`

### Receiving Slips

-   Table: `proc_rec_slip`
    -   Read Roles: `asset`, `procurement_user`
    -   Write Roles: `procurement_user`, `asset`
    -   Create Roles: `asset`, `procurement_user`
    -   Delete Roles: `procurement_user`, `asset`

  
  
**7\. Contract Management:  
  
**Below are the tabs shown under Contract Management section:  
![](/sys_attachment.do?sys_id=79cb433e93e66e14def533527cba100a)  
  
Listed below are the tables associated with each section, along with their corresponding access control details (ACLs):

###   
All Contracts / My Contracts

-   Table: `ast_contract`
    -   Read Roles: `procurement_user`, `contract_manager`
    -   Write Roles: `contract_manager`
    -   Create Roles: `contract_manager`
    -   Delete Roles: `contract_manager`

### My Approvals

-   Table: `sysapproval_approver`
    -   Read Roles: `approval_admin`, `catalog`, `itil`
    -   Write Roles: `approval_admin`, `catalog`, `itil`
    -   Create Roles: `approval_admin`, `catalog`, `itil`
    -   Delete Roles: `approval_admin`, `catalog`, `itil`

### Terms and Conditions

-   Table: `clm_terms_and_conditions`
    -   Read Roles: `contract_manager`
    -   Write Roles: `contract_manager`
    -   Create Roles: `contract_manager`
    -   Delete Roles: `contract_manager`

**Note**: All listed roles reflect table-level ACLs. Please be aware that field-level ACLs may also apply independently.

  
  

### Related Links

[https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/hardware-asset-management/reference/installed-with-ham.html](https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/hardware-asset-management/reference/installed-with-ham.html)
