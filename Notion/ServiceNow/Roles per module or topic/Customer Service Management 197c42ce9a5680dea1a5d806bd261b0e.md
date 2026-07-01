---
aliases:
  - "Customer Service Management"
tags:
  - roles
  - csm
  - customer-service-management
  - acl
---

# Customer Service Management

# Customer Service Management Roles and FAQs

### Description

The
 CSM product serves both B2B (business-to-business) and B2C 
(business-to-consumer) business purposes. There can be many different 
possible relationships and directions of engagement required by our 
users, including: roles, hierarchies, levels, and distinctions between 
similar roles.

Find out more in the below list of FAQs. Therefore, to ensure data 
access while maintaining data security for all types of business 
relationships, the CSM security model created nine primary roles:

- sn_customerservice_agent
- sn_customerservice_manager
- sn_customerservice.customer
- sn_customerservice.customer_admin
- sn_customerservice.customer_case_manager
- sn_customerservice.partner
- sn_customerservice.partner_admin
- sn_customerservice.consumer
- sn_customerservice.consumer_agent

### Internal roles and external roles

The CSM internal and external roles are divided if they contain 
sn_esm_agent and sn_esm_user. These two roles are the base roles in CSM.

- **Internal roles**: The internal roles are for internal
personnel such as agents and agent managers using the CSM application.
They all contain sn_esm_agent role as base role.
- **External roles:** The external roles are for external
personnel such as customers and partners using the customer portal, and
they all contain sn_esm_user role as base role.
- **public:** No login is required to access features or
functions with the public role (for example, public knowledge bases, a
public page such as *reset password*).

### Role hierarchy

There are six base roles in the Customer Service Management product:

- sn_esm_agent
- sn_esm_admin
- sn_esm_partner
- sn_esm_partner_admin
- sn_esm_user
- sn_esm_user_admin

The CSM primary roles are based on these base roles. The arrows indicate the "Role contains" relationships.

**Figure 1: Roles relationships**

