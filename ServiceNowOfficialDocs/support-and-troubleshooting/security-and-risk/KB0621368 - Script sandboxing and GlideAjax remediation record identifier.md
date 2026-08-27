---
title: "Script sandboxing and GlideAjax remediation record identifier"
aliases:
  - KB0621368
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621368
kb_number: KB0621368
last_modified: 2025-02-04
---

## Issue

#### **Script sandboxing and GlideAjax remediation record identifier**

* * *

This document assumes that you are familiar with the information in the following knowledge base articles:

-   [Script sandboxing remediation](https://support.servicenow.com/kb_view.do?sysparm_article=KB0550837 "Script Sandboxing Remediation KB")
-   [Audit and review GlideAjax transactions](https://support.servicenow.com/kb_view.do?sysparm_article=KB0550828 "GlideAjax Remediation KB")

Due to the challenging nature of the remediation efforts, ServiceNow has developed a process for providing affected customers with output from their instance that helps automate some of the manual steps in the knowledge base articles. _**The output should not be treated as a catch-all solution. It should be leveraged as a guide to focus work efforts efficiently. Manual review is still required and you should still exercise additional considerations before enabling the respective properties.**_

## Resolution

#### **How do I decipher the script sandbox audit output?**

* * *

Some sample output:

<table style="background-color: rgb(224, 224, 224);"><tbody><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>===== Checking Filters (sys_filter) =====</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############: Flagged functions: (function) [filter_inactive]</em><br>4368bcb3c611228f01b1d93114b4c484: Flagged functions: gs.badfunction<br>4419b177c611228f014c55ea1bf4b028: Flagged functions: gs.badfunction [filter_inactive]</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><span style="color: rgb(209, 35, 43);"><strong><em>#sys_id of filter#</em>&nbsp;- Flagged functions: <em>{function list} [is the sys_filter record marked active]</em></strong></span></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>2 out of 4 Record(s) Requiring Review</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>===== Checking Modules (sys_app_module) =====</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############: Flagged functions: (function) [module_inactive]</em><br>0ae0e7d89f002200f45c7b9ac42e70b5: Flagged functions: gs.badfunction&nbsp;<br>2ee1a6bac0a8006400a4effea456e356: Flagged functions: gs.badfunction [module_inactive]<br>6bf359f8d7600100c11180f29e6103f3: Flagged functions: gs.badfunction&nbsp;<br>6e5d46bec0a80005018bdc7a5d0da465: Flagged functions: gs.badfunction [module_inactive]<br>74d025e4c611227d00392d44292a7108: Flagged functions: gs.badfunction [module_inactive]</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><span style="color: rgb(209, 35, 43);"><strong><em>#sys_id of module#</em>&nbsp;- Flagged functions: <em>{function list} {is the sys_app_module record marked active}</em></strong></span></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>5 out of 101 Record(s) Requiring Review</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>===== Checking Client Scripts (sys_script_client) =====</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############: Flagged keywords: (function) [client_script_inactive]</em><br>26a640a90b012200a914e17696673a27: Flagged keywords: NonClientCallableScriptInclude&nbsp;<br>4db9cb50cb300200d71cb9c0c24c9c1c: Flagged keywords: NonClientCallableScriptInclude&nbsp;<br>67432496d7512200d105ef637e610342: Flagged keywords:&nbsp;NonClientCallableScriptInclude</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><span style="color: rgb(209, 35, 43);"><strong><em>#sys_id of client script#</em>&nbsp;- Flagged keywords: <em>{keyword list} {is sys_script_client record marked&nbsp;active}</em></strong></span></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>3 out of 833 Record(s) Requiring Review</strong></td></tr></tbody></table>

  
With the script sandboxing output, as items are reviewed and remediated the list should become shorter. You can request the output through the incident if necessary. 

1.  To approach the filters and modules, go to the respective table and search for the corresponding sys\_id.
2.  Look at the script in question.
3.  Find the function that has been flagged and replace as needed.

If the \[\*\_inactive\] text is next to the line item, then remediation is not necessary as long as the record is not going to be marked active at a later time.

1.  Similarly, with the client scripts, navigate to the respective table and find the record with the corresponding sys\_id.
2.  Confirm that the flagged keyword has been accurately flagged. If yes, determine if the related script include record should be made client callable (this is necessary after the property has been turned on). 

<table class="noteTable" style="border: 1px solid rgb(224, 224, 224);" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Note</strong>: D<span style="text-align: start;">o not mark script includes as client-callable unless the business context dictates. This change may expose sensitive information to the client side</span>.</td></tr></tbody></table>

#### **How do I decipher the GlideAjax audit output?**

* * *

Sample output:

<table style="background-color: rgb(224, 224, 224);"><tbody><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>===== Checking Client Scripts (sys_script_client) =====</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############ (table): role (action) [acl_script_dependent] [client_script_inactive]</em><br>1acc808e37413000158bbfc8bcbe5d1d (pc_vendor_cat_item): model_manager (write) [acl_script_dependent]<br>26a640a90b012200a914e17696673a27 (asmt_metric): assessment_admin (delete), assessment_admin (write)<br>2a4d1a74c0a801660137c5b6cccdd65f (cmn_schedule_span): itil_admin (create), schedule_admin (create), itil (read)<br>426a51503743100044e0bfc8bcbe5d71 (cmdb_model): model_manager (write)&nbsp;[client_script_inactive]<br>491bd135dfd23000cd7da5f59bf26327 (sc_task): itil_admin (delete), itil (read), catalog (read), itil (write)</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><span style="color: rgb(209, 35, 43);"><strong><em>#sys_id&nbsp;of client script#</em>&nbsp;(<em>database object</em>): <em>{role1}</em>&nbsp;(<em>action</em>) <em>[is this dependent on acl script]</em>,&nbsp;<em>{role2}</em>&nbsp;(<em>action2</em>)&nbsp;<em>[is this dependent on acl script] [is the sys_script_client record marked&nbsp;active]</em></strong></span></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>-- Checking for AJAXEvaluateSynchronously --</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############ [client_script_inactive]</em><br>34bd606edbc13200eb4dff561d9619ef</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong style="color: rgb(209, 35, 43);"><em>#sys_id&nbsp;of client script#</em></strong><strong style="color: rgb(209, 35, 43);"><em><strong> [is the sys_script_client record marked&nbsp;active]</strong></em></strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>6 Record(s) Requiring Review</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>===== Checking UI Pages (sys_ui_page) =====</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############: role (action) [acl_script_dependent]</em><br>9b7aedc60b2022009cfdc71437673a7c: atf_test_admin (read), atf_test_designer (read)<br>bc2a8260930331009c8579b4f47ffb53: admin (read), security_admin (read) [acl_script_dependent]<br>c1c9bb30c3612100a77f4ddcddba8f14: admin (read)&nbsp;</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><span style="color: rgb(209, 35, 43);"><strong><em>#sys_id of ui page#</em>: <em>{role1}</em>&nbsp;(<em>action1)</em>&nbsp;<em>[is this dependent on acl script]</em>,&nbsp;<em>{role2}</em>&nbsp;(<em>action2)</em>&nbsp;<em>[</em><em>is this dependent on acl script]</em></strong></span></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>-- Checking for AJAXEvaluateSynchronously --</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############</em><br>59dda46edbc13200eb4dff561d961908</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong style="color: rgb(209, 35, 43);"><em>#sys_id of ui page#</em></strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>4 Record(s) Requiring Review</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>===== Checking UI Macros (sys_ui_macro) =====</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############ [ui_macro_inactive]</em><br>d44e4272c33321000096dfdc64d3aea0<br>ea6d7293efa002008e4c36caa5c0fb11<br>ee82aea2472321004695d7527c9a7141 [ui_macro_inactive]<br>ef544b350a0a0b80004a112c80dfc665</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><span style="color: rgb(209, 35, 43);"><strong><em>#sys_id&nbsp;of ui macro# [</em><em>is the sys_ui_macro record marked active]</em></strong></span></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>-- Checking for AJAXEvaluateSynchronously --</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############ [ui_macro_inactive]</em><br>b2fde46edbc13200eb4dff561d961969</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong style="color: rgb(209, 35, 43);"><em>#sys_id&nbsp;of ui macro# [</em><em>is the sys_ui_macro record marked active]</em></strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>5 Record(s) Requiring Review</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>===== Checking Dynamic CMS Blocks (content_block_programmatic) =====</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############ [content_block_programmatic_inactive]</em><br>43010362ef370000914304167b2256d6<br>b13a6c2d0a0a0b12001c053d51928d20&nbsp;[content_block_programmatic_inactive]</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><span style="color: rgb(209, 35, 43);"><strong><em>#sys_id of cms block# [</em><em>is the content_block_programmatic&nbsp;record marked active]</em></strong></span></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>-- Checking for AJAXEvaluateSynchronously --</strong></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><em>############(sys_id)############ [content_block_programmatic_inactive]</em><br>b32e686edbc13200eb4dff561d961982&nbsp;</td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><span style="color: rgb(0, 0, 0);"><strong style="color: rgb(209, 35, 43);"><em>#sys_id of cms block# [</em><em>is the content_block_programmatic&nbsp;record marked active]</em></strong></span></td></tr><tr><td style="border: 1px dashed rgb(187, 187, 187);"><strong>3 Record(s) Requiring Review</strong></td></tr></tbody></table>

  
Unlike the script sandboxing output, the GlideAjax output does not become shorter as records are changed. As the necessary missing ACLs are added, the output should increase in size.

1.  Approach the client scripts and UI pages line items by determining if the related record and the roles/permission associated with them fulfill the business need for that table. If not, add the necessary ACLs to ensure that the necessary functionality is in place.
2.  For the UI macros and CMS blocks, ensure that any GlideAjax call is allowable by the current ACL configuration. If not, make the necessary changes.

The AJAXEvaluateSynchronously section under each record type highlights any use of the AJAXEvaluateSynchronously function that should not be used and should be replaced by GlideAjax.

## Additional Information

-   [Script sandboxing remediation](https://support.servicenow.com/kb_view.do?sysparm_article=KB0550837 "Script Sandboxing Remediation KB")
-   [Audit and review GlideAjax transactions](https://support.servicenow.com/kb_view.do?sysparm_article=KB0550828 "GlideAjax Remediation KB")
