---
title: "SAM - Import Adobe User Subscriptions: End-to-End Technical Guide"
aliases:
  - KB2966148
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2966148
kb_number: KB2966148
last_modified: 2026-04-21
---

## SAM - Import Adobe User Subscriptions: End-to-End Technical Guide

  

### Summary

This article explains everything that happens — technically and functionally — when the SAM - Import Adobe User Subscriptions scheduled job runs. It is written for someone who needs to understand not just what the job does, but how it does it, why each decision was made, and what to look at when something goes wrong.

**What This Job Is and Why It Exists**

Every Friday in the morning, a scheduled job quietly wakes up inside ServiceNow and begins a conversation with Adobe. Its sole purpose is to answer one question — who in your organization has an Adobe license right now, and is ServiceNow's records reflecting that accurately?                                         

The job is called SAM - Import Adobe User Subscriptions. It lives in the sysauto\_script table, belongs to the SaaS License Management Adobe Integration package, and runs inside the Software Asset Management - SaaS License Management application scope. It has been doing this every Friday without anyone having to think about it, keeping Adobe license data in sync so that SAM administrators always have an accurate picture for compliance, cost tracking, and reclamation.                                                                                                                                                                                                                      

**How the Story Begins — The Scheduled Job Script**

Before anything meaningful happens, the job does two things that set the stage for everything else.

First, it writes a record into the samp\_job\_log table. This happens before any processing begins. The reason is simple — if the job crashes halfway through, there is still proof it started. The log entry gets updated at the very end with either completed or failed, and if failed, the exact error message that caused it.                                      

Second, it checks whether the plugin sn\_sam\_saas\_int is active on the instance. This is the SaaS License Management engine. Without it, none of the script includes, tables, or logic that power the sync exist. If the plugin is off, the job marks itself failed in the log and exits immediately. There is nothing more to do.                                     

If both checks pass, it hands control over to the real engine — SamImportUserSubscriptionsAdobe.                                                                                          

**The Engine and How It Decides What to Process**             

SamImportUserSubscriptionsAdobe does not work alone. It extends a base class called AssetManagementPerGlideRecordBaseJob. Think of the base class as a factory floor manager. It knows how to walk through a list of records one by one and call a specific function for each. The child class just needs to tell it what records to fetch and what to do with each one.                                                                                                                                                          

The records it fetches come from samp\_sw\_subscription\_profile — the table where Adobe integration profiles are stored. But it does not fetch all Adobe profiles. It applies two filters. The profile\_type must equal adobe\_subscription, and the custom\_properties field must contain the text validate\_connection success. This second condition is the important one.

An admin must have previously opened the profile, clicked the validate connection button, and confirmed that ServiceNow can actually reach Adobe using the credentials on that profile. If that validation was never done or failed, the profile is silently excluded. The job only processes connections it knows are working.

For each profile that passes this filter, it calls importSubscriptionForProfile — the heart of the entire operation.                                                                        

**Getting Past Adobe's Front Door — Authentication**          

Before ServiceNow can ask Adobe anything, it needs to prove who it is. The profile holds everything needed to authenticate, and the authentication\_type field on the profile tells the job which method to use.

If the authentication type is jwt, the job builds a structured payload containing the Adobe Organization ID as the issuer, the Technical Account ID as the subject, a specially formatted audience URL built from the Client ID, an expiry timestamp set 24 hours into the future, and a metascope claim that grants access to Adobe's User Management SDK.

This payload is then signed using the RS256 algorithm with a certificate that is stored securely in ServiceNow's certificate store. The certificate's sys\_id, alias, and encrypted password are all read from the profile. The signed JWT is then sent to Adobe's IMS token exchange endpoint as a form-encoded POST request along with the client\_id and client\_secret.   

Adobe validates the signature and returns a short-lived access token.                                                                                                                                             

