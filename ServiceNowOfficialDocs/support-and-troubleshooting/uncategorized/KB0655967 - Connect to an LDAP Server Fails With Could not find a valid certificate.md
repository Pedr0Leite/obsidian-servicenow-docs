---
title: "Connect to an LDAP Server Fails With: \"Could not find a valid certificate\"
aliases:
  - KB0655967
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0655967
kb_number: KB0655967
last_modified: 2025-12-09
---

## Connect to an LDAP Server Fails With: "Could not find a valid certificate"

  

### Issue

Testing an LDAP Server connection on the instance and the connection test fails with the error:

**ldaps://xxx.xxx.xxx.xxx:636 Could not find a valid certificate**

or

**ldap://xxx.xxx.xxx.xxx:636 Could not find a valid certificate**

The node logs may show the following error:

2020-12-28 07:49:51 (394) worker.6 worker.6 txid=e7ba8baa1b99 SEVERE \*\*\* ERROR \*\*\* Cannot recover key  
java.security.UnrecoverableKeyException: Cannot recover key  
        at sun.security.provider.KeyProtector.recover(KeyProtector.java:315)  
        at sun.security.provider.JavaKeyStore.engineGetKey(JavaKeyStore.java:141)  
        at sun.security.provider.JavaKeyStore$JKS.engineGetKey(JavaKeyStore.java:56)  
        at sun.security.provider.KeyStoreDelegator.engineGetKey(KeyStoreDelegator.java:96)  
        at sun.security.provider.JavaKeyStore$DualFormatJKS.engineGetKey(JavaKeyStore.java:70)  
        at java.security.KeyStore.getKey(KeyStore.java:1023)  
        at sun.security.ssl.SunX509KeyManagerImpl.<init>(SunX509KeyManagerImpl.java:133)  
        at sun.security.ssl.KeyManagerFactoryImpl$SunX509.engineInit(KeyManagerFactoryImpl.java:70)  
        at javax.net.ssl.KeyManagerFactory.init(KeyManagerFactory.java:256)  
        at com.glide.certificates.DBKeyStoreSocketFactory.createKeyManagers(DBKeyStoreSocketFactory.java:138)  
        at com.glide.certificates.DBKeyStoreSocketFactory.initSSLContext(DBKeyStoreSocketFactory.java:116)  
        at com.glide.certificates.DBKeyStoreSocketFactory.init(DBKeyStoreSocketFactory.java:106)  
        at com.glide.certificates.DBKeyStoreSocketFactory.init(DBKeyStoreSocketFactory.java:98)  
        at com.glide.certificates.DBKeyStoreSocketFactory.<init>(DBKeyStoreSocketFactory.java:78)  
        at com.glide.sys.ldap.LDAP.setUseDBKeyStore(LDAP.java:109)  
        at com.glide.sys.ldap.LDAP.setup(LDAP.java:97)  
        at sun.reflect.GeneratedMethodAccessor710.invoke(Unknown Source)  
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
        at java.lang.reflect.Method.invoke(Method.java:498)  
        at org.mozilla.javascript.MemberBox.invoke(MemberBox.java:138)  
        at org.mozilla.javascript.NativeJavaMethod.call(NativeJavaMethod.java:300)  
        at org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2612)  
        at org.mozilla.javascript.optimizer.OptRuntime.callProp0(OptRuntime.java:85)  
        at org.mozilla.javascript.gen.\_refname\_\_1064.\_c\_testLDAPServers\_1(<refname>:17)  
        at org.mozilla.javascript.gen.\_refname\_\_1064.call(<refname>)  
        at org.mozilla.javascript.ScriptRuntime.doCall2(ScriptRuntime.java:2678)  
        at org.mozilla.javascript.ScriptRuntime.doCall(ScriptRuntime.java:2617)  
        at org.mozilla.javascript.optimizer.OptRuntime.callName0(OptRuntime.java:74)  
        at org.mozilla.javascript.gen.\_refname\_\_1064.\_c\_script\_0(<refname>:1)  
        at org.mozilla.javascript.gen.\_refname\_\_1064.call(<refname>)  
        at org.mozilla.javascript.ContextFactory.doTopCall(ContextFactory.java:563)  
        at org.mozilla.javascript.ScriptRuntime.doTopCall(ScriptRuntime.java:3459)  
        at org.mozilla.javascript.gen.\_refname\_\_1064.call(<refname>)  
        at org.mozilla.javascript.gen.\_refname\_\_1064.exec(<refname>)  
        at com.glide.script.ScriptEvaluator.execute(ScriptEvaluator.java:279)  
        at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:118)  
        at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:82)  
        at com.glide.script.ScriptEvaluator.evaluateString(ScriptEvaluator.java:73)  
        at com.glide.script.Evaluator.evaluateString(Evaluator.java:96)  
        at com.snc.automation.ScriptJob.executeInSingleDomain(ScriptJob.java:57)  
        at com.snc.automation.ScriptJob.execute(ScriptJob.java:41)  
        at com.glide.schedule.JobExecutor.lambda$executeJob$0(JobExecutor.java:113)  
        at com.glide.schedule.JobExecutor.executeJob(JobExecutor.java:116)  
        at com.glide.schedule.JobExecutor.execute(JobExecutor.java:100)  
        at com.glide.schedule\_v2.SchedulerWorkerThread.executeJob(SchedulerWorkerThread.java:300)  
        at com.glide.schedule\_v2.SchedulerWorkerThread.lambda$process$0(SchedulerWorkerThread.java:188)  
        at com.glide.worker.TransactionalWorkerThread.executeInTransaction(TransactionalWorkerThread.java:35)  
        at com.glide.schedule\_v2.SchedulerWorkerThread.process(SchedulerWorkerThread.java:188)  
        at com.glide.schedule\_v2.SchedulerWorkerThread.run(SchedulerWorkerThread.java:102)  
