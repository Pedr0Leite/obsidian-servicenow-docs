---
title: "Matching a ServiceNow instance version to its Edge Proxy version and JRE version"
aliases:
  - KB0634965
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634965
kb_number: KB0634965
last_modified: 2024-04-07
---

## Matching a ServiceNow instance version to its Edge Proxy version and JRE version

  

### Issue

Matching a ServiceNow instance version to its Edge Proxy version and JRE version  

Problem

* * *

Customers need to know which version of the Edge Proxy is shipped with their ServiceNow version, and which JRE is bundled with that version of the Edge Proxy.

Resolution

* * *

Locate the Java used by your Edge proxy on the **$proxy\_install\_dir/conf/wrapper.conf** file. Then validate the JDK version installed by using **java -version** for that installed java. Alternatively, your edge encryption logs shows the Java version when starting up.

To make this information easier to access, the below list shows the ServiceNow version that began shipping with a specific Edge Proxy, and which JRE is bundled with the Edge Proxy:

<table class="internalTable"><tbody><tr class="sphr"><td><strong>ServiceNow version</strong></td><td><strong>Edge version</strong></td><td><strong>JRE version</strong></td></tr><tr class="sp"><td>Geneva</td><td>1.1.0</td><td>1.8.0_40</td></tr><tr class="sp"><td>Helsinki</td><td>2.0.0</td><td>1.8.0_40</td></tr><tr class="sp"><td>Helsinki P1</td><td>2.1.0</td><td>1.8.0_40</td></tr><tr class="sp"><td>Helsinki P8</td><td>2.8.1</td><td>1.8.0_40</td></tr><tr class="sp"><td>Istanbul</td><td>3.0.9</td><td>1.8.0_40</td></tr><tr class="sp"><td>Istanbul P1</td><td>3.1.1</td><td>1.8.0_40</td></tr><tr class="sp"><td>Jakarta</td><td>11</td><td>1.8.0_121</td></tr><tr class="sp"><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table>

  

<table class="noteTable"><tbody><tr><td><img title="Note" src="/Note_25x.pngx" alt="" border="" hspace="" vspace=""></td><td><strong>Note</strong>: Locate the Java used by your Edge proxy on the <strong>wrapper.conf</strong>&nbsp;file. Validate the JDK version installed by using <strong>java -version</strong>.</td></tr></tbody></table>
