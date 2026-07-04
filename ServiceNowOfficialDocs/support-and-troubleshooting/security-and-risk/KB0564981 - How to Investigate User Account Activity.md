---
title: "How to Investigate User Account Activity "
aliases:
  - KB0564981
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0564981
kb_number: KB0564981
last_modified: 2026-06-09
---

## How to Investigate User Account Activity

  

### Issue

For the latest information about Monitoring user activity, see [Monitoring user activity](https://www.servicenow.com/docs/r/platform-administration/user-administration/user-admin-tools-landing.html "Monitoring user activity").

At any time there is a need to review specific user behavior, below are the recommended steps on how to review the transaction logs and event logs:

-   Locate the IP address of successful/failed login for a particular ServiceNow user for their instance
-   Modify the time frame of the search
-   Limiting the scope of the search by user name
-   Successful/Failed login attempts

### Procedure

#### Locate User Activity Process Steps

1.  Log in to the instance as an admin
2.  Identify Transaction Logs  
    -   Transaction logs by default are kept for over 49 days unless the instance admin has adjusted the table rotations for \[syslog\_transaction\] table.
3.  Navigate to System Logs > Transactions https://<instance\_name>.service-now.com/syslog\_transaction\_list.do
4.  Adjust filter to narrow down logs for investigative purposes  
    -   Required timeframe: The filter is "Created"
    -   Username: The filter set as "Created by" with the option of "starts with" either/or "contains"  
          
        ![](sys_attachment.do?sys_id=9c5a66f29799831c5ad8f6e11153af40)  
          
        
5.  Narrow the log date range  
      
            From this list view we can then adjust the filter as below:
    -   Created on – Adjust do any date or timeframe the customer needs
    -   Created by – Adjust to the affected username  
          
        
6.  Identify the IP address of the user login:  
    1.  Click on the cogwheel in the upper left corner of the table to open the Personalized list column.   
          
        ![](sys_attachment.do?sys_id=145aa6f29799831c5ad8f6e11153afe7)  
          
        
    2.  To view the IP address of the logged-in user you can add the IP address column to the list view via the Personalize List columns module.   
          
        ![](sys_attachment.do?sys_id=185ae6f29799831c5ad8f6e11153afe9)

* * *

#### Identify Successful/Failed Login Attempts

Note that this is only for local accounts.

1.  Log in to the instance as an admin
2.  Navigate to **System Logs > Events  
      
    **https://<instance\_name>.service-now.com/sysevent\_list.do?sysparm\_query=sys\_created\_onONToday%40javascript:gs.daysAgoStart(0)%40javascript:gs.daysAgoEnd(0)%5EGOTOnameSTARTSWITHSNC.Auth.DB  
      
    
3.  Adjust filter as follows:  
      
    ![](sys_attachment.do?sys_id=d85aa6f29799831c5ad8f6e11153aff4)  
      
    
4.  From this list view we can then adjust the filter as below:  
    -   Created on – Adjust do any date or timeframe the customer needs
    -   Created by – Adjust to the affected username

#### Additional Recommended Actions for Evaluating Activity of Concern 

Once the above steps have been completed, it is recommended that the customer also performs the following actions to determine if any suspicious activity has taken place that either was not captured in the logs identified or occurred outside of the current log retention period set:

1.  Determine the roles assigned to the target user by reviewing the sys\_user\_has\_role table and filtering to entries for the user in question.
2.  Review the sys\_audit table for any unexpected changes made within their instance – please see this docs page for more details: [https://www.servicenow.com/docs/csh?topicname=c\_UnderstandingTheSysAuditTable.html&version=latest](https://www.servicenow.com/docs/csh?topicname=c_UnderstandingTheSysAuditTable.html&version=latest) 
3.  Review their sys\_user table for any newly created users that are not recognized, especially those with privileged roles.
4.  Review Service Accounts and ensure they are configured according to best practices linked at this KB: [https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB1933421](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1933421) 
5.  Review if there are any newly scheduled jobs that are not recognized by the platform owner team. Please see this docs page for details on how to review Scheduled Jobs: [https://www.servicenow.com/docs/csh?topicname=view-scheduled-jobs.html&version=latest](https://www.servicenow.com/docs/csh?topicname=view-scheduled-jobs.html&version=latest) 
6.  Review the Customer Updates table for any unexpected activity. Details on how to navigate this table can be found in the linked documentation: [https://www.servicenow.com/docs/csh?topicname=r\_CustomerUpdatesTable.html&version=latest](https://www.servicenow.com/docs/csh?topicname=r_CustomerUpdatesTable.html&version=latest) 
7.  Review the Security Center Metrics dashboard (/now/security-center/my\_security\_metrics), especially the below metrics:

1.  1.  Privileged Users: Local logins of privileged users not protected by MFA in Security Center
    2.  Privileged Users: New users
    3.  Privileged Users: Successful logins
    4.  Users: Successful logins
    5.  Users: Inactive users who are not locked out
    6.  Users: New users
    7.  Privileged Identities: Admin users added  
    8.  Privileged Identities: Admin logins  
    9.  Authentication: Users using MFA Bypass
    10.  Authentication High privileged non-MFA users
    11.  Export: Total Exports 

**Reviewing Node Logs Based on IP Address**

To review your node logs for activity associated to a specific set of IP addresses, first ensure that all Node Logs are downloaded from your instance by following the instructions in the below KB: 

[https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB0826291](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0826291)

Once your node logs are downloaded, ensure that they are in a separate folder, then navigate to that folder in a your terminal of choice:

**Linux/Mac User Instructions:**

Add the IP addresses reported by ServiceNow to a txt file with the command below, pressing ctrl + D on a blank line when complete:

`cat > reported_ip_addresses.txt`

Once reported\_ip\_addresses.txt is created, run the below command.

It will loop through every log file in the folder and create the result files for each one:

\-- Command Begins --

`for LOG in app*localhost_log*.txt; do PREFIX=$(echo "$LOG" | grep -oE '^app[0-9]+'); echo "[$PREFIX] Step 1/3: searching for IPs..."; grep -F -f reported_ip_addresses.txt "$LOG" > "${PREFIX}_activity_from_ips.txt"; echo "[$PREFIX] Step 2/3: extracting txids..."; grep -oE 'txid=[0-9a-f]+' "${PREFIX}_activity_from_ips.txt" | sed 's/txid=//' | sort -u > "${PREFIX}_associated_txids.txt"; echo "[$PREFIX] Step 3/3: pulling all lines for those txids (this is the slow one on big files)..."; grep -F -f <(sed 's/^/txid=/' "${PREFIX}_associated_txids.txt") "$LOG" > "${PREFIX}_activity_from_txids.txt"; echo "[$PREFIX] Done."; done`

\-- Command Ends --

As it runs, you will see progress messages like:

`[app######] Step 1/3: searching for IPs...`

`[app######] Step 2/3: extracting txids...`

`[app######] Step 3/3: pulling all lines for those txids (this is the slow one on big files)...`

`[app######] Done.`

Next, see the Script Output section after Windows PowerShell Instructions.

**Windows PowerShell Instructions:**

Run this command. A window/prompt will let you type IPs. Type or paste your IP addresses one per line. When finished, enter a blank line (just press Enter on an empty line) to stop.

`$ips = @(); while ($true) { $line = Read-Host "Enter IP (blank line to finish)"; if ([string]::IsNullOrWhiteSpace($line)) { break }; $ips += $line.Trim() }; $ips | Set-Content -Path "reported_ip_addresses.txt"; Write-Host "Saved $($ips.Count) IP address(es)."`

This saves your IPs into `reported_ip_addresses.txt`, one per line.

Paste this entire block and press Enter. It loops through every matching log file in the folder and creates the result files for each one, with progress messages.

\-- Command Begins --

`$ipPatterns = Get-Content "reported_ip_addresses.txt" | Where-Object { $_.Trim() -ne "" } | ForEach-Object { [regex]::Escape($_.Trim()) }`

`Get-ChildItem -File | Where-Object { $_.Name -match '^app\d+.*localhost_log' } | ForEach-Object {`  
    `$log = $_.FullName`  
    `$name = $_.Name`  
    `$prefix = [regex]::Match($name, '^app\d+').Value`  
    `if ([string]::IsNullOrEmpty($prefix)) { $prefix = "unknown" }`

    `Write-Host "[$prefix] Step 1/3: searching for IPs..."`  
    `Select-String -Path $log -Pattern $ipPatterns | ForEach-Object { $_.Line } | Set-Content -Path "${prefix}_activity_from_ips.txt"`

    `Write-Host "[$prefix] Step 2/3: extracting txids..."`  
    `Select-String -Path "${prefix}_activity_from_ips.txt" -Pattern 'txid=([0-9a-f]+)' -AllMatches |`  
        `ForEach-Object { $_.Matches } |`  
        `ForEach-Object { $_.Groups[1].Value } |`  
        `Sort-Object -Unique |`  
        `Set-Content -Path "${prefix}_associated_txids.txt"`

    `Write-Host "[$prefix] Step 3/3: pulling all lines for those txids..."`  
    `$txids = Get-Content "${prefix}_associated_txids.txt" | Where-Object { $_.Trim() -ne "" } | ForEach-Object { "txid=" + [regex]::Escape($_.Trim()) }`  
    `if ($txids.Count -gt 0) {`  
        `Select-String -Path $log -Pattern $txids | ForEach-Object { $_.Line } | Set-Content -Path "${prefix}_activity_from_txids.txt"`  
    `} else {`  
        `Set-Content -Path "${prefix}_activity_from_txids.txt" -Value ""`  
    `}`

    `Write-Host "[$prefix] Done."`  
`}`

\-- Command Ends --

As it runs, you will see progress messages like:

`[app#######] Step 1/3: searching for IPs...`

`[app#######] Step 2/3: extracting txids...`

`[app#######] Step 3/3: pulling all lines for those txids (this is the slow one on big files)...`

`[app#######] Done.`

**Script Output**

For each node, three files are created, each prefixed with the node's `app######` identifier:

`app######_activity_from_ips.txt` — every log line that mentions one of your reported IPs

`app######_associated_txids.txt` — the unique transaction IDs (txids) pulled from those lines

`app######_activity_from_txids.txt` — every log line for those transactions, giving the full activity for each one

Review these logs to identify what activities were recorded in your node logs for your instance. For questions on how node logs are structured, please feel free to create a Case with ServiceNow Support.

### Release

### Resolution
