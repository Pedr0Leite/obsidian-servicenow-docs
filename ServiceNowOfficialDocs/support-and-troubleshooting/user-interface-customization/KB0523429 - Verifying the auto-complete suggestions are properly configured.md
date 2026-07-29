---
title: "Verifying the auto-complete suggestions are properly configured"
aliases:
  - KB0523429
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523429
kb_number: KB0523429
last_modified: 2025-01-26
---

## Verifying the auto-complete suggestions are properly configured

  

### Issue

Verifying the auto-complete suggestions are properly configured

Overview

* * *

The system dictionary is a table, called Dictionary Entries \[sys\_dictionary\], that contains details for each table in an instance. Administrators can make changes to the system dictionary that will affect functionality. The system dictionary provides customization options for tables and fields, which in turn define lists and forms. However, there are simpler user interfaces that can be used for common tasks, such as creating new tables and fields, rather than modifying the system dictionary directly. 

If the dictionary entry is not appropriately configured, it can cause several unexpected behaviors on a form, such as the auto-compete suggestion not working in a reference field. When troubleshooting field behavior, an important field to consider is Attributes. This field alters the behavior of a field or functionality that depends on the field. The attribute that corresponds to the auto-complete functionality is **ref\_auto\_completer**. This dictionary attribute specifies the name of a JavaScript class (client side) that creates the auto completion choice list. Valid class values are AJAX ReferenceCompleter, AJAXTableCompleter, and AJAXReferenceChoice.  

Procedure

* * *

To verify that the auto-complete suggestions on a reference field are properly configured:

1.  Navigate to the form that is experiencing unexpected reference field behavior.
2.  Right-click on the field label and select **Personalize Dictionary**. Alternatively, navigate to **System Definition > Dictionary** to view the system dictionary as a list and open a dictionary entry for a field or table. The dictionary form appears.
3.  Verify the data in the dictionary entry form for the broken reference field. For details on each of the fields that appear in the system dictionary, refer to [Modify Dictionary Entries](https://docs.servicenow.com/csh?topicname=t_ModifyADictionaryEntryFromAForm.html&version=latest "Modify Dictionary Entries").
4.  Fields that influence the auto-complete suggestions are: 
    
    <table class="internalTable" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;" width="30%"><strong>Field</strong></td><td style="vertical-align: middle; text-align: left;" width="70%"><strong>Description</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Type</td><td style="vertical-align: middle; text-align: left;">Defines the field type of the column.</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Max length</td><td style="vertical-align: middle; text-align: left;">Limits the length of a field.</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Reference</td><td style="vertical-align: middle; text-align: left;">Defines the table being referenced.</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Attributes</td><td style="vertical-align: middle; text-align: left;">Alters the behavior of a field or functionality that depends on the field. For details on&nbsp;auto-complete attributes for fields in a table that do not already have their own auto-complete attributes,&nbsp;see <a title="Auto-complete for reference fields" href="https://docs.servicenow.com/search?labels=3&amp;q=auto-complete+attribute" target="_blank" rel="noopener noreferrer nofollow">Auto-complete for reference fields</a>.</td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">Reference qual</td><td style="vertical-align: middle; text-align: left;">Filters the records available for a reference field.&nbsp;</td></tr></tbody></table>
    
    **  
    Note**: If there is a similar or same field on another form that is working, compare the two dictionary entries and make the necessary changes to make them consistent.
    
    After the necessary changes are made to the dictionary entry, click **Update** and test the auto-complete suggestions to verify the issue no longer exists.

<table class="noteTable" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: For details on configuring additional auto-complete options,&nbsp;see&nbsp;<a title="Auto-Complete for Reference Fields" href="https://docs.servicenow.com/search?labels=3&amp;q=auto-complete+attribute" target="_blank" rel="noopener noreferrer nofollow">Auto-complete for reference fields</a>.&nbsp;</td></tr></tbody></table>
