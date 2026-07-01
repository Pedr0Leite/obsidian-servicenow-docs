---
aliases:
  - "CMDB CSDM"
tags:
  - cta-program
  - exam-prep
  - cmdb
  - csdm
  - customer-service-management
---

# CMDB/CSDM

## In short, the **Configuration Management Database (CMDB)** creates and maintains the logical configurations your network infrastructure needs to support a ServiceNow service.

Organizations use the CMDB to build logical representations of assets, services, and the relationships between them. These relationships make up the infrastructure of an organization. Details about these components are stored in the CMDB which are used to monitor the infrastructure, helping ensure integrity, stability, and continuous service operation.

The ServiceNow CMDB consists of entities called configuration items (CI). Configuration item attributes must be maintained, and changes tracked, to ensure their dependencies and relationships with other CIs are accurate. A configuration item may be:

- A physical entity, such as a computer or router
- A logical entity, such as an instance of a database
- Conceptual, such as a Requisition Service

A CI does not exist on its own. It is this relationship data that makes the CMDB a powerful decision-support tool. Understanding the dependencies and other relationships among your CIs can tell you, for example, exactly who and what is affected by the loss of that bank of disk drives.

Configuration items differ from environment to environment because each customer has unique needs. Details about the exact physical attributes of a computer may be needed by one customer but may represent meaningless data to another. The NOW Platform provides a mechanism to easily define new classes of configuration items and new relationships that may exist between CIs. New classes can be defined that extend other classes.

# **What is CSDM?**

# The CSDM is the data framework that you follow when you set up ServiceNow applications.

The **Common Service Data Model (CSDM)** is a standard and consistent set of terms and definitions that span and can be used with all ServiceNow products. The CSDM terms and definitions enable service reporting and provide prescriptive guidelines for service modeling within the ServiceNow **Configuration Management Database (CMDB)**. The CMDB is a repository that creates and maintains the logical configurations your network infrastructure needs to support a ServiceNow service.

The CSDM data model supports multiple configuration strategies. The data model includes guidelines for using base system tables and relationships. Many ServiceNow products depend on data within this data model.

### **Benefits of using the CSDM**

The CSDM is a CMDB-based framework that identifies where to place data for the products that you're using. Also, the CSDM is the standard for all ServiceNow products that use the CMDB.

The CSDM is a blueprint that you can follow when you set up your ServiceNow application.

The CSDM conceptual model contains these domains:

- Foundation
- Design
- Build (in 4.0)
- Manage Technical Services
- Sell/Consume

Each domain in the CSDM conceptual model is associated with one or more products,

Select the (+) icon to learn about each domain of the CSDM 4.0 conceptual model.

![image.png](CMDB%20CSDM/image.png)

This module reviews a use case and accompanies Suzi, the CTA, as she helps her customer with configuration management processes and governance.

*Simply put, following the CSDM framework ensures that the data your customer's ServiceNow application requires maps correctly to the appropriate CMDB tables.* 
*If you don't follow this standard, your customer may not receive the full benefit of the ServiceNow products on the Now Platform**.***Suzi, Certified Technical Architect

**Nice to know!**

- Application service depends on Application
- Business application uses information objects
- Business application consumes application services
- Technical service offering contains Dynamic CI groups

As part of the CMDB implementation, Suzi's customer wants to use the CSDM to map their services to the CMDB to leverage the out of the box functionalities provided by ServiceNow.

There will be two phases in this use case. Select each tab to review objectives for each phase.

In **Phase 1** of the implementation, Suzi's customer wants to use the services for internal use cases only. They want to achieve the following:

- **Incident Management** - They want to use the structure of the CSDM in the incident management process to automatically route the incident to the right assignment group, based on the responsible technical service offering.
- **Change Management** - They want to use the structure of the CSDM in the change management process to automatically populate the right business approver group and the technical approver group for a change request. This will be based on the responsible technical service offering and the responsible business service offering.
- **Tracking** - Suzi's customer needs to track which service handles sensitive data.

