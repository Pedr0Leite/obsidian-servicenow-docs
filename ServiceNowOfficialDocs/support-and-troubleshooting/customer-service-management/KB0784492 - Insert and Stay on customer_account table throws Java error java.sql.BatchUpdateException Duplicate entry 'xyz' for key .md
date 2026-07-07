---
title: "Insert and Stay on customer_account table  throws Java error: java.sql.BatchUpdateException: Duplicate entry 'xyz' for key 'account_path"
aliases:
  - KB0784492
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0784492
kb_number: KB0784492
last_modified: 2024-04-16
---

## Issue

When the 'Insert and Stay' is selected on customer\_account table, a Java error similar to the following is automatically generated.

java.sql.BatchUpdateException: Duplicate entry '!(W5!!' for key 'account\_path'.

## Resolution

If a new customer account needs to be created then the 'New' button on customer\_account table should be used. In this case 'New' would not be the same as 'Insert and Stay' and will create a new record with a new account\_path. Also if an exiting account needs to be updated then the 'Update' functionality can be used instead of 'Insert and Stay'.

## Additional Information

## See the following link 

[Create a customer or partner account](https://docs.servicenow.com/csh?topicname=c_CustomerServiceManagement.html&version=latest "Create a customer or partner account")
