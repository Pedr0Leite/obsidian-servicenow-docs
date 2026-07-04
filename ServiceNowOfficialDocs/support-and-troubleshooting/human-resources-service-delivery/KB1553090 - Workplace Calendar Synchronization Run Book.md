---
title: "Workplace Calendar Synchronization Run Book"
aliases:
  - KB1553090
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1553090
kb_number: KB1553090
last_modified: 2024-12-12
---

## Text

###         **Microsoft Exchange Online Symptoms**

1.  [Setup/Configuration Issue (Normal Mode)](#setuporconfigurationissue)
2.  [Strict mode issues (Client Credentials grant type)](#Strictmodewithclientcreds)
3.  [Strict mode issues (Auth Code grant type)](#Strictmodewithauthcode)
4.  [Override Alias](https://docs.servicenow.com/bundle/utah-employee-service-management/page/product/workplace-calendar-synchronization/task/create-own-credential-and-connection-alias-for-strict-mode.html)
5.  [Reservations stuck in awaiting confirmation](#AwaitingConfirmation)
6.  [Reservations getting cancelled](#ReservationCancelled)
7.  [Sync state of reservation is changing to error while creating/updating](#SyncStateIssue)
8.  [Subscription not getting renewed](#SubscriptionRenewalIssue)
9.  [Sync past reservations is not working](#SyncPastIssue)
10.  [Not able to activate reservable sync configuration record / Activate button is not visible](#UnableToActivateRsv)
11.  [Fixes for common errors from outlook](#CommonErrors).

###       **Setup/Configuration Issue (Normal Mode)**

        Verify the below Application registry, Connection & credential aliases and Provider and Webhook registry records.

         1)  Navigate to application registry and open record with name "Microsoft Exchange Online\_clientCredentials" and check whether fields are populated and

               Also, Verify the **"OAuth Entity Scopes"** tab.

               ![](/sys_attachment.do?sys_id=19b597be471efd10f64de825126d43e7)

           2)  Validate connection & credential alias configurations

            a)  Navigate to Connection & Credentials  >   Credentials

                - Open record with name "MS Graph 1" and verify the field mapping

1.  1.  **OAuth Entity Profile** is "Microsoft Exchange Online\_clientCredentials default\_profile"

                \- Open record with name "MS Graph 2" and verify the field mapping

1.  1.   **OAuth Entity Profile** is "Microsoft Exchange Online\_clientCredentials default\_profile"

            b)  Navigate to Connection & Credentials  >  Connections

                - Open record with name "MS Graph 1" and verify the fields mapping

1.  1.    **Connection alias** is "sn\_ex\_online\_spke.Microsoft\_Exchange\_Online\_clientCred"
    2.   **Credential** is "Ms Graph 1" 
    3.  **Connection Url** is "[https://graph.microsoft.com](https://graph.microsoft.com)"

                - Open record with name "MS Graph 2" and verify the fields mapping

1.  1.    **Connection alias** is "sn\_ex\_online\_spke.Microsoft\_Exchange\_Online"
    2.   **Credential** is "Ms Graph 2" 
    3.  **Connection Url** is "[https://graph.microsoft.com](https://graph.microsoft.com)".

         3)  Verify the calendar provider/s

            - Navigate to "Calendar Provider" from filter navigation and open active record with Calendar processor as "Microsoft graph"

            - Verify the active reservable sync configuration with subscription field populated as per below reference.

               ![](/sys_attachment.do?sys_id=d1b5d7be471efd10f64de825126d4356)

        4)  Verify the webhook registry record  
          - Navigate to Microsoft Exchange Online Spoke > Webhook registry and open record with name "WSDRS Event Subscription" and verify the below fields  
             Client state,  
             Callbcak URL,  
             Path.  
  
       5)  For validating configurations on azure, use below doc as reference.  
             [Azure Setup Documentation](https://docs.servicenow.com/bundle/tokyo-employee-service-management/page/product/workplace-calendar-synchronization/task/authenticate-mxexchange-with-azure.html)

###       **Strict mode Issues (Client Credentials Grant Type)**

      Verify the Calendar provider and Application permissions on Azure portal.

         1) Navigate and open respective calendar provider and check the strict mode configuration as below 

           ![](/sys_attachment.do?sys_id=15b5d7be471efd10f64de825126d4352)

         2) Connection & Credentials configurations are same as in normal mode.

###    **Strict mode Issues (With Authorization Code Grant Type)**

    If customer is using multiple providers with different strict mode emails, Then overriding alias is must. Use this [Override Alias Doc](https://docs.servicenow.com/bundle/utah-employee-service-management/page/product/workplace-calendar-synchronization/task/create-own-credential-and-connection-alias-for-strict-mode.html "Override Alias Doc") to get more info.

    If customer is not using override alias and has only one provider, Follow the below steps.

       1) Open calendar provider and verify **Strict mode** is enabled and **Strict mode email** is not empty.

       2) Verify the below on Azure portal with customer.

             ![](/sys_attachment.do?sys_id=19b5d7be471efd10f64de825126d4331)

       3) Navigate to application registry and open record with name "Microsoft Exchange Online" and check whether fields are populated.

            ![](/sys_attachment.do?sys_id=d5b597be471efd10f64de825126d43eb)

       4) Validate connection & credential alias configurations

            a)  Navigate to Connection & Credentials  >   Credentials

                - Open record with name "MS Graph 1" and verify the field mapping

