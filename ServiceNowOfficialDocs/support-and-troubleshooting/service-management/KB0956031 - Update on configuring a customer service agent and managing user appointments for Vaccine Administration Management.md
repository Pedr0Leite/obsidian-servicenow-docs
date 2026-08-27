---
title: "Update on configuring a customer service agent and managing user appointments for Vaccine Administration Management"
aliases:
  - KB0956031
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0956031
kb_number: KB0956031
last_modified: 2025-01-03
---

## Update on configuring a customer service agent and managing user appointments for Vaccine Administration Management

  

### Summary

This article provides updated information on the processes currently documented in two docs.servicenow.com documentation topics: [Configure a customer service agent for Vaccine Administration Management](https://docs.servicenow.com/bundle/quebec-customer-service-management/page/product/vaccine-management/task/configure-customer-service-agent-for-vam.html) and [Managing user appointments as a customer service agent](https://docs.servicenow.com/bundle/paris-customer-service-management/page/product/vaccine-management/task/managing-user-appointments.html). In order to complete the second procedure successfully, you must complete the first procedure.

### Instructions

## Configure a customer service agent for Vaccine Administration Management

Customer service agents can be configured to receive a request from a user who wants to register for the vaccination program. The agent captures users' contact information, and then creates a vaccination appointment on their behalf.

### Before you begin

To modify the access control lists (ACLs), the user with the admin role must be assigned the security\_admin role.

**Note:** For more information about elevating privileged roles, see [Elevate to a privileged role](https://staging-docs-servicenow.zoominsoftware.io/bundle/quebec-platform-administration/page/administer/security/task/t_ElevateToAPrivilegedRole.html)

Role required: admin, security\_admin

**Procedure**

1.  Assign the sn\_vaccine\_sm.clinician role to the user with the sn\_customerservice\_agent role.
    
2.  Give the agent permission to create new users by assigning the user.admin role to the user with the sn\_customerservice\_agent role
    
3.  Create a new list in Agent Workspace to create a new user (Consumer User).
    
      
    1.  Navigate to **Workspace Experience > Administration > All Workspaces**.
        
    2.  Open the Agent Workspace record
        
    3.  In the Workspace lists related list, click **New**.
        
    4.  In the List name field, enter **Consumer Users.**
        
    5.  Set the Category value to **Customer**
        
    6.  Set the Table value to **Consumer user (csm\_consumer\_user)**
        
    7.  In the Roles field, add sn\_vaccine\_sm.clinician.
        
    8.  Select the **Active** check box.
        
    9.  Choose the fields you want displayed.
        
    10.  Click **Submit** to create the record.
         
    11.  Configure the form layout for **Consumer user (csm\_consumer\_user)** in Agent Workspace to add the Email, First Name, and Last Name field.
         
         For more information, see [Configuring the form layout](https://staging-docs-servicenow.zoominsoftware.io/bundle/quebec-platform-administration/page/administer/form-administration/concept/configure-form-layout.html).  
           
         
4.  Set up a new UI action for booking appointments.
    
    For more information about creating a UI action, see [Set up custom UI actions in Workspace](https://staging-docs-servicenow.zoominsoftware.io/bundle/quebec-servicenow-platform/page/administer/workspace/task/configure-agent-workspace-ui-actions.html).
    
      
    1.  Create a new UI action named **Book Appointment**.
        
    2.  Select a table from the **Vaccination Request** (sn\_vaccine\_sm\_request) field.
        
    3.  Select the **Active** check box.
        
    4.  Select the **Show update** check box.
        
    5.  Select the **Form button** check box.
        
    6.  In the **Condition** field, enter:
        
        current.state=='10' || current.state=='20' || current.state=='30'
        
    7.  In the **Script** field, enter the following code:
        
        ```
        if (current.state=='30')
        { current.state='20'; 
        current.update(); } 
        new sn_vaccine_sm.VaccineService().enrollForDosages(current.sys_id);
        ```
        
    8.  Select the **Workspace Form button** check box.
        
    9.  Click **Submit**.
        

## Managing user appointments as a customer service agent

**Before you begin**

Roles required: sn\_customerservice\_agent, sn\_vaccine\_sm.clinician, and user.admin

**Procedure**

1.  Create a consumer user on behalf of a user from the Vaccine Administration Management Agent Workspace.
    
      
    1.  Log in as a customer service agent.
        
    2.  Navigate to **Vaccine Administration Management > Vaccine Administration Management Workspace**.
        
    3.  On the Lists tab, navigate to **Customer > Consumer Users**.
        
    4.  Click **New**.
        
    5.  On the Create New Consumer User form, fill in the fields.
        
    6.  Click **Save**.
        
        A new information record for the user is created.
        
2.  Book an appointment from the Vaccine Administration Management Agent Workspace.
    
      
    1.  On the Lists tab, navigate to **Vaccination Request > All**.
        
    2.  Click **New**.
        
    3.  In the Create New Vaccination Request > Vaccination Request section, select the consumer record in the **Opened For** field.
        
    4.  Fill in the **Program**, **Preferred Center**, and **Location** fields.
        
        If any field is not available, configure the Workspace form layout to add the field. For more information about configuring the form layout, see [Configuring the form layout](https://staging-docs-servicenow.zoominsoftware.io/bundle/quebec-platform-administration/page/administer/form-administration/concept/configure-form-layout.html).
        
    5.  Ensure that the Preferred Center and Location fields have the same value.
        
    6.  In the Pre-Vaccine Questionnaire section, enter the details for the user.
        
    7.  Click **Save**.
        
          
        
        -   If the sn\_vaccine\_sm.enable\_appointment\_slot\_choice property is set to false, the appointment is automatically booked.
            
        -   If the sn\_vaccine\_sm.enable\_appointment\_slot\_choice property is set to true, click **Book Appointment**.
            
        
        The vaccination request, vaccination tasks, and appointments are created for the user. A QR code with the appointment confirmation and appointment details is sent via email to the user.
        
    8.  Assign the sn\_vaccine\_sm.user role to users who need to log in to the Vaccine Administration Management portal.
        
        For more information about adding a role, see [Assign a role to a user](https://docs.servicenow.com/bundle/quebec-platform-administration/page/administer/users-and-groups/task/t_AssignARoleToAUser.html).
        
3.  (Optional) Cancel an appointment from the Vaccine Administration Management Agent Workspace.
    
      
    1.  On the Lists tab, navigate to **Vaccination Task > All**.
        
    2.  Open the vaccination tasks for the user.
        
    3.  Click **Cancel Appointment**.
        
        If the appointment on the first task is cancelled, both appointments are cancelled. The second appointment cannot be cancelled independently.
        
4.  (Optional) Reschedule an appointment from the Vaccine Administration Management Agent Workspace.
    
      
    1.  On the Lists tab, navigate to **Vaccination Task > All**.
        
    2.  Open the vaccination tasks for the user.
        
    3.  Click **Cancel Appointment**.
    4.  Navigate to **Vaccination Requests > All** and open the vaccination request.
        
    5.  Click **Book Appointment** and reschedule the appointment.
