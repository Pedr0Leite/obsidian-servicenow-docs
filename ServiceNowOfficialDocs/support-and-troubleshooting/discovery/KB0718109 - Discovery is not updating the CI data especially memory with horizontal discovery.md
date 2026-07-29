---
title: "Discovery is not updating the CI data especially memory with horizontal discovery"
aliases:
  - KB0718109
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718109
kb_number: KB0718109
last_modified: 2025-01-03
---

## Issue

Discovery is not updating the CI data after horizontal discovery. When discovery runs, it pulls the memory value from Win32\_PhysicalMemory.

When the memory value changes dynamically, Win32\_PhysicalMemory registry is not updated until the server is restarted. The dynamic memory value is stored in Win32\_OperatingSytem.TotalVisibleMemorySize.

## Resolution

1.  To pull the dynamic memory value from the registry, add "Win32\_OperatingSytem.TotalVisibleMemorySize" to the list of WMI fields in "Windows - CPU / Memory probe".
2.  In the post processor script on the probe's sensor:_add var processors = g\_array\_util.ensureArray(output.Win32\_Processor);_
3.  In script, look for the line: _total\_memory += (parseFloat(Win32\_PhysicalMemory.Capacity) / 1048576);_ 
4.  Replace Win32\_PhysicalMemory. Capacity with Win32\_OperatingSytem.TotalVisibleMemorySize. If the value is in megabytes, you can remove the division by 1048576 when calculating the value.
