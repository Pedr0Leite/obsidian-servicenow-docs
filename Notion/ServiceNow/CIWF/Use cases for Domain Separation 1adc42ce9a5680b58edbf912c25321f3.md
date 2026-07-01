---
aliases:
  - "Use cases for Domain Separation"
tags:
  - domain-separation
  - ciwf
  - data-separation
  - delegated-administration
  - msp
---

# Use cases for Domain Separation

![image.png](Use%20cases%20for%20Domain%20Separation/image.png)

# **Understanding Domain Separation - Basics**

### **Issue**

Domain separation allows you to separate data, processes, and administrative tasks into logical groupings called domains. You can then control several aspects of this separation in different ways.

Domain separation is a little bit like an office or apartment building that rents or leases individual spaces to tenants. Similarly, Managed Service Providers, or MSP’s, can use Domain Separation within ServiceNow to lease parts of a ServiceNow instance to other organizations. That means that one instance can be used by multiple customers. With domain separation enabled, multiple customers can reside on the same instance, which is like different companies leasing space in the same office building. Just like an office has shared resources and spaces, the instance has global properties, data, and processes that are shared across all domains.

Domain separation can also enable global companies with unique business requirements for different parts of the world to segment and customize their instances.

Domain separation is the paid plugin that enables this configuration.

Also like a tenant in a leased building, each domain can have its own set of data that other domains cannot see. This is enabled by data separation.

Similarly, each domain in a ServiceNow instance can have unique functions and processes associated with it, such as customized business rules. Each domain in the instance can also have a different user interface associated with it. Both of these are possible by process separation

### **Domain Hierarchy**

Domains are set up as hierarchies that help to organize multiple domains and define the relationship between them.

