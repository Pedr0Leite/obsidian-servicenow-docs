---
title: "Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by \"security_admin\" Role"
aliases:
  - KB0758037
tags:
  - servicenow
  - support-kb
  - security_admin
  - roles
  - ldap
  - azure-ad
  - transform-map
  - import-sets
  - sys_user_role
area: access-controls-authentication
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758037
kb_number: KB0758037
last_modified: 2025-08-25
---

## Azure AD Sync or an Import (e.g. LDAP Group Import) Being Interfered with by "security\_admin" Role

  

### Issue

Azure AD sync or an Import (e.g. LDAP Group Import) fails to add users to the group via auto-provisioning if the group has security\_admin roles granted. 

Following example error will be seen in the node logs:

```
2021-10-14 14:19:33 (477) worker.7 worker.7 txid=63033d8cdbdb User admin without admin/security_admin role is not allowed to grant admin/security_admin-containing roles or groups.
2021-10-14 14:19:33 (477) worker.7 worker.7 txid=63033d8cdbdb Background message, type:error, message: User admin without admin/security_admin role is not allowed to grant admin/security_admin-containing roles or groups.
2021-10-14 14:19:33 (477) worker.7 worker.7 txid=63033d8cdbdb WARNING *** WARNING *** User admin without admin/security_admin role is not allowed to grant admin/security_admin-containing roles or groups.
2021-10-14 14:19:33 (477) worker.7 worker.7 txid=63033d8cdbdb SEVERE *** ERROR *** inserting
com.glide.db.DBActionInterruptionException: User admin without admin/security_admin role is not allowed to grant admin/security_admin-containing roles or groups.
        at com.glide.role_management.RoleManagementListener.enforceInsertRestrictions(RoleManagementListener.java:170)
        at com.glide.role_management.RoleManagementListener.onExecute(RoleManagementListener.java:103)
        at com.glide.db.DBAction.processListeners(DBAction.java:166)
        at com.glide.db.DBAction.executeAndReturnException(DBAction.java:204)
        at com.glide.script.GlideRecordITable.insert(GlideRecordITable.java:158)
        at com.glide.script.GlideRecord.insert(GlideRecord.java:4971)
        at com.glide.script.GlideRecord.insert(GlideRecord.java:4881)
        at com.glide.sys.ldap.LDAPGroups.createGroupMember(LDAPGroups.java:317)
        at com.glide.sys.ldap.LDAPGroups.addUsers(LDAPGroups.java:255)
        at com.glide.sys.ldap.LDAPGroups.setMembers(LDAPGroups.java:209)
        at com.glide.sys.ldap.LDAPGroups.setMembers(LDAPGroups.java:175)
        at sun.reflect.GeneratedMethodAccessor389.invoke(Unknown Source)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)
        at org.mozilla.javascript.NativeJavaMethod.call(NativeJavaMethod.java:300)
        at org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2612)
        at org.mozilla.javascript.optimizer.OptRuntime.callProp0(OptRuntime.java:85)
        at org.mozilla.javascript.gen.sys_script_include_e86a94620a0a0b26008e67598866c6ea_script_602._c_anonymous_9(sys_script_include.e86a94620a0a0b26008e67598866c6ea.script:72)
        at org.mozilla.javascript.gen.sys_script_include_e86a94620a0a0b26008e67598866c6ea_script_602.call(sys_script_include.e86a94620a0a0b26008e67598866c6ea.script)
        at org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2678)
        at org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2617)
        at org.mozilla.javascript.optimizer.OptRuntime.call2(OptRuntime.java:42)
        at org.mozilla.javascript.gen.sys_transform_script_0dc646160a0a0b26007beb877ee7cdf9_script_626._c_script_0(sys_transform_script.0dc646160a0a0b26007beb877ee7cdf9.script:15)
        at org.mozilla.javascript.gen.sys_transform_script_0dc646160a0a0b26007beb877ee7cdf9_script_626.call(sys_transform_script.0dc646160a0a0b26007beb877ee7cdf9.script)
        at org.mozilla.javascript.ContextFactory.doTopCall(ContextFactory.java:563)
        at org.mozilla.javascript.ScriptRuntime.doTopCall(ScriptRuntime.java:3459)
        at org.mozilla.javascript.gen.sys_transform_script_0dc646160a0a0b26007beb877ee7cdf9_script_626.call(sys_transform_script.0dc646160a0a0b26007beb877ee7cdf9.script)
        at org.mozilla.javascript.gen.sys_transform_script_0dc646160a0a0b26007beb877ee7cdf9_script_626.exec(sys_transform_script.0dc646160a0a0b26007beb877ee7cdf9.script)
        at com.glide.script.ScriptEvaluator.execute(ScriptEvaluator.java:279)
        at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:118)
        at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:82)
        at com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:321)
        at com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:225)
        at com.glide.script.fencing.GlideScopedEvaluator.evaluateScript(GlideScopedEvaluator.java:212)
        at com.glide.db.impex.transformer.TransformerScript.runScript(TransformerScript.java:70)
        at com.glide.db.impex.transformer.TransformerScript.runWhenScript(TransformerScript.java:133)
        at com.glide.db.impex.transformer.Transformer.runOnAfterScript(Transformer.java:302)
        at com.glide.db.impex.transformer.Transformer.transformBatch(Transformer.java:175)
        at com.glide.db.impex.transformer.Transformer.transform(Transformer.java:88)
        at com.glide.system_import_set.ImportSetTransformerImpl.transformEach(ImportSetTransformerImpl.java:304)
        at com.glide.system_import_set.ImportSetTransformerImpl.transformAllMaps(ImportSetTransformerImpl.java:117)
        at com.glide.system_import_set.ImportSetTransformer.transformAllMaps(ImportSetTransformer.java:91)
        at com.glide.system_import_set.ImportSetTransformer.transformAllMaps(ImportSetTransformer.java:77)
        at com.glide.system_import_set.ImportSetTransformer.transformAllMaps(ImportSetTransformer.java:72)
        at com.snc.automation.ScheduledImportSetJob.runImport(ScheduledImportSetJob.java:119)
        at com.snc.automation.ScheduledImportSetJob.runNextImport(ScheduledImportSetJob.java:65)
        at com.snc.automation.ScheduledImportSetJob.runNextImport(ScheduledImportSetJob.java:77)
        at com.snc.automation.ScheduledImportSetJob.runImport(ScheduledImportSetJob.java:53)
        at com.snc.automation.ScheduledImportJob.execute(ScheduledImportJob.java:52)
        at com.glide.schedule.JobExecutor.lambda$executeJob$0(JobExecutor.java:113)
        at com.glide.schedule.JobExecutor.executeJob(JobExecutor.java:116)
        at com.glide.schedule.JobExecutor.execute(JobExecutor.java:100)
        at com.glide.schedule_v2.SchedulerWorkerThread.executeJob(SchedulerWorkerThread.java:300)
        at com.glide.schedule_v2.SchedulerWorkerThread.lambda$process$0(SchedulerWorkerThread.java:188)
        at com.glide.worker.TransactionalWorkerThread.executeInTransaction(TransactionalWorkerThread.java:35)
        at com.glide.schedule_v2.SchedulerWorkerThread.process(SchedulerWorkerThread.java:188)
        at com.glide.schedule_v2.SchedulerWorkerThread.run(SchedulerWorkerThread.java:102)

2021-10-14 14:19:33 (478) worker.7 worker.7 txid=63033d8cdbdb SEVERE *** ERROR *** Error during insert of sys_user_grmember (Created 2021-10-14 16:19:33)
```

