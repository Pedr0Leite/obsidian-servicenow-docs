---
title: "Making import sets created for Import Set API calls \"Asynchronous\" to prevent Synchronous transform, for specific imports"
aliases:
  - KB0781666
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781666
kb_number: KB0781666
last_modified: 2025-11-04
---

## Making import sets created for Import Set API calls "Asynchronous" to prevent Synchronous transform, for specific imports

  

### Issue

All import sets created for Import SET API calls are "Synchronous". What this means is that as an import set row is created, it is transformed immediately.

To prevent immediate transform the import set can be made "Asynchronous". 

REST Import Set API method insertMultiple was added in Quebec

[https://docs.servicenow.com/bundle/quebec-paris-df3/page/release-notes/rn-combined/quebec-paris/quebec-paris-importandexport-release-notes.html](https://docs.servicenow.com/bundle/quebec-paris-df3/page/release-notes/rn-combined/quebec-paris/quebec-paris-importandexport-release-notes.html)

### Resolution

## Import Set API method insertMultiple

In Quebec a new method insertMultiple was added to the Import Set API. This method allows you to import multiple records and then transform them asynchronously:

[https://developer.servicenow.com/dev.do#!/reference/api/sandiego/rest/c\_ImportSetAPI](https://developer.servicenow.com/dev.do#!/reference/api/sandiego/rest/c_ImportSetAPI)#import-POST-insertMultiple

## Custom Business Rule (Not Supported)

This can be achieved as follows:

1.  Create a "Before" insert business rule on the sys\_import\_set table with a conditional check on the Import set table (table\_name) that should not be transformed synchronously.
2.  Under actions, add 'Mode' to 'Asynchronous'.
3.  Create a Scheduled job that runs every few minutes and transforms the 'asynchronous' import set, with the following script and set it to run 'Periodically'.

There is an OOB Scheduled Script Execution "Asynchronous Import Set Transformer", you can use that as a guideline and change line 8 (igr.addQuery("state", "loaded")) and replace it with the following 2 lines: 

igr.addQuery("table\_name", "the staging table name");  
igr.addQuery("state", "loading");

The complete Script:

<table><tbody><tr><td><pre style="margin: 0; line-height: 125%;"> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34</pre></td><td><pre style="margin: 0; line-height: 125%;">transformAsyncIset();

<span style="color: #008000; font-weight: bold;">function</span> transformAsyncIset() {
    <span style="color: #008000; font-weight: bold;">var</span> igr <span style="color: #666666;">=</span> <span style="color: #008000; font-weight: bold;">new</span> GlideRecord(<span style="color: #ba2121;">"sys_import_set"</span>);
    igr.addQuery(<span style="color: #ba2121;">"mode"</span>, <span style="color: #ba2121;">"asynchronous"</span>);
    igr.addQuery(<span style="color: #ba2121;">"table_name"</span>, <span style="color: #ba2121;">"STAGING_TABLE_NAME"</span>);
    igr.addQuery(<span style="color: #ba2121;">"state"</span>, <span style="color: #ba2121;">"loading"</span>);
    igr.query();
    <span style="color: #008000; font-weight: bold;">while</span> (igr.next()) {
        sTransform(igr);
    }
}

<span style="color: #008000; font-weight: bold;">function</span> sTransform(igr) {
    <span style="color: #008000; font-weight: bold;">var</span> mapsList <span style="color: #666666;">=</span> getMap(igr.table_name);

    <span style="color: #008000; font-weight: bold;">var</span> t <span style="color: #666666;">=</span> <span style="color: #008000; font-weight: bold;">new</span> GlideImportSetTransformerWorker(igr.sys_id, mapsList);
    t.setProgressName(<span style="color: #ba2121;">"Transforming: "</span> <span style="color: #666666;">+</span> igr.number);
    t.setBackground(<span style="color: #008000; font-weight: bold;">true</span>);
    t.start();
}

<span style="color: #008000; font-weight: bold;">function</span> getMap(sTable) {
    <span style="color: #008000; font-weight: bold;">var</span> mapGR <span style="color: #666666;">=</span> <span style="color: #008000; font-weight: bold;">new</span> GlideRecord(<span style="color: #ba2121;">"sys_transform_map"</span>);
    mapGR.addQuery(<span style="color: #ba2121;">"source_table"</span>, sTable);
    mapGR.addActiveQuery();
    mapGR.query();

    <span style="color: #008000; font-weight: bold;">var</span> mapsList <span style="color: #666666;">=</span> [];
    <span style="color: #008000; font-weight: bold;">while</span> (mapGR.next())
        mapsList.push(mapGR.getUniqueValue());

    <span style="color: #008000; font-weight: bold;">return</span> mapsList.join();
}
</pre></td></tr></tbody></table>
