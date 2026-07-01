---
aliases:
  - "Notes for Presentation"
tags:
  - ciwf
  - csdm
  - case-management
  - domain-separation
  - foundational-data-models
  - install-base-management
---

# Notes for Presentation

### **Detailed Notes for Each Question**

### **Question 1: How does Boxeo’s case align with CIWF Foundational Data Models?**

- Boxeo aligns with **CIWF Foundational Data Models** because its challenges directly involve **customer data management, installed base tracking, and case handling**, which are core to **Customer Data Foundation, Install Base Management, and Case Management**.
- The company needs a **centralized data model** to manage customer interactions, entitlements, and service requests efficiently.
- Using a **standardized foundational model** improves **data consistency, reduces manual effort, and enhances automation**, aligning with CIWF’s goal of optimizing customer service processes.

### **Question 2: Why does TMT (Telecommunications, Media, and Technology) Data Model apply to Boxeo?**

- Boxeo operates in a **technology-driven environment** where customer data, service requests, and product management need **industry-specific data models** to ensure seamless operations.
- The **TMT Data Model** is relevant because it provides **pre-built structures for handling complex customer relationships, product entitlements, and service requests**, which directly address Boxeo’s **integration challenges and customer support inefficiencies**.
- Adopting the **TMT Model** ensures that Boxeo can scale its operations while maintaining compliance with industry standards.

### **Question 3: What does this feedback mean? ("Install Base Items should be covered by Installed Products, so you are looking for something different.")**

- The feedback suggests that **Install Base Items and Installed Products** may be duplicating the same concept in your answer.
- Instead of repeating **Installed Products**, look for another key data component that supports **Install Base Management**, such as **"Entitlements" (to track service eligibility) or "Maintenance Records" (to track service history on installed products)**.

### **Question 4: Specific Record (Table) Names for Each Capability**

For each capability, reference the **exact database records (tables)** that are being used:

1. **Field Service Management** → `Work_Order` & `Work_Order_Task`
2. **Sales and Order Management** → `Orders`
3. **Customer Project Management** → `Customer_Project` & `Customer_Project_Task`
4. **Proactive Service Experience Workflows** → `Incident`, `Alert`, `Case`
5. **Service Bridge** → `Provider`
6. **Omnichannel Add-ons** → `Email`, `Interaction`

These are **specific records (tables)** that store data in ServiceNow, ensuring accurate process tracking.

### **Question 5: Alignment with CIWF Goals**

- **Streamlined Case Handling Across Business Units** → Aligns with **Case Management** by ensuring that cases are managed across **CSM, FSM, and SOM**, reducing duplication.
- **Improved Response Times & SLA Compliance** → Aligns with **Install Base Management**, ensuring that service teams have **real-time product and entitlement data** for faster resolution.
- **Enhanced Customer Satisfaction & Visibility** → Aligns with **Customer Data Foundation**, enabling **360-degree customer views, automated workflows, and real-time tracking of service requests**.

### **Question 6: Case Management as a Foundational Data Model**

- **How It Supports CSM, FSM, and SOM for Boxeo:**
    - **CSM (Customer Service Management)** → Standardizes case handling and escalations.
    - **FSM (Field Service Management)** → Ensures **field technicians receive accurate case data for on-site issue resolution**.
    - **SOM (Sales and Order Management)** → Links service cases to product orders, ensuring smooth customer interactions.
- **Key Data Components:**
    - `Case` → Stores customer-reported issues.
    - `Service Tasks` → Breaks cases into actionable tasks.
    - `Entitlement Validation` → Ensures only authorized customers receive specific support.

This answer ties **Case Management** back to Boxeo’s real-world **customer support inefficiencies** and shows how **a structured model improves response times and case handling accuracy**.

**Question 1**

Boxeo Tech is a B2B company in the hardware and support services space, and they work closely with customers across multiple business units.

This project focuses on improving service delivery across their customer support, sales and order management, and field service teams.

For question one, we’re looking at core personas each with distinct responsibilities and challenges that need alignment through CIWF.

By aligning each persona to a single unified portal, we streamline their experience, ensure relevant data and actions are tailored to their role.