[](https://support.servicenow.com/sys_attachment.do?sys_id=a35a6066db42b450e515c223059619b0)

TOP domain: TOP is the root domain in the hierarchy. Only process records are associated with TOP; these records specify universal, instance-wide processes and platform elements.

Customer domains are associated with data and process settings that are unique to that customer. They can also have customer-specific UI settings.

Some customers grant a domain specifically for the MSP company to use. If defined, the MSP domain can be used as a data domain to manage internal business and data (tasks, users, CI’s, etc.).

ServiceNow usually recommends that customers have one Default domain set for their instance. The Default domain can be anywhere in the hierarchy. It is a holding area for a record until it is assigned to a domain by an admin or assigned automatically based on business rules. Records in the Default domain are only visible to the admin user. If you do not set a Default domain, new, unassigned records are placed in the Global domain.

### **Data Separation versus Process Separation (aka. Delegated Administration)**

### **Data Separation**

Data separation is enforced at the database level through the use of the sys_domain column in tables. About 1000 base platform tables already have this column, making them “domain-separated.” When a customer logs in under a domain and pulls up a domain-separated table, the system uses built-in queries to pull data only from that domain.

To make a custom table domain-separated, add the sys_domain field to the table. However, extensive testing should be done by customers to ensure the table behaves as expected.

[](https://support.servicenow.com/sys_attachment.do?sys_id=b75a6066db42b450e515c223059619b5)

Based on the hierarchy, users can see data in their home domain and child domains of that home domain. They do not have access to data in their parent domains, peer domains, or domains in other branches of the hierarchy.

In this example, Cloud Dimensions is the MSP. They have two customers; Stark Industries, which has two child domains of its own, and Globex which has one child. Because Cloud Dimensions is at the top of the hierarchy, it can see the data for both Stark and its customers, as well as the data for Globex and its customer. Stark can see the data for both of its child companies, however, Customer 1 and Customer 2 can only see their own data because they are both at the bottom of the hierarchy.

### **Process Separation (Delegated Administration)**

Likewise, processes can be domain-separated. Process separation is enabled through the use of the sys_overrides column in domain-aware tables. Any table that contains both the sys_domain and the sys_overrides fields can be configured to have different processes from the parent domain. For example, you could have a business rule that exists in the Top domain, and then override it for a child domain to run a different business rule. As another example, two users who sign into different domains might see two different user interfaces in the instance.

If you activate only data separation and not process separation, all domains will use the same business rules. In addition, you can choose to ***not*** separate data, just processes.

Here are the objects that can be process separated within ServiceNow

[](https://support.servicenow.com/sys_attachment.do?sys_id=7b5a6066db42b450e515c223059619ba)

System policy functions such as assignment rules, approval rules, SLA management, inactivity monitors, email notifications, business rules, client scripts, UI policies, or UI actions, can be defined globally or specifically for a particular domain.

Forms, lists, Related Lists, and Choice Lists can also be domain-specific. For example, if a particular domain requires different fields on their Incident form, no problem! If a customer wants a different set of choices in a Choice List, they can customize the Choice List for their domain.

Service providers can even customize the branding and user interface elements for a domain.

Here is how the process separation rules flow within the instance.

[](https://support.servicenow.com/sys_attachment.do?sys_id=b75a6066db42b450e515c223059619c0)

### **Exclusion list Tables for Domain Separation**

There are some tables and applications that should never be domain-separated, and some other tables and applications where just adding the sys_domain field is not enough to achieve domain separation. Therefore, domain separating these tables is not recommended.

Detailed information on domain separating non-out of box tables as well as these Exclusion list tables are available here:

[Tips for Domain Separating 'NON Out of Box Domain separated' Tables](https://support.servicenow.com/nav_to.do?uri=/kb_view.do%3Fsysparm_article%3DKB0662346)

### **Contains and Visibility Domains**

### **Contain Domains**

There may be times when we want some customers to see data from a domain that is not under them in the hierarchy. There are two ways to expand visibility to data: the Contains table, and Visibility tables.

The domain_contains table allows users of a domain (called the “containing” domain) to see data from another domain (or the “contained” domain). The records in this table define the “contains” relationship, and this *applies to data only, not processes*.

The hierarchy rules still apply, so domains that have a contains relationship to another domain can see that data in addition to whatever they would see as a result of their hierarchy relationships. The session domain is also still honored: for example, an employee of the ACME domain will always be logged into ACME, even though their domain may “contain” another domain.

[](https://support.servicenow.com/sys_attachment.do?sys_id=7b5a6066db42b450e515c223059619c5)

For example, you might want Customer 1 to be able to view data for Customer 2. In this case, the Customer 1 domain would contain the Customer 2 domain. You can also specify a circular containership, where two domains can see each other’s data.

[](https://support.servicenow.com/sys_attachment.do?sys_id=fb5a6066db42b450e515c223059619f0)

### **Visibility Domains**

The domain visibility tables (sys_user_visibility and sys_user_group_visibility), allow specific users or groups to view data for a domain that they couldn’t otherwise access in the hierarchy. For example, if a user or group in the Customer 1 domain needs visibility to the Customer 2 domain, you can add the visibility to the user profile.

Visibility rules can be used with contains relationships, or they can be used separately.

[](https://support.servicenow.com/sys_attachment.do?sys_id=bf5a6066db42b450e515c223059619f5)

[](https://support.servicenow.com/sys_attachment.do?sys_id=806aa066db42b450e515c22305961908)

In the example below, MSP contains TOP, which allows MSP domain access to all of the domains in TOP and under. Similarly, ITIL Group has visibility to ACME and Oceanic Airlines, so all users in the ITIL group will be able to view data for these 2 domains.

[](https://support.servicenow.com/sys_attachment.do?sys_id=cc6aa066db42b450e515c2230596190d)

### **Related Links**

- [KB0716268: Domain Separation - Advanced Concepts and configurations](https://support.servicenow.com/kb_view.do?sysparm_article=KB0716268)
- [Understanding Domain Separation](https://docs.servicenow.com/csh?topicname=c_DomainSeparation.html&version=latest)
- [Visibility and Contains Domains](https://docs.servicenow.com/csh?topicname=c_DomainVisibility.html&version=latest)
- [Create contains relationships between domains](https://docs.servicenow.com/csh?topicname=t_CrContRelBetDom.html&version=latest)
- [Change domain visibility](https://docs.servicenow.com/csh?topicname=t_ChangeDomainVisibility.html&version=latest)
- [Domain separation setup and basic administration](https://docs.servicenow.com/csh?topicname=c_DomainSeparationSetup.html&version=latest)
- [Delegated administration](https://docs.servicenow.com/csh?topicname=c_DelegatedAdministration.html&version=latest)
- [Troubleshoot domain separation errors](https://docs.servicenow.com/csh?topicname=r_TroubleshootDomainSeparationError.html&version=latest)
- [Enable verbose domain logging and debug messages](https://docs.servicenow.com/csh?topicname=t_EnableDomainLogDebugMsgs.html&version=latest)
- [Application support for domain separation](https://docs.servicenow.com/csh?topicname=domain-separated-apps.html&version=latest)

## Related

- [[CIWF]]
- [[Notes for Presentation]]
- [[Domain Separation]]
- [[CMDB]]
- [[CMDB & CSDM]]