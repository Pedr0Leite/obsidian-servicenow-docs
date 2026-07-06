---
title: "How does Discovery calculate CPU Count/CPU Core Count"
aliases:
  - KB0696858
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696858
kb_number: KB0696858
last_modified: 2025-01-17
---

## How does Discovery calculate CPU Count/CPU Core Count

  

### Issue

Sometimes people may have questions why the Discovered CPU Count/CPU Core Count on Windows/Linux CI does not match what they see in Windows Task Manager. Actually, that is an expected result from Discovery.

### How CPU Count/CPU Core Count is calculated

On a Computer CI form, the "CPU count" means the number of physical CPUs (sockets). The "CPU core count" means the number of cores in one physical CPU (socket). 

When we are looking at the CPUs from the Task Manager/vSphere/lscpu, it doesn't actually show the number of physical CPUs. Instead, we will see the number of total logical CPUs (virtual CPU), which is a multiplication of "physical CPUs" and "cores per CPU" (and hyper-thread if there is). This is how customers are seeing "mismatching" results.

The "socket" number is the number of physical CPUs, it always matches the "CPU count". The "core per socket" number always matches the "CPU core count". And the final logical CPU number is their multiplication.

### Example

For example, if one server has 2 physical CPUs, each CPU has 4 cores, without hyper-thread (cpu\_core\_thread = 1) you will see 8 CPUs in the Task Manager or vSphere. If the hyper-thread is enabled (cpu\_core\_thread = 2), the total CPUs will be 16. The cpu\_core\_thread value is not showing on the CI but it can be seen by the "Show XML" menu on the CI form. 

![](sys_attachment.do?sys_id=d5670c9d1b8985d0ccc253da234bcbab)

### Related Links

More details can be seen in probes "Linux - CPU" and "Windows - CPU / Memory"