### Release

-   Instance on London or Later releases.
-   Configuration for auto user provisioning with Azure Active Directory done. 
-   The group in which the user has to be provisioned has a Security\_admin role assigned. 

### Cause

There are some design changes in the sys\_user\_role ACL with the READ operation since the London release. Per the change we have locked the contains role checks in the ACL for READ operations.

### Resolution

There are two solutions:

(1) Remove the security\_admin role from the group role for the user to sync/provisioned to the group.

(2) In cases where a transform map is used a user with the security\_admin role may be impersonated and apply the security\_admin role before the transforming is done:

Create an OnStart script as in this example:

```
(function runTransformScript(source, map, log, target /*undefined onStart*/ ) {

    gs.getSession().impersonate('6816f79cc0a8016401c5a33be04be441'); // impersonate a user with security_admin role, its sys_id from the sys_user table is used here
    GlideSecurityManager.get().enableElevatedRole('security_admin'); //elevate to security_admin

})(source, map, log, target);
```

### Related Links

The security\_admin role is an elevated privilege role provided with High-Security Settings that lets users create and change access controls and change High-Security Settings.

In the base system, only the default System Administrator (admin) user has the security\_admin role. Since it requires elevating privileges, the admin user does not have this role at login. After elevating privileges, the admin user has the security\_admin role for the duration of the user session.

Reference: [https://docs.servicenow.com/csh?topicname=security-admin-role.html&version=latest](https://docs.servicenow.com/csh?topicname=security-admin-role.html&version=latest)

## Related

- [[KB0753001 - Some roles are not  visible and cannot be exported from the [sys_user_role] list table]] — same London-release sys_user_role read ACL change
- [[KB0610548 - Default admin account missing security_admin role]] — another security_admin role edge case
- [[security-admin-role]] — official docs on the security_admin elevated role
