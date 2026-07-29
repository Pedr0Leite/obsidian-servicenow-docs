---
title: "Classic Mobile UI limitations"
aliases:
  - KB0551212
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551212
kb_number: KB0551212
last_modified: 2024-04-07
---

## Classic Mobile UI limitations

  

### Issue

Compared to the Desktop UI, the Mobile UI allows less user customization. In the following section, you can view the different customizations that are supported and not supported by the Mobile UI.

### Resolution

The supported features of Mobile UI are:

-   Personal favorites and tags
-   Order of Home sections
-   Client-side scripts
    -   Client scripts
    -   UI Policies
    -   Catalog Client scripts
    -   Catalog UI Policies

-   UI Actions
    -   List button (attached to the record in the list)
    -   Form button
    -   Form more item
-   Directing UI actions to external links (in a new tab only)
-   Unique view of list and form
-   Unique customization of Catalog items and categories

For more available customizations of the Mobile UI, on your instance, go to **System Properties > Mobile UI Properties**. 

The unsupported features of Mobile UI are:

-   Adding new sections to the homepage
-   UI Actions on the list header
-   Changing the CSS of the UI (font size, icons size, margins, etc.)
-   Directing modules or favorites to external links
-   Customizing the auto-complete attributes on a reference field

Other base system elements/features which are not supported on the Mobile UI (taken from product documentation):

-   [HTML fields](https://docs.servicenow.com/csh?topicname=c_UseHTMLFields.html&version=latest "Using HTML Fields")
-   [Live Feed](https://docs.servicenow.com/csh?topicname=c_GetStartedWithLiveFeed.html&version=latest "Live Feed")
-   Switching to the standard browser interface from the smartphone interface
-   [Interceptors](https://docs.servicenow.com/ "Legacy: Using an Interceptor to Gather Data for a New Record")
-   These [variable types](https://docs.servicenow.com/csh?topicname=r_VariableTypes.html&version=latest "Variable Types"):
    -   Macro With Label
    -   UI Page
    -   List Collector
    -   HTML
    -   Macro
    -   Label
    -   Break
-   [Data lookup rules](https://docs.servicenow.com/csh?topicname=t_DataLookupRule.html&version=latest "Data Lookup and Record Matching Support")