In **Phase 2** of the implementation Suzi's customer wants to make the services available for their business-to-business customers. Therefore, they need to link the CMDB data model to the CSM data model to support the following use cases.

- **Case Management** - Customers who bought a service from Suzi's customer should be able to log cases against the specific service offering they bought. Cases should be automatically routed to the right assignment group. If the agent decides to create an incident for that case, the information about the service should be automatically transferred to the incident so that the incident will be automatically routed to the right assignment group.
- **Transparency** - ****The business should be able to see which customer bought which offering.

# Phase one

In order to achieve the customer's goals, Suzi must first understand their current state. Suzi works hard to ensure that foundation data is correct in the system, such as users linked correctly to their managers, locations, companies, and departments.

I keep in mind that locations are not always accurate or correctly filled in, and the manager name is sometimes incorrectly linked when teams have been reorganized.Suzi, Certified Technical Architect

Other items that Suzi has noted are:

- Some strategic applications are available in multiple geographies. In some cases, regional and non-strategic applications have remained and continued to be used, but these are not detailed in the file.
- There are different service level commitments per geography.
- The customer has ITSM and CSM subscriptions as well as ITOM visibility. They have only implemented Discovery so far.
- Changes are always approved globally by the same team per application.
- Technical support groups are defined globally per application.
- Service desk support groups are different per application and geography to support services offered to the business.
- The business application table is currently filled with the list of applications which is used by the ITSM processes.

### **Workshop scenario - the invitation**

As the Certified Technical Architect, it is Suzi's responsibility to gather all the needed information to create the data model for her customer and map it to the services they use.

She has studied the white paper and her goal is to create a data model up to the "Run" maturity level.  Therefore, she plans a workshop with the necessary stakeholders.

Suzi invites the following personas:

**Service owner**

**Process owner**

**Enterprise architect**

**Technology service owner**

