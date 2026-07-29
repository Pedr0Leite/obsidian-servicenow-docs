---
title: "App Node Runs Out of Memory Immediatelly When Opening a Knowledge Article That Has Data On The Wiki Column"
aliases:
  - KB0814798
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814798
kb_number: KB0814798
last_modified: 2024-04-23
---

## App Node Runs Out of Memory Immediatelly When Opening a Knowledge Article That Has Data On The Wiki Column

  

### Issue

The error "connection reset" appeared when attempting to load any page and some applications e.g. Knowledge fails to load entirely.

  

Sample Stack Trace: 

main,Default-thread-15,5,attrs=(session\_id=DD61FE51416221006D9E93550E517FB8)  
info.bliki.wiki.filter.WikipediaParser.encodeHtml(WikipediaParser.java:499)  
info.bliki.wiki.filter.WikipediaParser.getNextToken(WikipediaParser.java:1246)  
info.bliki.wiki.filter.WikipediaParser.runParser(WikipediaParser.java:2047)  
info.bliki.wiki.filter.WikipediaParser.parseRecursive(WikipediaParser.java:2343)  
info.bliki.wiki.filter.WPCell.filter(WPCell.java:121)  
info.bliki.wiki.filter.WPRow.filter(WPRow.java:106)  
info.bliki.wiki.filter.WPTable.filter(WPTable.java:97)  
info.bliki.wiki.filter.WikipediaParser.getNextToken(WikipediaParser.java:677)  
info.bliki.wiki.filter.WikipediaParser.runParser(WikipediaParser.java:2047)  
info.bliki.wiki.filter.WikipediaParser.parseRecursive(WikipediaParser.java:2343)  
info.bliki.wiki.filter.WikipediaParser.parse(WikipediaParser.java:2287)  
info.bliki.wiki.filter.AbstractWikiModel.render(AbstractWikiModel.java:139)

### Cause

1.  The reason why the app nodes restart is due to malformed wiki text markups on the wiki value of on the KB.
2.  The malformed wiki markups is any text that has '{' or '}' on the wiki column value. This is related to [PRB606244](https://support.servicenow.com/problem.do?sys_id=6a0f2e196fa6ad00a2c1f7307f3ee41f&sysparm_record_target=problem&sysparm_record_row=1&sysparm_record_rows=1&sysparm_record_list=numberSTARTSWITHPRB606244%5EORDERBYDESCsys_created_on "PRB606244").  
    
3.  Every time a user accesses the KB with the malformed wiki markups of '{' or '}', it runs the app node our of memory immediately which then restarts the app node, which is why users keep getting the "cannot connect message" time to time.

  
  

### Resolution

1.  Export the KB that has the malformed wiki markups of '{' or '}' as an XML file.
2.  Open the exported XML file and remove all characters that contain '{' or '}'.
3.  Re-import the updated XML file as an XML import -> it will overwrite the current KB that had the malformed wiki markups of '{' or '}' and it will open really quickly and it will also not run the app node out of memory
