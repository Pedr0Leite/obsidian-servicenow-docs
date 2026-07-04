---
title: "How to make a record producer and catalog item public on a CMS page"
aliases:
  - KB0551300
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551300
kb_number: KB0551300
last_modified: 2025-02-25
---

## How to make a record producer and catalog item public on a CMS page

  

### Issue

It is common for users to request that record producers and catalog items be made public on the Content Management System. Since Service Now locks everything down, it can be difficult to make this work. Here are the steps based on the base system ESS Portal. Before the administrator proceeds with the steps below, it is required to have elevated security privileges and to check the access control rules allowing on the \[sc\_cat\_item\] table and fields.

### Solution

#### 1\. Make the CMS public

The first thing you need to do is make your CMS public. To do this make the **Login Page** field blank on your site.

![](/sys_attachment.do?sys_id=72eca422db82b450e515c2230596199f)

 **Note:** If you notice that certain blocks are not rendering, check the block and make sure the **logged in** check box is not checked.

#### 2\. Public Page

UI Pages by default require a login. We can change this by [making them public](https://docs.servicenow.com/csh?topicname=t_MakeAPagePublic.html&version=latest). Go to the \[sys\_public\] table and add these to the UI Page:

-   com.glideapp.servicecatalog\_cat\_item\_view
-   com.glideapp.servicecatalog\_category\_view
-   item\_option\_new
-   question
-   service\_catalog

If you have another page that requires a login, check the URL and the page ending in .do. Add this to the **Public Pages**.

Post Kingston, you need to add a **public** role to **service\_catalog** processor.

You also might have a page in an iframe where the main layout renders, but the content in the iframe is requesting a login. To fix this, use the browser’s developer tool and select the iframe. You should see something like this.

<iframe width="100%" height="1484" frameborder="0" border="0" src="com.glideapp.servicecatalog\_category\_view.do?sysparm\_nameofstack=1b5cea177bc2020026ef707d784d4d0a&amp;sysparm\_parent=d258b953c611227a0146101fb1be7c31&amp;sysparm\_clear\_stack=yes" allowtransparency="true" name="gsft\_main" scrolling="no" id="gsft\_main"></iframe><

Look for the part with the src, just like the URL, you will want to make the.do public.

#### 3\. Making the Catalog Item public

To make a Catalog Item/Record Producer public, make both the **item** and the **variables** **public**.

-   To make the item public, create a **User Criteri**a with **Public** Role. Use **Catalog Item** to be available for this public **User Criteria**. Make sure there is no user criteria in the **Not Available For** section.  
    If you have glide.sc.use\_user\_criteria to **false,** make sure the **roles** field is on the form and add the **public** role to it. Using entitlement is a deprecated behavior of securing **Catalog Item** from Fuji and should be avoided.  
      
    
-   Set two step check out to false. (glide.sc.checkout.twostep = false).   
      
    
-   To make the variables public, add **Write**, **Read**, and **Create** roles to the related list.

![](/sys_attachment.do?sys_id=beeca422db82b450e515c223059619bb)

### Related Links

This should make most variables public. There are a few exceptions.

1.  **Checkbox** cannot be made public. Instead, use a Yes/No variable or Lookup Select Box with two options.
2.  Variables that reference other tables will require further work. **List Collectors** will not work. **References** will require read ACLs with the public role and tablename\_list added to sys\_public (reference icon will work, autocomplete will not). **Lookup Select Boxes** that reference another table will require read ACLs with the public role.

 **Note:** As a side effect of making service catalog public, if the session of an authenticated user expires before checkout, the subsequent request and requested item records are created with user fields as "Guest".
