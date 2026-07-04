---
title: "Error importing data directly from one instance to another via XML data source."
aliases:
  - KB0550021
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0550021
kb_number: KB0550021
last_modified: 2024-04-07
---

## Error importing data directly from one instance to another via XML data source.

  

### Issue

Error importing data directly from one instance to another through XML data source  
  

Problem

* * *

When importing data directly from one instance to another instance via XML data source sometimes an error occurs: _The current node has been removed using a method other than Iterator#remove()_ in the progress page.

Symptoms

* * *

After executing the data source, in the progress page you can see the following:

-   The state is **complete** and completion code is **Error** with the message: _The current node has been removed using a method other than Iterator#remove()_
-   In the local host logs the following stack trace appears:
-   ImportProcessor SYSTEM SEVERE \*\*\* ERROR \*\*\* com.glide.db.impex.XMLLoader   
    java.util.ConcurrentModificationException: The current node has been removed using a method other than Iterator#remove()   
    at org.apache.axiom.om.impl.traverse.OMAbstractIterator.hasNext(OMAbstractIterator.java:67)   
    at org.jaxen.util.DescendantAxisIterator.hasNext(DescendantAxisIterator.java:101)   
    at com.glide.xpath.GlideStep$GlideStepImpl.nextFromIterator(GlideStep.java:80)   
    at com.glide.xpath.GlideAllNodeStep.nextFromIterator(GlideAllNodeStep.java:49)   
    at com.glide.xpath.GlideXPath.selectNextNode(GlideXPath.java:118)   
    at com.glide.util.XMLStreamDocument.selectNextNode(XMLStreamDocument.java:284)   
    at com.glide.db.impex.XMLLoader.next(XMLLoader.java:175)   
    at com.glide.db.impex.XMLLoader.getColumnAttributes(XMLLoader.java:291)   
    at com.glide.db.impex.AbstractLoader.createTableFromImportData(AbstractLoader.java:375)  
      
    

Cause

* * *

The problem seems to be triggered when both element and its attribute are named similar. In other words, whenever a table and its field has the same name, this issue happens when import is performed through the xml datasource from one instance to another.

For example, **https://xxxx.service-now.com/u\_sar\_item.do?XML**

<xml>   
<u\_sar\_item> -----------------------------------------------------------------------------> Element name   
<sys\_created\_by>NORMOYS</sys\_created\_by>   
<sys\_created\_on>2015-05-07 15:31:54</sys\_created\_on>   
<sys\_id>0f5844cf9973310001ccc5dc7b0dd344</sys\_id>   
<sys\_mod\_count>0</sys\_mod\_count>   
<sys\_updated\_by>NORMOYS</sys\_updated\_by>   
<sys\_updated\_on>2015-05-07 15:31:54</sys\_updated\_on>   
<u\_association/>   
<u\_item\_display>Business Central OLB</u\_item\_display>   
<u\_sar\_item>ce88fdfaa467b5009a24c1eea0d7430c</u\_sar\_item> ------>Attribute with the same name as element.   
<u\_task\_approvers/>   
<u\_task\_instructions/>   
</u\_sar\_item>   

 u\_sar\_item is the table name, and it also has a field named u\_sar\_item.  
  

  
Resolution

* * *

Rename either the element/table or the attribute/field so that the names do not match.