1.  1.  **OAuth Entity Profile** is "Microsoft Exchange Online default\_profile"

                \- Open record with name "MS Graph 2" and verify the field mapping

1.  1.   **OAuth Entity Profile** is "Microsoft Exchange Online default\_profile"

            b)  Navigate to Connection & Credentials  >  Connections

                - Open record with name "MS Graph 1" and verify the fields mapping

1.  1.    **Connection alias** is "sn\_ex\_online\_spke.Microsoft\_Exchange\_Online\_clientCred"
    2.   **Credential** is "Ms Graph 1" 
    3.  **Connection Url** is "[https://graph.microsoft.com](https://graph.microsoft.com)"

                - Open record with name "MS Graph 2" and verify the fields mapping

1.  1.    **Connection alias** is "sn\_ex\_online\_spke.Microsoft\_Exchange\_Online"
    2.   **Credential** is "Ms Graph 2" 
    3.  **Connection Url** is "[https://graph.microsoft.com"](https://graph.microsoft.com)

        5) **Note**: Once the entire setup is done, Navigate to credentials and open records **"MS Graph1"** & **"MS Graph 2"** and click on "**Get OAuth Token**" link and login  
              with strict mode user credentials.

###       **Reservations stuck in awaiting confirmation**

     Reservations gets stuck in awaiting confirmation for sync enabled rooms due to various reasons. So, lets divide the analysis into 2 parts

       **Part1 (WSD to Exchange)**

            Find out whether the call to exchange is successful or not by looking in to below points

1.  Synchronization state of reservation should be in "Synchronization required", Parallely look for the flow execution of  "Insert Calendar Sync Event"
2.  There should be an event created for this reservation in "**sn\_wsd\_rsvsync\_event**" table for the action(create/update/delete). If not, look for the flow execution "Generate Payload and Queue Event"
3.  Event record **State** should be processed and **Response** should contain "event\_id" & "icaluid". If not, we can find the error message in response itself or can refer to flow executions "Calender event create" for create & "Calender event update" for update.
4.  Finally, "**External Id"** and **"External Ical"** fields should be populated on Reservation record.

      **Part2 (Exchange to WSD)**

          Identify whether exchange has notified us back with confirmation or not.

1.  Open calendar provider and find the "Reservable sync config" record of the location from related list and check the fields **Active** is set to true and **Subscription** is populated.
2.  If subscription is not present, **Deactivate** the record and then **Activate** it back using **UI Actions**, Paralelly look for flow execution "**Create or Update Subscriptions for Resources**".
3.  If subscription is present, check the field **Status** is "Active", **Status code** is "200"/"201" & **Expiry Date** is in the future. If not, look for the latest execution of "**Renew Subscriptions**" flow and see any errors/logs present in "Context Record" of the flow for this subscription record.
4.  There should be an entry for the reservation in "**sn\_ex\_online\_spke\_events**" table (Filter the record using reservation subject / location / date / icaluid)
5.  If the entry for reservation is present in "**sn\_ex\_online\_spke\_events**" table and reservation is still in awaiting confirmation, Then look for system logs created around the event created time and start debugging the logic of scheduled job "**Create and Update Reservations from Events**" to find the root cause.
6.   If there is no entry in "**sn\_ex\_online\_spke\_events**" table, Look for the entries created in "**sn\_ex\_online\_spke\_webhook\_notification**" **OR**  "**sn\_ex\_online\_spke\_callback\_queue**" table which got created around same time frame (2-4 mins) when reservation was created. Use the filters as in below screenshot. ![](/sys_attachment.do?sys_id=6db5d7be471efd10f64de825126d438f) 
7.  If there is entry in "**sn\_ex\_online\_spke\_callback\_queue**" table but did not reflect in "**sn\_ex\_online\_spke\_events**" table, Start debugging **Business Rules** on the "**sn\_ex\_online\_spke\_callback\_queue**" table for respective change type.
8.   If there is entry in "**sn\_ex\_online\_spke\_webhook\_notification**" table but did not reflect in "**sn\_ex\_online\_spke\_callback\_queue**" table, Debug the schedule job "**Queue Webhook Events**" and look into system logs.
9.   If there is no entry in "**sn\_ex\_online\_spke\_webhook\_notification**" table, look for system logs created around that time with message "Client State is not valid".
10.   If there is errored log with message that contains "Client State is not valid" / "Client State validation", then customer has to generate new client state and recreate all subscriptions.
11.   If there is no such log, Then room has not accepted the meeting (We need to check / get confirmation from customer whether room has accepted the invite or not)
12.   If room has accepted the invite and no callback received, Outlook will sometimes miss to notify immediately, which it will do with delay after certain amount of time (mostly in 4-5 hours but some times it can take up to day)