**Persona One:** Boxeo Sales Representative

- Work in the sales team often needs to open tickets on behalf of customers.
- Relates to customers and internal project and support teams to deliver the service.
    - **Business to: Employee (B2E)**
    - **Foundational Data Model:**
        - Account
        - Contact
        - Partner
        - Contributor
    - **Configuration Objects:**
        - Business Location
        - Sold Products
        - Install Base Items
        - Addresses
    - **Portal:**
        - Business Location Service Portal (blsp), Costumer (csm), Consumer (csp), Employee (esc)

**Persona Two:** B2B Customer Administrator (External Persona – Business Customer Representative)

- A company that is customer of Boxeo that needs support for Boxeo products
    - **Business to:** Business to Business (B2B)
    - **Foundational Data Model:**
        - Account
        - Contact
        - Contract
        - Entitlement
    - **Configuration Objects:**
        - Install Base Items
        - Sold Product
        - Addresses
    - **Portal:**
        - Customer Support Portal (csm) (Provides business customers with access to case management, asset tracking, and service requests).

**Persona Three:** B2C Consumer (External Persona – Individual Consumer)

- A client (consumer) that buys a product, like an anti-virus from a Boxeo reseller and it is supported by the Boxeo Tech company.
    - **Business to:** Business to Customer (B2C)
    - **Foundational Data Model:**
        - Consumer
        - Sold Product
        - Install Base Item
    - **Configuration Objects:**
        - Consumer
        - Household
        - Household Member
    - **Portal:**
        - Customer Service portal (csp) (Offers a self-service experience for submitting cases, tracking assets, and managing subscriptions)

**Persona Four:** Customer Support Agent (Internal Persona)

- Resells Boxeo services to consumers
    - **Business to:** Business-to-Consumer (B2B2C)
    - **Foundational Data Model:**
        - Account
        - Contacts
        - Partner
    - **Configuration Objects:**
        - Business Location
        - Sold Products
        - Install Base Items
        - Addresses
    - **Portal:**
        - Business Location Service Portal (blsp)

**Question 2**

Boxeo is struggling with fragmented service data, inefficient field handoffs, and customers needing integration between systems.

To solve this, CIWF’s Foundational Data Models come in.

We’ve identified three key pain points at Boxeo.

For each, we’ve mapped a foundational CIWF data model that helps address the challenge.

Pain Point One: Customers do not see their correct products on the portal and have attributes that do not relate to their products

- Foundational Data Model: Install Base Management

Why Install Base Management?

It ensures that customer products are correctly registered and linked to their accounts.

It aligns CMDB and Product Catalog data to eliminate discrepancies.

It provides a single source of truth for both customers and support teams.

- Key Capability:
- CMDB
- Product Catalog
- Value Realized:
- By using Sold Products and Install Base Items to reflect exactly what the customer has purchased, Boxeo can build personalized product visibility in the portal. This solves the issue of customers seeing shared infrastructure or unrelated product attributes by linking the correct CIs to customer accounts. Leveraging the Product Catalog ensures customers only interact with services they’re entitled to, and CMDB alignment provides accurate technical context for those services. This leads to better customer experience, reduced support tickets, and higher portal adoption.

Pain Point Two: Boxeo Tech is claiming they see low value in ServiceNow due to maintenance costs across all the applications working together and upgrading process due to the level of customization (too manual, long, and slow process).

- Foundational Data Model: Customer Data Foundation
    
    Why Customer Data Foundation?
    

Customer Data Foundation solves one of Boxeo’s biggest problems: domain separation. Right now, their platform is heavily customized, with separate processes per customer. This increases testing and upgrade effort and slows down value delivery.

By replacing domain separation with Customer Data Foundation, Boxeo can still isolate customer data — but do it in a smarter way. Instead of isolating entire domains, we use ACLs, entitlements, and contact-account relationships. This simplifies the platform and reduces ongoing maintenance costs, all while preserving data integrity and compliance.

- Key Capability:
    - Incident Management
    - Technology Product Support Case Management
