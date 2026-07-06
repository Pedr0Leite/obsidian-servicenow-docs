---
title: "How to create a connection between Application to MSSQL DB Servers in Service Map"
aliases:
  - KB0780736
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780736
kb_number: KB0780736
last_modified: 2024-12-03
---

## How to create a connection between Application to MSSQL DB Servers in Service Map

  

### Issue

Need help to create a connection between application to MSSQL db servers in service map. Any out of box patterns available??

### Resolution

Either:  
  
1) Use "MSSql DB On Windows Pattern":

For your purpose, we have MSSQL OOB pattern that you can use "MSSql DB On Windows Pattern":  
  
[Applications supported by Discovery and Service Mapping](https://docs.servicenow.com/bundle/orlando-it-operations-management/page/product/service-mapping/reference/r_SupportedApplications.html "Applications supported by Discovery and Service Mapping")  
  
[MSSQL server discovery](https://docs.servicenow.com/bundle/rome-it-operations-management/page/product/discovery/reference/mssql-data-collected-pattern.html "MSSQL server discovery")

or 2) Add a connectivity section: (as per your need)

"You may have a Web Application, for example, which has discovered the Load Balancer and IIS Web Server and you want to add Application Server & MS-SQL Database server to complete the Service Map.  
  
In which case, "You are going to need to add a connectivity section to the IIS Virtual Directory Pattern that parses the URL out of the config file. Once you do that you should see the next hop IIS server and it may or may not find the database server. If it doesn't then you will have to do something similar in which you will create a connectivity section to pull out the configuration for the SQL server. It will most likely either be in the web.config file (make sure your URLs are correct so they go into the right IIS Website) or some other configuration file that may reference the ODBC DSN setup in Windows (which you can pull from the registry). "  
  
[Service Mapping for a Web Application](https://community.servicenow.com/community?id=community_question&sys_id=0029351adb5b1b005ed4a851ca9619df)  
  
  
  
  

### Related Links

-   [Customizing the patterns](https://docs.servicenow.com/bundle/kingston-it-operations-management/page/product/service-mapping/concept/c_MappingPatternsCustomization.html "Customizing the patterns")
