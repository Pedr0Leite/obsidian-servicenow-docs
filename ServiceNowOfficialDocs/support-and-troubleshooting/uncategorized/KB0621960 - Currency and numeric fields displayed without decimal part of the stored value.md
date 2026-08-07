---
title: "Currency and numeric fields displayed without decimal part of the stored value"
aliases:
  - KB0621960
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621960
kb_number: KB0621960
last_modified: 2024-04-07
---

## Currency and numeric fields displayed without decimal part of the stored value

  

### Issue

Currency and numeric fields are displayed without the decimal part of their value

Symptoms  

* * *

All values for numeric fields (decimal fields, currency, price) are displaying a truncated value for the decimal part. Though the values are stored in the database correctly with decimal values, on the UI (anywhere in the ServiceNow application), the decimal part is not displayed for decimal fields. For currency and price fields, the decimal part shows as **,00**. The values are not rounded (based on the decimal value in the database); the decimal value is just truncated from the value.  

![showing the issue in a test table](sys_attachment.do?sys_id=8e6a2466db42b450e515c223059619ed "showing the issue in a test table")  
  
When using **show XML** on a record to see the values retrieved from the database, the decimal values are also not there.

Cause

* * *

This issue is likely to occur on self-hosted instances only, using an Operating System installed in non-US English.  
In the database, the values are stored correctly with decimal values, using the (**.**) as the decimal point:  
 

<table class="internalTable" style="width: 1047.27px;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>u_decimal</strong></td><td style="vertical-align: middle; text-align: left;"><strong>u_currency</strong></td><td style="vertical-align: middle; text-align: left;"><strong>u_price</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">53.50</td><td style="vertical-align: middle; text-align: left;">53.50</td><td style="vertical-align: middle; text-align: left;">53.50</td></tr></tbody></table>

  
However, the application servers (nodes) are started with a user that has the **$LANG** environment variable set to a locale that uses a comma (**,**) for the decimal point.   
For example:   

```
$ echo $LANGfr_FR.UTF-8
```

When the application nodes are started by that user (using /glide/bin/glide.sh or /glide/nodes/<instance\_port>/startup.sh), it expects comma values for decimal points, which it does not receive from the database (as that sends '**.**'). As a result, the part after the decimal point is ignored and the value is displayed as truncated for decimal fields, with zeros for the decimal part of currency and price fields.

Resolution

* * *

Before starting the application nodes, ensure the language variable (**LANG**) is set to a value that uses (**.**) for decimal points.  
For example, for an instance called labinst, running on port 16000:  
  

```
$ set LANG='en_US.UTF-8'----- or (depending on OS) -----$ export LANG='en_US.UTF-8'$ echo $LANGen_US.UTF-8$ /glide/bin/glide.sh startStarting glide software: - node: Starting labinst_16000Cleaning local tmp: /glide/nodes/labinst_16000/tmpStarting Glide (labinst_16000)...
```

  
The locale settings used for displaying data in the application are determined by the glide.system.locale system property. If that is set to a locale that uses a decimal point as comma (For example, **fr.FR**), then the users see a comma instead of a decimal point, even though the database stores a decimal point.  
  
At user level, the system property can be overridden by the country (and language) in the sys\_user record. That determines how numeric values are displayed.  
  
Starting the nodes with the modified LANG variable displays new and existing values for numeric fields containing decimal values correctly, as they were stored in the database with decimal values.  
  
When re-queried, newly entered records display correctly:  
  
![](sys_attachment.do?sys_id=126a2466db42b450e515c223059619f8) 

<table class="noteTable" style="width: 1047.27px;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Note" src="/Note_25x.pngx" align="baseline" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: For currency and price fields, the display value for existing records (entered when the application nodes were started with the invalid LANG setting) still show as <strong>,00</strong>:</td></tr></tbody></table>

 ![currency and price values not correct yet](sys_attachment.do?sys_id=9e6a6466db42b450e515c2230596190d "currency and price values not correct yet")

For displaying values in the application for currency and price fields, the values are not read from the base table, but from tables **fx\_currency\_instance** (for currency fields) and **fx\_price** (for price fields) (which reference the base table, record and field). That allows the application to deal with multiple currencies. The values are stored without decimal places (saved when they were created when the application servers were started in french). New records created after the variable change are stored there with decimal values.

Updating the values manually in the form updates them in the database and they display correctly when queried. Alternatively, a datafix script is required to modify existing values in **fx\_currency** and **fx\_price**. They have a reference to the base table, record and field which has the correct value in the reference currency. In a single currency instance, this is the same as the currency used in **fx\_currency\_instance** and **fx\_price**. In a multi currency instance, conversion would be required.