If the authentication type is oauth, the journey is different. The job reads the connection alias from the profile, looks up the associated http\_connection record, navigates to the linked oauth\_entity\_profile, and from there extracts the client\_id, client\_secret, and app\_registry name. The client secret is decrypted on the fly using the platform's built-in decryption — it is never logged or stored in plain text anywhere. The job then calls GlideOAuthClient.requestToken() using the client\_credentials grant type with scopes openid, AdobeID, and user\_management\_sdk. Adobe returns the access token directly.

Whichever method was used, the access token is then set on the REST client and injected into every subsequent API call as a Bearer token in the Authorization header, alongside the x-api-key header which Adobe requires for all User Management API requests.                                                               

**The REST Client and How It Talks to Adobe**                 

All actual HTTP communication with Adobe flows through SampAdobeRestClient. One of its most important behaviors is how it handles failure. Every API call goes through a retry mechanism that makes up to three attempts before giving up. It specifically watches for HTTP status codes 429 which is Adobe's rate limit response, as well as 502, 503, and 504 which indicate Adobe's servers are temporarily struggling.

When it sees any of these, it checks whether Adobe sent back a Retry-After header. If yes, it waits exactly that many seconds plus one second of buffer. If no header was provided, it starts with a 60 second wait and doubles it on each subsequent retry. Only after three failed attempts does it throw an error and let the calling code deal with it. This behavior means the job respects Adobe's systems and coexists cleanly with anything else in the organization that might be hitting the same API.

The job makes three categories of calls to Adobe. It fetches the full list of products for the organization once — this gives it the product codes and names for everything the org has licensed. It then paginates through product groups, incrementing a page counter until Adobe signals that the last page has been reached. Finally, for each product group, it paginates through the group's members, fetching users page by page until there are no more.

**Loading the Exclusion Rules Before Touching Any Data**

 Before the import begins, the job loads two sets of rules into memory that control who and what gets skipped.

The first set comes from samp\_sw\_subscription\_id\_excl\_rule. These are product code exclusions. An admin may have said that a certain Adobe product identifier should never be imported into ServiceNow — perhaps it is a test license or an internal entitlement that should not appear in SAM reporting.     

The second set comes from samp\_sw\_subscription\_user\_excl\_rule. These are user exclusions. Specific email addresses or UPNs can be excluded, either globally or scoped to a specific profile type. A user with no profile\_type on their exclusion record is excluded from all Adobe profiles.

If the combined total of all applicable rules is under ten thousand, the job loads them all into a simple in-memory dictionary where the lookup is instantaneous. If there are more than ten thousand rules, it skips caching to avoid memory issues and falls back to querying the database individually for each user and product it encounters. Either way the logic works — the cached path is just dramatically faster.

**The Import Itself — Ten Steps That Keep Everything in Sync**

**Deactivating everything first :** The job begins the actual sync by marking all currently active subscription records for this profile as inactive in samp\_sw\_subscription. It uses a bulk update with setWorkflow disabled and updateMultiple — bypassing Business Rules entirely. This is intentional. With potentially thousands of records, triggering business rule chains on each one would make the job run for hours. By marking them all inactive upfront, the job creates a clean slate and enters what is known as a soft delete pattern. Anything that gets re-confirmed from Adobe will be marked active again. Anything that does not get confirmed will be deleted at the end.                                                  

**Creating a picklist entry:** Before writing subscription data, the job ensures a choice record exists in sys\_choice for the instance\_name field on samp\_sw\_subscription. This is how the profile's name appears in dropdown fields on subscription records. If the choice already exists nothing happens. If not, it is created using the modern GlideQuery API. The profile's display\_name is used as the label, trimmed to 100 characters.

**Fetching everything from Adobe:** The job calls getProducts() once to get all product codes the org has. Then it loops through all product groups. Only groups where the type field equals PRODUCT\_PROFILE are relevant — Adobe returns other group types that have no bearing on licensing. At the same time it pre-loads from samp\_sw\_subscription\_product\_definition any records whose external\_id starts with ADOBESINGLEAPP\_ into a local dictionary. This is used a moment later to identify single app licenses.

