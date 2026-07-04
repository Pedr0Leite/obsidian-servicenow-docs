---
title: "Currencies in the ServiceNow Platform"
aliases:
  - KB0550644
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550644
kb_number: KB0550644
last_modified: 2025-04-09
---

## Issue

The purpose of this document is to present the technical foundations of currencies and increase awareness to avoid generation of incidents or problems due to misunderstandings.

## Resolution

**Muti Currency Model**

* * *

Gives the user the option to select the currency in a drop-down on a **Currency** field. The values of the drop-down are retrieved from the active entries in the **fx\_currency** table.

![](/sys_attachment.do?sys_id=daeb9d6e1b768114ed6c9979b04bcbc4)

The user entry is mapped to fx\_currency\_instance.amount and fx\_currency\_instance.currency

-   This is not the reference amount/currency
-   These fields are used for the conversion

![](/sys_attachment.do?sys_id=02eb9d6e1b768114ed6c9979b04bcb88)

The base currency (set by the **glide.system.locale** property) is the reference currency (_fx\_currency\_instance.reference\_currency_). If the property is not set it will default to USD ($).

   
  

**Single Currency Model**

* * *

Hides the currency drop-down option on the Currency field. The **glide.i18n.single\_currency.code** property sets the display currency when users are populating the Currency field.

![](/sys_attachment.do?sys_id=9eeb9d6e1b768114ed6c9979b04bcb90)

We are still using GlideLocale (referring to the **glide.system.locale** property) in the _fx\_currency\_instance_ records. So this should match with the single currency code (the **glide.i18n.single\_currency** property). If the two properties do not match, the system will behaves unexpectedly, showing inconsistencies on currency fields while searching, sorting, or performing calculations.

**Can we delete fx\_currency\_instance records?**

* * *

When deleting these records, they will get regenerated using the referenced record's value for that Currency field(s). So this can be done while using the Single Currency Model, as the instance is only using the one correct set for currency.

Whereas, when using the multi-currency model, we should not be deleting it as the _fx\_currency\_instance_ record is used to store the currency selected by the user when populating/updating the associated record. So when the record is re-created it could be using a value intended for another currency (e.g. GBP), but treating it as the base currency (e.g. USD) for the conversion, which will throw things off.

  
  

**Switching to the Single Currency Model**

* * *

Instances are using the Multi Currency Model OOB, so there would be administrators who do not need that setting, but could not necessarily be aware the Single Currency Model is not OOB.

It is best practice to setup the correct model and locale among the initial configuration of the instance. However, there is the possibility that this was missed out and only realized at a later stage.

Just setting the **glide.i18n.single\_currency** property to **true** can lead to spurious results as indicated in the previous section.

When moving to the Single Currency Model, you should follow these (high level) guidelines:

1.  Make sure there are no records left over where the currency does not match the target currency that the customer would like to switch to.
2.  Set the **glide.system.locale** property to the target currency.
3.  Set the **glide.i18n.single\_currency.code** property to the target currency.
4.  Set the **glide.i18n.single\_currency** property to **true**.

  
  

**Testing/Scripting Currency Values**

* * *

Best practice for the scripting is to use getSessionValue and getReferenceValue.

<table><tbody><tr><td><pre style="margin: 0px; line-height: 125%;"> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11</pre></td><td><pre style="margin: 0px; line-height: 125%;"><span style="color: #008800; font-style: italic;">//session.onlineImpersonate('uk.admin');</span>

<span style="color: #000080; font-weight: bold;">var</span> gr = <span style="color: #000080; font-weight: bold;">new</span> GlideRecord(<span style="color: #0000ff;">'alm_asset'</span>);
<span style="color: #000080; font-weight: bold;">if</span> (gr.get(<span style="color: #0000ff;">'00a96c0d3790200044e0bfc8bcbe5dc3'</span>)) {
  gs.print(gr.cost); <span style="color: #008800; font-style: italic;">// getting value from database</span>
  gs.print(gr.cost.getSessionValue()); <span style="color: #008800; font-style: italic;">// getting value based on user's session/locale</span>
  gs.print(gr.cost.getReferenceValue()); <span style="color: #008800; font-style: italic;">// getting value from fx_currency_instance table</span>
  gs.print(gr.cost.getDisplayValue());
}

<span style="color: #008800; font-style: italic;">//session.onlineUnimpersonate();</span>
</pre></td></tr></tbody></table>

## Additional Information

How to use different currencies on an instance: [KB0596448](https://hi.service-now.com/kb_view.do?sysparm_article=KB0596448 "KB0596448")
