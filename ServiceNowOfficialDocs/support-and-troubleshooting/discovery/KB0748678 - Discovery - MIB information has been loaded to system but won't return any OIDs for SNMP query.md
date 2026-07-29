---
title: "Discovery - MIB information has been loaded to system but won't return any OIDs for SNMP query"
aliases:
  - KB0748678
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748678
kb_number: KB0748678
last_modified: 2024-04-07
---

## Discovery - MIB information has been loaded to system but won't return any OIDs for SNMP query

  

### Issue

# Symptoms

-   Discovery - Aruba Controller MIB has been loaded to system and won't return any SNMP query
-   " No valid OID s specified " message in ECC queue records when running custom SNMP classifier.

# Release

All versions

# Cause

-   MIB file references/dependencies are not loaded to MID server. This can be validated in the ECC queue logs when the mid server is restarted.
-   MIB string is incorrect or there are multiple paths creating invalid MIB string. Hence MID server couldn't translate the MIB string to numeric value using all the MIBs that were uploaded. 

# Resolution

1.  MIB file references/dependencies are not loaded to MID server. "ARUBA-6-5-4-3-MIB"  referenced MIB file references ARUBA-MIB and ARUBA-TC mibs and these weren't loaded to MID Server. This prevented MID Server from loading all Aruba MIBs properly.   
       - Download missing files from the appropriate vendor's website and upload to MID Server MIB List under MID Server -> SNMP MIBs.  
      
    2\. Incorrect MIB String translates to an invalid object identifier ( OID ).  Example: Incorrect OID string -  "iso.org.dod.internet.private.enterprise.aruba.arubaEnterpriseMibModules.switch.wlsxEnterpriseMibModules.wlsxWlanMIB.wlsxWlanStateGroup.wlsxWlanAccessPointInfoGroup.wlsxWlanAPTable.wlanAPModelName"   
    \- Need to change "enterprise" to  "enterprises" for the example.  
      
    3\. A missing attribute in OID path. Example: "iso.org.dod.internet.private.enterprise.aruba.arubaEnterpriseMibModules.switch.wlsxEnterpriseMibModules.wlsxWlanMIB.wlsxWlanStateGroup.wlsxWlanAccessPointInfoGroup.wlsxWlanAPTable.wlanAPModelName"   
    \- There is one more OID path between "wlsxWlanAPTable" and "wlanAPModelName". The missing OID was "wlsxWlanAPEntry". Add this OID such that the final OID string is below -   
    "iso.org.dod.internet.private.enterprises.aruba.arubaEnterpriseMibModules.switch.wlsxEnterpriseMibModules.wlsxWlanMIB.wlsxWlanStateGroup.wlsxWlanAccessPointInfoGroup.wlsxWlanAPTable.wlsxWlanAPEntry.wlanAPModelName"

Above resolution is for a sample issue and are some of the reasons for Discovery returning no OIDs for SNMP query.
