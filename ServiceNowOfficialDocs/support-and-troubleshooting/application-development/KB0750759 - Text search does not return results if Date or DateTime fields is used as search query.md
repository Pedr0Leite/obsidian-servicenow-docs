---
title: "Text search does not return results if Date or Date/Time fields is used as search query"
aliases:
  - KB0750759
  - Text search does not return results for Date or Date/Time fields
area: application-development
tags:
  - servicenow
  - support-kb
  - text-search
  - zing
  - indexing
  - global-search
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750759
kb_number: KB0750759
last_modified: 2024-04-07
---

## Issue

Text search does not return results if Date or Date/Time fields is used as search query

## Resolution

The date and date/time fields are not indexed in the platform. Zing is basically a string search engine and it does not index date time fields. There are cases where users might see date, date/time data returning some results for certain records and this is because that same data was mentioned elsewhere in the record other than the date time field. 

There is currently no way to index date and time fields.

## Additional Information

[Zing text indexing and search engine](https://docs.servicenow.com/csh?topicname=c_ZingTextSearch.html&version=latest "Zing text indexing and search engine")

[Features of Zing text indexing and search engine](https://docs.servicenow.com/csh?topicname=features-zing.html&version=latest "Features of Zing text indexing and search engine")

## Related

- [[KB0817535 - Optimize text search responsiveness]]
- [[KB0814590 - Test Search Warning in log - JoinQuery invalid field name document_number]]
- [[KB0542700 - Debugging legacy text search issues]]
- [[KB0546326 - Text search index debugging script]]