**Figuring out what each group represents:**  Adobe has two fundamentally different types of product groups. Suite licenses like Creative Cloud All Apps bundle many products together. Single app licenses like Photoshop or Illustrator are one specific tool. The job detects which is which based on how Adobe names the group.                                        

For suites, it matches the group's productName against the products list, stripping out any keyword annotations Adobe may have added in parentheses before comparing. For single apps, Adobe formats the name as something like Photoshop followed by parentheses containing keywords including the text Single App - Enterprise. The job finds the position of the phrase Single App within the name, extracts everything from that point to the next comma or closing parenthesis, and uses that as the product code. It also checks whether an ADOBESINGLEAPP\_Photoshop entry exists in the pre-loaded dictionary to determine the assigned\_software\_identifier, which matters for cost allocation and reclamation later.

**Creating or updating subscription records:** For each active user in each product group, the job first checks the exclusion rules. If the user's email or the product code matches any exclusion, the record is skipped entirely. Otherwise it queries samp\_sw\_subscription looking for an existing record that matches on subscription\_profile, external\_user\_id, and subscription\_identifier together. If one is found it updates the record and marks it active again. If not, it creates a new one using insertDisableBR which skips Business Rules for performance.

Every record written gets its active flag set to true, user\_principal\_name and external\_user\_id populated from Adobe, subscription\_identifier set to the product code, subscription\_profile linked back to the profile, sourced\_from\_integration set to yes, and instance\_name set to the profile sys\_id corresponding to the picklist entry created earlier.         

**Resolving the software model:** Every subscription record must be linked to a software model in cmdb\_software\_product\_model for SAM to do anything useful with it — cost tracking, compliance, reclamation. Resolving a product code to a software model follows a waterfall of four increasingly expensive lookups.                                                    

The first level is an in-memory dictionary called skuSoftwareModelMap that persists across the entire job run. If the same product code has already been resolved once, the cached sys\_id is returned with zero database queries. On a large Adobe organization with thousands of users sharing a handful of product codes, this eliminates the vast majority of resolution work.                                          

The second level checks whether any existing subscription record with the same product code and profile type already has a software model set. If yes, that model is reused.                                                                                                                                                                                          

The third level queries samp\_sw\_subscription\_product\_definition for an active record matching the product code and profile type, navigates to the linked samp\_sw\_entitlement\_definition, and then queries cmdb\_software\_product\_model matching across product, version, edition, platform, language, and their corresponding operators. If exactly one model matches it is used. If multiple match, the oldest one by creation date is returned. If none match, the job automatically creates a new software model from the entitlement definition.

The fourth level handles complete resolution failure. The product code is recorded in samp\_sw\_unrecognized\_subscription\_identifier so an admin can see it and manually map it to the correct model. If an admin has already done that mapping from a previous run, the mapped model is returned and the subscription is populated correctly going forward.            

**Matching Adobe users to ServiceNow users:** Each subscription needs to know which sys\_user record it belongs to. The job queries sys\_user looking for a record where email matches the UPN, or where user\_name matches the portion of the UPN before the at symbol. Active users are preferred over inactive ones. A system property called                sn\_itam\_samp.user\_resolution\_exclude\_table can hold table names to exclude from this search, useful when extended user tables should not be considered.

Alongside the sys\_user match, the job maintains samp\_discovered\_user records. These track Adobe users independently of whether they exist in sys\_user yet. The coalesce key is external\_user\_id. If a discovered user record already exists for this email and profile type combination, its user reference is updated. If not, a new one is created with the      display\_name set to the portion of the UPN before the at symbol. The subscription record is then linked to its discovered user.

**Stamping last activity:** Knowing someone has a license is not enough — SAM needs to know if they are actually using it. The job loops through all active subscriptions for the profile and looks up records in samp\_sw\_usage, which holds software usage telemetry. For Creative Cloud All Apps subscriptions it first resolves all child component products throughsamp\_m2m\_suite\_entitlement\_def using a GlideAggregate query grouped by child product, then searches usage across all of them. For single app subscriptions it queries usage only for that specific product. The maximum last\_used\_time found is written back to the subscription as last\_activity. This single date field is what the reclamation engine later uses to identify licenses that have gone unused for too long.                                                                                                                                                                                                                              

