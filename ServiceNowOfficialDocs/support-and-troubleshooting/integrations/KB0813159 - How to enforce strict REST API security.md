---
title: "How to enforce strict REST API security"
aliases:
  - KB0813159
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813159
kb_number: KB0813159
last_modified: 2025-03-28
---

## How to enforce strict REST API security

  

### Issue

Whilst it is possible to lock down the REST API user ACLs to selectively access a table, but not others, there are out of the box ACLs that were intended for this purpose that are not well know because they are not enabled by default. See info below.

### Release

All

### Cause

This is useful to know in a context where security should be enforced so only what is permitted should be granted.

### Resolution

This is an extract from the relevant docs  
  
REST API ACLs  
[https://docs.servicenow.com/csh?topicname=c\_RESTAPI.html&version=latest](https://docs.servicenow.com/csh?topicname=c_RESTAPI.html&version=latest)

## REST API security

By default, ServiceNow REST APIs use basic authentication or OAuth to authorize user access to REST APIs/endpoints. You can also configure your instance to use [multi-factor authentication](https://docs.servicenow.com/csh?topicname=c_RESTAPI.html&version=latest#c_RESTAPI__multi-factor-auth-inbound-REST) to access REST APIs. There is no support for inbound mutual authentication.

The user ID that you specify in a REST endpoint call is subject to access control in the same way as an interactive user. Each request requires the proper authentication information, such as user name and password. Ensure that each endpoint request includes an Authorization header with sufficient credentials to access the endpoint.

ServiceNow REST APIs also support cookies that enable binding to the existing session.

## REST API roles

In addition to user authentication, each REST endpoint can have different requirements for the roles required to access the endpoint. Some require the admin role and others require API specific roles. Role requirements are specified in the access control list (ACL) associated with the REST API/endpoint. For specifics on the valid roles for each REST API/endpoint, refer to the [REST API reference](https://docs.servicenow.com/csh?topicname=api-rest.html&version=latest) or locate the associated ACL for the API/endpoint within an instance through Security System > Access Control (ACL).

## REST API ACLs

REST API ACLs define criteria, such as the roles needed and conditions that a user must meet to access a ServiceNow REST API or endpoint. A single ACL may be defined for an entire REST API, such as the Table API and Attachment API ACLs, or for an individual endpoint, such as the Table API and Attachment API ACLs that only applies to MetricBase PUT methods.

The following ServiceNow REST API ACLs are available in the base system but are deactivated by default. All other ServiceNow REST API ACLs are active by default.

-   Table API
-   Aggregate API
-   Import Set API
-   Attachment API

## IMPORTANT NOTE

Please review carefully [KB0794090 - When trying to select a walk-up location as the Walk-up user, the location box infinitely loads. Why?](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794090 "KB0794090") as there is a mandatory trade off between the two.

While activating this ACL does enhance security by requiring all Table API users to have the `snc_platform_rest_api_access` role, customers who rely on the Walk-up Experience must decide whether to prioritize security hardening or maintain Walk-up functionality.

If the customer intends to use Walk-up Experience, they should not activate this ACL to prevent issues.
