---
title: "Control roles available in CSM Portal User Management for Customer Admins"
aliases:
  - KB0690035
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690035
kb_number: KB0690035
last_modified: 2025-01-07
---

## Issue

# Description

* * *

You can control what roles are available from the slushbucket in the Customer Service User Management interface via specifying the available roles in the system property "sn\_customerservice.contact\_role\_assignment".

You will need a slight code modification to ensure this is honoured in the Service Portal interface for Customer Service Management.

# Procedure

* * *

1) Find "sn\_customerservice.contact\_role\_assignment" property and remove the "sn\_customerservice.customer" from it

https://<instance>.service-now.com/sys\_properties\_list.do?sysparm\_query=nameSTARTSWITHsn\_customerservice.contact\_role\_assignment

2) Find the SP widget "Contact Roles" - sp\_widget\_c22de8e8c302120058879f2974d3ae02.xml

https://<instance>.service-now.com/sp\_widget\_list.do?sysparm\_query=nameSTARTSWITHContact%20Roles

3) Change the Server script code lines 27 - 37 from the below original code:

    //read roles
    var gr = new GlideRecord('sys\_user\_has\_role');
    gr.addQuery('user', contact.getUniqueValue());
    gr.addQuery('inherited', false);
    gr.query();
    var roles = \[\];
    while(gr.next()) {
        var role = gr.getDisplayValue('role');
        if (!gs.nil(role))
            roles.push(role);
    }

to the following:

    //read roles
    var gr = new GlideRecord('sys\_user\_has\_role');
    gr.addQuery('user', contact.getUniqueValue());
    gr.addQuery('inherited', false);
    gr.query();
    var roles = \[\];
    while(gr.next()) {
        var role = gr.getDisplayValue('role');
        if (!gs.nil(role)){
            //To honor the sys property about editable roles
            var availableRoles = gs.getProperty('sn\_customerservice.contact\_role\_assignment','');
            availableRoles = availableRoles.split(',');
            if (availableRoles.indexOf(role) != -1)
                roles.push(role);
        }
    }

This forces the role slushbucket to honour the "sn\_customerservice.contact\_role\_assignment" property which controls what roles are exposed to customer\_admin. 

# Applicable Versions

* * *

All releases with Customer Service Management plugin installed.
