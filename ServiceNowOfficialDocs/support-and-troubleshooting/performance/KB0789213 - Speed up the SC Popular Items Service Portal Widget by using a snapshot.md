---
title: "Speed up the \"SC Popular Items\" Service Portal Widget by using a snapshot"
aliases:
  - KB0789213
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789213
kb_number: KB0789213
last_modified: 2026-05-01
---

## Text

### Symptoms

When users navigate to the Service Catalog home page in the Service Portal, one of the widgets that they will see by default is the "Popular Items" widget.

This widget will show the most popular "Catalog Item" \[sc\_cat\_item\] records.  Popularity is based on the count of related "Requested Item" \[sc\_req\_item\] records created from those catalog items.

As the number of Requested Item records increases, the cost of calculating the top popular items becomes more expensive.

This causes expensive queries in the database.

This increases the response time of the widget / portal page. 

This can also impact semaphore usage/contention and even lead to semaphore exhaustion.

### Cause

This issue is documented in the following known problem:

PRB1386320  
Out-of-the-box "SC Popular Items" sc-popular-items widget causes excessive queries

Which is documented in the following KB:

[KB0821439](/kb_view.do?sysparm_article=KB0821439 "KB0821439")  
Out-of-the-box sc-popular-items widget causes excessive queries

The slowness is due to the expensive **aggregation** in the widget server script. 

The New York version of this widget has the following code:

var items = \[\];  
  
var count = new GlideAggregate('sc\_req\_item');  
count.addAggregate('COUNT','cat\_item');  
count.groupBy('cat\_item');  
count.addQuery('cat\_item.sys\_class\_name', 'NOT IN', 'sc\_cat\_item\_guide,sc\_cat\_item\_wizard,sc\_cat\_item\_content');  
count.addQuery('cat\_item.sc\_catalogs', 'IN', data.sc\_catalog);  
count.addQuery('cat\_item.visible\_standalone','true');  
count.addEncodedQuery('cat\_item.hide\_sp=false^ORcat\_item.hide\_spISEMPTY');  
count.orderByAggregate('COUNT', 'cat\_item');  
count.query();  
while (count.next() && items.length < data.limit) {  
if (!$sp.canReadRecord("sc\_cat\_item", count.cat\_item.sys\_id.getDisplayValue()))  
continue; // user does not have permission to see this item  
  
var item = {};  
item.count = 0 - count.getAggregate('COUNT', 'cat\_item');  
item.name = count.cat\_item.name.getDisplayValue();  
item.short\_description = count.cat\_item.short\_description.getDisplayValue();  
item.picture = count.cat\_item.picture.getDisplayValue();  
item.price = count.cat\_item.price.getDisplayValue();  
item.hasPrice = count.cat\_item.price != 0;  
item.sys\_id = count.cat\_item.sys\_id.getDisplayValue();  
items.push(item);  
}

This code generates a query similar to the following:

