---
title: "Receiving the error while updating the Adobe Subscription certificate"
aliases:
  - KB1446558
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1446558
kb_number: KB1446558
last_modified: 2026-03-27
---

## Receiving the error while updating the Adobe Subscription certificate

  

### Issue

Encountering the following error after adding a new certificate.

`Connection Failed. Could not match JWT signature to any of the bindings. invalid_token`

**Steps To Reproduce:** 

1) HOP to the instance.  
2) Navigate to samp\_sw\_subscription\_profile.LIST  
3) Click on UI action/related link --> Validate Adobe Credential  
4) It will error out with below   
Connection Failed. Could not match JWT signature to any of the bindings. invalid\_token

### Release

ALL

### Cause

1\. Identifying the most probable cause by enabling debug properties in the sys\_properties table.

`glide.rest.debug` to true  
`glide.outbound_http_log.override` to true  
`glide.outbound_http_log.override.level` ALL

2\. For example, if the below error is being observed in the node logs during the above steps to reproduce.

```
21:18:38.413 Debug Default-thread-14 75E7CBFB1B7329147B4D20A7B04BCB2F txid=9389433f1b73 DEBUG: Certificate TMCAJuly7latest of Type pkcs12_key_store is NOT supported in cache!

21:18:39.018 Info Default-thread-14 75E7CBFB1B7329147B4D20A7B04BCB2F txid=9389433f1b73 OUTBOUND_HTTP: protocol=HTTP/1.1 response_status=400 response_time=672 request_length=803 response_length=100 app_scope=global session_id=75E7CBFB1B7329147B4D20A7B04BCB2F transaction_name="#916383 /samp_sw_subscription_profile.do" transaction_id=9389433f1b7329147b4d20a7b04bcbf9 user_name=XXXX.XXXX@snc mid_server= source_table=sys_script_include source_record=a47d8273875203003800ed4d87cb0b29 system_id=appXXXXXXX.syd101.service-now.com:XXXXXXXXXXXXX method=POST log_level=All scheme=https hostname=ims-na1.XXXXXXX.com path=/ims/exchange/jwt
21:18:39.019 Info Default-thread-14 75E7CBFB1B7329147B4D20A7B04BCB2F txid=9389433f1b73 event="HTTP_OUTBOUND_REQUEST" session_id="75E7CBFB1B7329147B4D20A7B04BCB2F" user_name="XXXX.XXXX@snc" protocol="HTTP/1.1" response_status="400" response_time="672" request_length="803" response_length="100" app_scope="global" transaction_name="#916383 /samp_sw_subscription_profile.do" transaction_id="9389433f1b7329147b4d20a7b04bcbf9" source_table="sys_script_include" source_record="a47d8273875203003800ed4d87cb0b29" system_id="appXXXXXX.syd101.service-now.com:XXXXXXXXXXXX" method="POST" log_level="All" log_type="SECLOG" session_id="4BCB2F" source_ip="149.96.221.228" tx_num="916383" url="/samp_sw_subscription_profile.do" domain="global" http_last_time="1688962713019" jsession_id="930DCE" http_uagent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" user="XXX.XXXXX@snc" user_id="XXXXX.XXXXX@snc" http_time_zone="Australia/Melbourne" user_group="[]" http_browser="chrome"
21:18:39.021 Info Default-thread-14 75E7CBFB1B7329147B4D20A7B04BCB2F txid=9389433f1b73 tx_pattern_hash=-368893333 *** End #916383 /samp_sw_subscription_profile.do, user: XXXXXX.XXXXXX@snc, total time: 0:00:00.798, processing time: 0:00:00.798, CPU time: 0:00:00.191, SQL time: 0:00:00.056 (count: 191), Cache build time: 0:00:00.005, source: 149.96.221.228, type: form
```

3\. Then it is clearly evident that the customer certificates used have issues.

### Resolution

Customers to work with their security or certificate provider and make sure right certificate is being used while setting up Adobe profile integration in the servicenow instance.