In the invitation, Suzi includes the [ITSM – Customer Workshop Preparation Guide(opens in a new tab)](https://nowlearning.service-now.com/nowcreate?id=nc_asset&asset_id=f1aa1b69db2d41542a923ca8f49619a5) provided by ServiceNow in Now Create, so that everyone can prepare for the workshop.

As a response to the invitation, the customer has filled out the preparation guide and Suzi now has a good understanding of how the customer currently manages their services.

Review the spreadsheet Suzi has gathered from the customer, attached below. This will be referenced in this section.

Question: Suzi's customer is currently assigning incidents and changes to the records in their business application table. All applications from column C are included in the table. Is this the correct approach? 

Answer: No, according to CSDM these are not the right structures to use for ITSM processes since they belong to the design domain.

### **Maturity level - Crawl**

At this point the data model that Suzi defined so far corresponds to the “crawl” maturity level. This level of CMDB modeling allows ITSM to start tracking incidents, problems, and change requests against application services. Additionally, it lays the ground work to manage against services.

![image.png](CMDB%20CSDM/image%201.png)

### **Maturity level - Walk**

At this point, the data model that Suzi defined so far corresponds to the “walk” maturity level. The walk level focuses on the management of technology services. Configuration items that are automatically discovered can now also be synchronized with manual meta data such as support group and technical approval group through technical service offerings.

![image.png](CMDB%20CSDM/image%202.png)

### **Maturity level - Run**

At this point the data model that Suzi defined so far corresponds to the “run” maturity level and it is possible to see the impact that the technology can have on the business.

The impact assessment for ITSM can identify impacted services and service offerings on incidents, problems, and changes for the selected CIs. Also, the related subscribed by tables are populated to identify who is impacted.

![image.png](CMDB%20CSDM/image%203.png)

**Complete data model for bank scenario discussed on week 2**

![image.png](CMDB%20CSDM/image%204.png)

# Phase two

After Suzi completed the phase one implementation of the CSDM, her customer decided to make the services also available for their business-to-business customers. At this point, the foundation of Customer Service Management (CSM) is already implemented and most of their customers are already live on ServiceNow. Now Suzi’s task is to make the services available to the customers in alignment to the CSDM in phase two.

The data model Suzi created in phase one consists of configuration items (CI) and links to internal CMDB classes. These are normally all internal and not customer facing. For the implementation of the Customer Service Management product view she has to use record types that are available in CSM and link these to the internal CMDB classes.

![image.png](CMDB%20CSDM/image%205.png)

### **CSM data model**

Suzi plans to use concepts around the CSM data model to accomplish phase two. Select each card below to learn more about the concepts. 

**Account -** An account is a supported external customer and a contact is a user who is an employee of an account.
**Sold product -** Sold products represent the products or services that have been sold to an account or consumer.
**Install base item -** Install base items are configuration items accessible to customers. They refer to an application service CI for SaaS products, and are used to track instances that have been provisioned for an account or consumer.
**Installed product -** An installed product is the relationship between a sold product and an install base item. Installed products provide information on the instances that a sold product is deployed on.
**Product model -** Product models are specific versions or configurations of products sold to and supported for customers. Service model is a class of product models to define Software as a Service (SaaS) products.

### **Mapping**

Suzi will use sold products and install base items to make the service offerings and application services accessible for their customers.

The reference between a sold product and a service offering is not available OOB. You need to activate the plugin “Customer Service with Service Portfolio Management (SPM)” first. This will give you the reference to service offering from the sold product. After activating the plugins, the service offering field must be added to the sold product form by a system administrator, as it is not visible by default.

![image.png](CMDB%20CSDM/image%206.png)

In order to use the sold products and install base items, leveraged by CSM, the "Customer Service Install Base Management" plugin must be activated. Though, if the reference between a sold product and a service offering is required as well, the "Customer Service with Service Portfolio Management (SPM)" plugin must be activated in addition.

If neither plugins have been installed, it's sufficient to only activate the "Customer Service with Service Portfolio Management (SPM)" plugin as the latter automatically installs the "Customer Service Install Base Management" plugin.

**Service model**

A service model is a class of product models to define Software as a Service (SaaS) products. It defines the service and contains the different attributes, choices, and components that can be configured to a customer’s specifications.

Because you can only link service offerings to sold products which are from the same model, Suzi needs to create a service model for services that are sold to customers.

## **Offerings for customer**

Suzi decides to start with the credit check service so that she can use this service later as a blueprint.

- Suzi's customer offers this service to their business-to-business customers with different options and commitment. That makes it necessary to create two new business service offerings. “Credit Check Customer Basic” and “Credit Check Customer Premium”.
- In phase one where only application services for production instances created were in the CMDB, now the customer also wants to track issues from customers with test instances.

So Suzi also creates an application service for the credit check test instance.

## **Credit check customer basic**

**Instance** - Only one production instance of service

**Commitment** - Resolution SLA 2 business days

## **Credit check customer premium**

**Instance** - One production and one test instance of their service

**Commitment** - Resolution SLA 4 hours + premium support

![image.png](CMDB%20CSDM/image%207.png)

The internal records are present for the credit check service.

Next, Suzi creates the external records for the pilot customer.

# **Pilot customer**

ACME is the first customer that bought the credit check service from Suzi's customer.

![image.png](CMDB%20CSDM/image%208.png)

- If a customer buys the service “credit check” Suzi needs to create a sold product for that account and reference the corresponding service offering in that sold product. Through the sold product the account is automatically subscribed to that service offering.
- Depending on the number of instances that are part of the offering for the customer, Suzi needs to create the install base items. These have a reference to the applicable application service.

# **Summary**

- [ ]  Here are the key takeaways to remember from phase two:
- [ ]  CMDB records are internal, CSM uses its own record types
- [ ]  If your customer sells services to their customers, you should plan to use sold products and install base items in CSM
- [ ]  Install base items reference application services or CIs in general
- [ ]  Sold product and service offerings that belong together must reference the same product model

![image.png](CMDB%20CSDM/image%209.png)

## Related
- [[Study for AI questions]]
- [[CSDM]]
- [[CMDB and CSDM]]
- [[CMDB]]
- [[Customer Service Management (CSM)]]