- Value Realized:
    - The use of domain separation has introduced heavy maintenance costs and complicated the upgrade path. Instead of domain separation, Boxeo can adopt Customer Data Foundation which supports data segregation using ACLs, roles, and entitlements. This preserves customer data integrity without overengineering. By rebuilding CSM on a new instance, without domain separation, Boxeo can simplify workflows, reduce testing overhead during upgrades, and get faster time-to-value with out-of-the-box (OOTB) features. It also enables scalable support case handling and reuse of common processes across customers.

Pain Point Three: Customers do not see their correct products on the portal and have attributes that do not relate to them

- Foundational Data Model: TMT (Telecommunications, Media, and Technology) Data Model
- 
    
    Why TMT?
    

The TMT Data Model is the best choice for Pain Point Three (Customers need to integrate their instances with Boxeo’s instance) because Boxeo operates as a technology provider offering managed services to multiple customers, and TMT is designed for service providers who need to manage complex customer relationships, assets, and service interactions across different platforms.

- Key Capability:
    - Service Bridge
    - Case Types
- Value Realized:
    - Service Bridge allows customers to log cases in their own ServiceNow instances and have them automatically replicated into Boxeo’s instance. This eliminates the need for customers to use Boxeo’s portal and prevents duplicate case reporting. The use of standard Case Types enables Boxeo to apply automation and reporting consistently. Together, these capabilities support real-time collaboration, lower case volumes, and improved service transparency. It also strengthens Boxeo’s positioning as a modern service provider with customer-first integration models.

**Question 3**

Question 3 focuses on explaining what and how capabilities categorized as “Needs to be re-implemented”  need to be re-implemented.

Capability List:

TMT Specific Applications

- Technology Product Support Case Application

Customer Data Foundation

- Consumers

Install base Management

- Product Models
- Install Base Items
- 
    
    Case Management
    
- Case Types
- 
    
    Advanced Work Assignment
    
- Capacity
- Availability
- Skills Management
- 
    
    Service Management
    
- TSM with change Management
- TSM with Incident Management

Capability classified as 'Needs to be re-implemented’

TSM with Change Management and CMDB

- Why re-implementation is needed:

Customers can request changes and CMDB record changes (all fields as needed) in the portal, which is a great risk for the quality of data stored within the CMDB table. A well-designed Change Management process will make sure all changes to the CMDB records are correctly documented, reviewed and approved before applied.

Also, the CMDB not being compliant with CSDM makes it harder to manage.

Capability classified as 'Needs to be re-implemented’

TSM with Incident Management

- Why re-implementation is needed:

Since domain separation needs to be replaced, new access controls with more accurate permissions need to be created. This will ensure data compliance and the privacy.

Also, Boxeo Tech currently allows non-technical users with ITIL roles to access and modify ITIL records. This resulted in issues with data compliance and access permissions. Re-implementation focuses on securing permissions to improve compliance and reliability.

Capability classified as 'Needs to be re-implemented’

Consumers

- Why re-implementation is needed:

Boxeo have multiple data scatter across multiple systems, including a legacy CRM system. This might lead to inconsistencies in the data and can lead to a negative impact in customer service and decision-making. OOB tables can be used for the purpose of saving data, preventing unnecessary table creation and allowing the support to the platform to become easier.

**Question 4**

Here we’ve selected six capabilities from the CIWF Capability Map that align directly with Boxeo’s use cases.

For each capability, I’ve identified the specific transactional records, like work_order for Field Service Management, and prerequisite applications that must be in place to support each use case. This structure helps Boxeo clearly understand implementation dependencies.

Capability One: Field Service Management

Use Case:

Field Service Management is used to manage field technician assignments, track service requests, and support site work currently being recorded as incidents. It enables Boxeo Tech to streamline field operations by creating structured workflows for on-site activities, ensuring tasks are completed efficiently.

Two Records:

- Work Order
- Work Order Task

Two Pre-Req Apps:

- Customer Case Management - Links customer cases to field service operations, ensuring that field tasks are properly initiated from customer-reported issues.
- Capacity and Reservations Management

Capability Two: Sales and Order Management

Use Case:

Sales and Order Management streamlines lead-to-cash processes, allowing Boxeo to manage the sales cycle and customer orders. It ensures that customer data and product specifications are accurately captured during the order process and supports fulfillment workflows.