SQL06:59:34.474: Time: 0:00:05.171 for: myinstance\_1\[glide.10\] SELECT ... 
FROM ((task task0 LEFT JOIN sc\_cat\_item sc\_cat\_item1 ON task0.\`a\_ref\_1\` = sc\_cat\_item1.\`sys\_id\` ) LEFT JOIN sys\_metadata sys\_metadata2 ON sc\_cat\_item1.\`sys\_id\` = sys\_metadata2.\`sys\_id\` ) 
WHERE task0.\`sys\_class\_name\` = 'sc\_req\_item' AND sys\_metadata2.\`sys\_class\_name\` NOT IN ('sc\_cat\_item\_guide' , 'sc\_cat\_item\_wizard' , 'sc\_cat\_item\_content') 
AND sc\_cat\_item1.\`sc\_catalogs\` = 'e0d08b13c3330111c8b837659bba8fb4' AND (sc\_cat\_item1.\`hide\_sp\` = 0 OR sc\_cat\_item1.\`hide\_sp\` IS NULL ) 
GROUP BY task0.\`a\_ref\_1\`,sc\_cat\_item1.\`name\` 
ORDER BY count\_of\_45033948 DESC ,sc\_cat\_item1.\`name\` /\*...\*/

The full query looks like this:

SELECT task0.\`a\_ref\_1\` AS \`cat\_item\`, count(\*) AS count\_of\_45033948
FROM ((task task0 LEFT JOIN sc\_cat\_item sc\_cat\_item1 ON task0.\`a\_ref\_1\` = sc\_cat\_item1.\`sys\_id\` ) LEFT JOIN sys\_metadata sys\_metadata2 ON sc\_cat\_item1.\`sys\_id\` = sys\_metadata2.\`sys\_id\` ) 
WHERE task0.\`sys\_class\_name\` = 'sc\_req\_item' AND sys\_metadata2.\`sys\_class\_name\` NOT IN ('sc\_cat\_item\_guide' , 'sc\_cat\_item\_wizard' , 'sc\_cat\_item\_content') 
AND sc\_cat\_item1.\`sc\_catalogs\` = 'e0d08b13c3330111c8b837659bba8fb4' AND (sc\_cat\_item1.\`hide\_sp\` = 0 OR sc\_cat\_item1.\`hide\_sp\` IS NULL ) 
GROUP BY task0.\`a\_ref\_1\`,sc\_cat\_item1.\`name\` 
ORDER BY count\_of\_45033948 DESC ,sc\_cat\_item1.\`name\`

The query performs an aggregation (GROUP BY cat\_item) to get the count of records for each catalog item in the current catalog.

### Resolution

The widget is slow because of the slow query.  The query is slow because it's reading a lot of data from the Requested Items table and aggregating the count.

One solution for this slow widget is to defer the expensive aggregation of the Requested Items table to a scheduled job that would perform the expensive aggregation and save a snapshot of the results in a table, and modifying the widget to query the snapshot.

This solution is valid if the ranking of popular items does not change significantly enough to warrant every end user from performing this calculation.

In general, the steps to resolve this are:

1) Create a user-defined table to store the results of the snapshot.

2) Create a scheduled job to periodically refresh the snapshot.

3) Clone the SC Popular Items and modify the Server script of the new widget to query the snapshot table.

4) Modify any an all Instances of the SC Popular Items widget to the new widget.

Here are more detailed steps:

1) Create a user-defined table to store the results of the snapshot:

a) Navigate to the System Definition > Tables module.

b) Click on the "New" button.

c) Enter the following information:

Label: Popular Items

Name: u\_popular\_items

d) Uncheck the "Create module" checkbox.

e) Click on the Additional actions > Save context menu item.

f) Add the following Table Columns to the table:

Column label: Catalog Item

Column name: u\_sc\_cat\_item

Type: Reference

Reference: Catalog Item \[sc\_cat\_item\]

g) Add the following Table Column to the table:

Column label: Count

Column name: u\_count

Type: Integer

Max length: 40

h) Click on the Additional actions > Save context menu item.

![](/sys_attachment.do?sys_id=7dea92a5471b6610bb78d9d8736d43d2)

2) Create a scheduled job to periodically refresh the snapshot:

a) Navigate to the System Definition > Scheduled Jobs module.

b) Click on the "New" button.

c) Click on the "Automatically run a script of your choosing" link.

d) Enter the following Information:

Name: Refresh Popular Items Snapshot

Run: Daily \*

Time: 00:00:00 \*

Run this script:

// Start of Script  
  
truncateSnapshot();  
refreshSnapshot();  
  
function truncateSnapshot() {  
    new GlideTableCleaner('u\_popular\_items', 1, 'sys\_created\_on').clean();  
}  
  
function refreshSnapshot() {  
  var gaReqItem = new GlideAggregate('sc\_req\_item');  
  gaReqItem.addAggregate('COUNT', 'cat\_item');  
  gaReqItem.groupBy('cat\_item');  
  gaReqItem.addQuery('cat\_item.sys\_class\_name', 'NOT IN', 'sc\_cat\_item\_guide,sc\_cat\_item\_wizard,sc\_cat\_item\_content');  
  //gaReqItem.addQuery('cat\_item.sc\_catalogs', 'IN', data.sc\_catalog);  
  gaReqItem.addQuery('cat\_item.visible\_standalone', 'true');  
  gaReqItem.addEncodedQuery('cat\_item.hide\_sp=false^ORcat\_item.hide\_spISEMPTY');  
  gaReqItem.orderByAggregate('COUNT', 'cat\_item');  
  gaReqItem.query();  
  while (gaReqItem.next()) {  
    var gr = new GlideRecord('u\_popular\_items');  
    gr.initialize();  
    gr.u\_sc\_cat\_item = gaReqItem.cat\_item;  
    gr.u\_count = gaReqItem.getAggregate('COUNT', 'cat\_item');  
    gr.insert();  
  }  
}  
  
// End of Script

Although Daily at midnight may be sufficient for some cases, you might consider altering the Run schedule per your specific needs. The more often you run the job, the more up-to-date the snapshot will be.

e) Click on the Additional actions > Save context menu item.

f) Click on the "Execute Now" button.

![](/sys_attachment.do?sys_id=bdea92a5471b6610bb78d9d8736d43ce)

3) Create the alternative Service Portal Widget:

a) Navigate to the Service Portal > Widgets module.

b) Search for the "SC Popular Items" widget and open the form.

c) Click on the "Clone Widget" button.

d) Change the Name field from "Copy of SC Popular Items" to "SC Popular Items from Snapshot"

e) Change the Server script field to the following:

data.sc\_catalog = $sp.getValue('sc\_catalogs') || $sp.getValue('sc\_catalog');  
data.showPrices = $sp.showCatalogPrices();  
data.limit = options.limit || 9;  
var items = \[\];  
  
var grCount = new GlideRecord('u\_popular\_items');  
grCount.addQuery('u\_sc\_cat\_item.sc\_catalogs', 'IN', data.sc\_catalog);  
grCount.orderByDesc('u\_count');  
grCount.query();  
  
while (grCount.next() && items.length < data.limit) {  
if (!$sp.canReadRecord("sc\_cat\_item", grCount.u\_sc\_cat\_item.sys\_id.getDisplayValue()))  
continue; // user does not have permission to see this item  
  
var item = {};  
item.count = grCount.u\_count.getDisplayValue();  
item.name = grCount.u\_cat\_item.name.getDisplayValue();  
item.short\_description = grCount.u\_cat\_item.short\_description.getDisplayValue();  
item.picture = grCount.u\_cat\_item.picture.getDisplayValue();  
item.price = grCount.u\_cat\_item.price.getDisplayValue();  
item.hasPrice = grCount.u\_cat\_item.price != 0;  
item.sys\_id = grCount.u\_cat\_item.sys\_id.getDisplayValue();  
items.push(item);  
}  
  
if (options.include\_record\_producers == 'true' || options.include\_record\_producers == true) {  
var producers = 0;  
var gaCount = new GlideAggregate('sc\_item\_produced\_record');  
gaCount.addQuery('producer.sc\_catalogs', 'IN', data.sc\_catalog);  
gaCount.addEncodedQuery('producer.hide\_sp=false^ORproducer.hide\_spISEMPTY');  
gaCount.addAggregate('COUNT', 'producer');  
gaCount.groupBy('producer');  
gaCount.orderByAggregate('COUNT', 'producer');  
gaCount.query();  
while (gaCount.next() && producers < data.limit) {  
  
var catalogItemJS = new sn\_sc.CatItem(gaCount.getValue('producer'));  
if (!catalogItemJS.canView(gs.isMobile()) || !catalogItemJS.isVisibleServicePortal())  
continue;  
var catItemDetails = catalogItemJS.getItemSummary();  
  
var item = {};  
item.count = gaCount.getAggregate('COUNT', 'producer');  
item.name = catItemDetails.name;  
item.short\_description = catItemDetails.short\_description;  
item.picture = catItemDetails.picture;  
item.price = catItemDetails.price;  
item.hasPrice = item.price != 0;  
item.sys\_id = catItemDetails.sys\_id;  
item.page = 'sc\_cat\_item';  
items.push(item);  
producers++;  
}  
}  
  
data.items = items;

f) Click on the Additional actions > Save context menu item.

![](/sys_attachment.do?sys_id=65ea92a5471b6610bb78d9d8736d43ca)

4) Modify any an all Instances of the SC Popular Items widget to the new widget.

a) Navigate to the Service Portal > Widget Instances module

b) Filter the list on Widget Name = SC Popular Items

c) For each instance of the SC Popular Items widget, edit the Widget field and point it to the newly created "SC Popular Items from Snapshot" widget..

### Additional Information

[SC Popular Items widget](https://docs.servicenow.com/bundle/newyork-servicenow-platform/page/build/service-portal/concept/sc-popular-items.html "SC Popular Items widget")
