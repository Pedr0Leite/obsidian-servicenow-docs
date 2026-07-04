---
title: "Advanced configuration for traffic-based Discovery"
aliases:
  - KB0597467
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597467
kb_number: KB0597467
last_modified: 2024-10-01
---

## Advanced configuration for traffic-based Discovery

  

### Issue

Overview

* * *

Service Mapping can discover configuration items (CIs) by following traffic connections between CIs. This method is referred to as traffic-based discovery. Service Mapping detects outbound connections using the netstat and lsof commands. Starting with the Istanbul release, Service Mapping also supports the Netflow protocol. The Netflow-based discovery is not enabled by default and must be configured.  
  
By default, traffic-based discovery is enabled in Service Mapping and relevant properties are configured to use default values, as described in [Properties installed with Service Mapping](https://docs.servicenow.com/ "Properties installed with Service Mapping").   
  

Detailed explanation

  

* * *

If necessary, you can configure the following advanced properties:  
  
  

<table class="internalTable" style="border: 1px solid #e0e0e0;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle; text-align: left;"><strong>Parameter name</strong></td><td style="vertical-align: middle; text-align: left;"><strong>Description</strong></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">sa.cmdb_tcp_refresh</td><td style="vertical-align: middle; text-align: left;"><strong>Description</strong>: This parameter defines if Service Mapping runs the ADM probe to update information on traffic-based connections in the cmdb_tcp table. If this parameter is set to true, Service Mapping runs the ADM probe before the discovery process.<p style="text-align: start;"><strong>Type</strong>: true/false</p><p style="text-align: start;"><strong>Default value</strong>: true</p><p style="text-align: start;"><strong>Other possible values</strong>: false</p><p style="text-align: start;"><strong>Location</strong>: This property is not added to the sys_properties table by default. If necessary, <a title="create this value" href="Add%20a%20property%20using%20sys_properties.list" target="_blank" rel="noopener noreferrer">create this value</a>.<br><br></p><p><strong>Update from version Y and later (including WP9, XP2):</strong></p><p>Windows - ADM Multiple has been disabled and is no longer supported.</p><p>The default value has been changed to false.</p><p>The property should not be added.<br>If the property already exists for the customer, it should be deleted, or its value changed to false.</p></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">&nbsp;<span style="text-align: start;">&nbsp;sa.cmdb_tcp_refresh_time_minutes</span></td><td style="vertical-align: middle; text-align: left;"><strong>Description</strong>: Data&nbsp;on traffic-based connections is stored in the cmdb_tcp table. If the data is stored before the period of time defined by this parameter, Service Mapping updates this data in the table.<p style="text-align: start;"><strong>Type</strong>:&nbsp;integer</p><p style="text-align: start;"><strong>Default value</strong>:&nbsp;1440</p><p style="text-align: start;"><strong>Other possible values</strong>:&nbsp;any non-negative number</p><p style="text-align: start;"><strong>Location</strong>: This property is not added to the sys_properties table by default. If necessary, <a title="create this value" href="Add%20a%20property%20using%20sys_properties.list" target="_blank" rel="noopener noreferrer">create this value</a>.</p></td></tr><tr class="sp"><td style="vertical-align: middle; text-align: left;">&nbsp;<span style="text-align: start;">sa.traffic_based.wait_for_adm_probe&nbsp;</span></td><td style="vertical-align: middle; text-align: left;"><strong>Description</strong>: The ADM probe updates information on traffic-based connections during discovery performed by Service Mapping. This parameter defines if Service Mapping waits until the ADM probe completes updating information before running the discovery process.<p style="text-align: start;"><strong>Type</strong>: true/false</p><p style="text-align: start;"><strong>Default value</strong>: true</p><p style="text-align: start;"><strong>Other possible values</strong>: false</p><p style="text-align: start;"><strong>Location</strong>: This property is not added to the sys_properties table by default. If necessary, <a title="create this value" href="Add%20a%20property%20using%20sys_properties.list" target="_blank" rel="noopener noreferrer">create this value</a>.</p></td></tr></tbody></table>

  
  

Procedure

* * *

Add the required properties to the sys\_properties table as described in [Add a property using sys\_properties.list](https://docs.servicenow.com/csh?topicname=t_AddAPropertyUsingSysPropsList.html&version=latest "Add a property using sys_properties.list").