One Record:

- Order

Two Pre-Req Apps:

- Install Base Management - Tracks sold products and installed items, enabling accurate order fulfillment and lifecycle management.
- Product Catalog Advanced - Provides a structured catalog of available products and services, ensuring orders are aligned with predefined offerings.

Capability Three: Customer Project Management

Use Case:

Enables Boxeo Tech customers to manage complex projects with multiple tasks and provide end users with visibility into these projects. For Boxeo, this also supports the deployment of new services for customers uses Service Portfolio Management

Two Records:

- Customer Project
- Customer Project task

Two Pre-Req Apps:

- Project Portfolio Management (PPM) – Manages the portfolio of projects and aligns them with Boxeo’s strategic goals
- Customer Case Management – Links customer issues or requests to project tasks, ensuring the project meets customer expectations

Capability Four: Proactive Service Experience Workflows (PSEW)

Use Case:

It automates communications with customers during service outages or other incidents. It ensures that affected customers receive timely updates and alerts, reducing frustration and enhancing transparency during service disruptions.

Three Records:

- Incident
- Alert/Event
- Case

Three Pre-Req Apps:

- Customer Case Management - Ensures customer cases are linked to incidents or alerts, streamlining communication.
- Event Management - Monitors infrastructure for events and alerts, which feed into the incident management process.
- Install Base Management - Identifies which customers or products are affected by the incident, ensuring accurate communication.

Capability Five: Service Bridge

Use Case:

Service Bridge connects Boxeo’s ServiceNow instance with customer instances, enabling seamless collaboration between Boxeo, its customers, and partners. This integration facilitates inter-service operations, allowing data to flow between systems in real time.

One Record:

- Provider

One Pre-Req App:

- Customer Case Management - Ensures customer cases and service records are synchronized between Boxeo’s system and customer systems, enabling consistent collaboration.

Capability Six: Omnichannel add-ons

Use Case:

Omnichannel Add-ons provide unified communication channels (email, phone, chat, etc.) for customer interactions. These add-ons automate the creation of interactions and cases for incoming communications, reducing manual effort and improving the efficiency of customer service.

Two Records:

- Interaction
- Email

Two Pre-Req Apps:

- Customer Case Management - Links interactions (email or phone) to cases, ensuring seamless customer service workflows.
- Computer Telephony Integration - Automates phone interactions and case creation, ensuring efficient handling of customer calls.

**Question 5**

Question 5 highlights what must be adapted in Boxeo’s current ITSM environment. We’re not just introducing new models—we’re improving what already exists.

Existing ITSM Implementation Aspect One:

Boxeo’s current ITSM setup needs several targeted improvements to prepare for CIWF adoption. The first is Access Control Lists. Right now, domain separation is being used to restrict access, but that adds unnecessary complexity. By shifting to role-based ACLs, this ensures that only authorized employees can view or edit sensitive customer records, and with this, we maintain data privacy, but in a way that’s easier to manage and scale across the organization.

- Modification: Reconfigure ACLs to use role and group-based access instead of relying on domain separation. This ensures that only authorized employees can view or edit sensitive customer records, improving data security and simplifying permissions across the platform.
    
    Access Control Lists (ACLs)
    
- Alignment with CIWF Goals:
- Data Privacy & Compliance: Prevents unauthorized access to customer data.
- Reduced Customization Overhead: Removes need for domain-specific ACLs.
- Scalable Administration: Supports a single, consistent access model across teams.

Existing ITSM Implementation Aspect Two:

The second change is around Case Management. Today, different teams handle incidents, field requests, and order changes using separate processes. CIWF recommends a unified case structure, so support teams, field techs, and order teams all collaborate on the same record. That leads to fewer delays and stronger SLA performance.

- Modification:
    
    Case Management
    

Implement a standardized Case Management model across CSM, FSM, and SOM to manage all service-related interactions. This centralizes support processes and improves collaboration across business units.

Alignment with CIWF Goals:

- Unified Service Delivery: Enables cross-team collaboration on a shared case record.
- Faster Issue Resolution: Aligns with SLAs and improves task routing.
- Customer Transparency: Supports real-time tracking and consistent communication.

