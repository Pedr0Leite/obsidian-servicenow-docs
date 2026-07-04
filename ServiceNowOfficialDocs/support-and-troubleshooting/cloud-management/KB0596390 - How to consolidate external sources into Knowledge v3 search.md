---
title: "How to consolidate external sources into Knowledge v3 search"
aliases:
  - KB0596390
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596390
kb_number: KB0596390
last_modified: 2024-04-07
---

## How to consolidate external sources into Knowledge v3 search

  

### Issue

# How to consolidate external sources into Knowledge v3 search

  
  

# Overview

* * *

Knowledge v2 (Eureka and earlier) had a feature called Navigation Add-ons that was used to show search results from external sources, which is now deprecated.

The new v3 framework to crawl external sources such as Documentation and Community uses scheduled jobs to extract the content from other sources and falls back on [Zing Search](https://docs.servicenow.com/csh?topicname=c_ZingTextSearch.html&version=latest) to index and provide search results. The following diagram shows the flow of data.

![](/sys_attachment.do?sys_id=274d68a2db82b450e515c22305961966)

# About the framework

* * *

The framework is mostly housed within a scheduled job that uses APIs of the external content source to extract content. The scheduled job then saves the sources as individual articles in a separate Knowledge Base. Using periodic runs of the scheduled job, the content will be synched over to the KB.

This framework provides a guideline for you to implement external source searching for your instance.

## Configuration object

In order to manage multiple content sources effectively, you need to have a configuration object. This stores the details about the external content source, and how the content will be mapped into the Knowledge Base within your instance. Consider managing the details listed in the following table.

<table border="1"><tbody><tr><td>Target Knowledge Base</td><td>The KB where the extracted content would be transformed into individual articles. You should create the Target Knowledge base before you configure this.</td></tr><tr><td>Security</td><td>Set up access to the articles that are being created through the scheduled job from a particular source.</td></tr><tr><td style="border: 1px solid black;">Source URL endpoint (or other config)</td><td style="border: 1px solid black;">A config or URL that can be used by the scheduled job to call the external content source.</td></tr><tr><td style="border: 1px solid black;">Redirect URL</td><td style="border: 1px solid black;">When returning search results, you may need a base URL to use to build the final URL for the source content</td></tr><tr><td style="border: 1px solid black;">Security</td><td style="border: 1px solid black;">Define the content security</td></tr><tr><td style="border: 1px solid black;">Category Mapping</td><td style="border: 1px solid black;">Define which KB categories will be assigned to articles that are being created by the content source. You should create the categories in the Target Knowledge base, before you define this mapping.</td></tr></tbody></table>

## Synchronization logic

Once the content is extracted, you should check against existing articles. A checksum is a good way to verify changes.

-   If the content is new, then _Create_ a new article.
-   If the content exists in the KB, but is updated, then _Update_ the article.
-   If the content exists in the KB, but is not modified, _Ignore_.
-   If the content exists in the KB, but is no longer found in content source, then _Expire_ the 'containing article' so that it's no longer available in search.

## Incremental crawl vs. Full crawl

Fine-tune the synchronization process based on how frequently the external content source is modified.

-   Adding and updating existing articles (_incremental_) may be performed more frequently.
    
-   A _Full_ crawl (which includes comparing existing content for deletes) should be done less frequently. Because this process hits the source content system heavily, consider some degree of planning and throttling.
    

## Wrapper/holding article

The article created as a result of this process has a few other values to be set, as listed in the following table.

<table border="1"><tbody><tr><td style="border: 1px solid black;">Knowledge Base</td><td style="border: 1px solid black;">Set the Knowledge base with regards to the config object for that particular external source.</td></tr><tr><td style="border: 1px solid black;">Category</td><td style="border: 1px solid black;">Set the category based on the config object that maps an attribute of the source (like URL) to a particular category defined for that Knowledge Base.</td></tr><tr><td style="border: 1px solid black;">Roles</td><td style="border: 1px solid black;">The Roles for which the external content will be available to.</td></tr><tr><td style="border: 1px solid black;">Language</td><td style="border: 1px solid black;">The language under which the imported article will be available to.</td></tr><tr><td style="border: 1px solid black;">Text Body</td><td style="border: 1px solid black;">It's advisable to strip off the HTML from the external content and store only the text of the article within the wrapper article.</td></tr><tr><td style="border: 1px solid black;">Meta</td><td style="border: 1px solid black;">You may use an external service to generate meta that will be associated with that article.</td></tr><tr><td style="border: 1px solid black;">Valid to date</td><td style="border: 1px solid black;">The date until which this wrapper article will be available (recommended to keep it less, so that stale articles are not indexed).</td></tr><tr><td style="border: 1px solid black;">Workflow State</td><td style="border: 1px solid black;">Make sure that the article state is set to Published, to ensure visibility to all. Also don't set any workflows.</td></tr><tr><td style="border: 1px solid black;">Click-through URL</td><td style="border: 1px solid black;">The default Article URL needs to be replaced with the URL of the source. You will typically need to concatenate a base URL of the content source with the URL for that article.</td></tr></tbody></table>
