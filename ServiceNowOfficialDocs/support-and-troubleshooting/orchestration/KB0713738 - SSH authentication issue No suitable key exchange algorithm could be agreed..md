---
title: "SSH authentication issue : No suitable key exchange algorithm could be agreed."
aliases:
  - KB0713738
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713738
kb_number: KB0713738
last_modified: 2025-01-02
---

## SSH authentication issue : No suitable key exchange algorithm could be agreed.

  

### Issue

SSH authentication or connection failure: No suitable key exchange algorithm could be agreed.

This message can be seen either during Discovery or Orchestration Activity and this could be due to MID server still using legacy SSH client J2SSH.

### Resolution

Enable the use of SNCSSH client for Discovery and Orchestration.

<table id="r_SSHDiscoveryParameters__table_hfq_ty2_xp" class="table frame-all" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: 0px; border-spacing: 0px; border-collapse: collapse; background-color: #fafafa; width: 813px; border-left: 0px; border-right: 0px; max-width: 100%; border-bottom: 1px solid #dddddd; color: #343d47; font-family: Source_Sans_Pro, Gotham, Helvetica, Arial, sans-serif; font-size: 16px;"><tbody class="tbody" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: 0px;"><tr class="row" style="box-sizing: border-box; padding: 0px; margin: 0px -15px; outline: 0px; border-left: 0px; border-right: 0px; border-bottom: 0px;"><td class="entry colsep-1 rowsep-1" style="box-sizing: border-box; padding: 8px; margin: 0px; outline: 0px; line-height: 1.42857; vertical-align: top; border-top: 1px solid #dddddd;" headers="r_SSHDiscoveryParameters__table_hfq_ty2_xp__entry__1 ">Enable the&nbsp;<span class="ph" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: 0px;">ServiceNow</span>SSH Client</td><td class="entry colsep-1 rowsep-1" style="box-sizing: border-box; padding: 8px; margin: 0px; outline: 0px; line-height: 1.42857; vertical-align: top; border-top: 1px solid #dddddd;" headers="r_SSHDiscoveryParameters__table_hfq_ty2_xp__entry__2 ">mid.ssh.use_snc</td><td class="entry colsep-1 rowsep-1" style="box-sizing: border-box; padding: 8px; margin: 0px; outline: 0px; line-height: 1.42857; vertical-align: top; border-top: 1px solid #dddddd;" headers="r_SSHDiscoveryParameters__table_hfq_ty2_xp__entry__3 ">Enables the&nbsp;<span class="ph" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: 0px;">ServiceNow</span>&nbsp;SSH client (SNCSSH) on individual MID Servers. SNCSSH is a&nbsp;<span class="ph" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: 0px;">ServiceNow</span>&nbsp;implementation of an SSH client and is active by default for all MID Servers on new instances, via a&nbsp;<a class="xref" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: none; background-color: transparent; color: #d1232b; text-decoration-line: none; cursor: pointer;" title="Use properties to control the behavior of all probes on a MID Server or all probes on all MID Servers." href="https://docs.servicenow.com/csh?topicname=r_MIDServerProperties.html&amp;version=latest#r_MIDServerProperties">MID Server property</a>. Enabling the&nbsp;<span class="ph" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: 0px;">ServiceNow</span>SSH client disables the legacy J2SSH client.<div class="note important note_important" style="box-sizing: border-box; padding: 0px; margin: 20px 40px; outline: 0px;"><span class="note__title" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: 0px; font-weight: bold;">Important:</span>&nbsp;Mixing SSH client types for MID Servers connected to the same instance is not a good practice.</div><ul id="r_SSHDiscoveryParameters__ul_rz1_p1f_xp" class="ul" style="box-sizing: border-box; padding: 0px 0px 0px 30px; margin: 10px auto 5px; outline: 0px; overflow-wrap: break-word; list-style-position: inside;"><li class="li" style="box-sizing: border-box; padding: 0px; margin: 0px; outline: 0px;">Type: true | false</li><li class="li" style="box-sizing: border-box; padding: 0px; margin: 6px 0px 0px; outline: 0px;">Default value: false</li></ul></td></tr></tbody></table>

[https://docs.servicenow.com/csh?topicname=r\_MIDServerProperties.html&version=latest](https://docs.servicenow.com/csh?topicname=r_MIDServerProperties.html&version=latest)