Existing ITSM Implementation Aspect Three:

Finally, we need to optimize Incident and Request handling. Today, too much is done manually—routing cases, assigning tasks. With CIWF, we apply automation and assignment logic based on things like availability and skills. That reduces backlog, improves response times, and gives managers real-time visibility into work progress.

- Modification:
    
    Incident, Service Request and Case Management Processes
    

Redesign Incident and Request workflows using automation, task assignment rules, and categorization. Remove reliance on manual routing and generic record producers.

Alignment with CIWF Goals:

- Operational Efficiency: Automates repetitive tasks, reduces errors.
- SLA Compliance: Ensures timely assignment based on priority and availability.
- Performance Visibility: Enables live dashboards and proactive monitoring.

**Question 6**

Foundational Data Model One: Customer Data Foundation

How It Supports CSM, FSM, and SOM for Boxeo:

The Customer Data Foundation ensures consistent, structured customer data across CSM, FSM, and SOM by managing customer relationships, accounts, and contact data. It enables Boxeo to maintain data integrity, rightful access, and compliance when sales, customer success, and consulting teams interact with ITIL records.

Key Data Components:

- Accounts – Represents B2B customer organizations, ensuring structured customer records.
- Contacts – Tracks customer representatives, allowing controlled access to cases.
- Entitlements and SLAs – Ensures customers receive the correct level of support, preventing service misalignment.

Foundational Data Model Two: Install Base Management

How It Supports CSM, FSM, and SOM for Boxeo:

Install Base Management provides visibility into sold and installed products, ensuring accurate tracking of customer-owned assets and service entitlements. This is critical for customer service cases (CSM), field service work (FSM), and order management (SOM).

Key Data Components:

- Install Base Items – Represents sold and installed products, supporting accurate entitlement validation.
- Product Models – Defines product specifications, ensuring service teams have the correct technical details.
- Locations – Identifies where assets are installed, supporting field service scheduling and product lifecycle tracking.

Foundational Data Model Three: Case Management

How It Supports CSM, FSM, and SOM for Boxeo:

The Case Management foundational data model ensures structured handling of customer service requests, field service escalations, and order-related issues. It provides a centralized framework for managing customer interactions, enabling Boxeo to track, resolve, and analyze service cases efficiently across CSM, FSM, and SOM.

Key Data Components:

- Case Types – Categorizes customer service issues, ensuring structured workflows for resolution.
- Service Orders – Standardizes customer requests related to product issues, order modifications, or service escalations.
- Entitlements & SLAs – Ensures proper case prioritization and response times based on customer agreements.

**Question 7**

Condition One: Need for Strict Data Segregation Between Tenants

- This applies when data visibility must be completely restricted between customers, with no overlap in support agents or shared records. This condition does not apply to Boxeo!
- Boxeo supports multiple customers but does not require full isolation of data. Instead, they use shared support teams and overlapping processes.
- Alternative: Boxeo can use CSM ACLs, roles, and entitlements to restrict access to records and data elements—without domain separation.

Condition Two: Separate Administration and Configuration by Customer

- This applies if each customer has dedicated admins who need to manage their own processes, SLAs, catalog, etc. This condition does not apply to Boxeo!
- All administration is centralized. Boxeo does not allow customers to configure their own processes. Instead, Boxeo should simplify administration by removing domain separation and using standard ACL and group-based access.

Condition Three: Unique Business Processes Per Tenant or Customer

- This condition is met when customers require separate workflows, forms, or logic based on their unique service needs. This condition does not apply to Boxeo!
- Boxeo runs standardized workflows across all customers (e.g., request, incident, and case flows) and does not customize per tenant. Using CIWF Foundational Models allows consistent handling of service requests across CSM, FSM, and SOM.

Boxeo's Conditions:

Why Domain Separation Is Not Suitable for Boxeo?

There are three key conditions where domain separation is recommended:

1. When you need strict data segregation
2. When you have unique workflows per customer
3. When you allow separate admin and configuration per customer.

Boxeo doesn’t meet any of these. All workflows are shared, data access can be controlled with ACLs, and admin is centralized. So instead of domain separation, we recommend using CIWF foundational models like Customer Data Foundation and Install Base Management to structure visibility and entitlement, while reducing platform complexity.