2020-12-28 07:49:51 (396) worker.6 worker.6 txid=e7ba8baa1b99 WARNING \*\*\* WARNING \*\*\* LDAP API - LDAPLogger : Unable to load certificates from DB  
2020-12-28 07:49:51 (396) worker.6 worker.6 txid=e7ba8baa1b99 WARNING \*\*\* WARNING \*\*\* LDAP: Unable to load certificates from DB  
\[...\]  
2020-12-28 07:49:51 (544) worker.6 worker.6 txid=e7ba8baa1b99 LDAP API - LDAPLogger : xxx.xxx.xxx.xxx:636  
2020-12-28 07:49:51 (544) worker.6 worker.6 txid=e7ba8baa1b99 LDAP API - LDAPLogger : Communication error: xxx.xxx.xxx.xxx:636  
2020-12-28 07:49:51 (544) worker.6 worker.6 txid=e7ba8baa1b99 LDAP API - LDAPLogger : javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target  
2020-12-28 07:49:51 (549) worker.6 worker.6 txid=e7ba8baa1b99 SEVERE \*\*\* ERROR \*\*\* LDAP: LDAP Server: LDAP Server URL: ldap://xxx.xxx.xxx.xxx:636/ failed scheduled connection test. ErrorCode: 10402. ErrorMessage: Could not find a valid certificate.

### Release

All releases

### Cause

There are two known causes for this issue.

#### Cause #1

The LDAP server does not present a valid certificate chain to the instance. This may be because

-   the leaf certificate or intermediate/root certificate may be expired
-   the chain is missing the intermediate/root certificate
-   the chain contains an incorrect/unrelated certificate
-   the chain contains a self-signed certificate and that certificate is not recognized by the instance.

(this is not an exhaustive list)

How to set up certificates for LDAPS connections is discussed in this documentation: [Certificates](https://docs.servicenow.com/csh?version=latest&topicname=c_Certificates.html "Certificates")

#### Cause #2:

There is an invalid certificate defined in the x509 Certificate module (sys\_certificate list view).  The LDAP server record has a Related Link called "Certificate List", when that is selected you are taken to the x509 Certificate module (sys\_certificate list view). This means the system will check all of the certificates in that list to find a valid one for the LDAP SSL connection.  While checking the list of certificates, if the system comes across an invalid certificate before it gets to one that is valid for the SSL connection the error will occur.

### Resolution

**There are two ways to resolve this issue for Cause #1:**

1.  Set the system property com.glide.communications.httpclient.verify\_hostname to **false**, while keeping the com.glide.communications.trustmanager\_trust\_all property set to **true**. In this configuration, the system again makes the instance trust the Certificate Authority CA for a certificate. This ensures the instance accepts self-issued certificates. This is NOT recommended in production instances as it lowers the security settings of the instance. The recommended way is to fix the actual certificate.
2.  Check the certificate chain presented by the LDAP server and fix any issues. If self-signed certificates are used, make sure to upload the  intermediate/root certificate to the instance by following the documentation on Certificates referenced above: [Certificates](https://docs.servicenow.com/bundle/paris-platform-administration/page/administer/general/concept/c_Certificates.html "Certificates")

**For Cause #2:**

1.  Go to the x509 Certificate module (sys\_certificate list view)
2.  Open each certificate in the list and select the Related Link "Validate Stores/Certificates", if the certificate does not validate set it to Active = false and check the LDAP connection again.  Deactivate each certificate until the one or ones causing the issue are found.
3.  Once the offending certificate(s) are found leave them inactive or correct the issue to make them valid, e.g. entering the correct password for a keystore or adding a keystore attachment or updating the PEM Certificate value to a valid value, e.g. to one that is not expired.  Once the certificate passes validation it can be made active again.
4.  Once the certificate manipulation is complete check the LDAP connection again to make sure it still connects successfully.