**Creating the reclamation rule:** After the subscription data is in shape, the job checks whether a reclamation rule exists in samp\_sw\_reclamation\_rule for Creative Cloud, linked through samp\_m2m\_rule\_product. If a rule already exists nothing changes. If not, it creates one with a 60 day inactivity threshold, reclamation type set to last\_used\_date, user notification enabled, a 3 day advance warning before reclamation, and a minimum of 3 subscribed products threshold that is specific to Creative Cloud's suite nature. It then creates a parent M2M record linking the rule to Creative Cloud, and child M2M records for each Creative Cloud component product resolved from samp\_m2m\_suite\_entitlement\_def. This entire operation is idempotent — it checks before inserting and will never create duplicate rules.                                                                                                                                                                                    

**Cleaning up the leftovers:** Any subscription records that are still marked inactive at this point were in ServiceNow from the previous sync but did not appear in Adobe's data this time. These users have lost their Adobe licenses, left the organization, or had their access removed. Their records are permanently deleted using deleteMultiple without workflow, keeping the subscription table clean and accurate.

**The Safety Net — What Happens When Things Go Wrong**

 The entire import process for each profile is wrapped in a try-catch block. If anything throws an exception at any point — an Adobe API timeout, an unexpected null value, a database error — the catch block immediately calls markSubscriptionActive() which runs a bulk update restoring all subscription records for that profile back to active. No data is lost.

The instance ends up exactly where it started before this run. The error message and profile sys\_id are thrown upward, caught by the scheduled job script, and written into samp\_job\_log as the failure reason. The next Friday the job tries again from scratch.                                                                              

**Making Sure Two Copies Never Run at the Same Time**         

Before any processing begins, the job checks sys\_trigger for entries related to its own sys\_id where state equals 1, meaning currently executing. If it finds two or more such entries, it means another instance of the same job is already running — perhaps the previous run is still going. In that case it logs an error and exits immediately. This guard exist because two instances running simultaneously would conflict destructively — one deactivating records while the other is trying to reactivate them. Additionally any job log records from previous runs that are stuck in in-progress are bulk-updated to failed before execution begins, preventing stale log entries from polluting reporting.                      

**After All Profiles Are Done**                               

Once every Adobe profile has been processed, control returns to the scheduled job script which calls SampSubscriptionUtil.countAllSubscriptionsInstalls(). This recounts the total number of subscription installs across the entire instance and updates aggregated counts used by SAM dashboards and compliance reports. Then the job log is updated to completed and the job goes back to sleep until next Friday.                                                                                                                                                                                                                                                     

**Where to Look When Things Go Wrong**                        

If the job failed, the first place to go is samp\_job\_log. Find the most recent record for this job and read the message field. It will tell you exactly which profile failed and what the exception was.

If subscriptions are missing after a successful run, open the integration profile in samp\_sw\_subscription\_profile and look at custom\_properties. The validate\_connection field must say success. If it does not, the profile was never processed.                                                                                                         

If subscription records exist but have no software model, the product code from Adobe is unrecognized. Check samp\_sw\_unrecognized\_subscription\_identifier, find the product code, and manually link it to the correct cmdb\_software\_product\_model record.              

If a subscription is not linked to a sys\_user, check whether the Adobe UPN matches the email or user\_name of any active user in sys\_user. Also check both exclusion rule tables to confirm the user is not being skipped.

If the job did not run at all, check sys\_trigger for this job's sys\_id. A record stuck in state 1 from a crashed previous run can block future executions.          

If Adobe authentication is failing, check the profile's authentication\_type. For JWT verify the certificate has not expired. For OAuth check the http\_connection record and confirm the linked credential is still valid and the OAuth token has not been revoked.