###       **Reservations Getting Cancelled**

        Reservations gets cancelled by system in below cases

1.  If user manually cancels it from the portal (We can track it by looking for entry in "**sn\_wsd\_rsvsync\_event**" table by applying filter on reservation and action)
2.  If we receive callback from exchange to cancel the reservation (We can track it by looking for entry in "**sn\_ex\_online\_spke\_callback\_queue**" table), Please note that data in this table will get deleted based on retention policy. Mostly we will have 5 days old data.
3.  If reservation is stuck in awaiting confirmation with "External Ical" & "External Id" fields populated ,for more than 5 hours waiting for exchange to notify (This schedule job "**Clean-up Awaiting/Rejected Reservations**" cancels the reservation)
4.  If reservation is stuck in awaiting confirmation without "External Ical" & "External Id" fields populated (This schedule job "**Reservation daily tasks**" cancels reservations)

###       **Sync State of Reservation is Changing to Error While creating/updating**

     One of the possible reasons for this might be that an active reservable sync configuration record is present with both the fields  **Location** and **Configuration item** as empty.  
        This could be due to deletion of a space/room after configuring sync with it.

      **Fix**: The reservable sync configuration records should be deleted If both the fields location and configuration item are empty.

###    **Subscription Not Getting Renewed**

     There is a daily job "Renew Subscriptions" flow that runs every day to check and renew if any subscription is going to get expired in next 24 hrs.

1.   Verify the Connection & Credentials as per provider configuration.(Refer topic #1 & #2)
2.   Navigate to "Microsoft Exchange Online Spoke" > "Webhook Registry"  and open record "WSDRS Event Subscription" and verify Callback url, Client state and Path
3.  If the daily job has failed to handle it , Look in to the latest execution of the flow and determine the error.
4.  If the subscription Renewal fails while trying to generate from reservable sync configuration record , then look into the flow execution of "**Create or Update Subscriptions for Resources**".

###     **Sync past reservations is not working**

       Refer to the documentation [Link](https://docs.servicenow.com/en-US/bundle/vancouver-employee-service-management/page/product/workplace-calendar-synchronization/task/sync-past-reservation.html)

          The above documentation link helps only during initial setup. If customer wants to do **Past Sync** at later point of time after initial setup, Follow below steps.

1.  Navigate to All > Workplace Calendar Synchronization > Configuration > Calendar Providers
2.  Select the calendar provider for which you want to synchronize past reservations.
3.  On the Provider form, ensure that the Active option is enabled.
4.  Ensure that Sync past reservations field is enabled.
5.  Ensure that "Sync start time" and "Sync end time" is populated.
6.   From the related list, Open subscriptions related to reservable sync config records for which past sync needs to be performed. (Subscription status has to be active with Status code 200/201)
7.  Update the last sync time of those subscription records to date from which sync need to be performed. Also, make sure the difference between subscriptions "Last Sync Time" and Providers "Sync end time" is not more than 1825 days.
8.  Then Deactivate and Activate the reservable sync config record using UI Actions.
9.   Sync past will process in the back end and start pulling reservations . If not, start debugging the root cause from the BR "**Sync Past Events**" and system logs

###      **Not able to activate reservable sync configuration record / Activate button is not visible**

     Follow the below steps to activate/deactivate reservable sync configuration record's

1.  Navigate to All > Workplace Calendar Synchronization > Configuration > Calendar Providers
2.  Select the calendar provider to which reservable sync config records are linked to.
3.  From the related list "Reservable Sync Configurations" you can select single/multiple records and click on list choice menu to choose "Activate/Deactivate" UI Actions.
4.  If the activation is not happening, Debug the execution of flow "**Create or Update Subscriptions for Resources**" and find the root cause.

###     **Fixes for common errors thrown from outlook**

     [Refer to Microsoft error responses doc](https://learn.microsoft.com/en-us/graph/errors)

     Below are some common REST responses from exchange.

     1. “Access to oData is Disabled” / “Invalid Object” 

         **Fix**: **Resource/User needs to be in scope of tenant Id(Client Id)**

     2. “Resource not found" / "Invalid Resource” 

         **Fix: Verify the below points**

1.  Check whether given "Email ID" is valid or not
2.  Check whether there is proper resource mailbox for the email in "office.com" portal
3.  Resource/User needs to be in scope of tenant Id(Client Id)