This approach improves upgradeability, lowers cost, and supports Boxeo’s need for scalable service delivery.

By avoiding domain separation and utilizing the following alternatives, Boxeo can achieve its goals of scalability, simplified management, and improved service quality.

- Do you have specific separate business processes for front and middle offices or per customer?
    - Boxeo has distinct customer service (CSM), field service (FSM), and order management (SOM) processes, requiring structured workflows.
    - CIWF Foundational Data Models provide a standardized way to manage these processes without requiring complete separation between customers.
    - Instead of isolating customers into different domains, role-based access and entitlement controls ensure process integrity.
- Do you require contractors or outsourced vendors to support specific customer accounts or locations?
    - Boxeo engages third-party vendors for field service and support, requiring accurate entitlement tracking.
    - The Install Base Management model helps manage customer-owned assets, while Case Management ensures appropriate ticket handling for both Boxeo and its partners.
    - CIWF Foundational Data Models allow vendor-specific access controls without needing full domain separation.
- Do you need UI elements or objects targeted to a specific role?
    - Boxeo requires role-specific dashboards and workflows for agents handling cases, field technicians fulfilling service orders, and managers overseeing operations.
    - CIWF models support role-based access within a unified environment, ensuring that users only see what’s relevant to them without segmenting the instance.

**Question 8**

**Current Key Persona List missing from the image:**

1. **Costumer Service Agents:** internal employees that resolve the cases that the customers address to Boxeo.
2. **Project Manager:** manages customers projects that uses SPM application capabilities to oversee the project progress and resource assigned.
3. **Field Technician** – Responsible for on-site service and field operations, using tools like dynamic scheduling and crew optimization in FSM.
4. **Sales** – Manages customer accounts, handles the commercial catalog, and uses CPQ (Configure, Price, Quote) tools.
5. **Customer** – The one who initiates service requests, raises incidents, or seeks product support. This persona interacts with the Customer Service Portal and primarily deals with product/service issues, updates, and status checks.
6. **Consumer:** a consumer who as bought products or services through a reseller. The consumer expects support comes directly from Boxeo.

**Key Capability List:**

- **Case Management** Handles customer-reported issues, service requests, and escalations, enabling structured intake, assignment, and resolution across CSM, FSM, and SOM teams.
- **Incident Management** Restores normal service operations quickly by tracking, assigning, and resolving unplanned disruptions through standardized ITIL-aligned processes.
- **Field Service Mgmt.** Coordinates field technician assignments, enables scheduling, and manages on-site service delivery, including work orders and parts tracking.
- **Event Management** Monitors events from infrastructure (e.g., SolarWinds), correlates them into alerts, and initiates incident workflows to resolve customer-impacting issues proactively.
- **Service Level Management** - Defines, tracks, and enforces SLAs to ensure consistent and measurable service delivery aligned with customer expectations and contractual commitments.
- **Project Portfolio Management** Manages strategic and operational projects by organizing tasks, resources, and timelines, supporting visibility and prioritization across the delivery pipeline.
- **Strategic Portfolio Management Integration** Connects service delivery efforts with strategic planning, aligning customer projects and demand with long-term business objectives and value realization.
- **Advanced Work Assignment** Optimizes task routing by assigning work based on skills, availability, location, and capacity—ensuring the right person handles the right work at the right time.
- **Change Management** Controls the lifecycle of changes, from request to approval and implementation, to minimize risk and ensure traceability across impacted services and assets.
- **Proactive Service Experience Workflows** Delivers automated, context-aware communication to affected customers during incidents or outages, improving transparency and customer satisfaction.
- **Sales and Order Management TMT** Supports lead-to-cash processes in the telecommunications and technology space, including order capture, MACD changes, and order fallout support.
- **Post Sales Engagement Core** Manages the customer relationship after the initial sale by coordinating product support, entitlements, and ongoing engagement activities.

## Related

- [[CIWF]]
- [[Use cases for Domain Separation]]
- [[Improvements]]
- [[CMDB]]
- [[CSDM 5]]
- [[Domain Separation]]