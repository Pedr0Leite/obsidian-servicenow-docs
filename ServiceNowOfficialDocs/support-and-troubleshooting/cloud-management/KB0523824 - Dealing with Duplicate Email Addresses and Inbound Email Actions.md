---
title: "Dealing with Duplicate Email Addresses and Inbound Email Actions"
aliases:
  - KB0523824
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523824
kb_number: KB0523824
last_modified: 2023-12-15
---

## Issue

Sometimes, over the course of a ServiceNow instance lifespan, data can get messy.  One of the ways this presents itself is through multiple ServiceNow accounts being created for the same person, and one of the places this can cause an issue is when that user attempts to use email to submit a new Ticket.  If there are multiple matching Users for an email address, ServiceNow will simply use the first one it comes to, which may be the wrong one.  This solution provides a method to alert that user to the existence of multiple accounts and, subsequently, to ask them to eliminate their redundant accounts.

**NOTE: Please be aware that the method described below is a customisation and hence it will be out of scope of support should any issues arises from its implementation**

**Detailed Explanation**

This method intercepts inbound emails and checks for the existence of multiple active accounts for that email address.  If multiple accounts are found, it halts record creation and generates a notification to the user asking that they log into the instance to submit their record and contact the Help Desk to clean up the erroneous accounts.

**Steps to Implement**  

1.  Create a script include called 'u\_isDupeEmail' with the following script:  
    
    _function u\_isDupeEmail(emailAddy){_  
       _var gr = new GlideAggregate('sys\_user');_  
       _gr.addQuery('active', true);_  
       _gr.addQuery('email', emailAddy);_  
       _gr.addAggregate('COUNT');_  
       _gr.query();_  
       _var numEmail = 0;_  
       _if (gr.next()){_  
          _numEmail = gr.getAggregate('COUNT');_  
       _}_  
       _if (numEmail > 1) {_  
          _return true;_  
       _}_  
       _return false;_  
    _}_
    
2.  In the Registry, create a new event called '**user.duplicate.emails**' on the sys\_user table.
3.  Create a new notification called **'User multiple accounts on the 'Incident'** table with the following specifications:
    1.  When to send: '**Event is fired' - 'user.duplicate.emails**'
    2.  Who will receive: **'Event parm 1 contains recipient**'
    3.  What it will contain:
4.  Create a new Inbound Email Action configured as follows.  This particular implementation also creates an audit record in the '**u\_duplicate\_email\_record**' table.  This is not a necessary addition, but may be useful to help track active users with multiple accounts:![](/sys_attachment.do?sys_id=c36d5a3a974f31908a073cbe2153afc1)