[](https://support.servicenow.com/sys_attachment.do?sys_id=5644d9a9dbb21d18770be6be13961999)

### External role levels

The relationships between customer and partner roles are:

- **sn_customerservice.partner_admin** can do **everything** that sn.customerservice.customer_admin can do, **not** vice versa.
- **sn_customerservice.partner** can do **everything** that sn.customerservice.customer can do, **not** vice versa.
- **sn_customerservice.partner** and **sn.customerservice.customer** can **only** view the cases created by themselves, not the cases created by other people.
- **sn_customerservice.partner_admin** can view **all** the cases belonging to their own accounts and their customer accounts.
- **sn_customerservice.customer_admin** can **only** view all the cases belonging to their own accounts.
- **sn_customerservice.customer_case_manager** can create
cases on behalf of all contacts in his own account and sub-accounts, but doesn't have administrative privileges as
sn_customerservice.customer_admin.

**Figure 2: Partner and customer roles**

[](https://support.servicenow.com/sys_attachment.do?sys_id=d644d9a9dbb21d18770be6be13961996)

### The distinction between similar roles

**Admin, agent, and consumer agent:** can all create cases, modify cases, and interact with most of the entities. The differences are:

- Admin can create and delete most of the entities.
- Agents and consumer agents usually can create, update, and read entities, but they cannot delete any records.
- Contacts and Accounts visible only to B2B agents (sn_customerservice_agent).
- Consumers visible only to B2C agents (sn_customerservice.consumer_agent).

**Customer and consumer**

Customer roles are for B2B business needs, which provide service to 
business customers. Consumer roles have been introduced to support the 
scenarios for individual customers in B2C mode. They provide case 
management, asset, contracts, and entitlement service, and also provide 
phone-based support for individual consumers.

- The consumer has the right to create cases for themselves after logging in.
- Consumer_agent is a B2C consumer service agent. Has the right to create, read, and update consumer records and cases.
- Customer agents and consumer agents handle similar use cases but deal with different groups of users.
- Customer agent does not have access to consumer related cases. (Consumer agent does not have access to customer cases.)

### FAQs

**1. Q: Can we assign both internal roles and external roles to the same user?**

A: No. A user should never be assigned any combinations of both the 
internal and external roles, such as sn_publication.author and 
sn_customerservice.customer_admin.

**2. Q:** **What happens when there is no role.**

A: When a user does not have any role, then the platform assigns 
snc_internal role to the user whenever the user record is opened or any 
API checks for the role on this user. Checking the role on any user is 
done by platform API 'hasRole' which adds snc_internal role if there is 
no role assigned to the user.

**3. Q: What needs to be done when users are imported through a file (typically done as part of legacy data migration)?**

A: Typically when data is imported from a file, no business rule is
 run and in this case, these users are not assigned any role. if these 
users are customer contact then they should be given the role 
'sn_customerservice.customer'. But if these users are consumers, then 
sn_customerservice.consumer role should be given to these users.

**4. Q: What needs to be done when users are migrated through 
the transformation map having the option 'Run business rules' unchecked 
(Migration of data by disabling the business rules is typically done to 
improve performance of the migration)?**

A: Typically when data is migrated using the transformation map with the option '**Run business rules**'
 unchecked, no business rule is run and in this case, these users are 
not assigned any role. if these users are customer contact then they 
should be given the role 'sn_customerservice.customer'. But if these 
users are consumers, then sn_customerservice.consumer role should be 
given to these users.

**5.  Q: What is the meaning of the public role and how it is related here?**

A: The public role means no login is required to access features or
 functions, such as topics, articles, etc. on CSM portals. It is not 
related to either internal or external roles.

**6. Q: Any difference between snc_internal, snc_external, 
sn_esm_user? Who else is not covered by these three roles? Any overlaps?**

A:  The sn_esm_user role contains snc_external. The snc_internal and 
snc_external roles are base roles from the platform level to 
differentiate company employees and out-of-company login users. A user 
has to be either snc_internal or snc_external, and cannot be both at the
 same time.

**7. Q: Can customer agents handle consumer agent's cases? Explain the difference between the two roles.**

A: Customer agent cannot handle consumer agent's cases. The customer 
agent is for B2B and the consumer agent is for B2C. They deal with 
different groups of cases.

**8. Q: We already have agent/customer roles - why do we need esm_agent/esm_user?**

A: The sn_customerservice_agent and sn_customerservice.customer are 
in a customer service scoped app. When you need to validate global table
 records via scripted AC, you need a way to access the global scope from
 the scoped app itself. The esm_agent/esm_user roles were introduced to 
resolve this issue.

**9. Q: What is the scripted ACL and how it has been used in CSM?**

A: ACL is an access control list. The ServiceNow platform uses ACLs 
to control data and resource access for different groups of 
users. Sometimes, to implement more complicated ACLs, a script can be 
added to implement conditions that cannot be expressed just by roles. 
This provides the flexibility for users to include their own business 
logic in ACLs that are not limited to existing roles.

**10. Q: Do I really need to use CSM supplied esm roles? Can I use my own roles?**

A: Yes, users can always create their own roles, but they will bypass
 the business rules/ACLs that are already implemented. Users need to 
start from the beginning to implement the related business logic for the
 new roles they created.

**11. Q: Can we use domain separation (separate account) to provide security and thus avoid the explicit role plugin?**

A: Domain separation can deal with some use cases about account 
hierarchy but because it is a separate plugin, the cost would be higher.
 The role-based model is more suitable for CSM product to deal with the 
regular use cases.

**12. Q: Can the partner role view all the cases in the partner account and its customer account? How about partner_admin?**

A: No. The partner role can view only the cases created by 
themselves for both their own account and their customer accounts. The 
partner_admin role can view all cases in their own account and their 
customer accounts.

**13. Q: If a table could be accessed by role 'A' but could not
 be accessed by role 'B', and there is one user with both A and B roles,
 what happens?**

A: If there is an ACL for the table for either role A or role B, as 
long as the user has one of the roles specified in the role list in ACL,
 then they would be able to access the table. If there is a query 
business rule for either role A or role B, then it depends on the 
business logic to determine how it works. Some conflicting roles are not
 supposed to be added to one user at the same time, such as 
sn_esm_user/sn_esm_agent, because it may trigger business rules/other 
components to have unexpected behaviors.

**14. Q: Should I add my new role to sn_esm_user or to specifically consumer? Why?**

A: If you need to create a new role parallel with consumer and do 
similar jobs, make sure the new role contains sn_esm_user since base 
level roles, sn_esm_* have been regulated in business rules and 
elsewhere to maintain the features for external consumers. If you need 
to create a new role higher than consumer level that is similar to or 
higher than consumer_agent, just include the consumer role.

**15. Q: Should I add my new role to sn_esm_agent or to specifically Customer Agent?**

A: Same with question 11. If a similar role as to how customer agent 
works is added, make sure the new role contains sn_esm_agent.

**16. Q: What is the difference between the customer agent and consumer agent?**

A: Customer agent is for B2B and has access to contact and account. The consumer agent is for B2C and has access to consumer.

**17. Q: What does the customer manager role do?**

A: Customer manager sees what customer and consumer agents can see. 
Customer manager can create accounts, contacts, consumers, assets, 
entitlements, contracts, account relationship, and contact 
relationships.

**18. Q: Why do we use both scripted ACL and query business rules in CSM security model to deal with roles logics?**

A: If we just used ACLs, in tables with a large number of records all
 the records would be validated before proceeding. This would cause 
performance issues. Scripted ACL and query business rules can filter out
 most of the unrelated records in a table before the rest runs through 
the ACLs. This can greatly improve the overall performance.

**19. Q: What is the difference between customer and customer admin?**

A: Customer can access their account and any account through contact 
relationship. Customers can see only cases created for themselves. 
Customer admin can access the above and all accounts in the account 
hierarchy. Customer admin sees all contacts and cases created for all 
their accessible accounts.

**20. Q: What is the difference between partner and partner admin?**

A: A partner is a customer and all accounts with which there is a 
partner relationship to their account. Partner sees all accessible 
accounts/contacts but only cases created by themselves or for 
themselves. Partner admin is a partner and can see all accessible 
accounts/contacts and all cases created for the accessible accounts.

**21. Q: Are there any changes in CSM roles between releases?**

A: The major change about roles is that sn_customerservice.consumer 
and sn_customerservice.consumer_agent roles were not present before 
Istanbul. They were introduced to support the scenarios for individual 
customers in B2C mode starting with the Istanbul release. There have not
 been any other major changes in the CSM product.

**22. Q: What is the case manager role?**

A: The case manager role has all the privileges of the 
sn_customerservice.customer role, plus it can create a case on behalf of
 another contact in the account, view a list of cases belonging to the 
account and edit cases belonging to the account. Also 
sn_customerservice.customer_case_manager must observe existing account 
hierarchy and account relationship restrictions. This role is assignable
 from the customer portal by customer admin and partner admin roles.

### Additional Information

For more information about the CSM product, see the [Customer Service Management](https://docs.servicenow.com/csh?topicname=c_CustomerServiceManagement.html&version=latest) product documentation topic.

For information about role definitions and functionalities, see the [Roles installed with Customer Service Management](https://docs.servicenow.com/csh?topicname=r_RolesInstalledWithCustomerService.html&version=latest) topic.

## Related

- [[Roles per module or topic]]
- [[CSM]]
- [[Roles and FAQ]]
- [[Customer Service Management (CSM)]]