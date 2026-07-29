---
title: "Multi Factor Authentication (MFA) does not work with Google Authenticator. Response Invalid Error"
aliases:
  - KB0748960
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748960
kb_number: KB0748960
last_modified: 2025-01-16
---

## Multi Factor Authentication (MFA) does not work with Google Authenticator. Response Invalid Error

  

### Issue

When configuring the Google Authenticator plugin in Chrome, or using any other MFA tool from your phone, and scanning the coded image, the tokens are not valid and error :  "Response not valid". 

### Cause

The root cause is time synchronization. Multi-Factor authentication with a cellphone application is very time sensitive. If the phone does not get network time, the time difference between the phone that has the MFA code and the instance might be greater than the life-time for the MFA token.

### Resolution

First, you should set up your phone to use the network time. 

For an **Android** devices, go to:  
  

↳ _Settings > System > Date and Time_ and ensure that "Use network-provided time" is selected.

↳ If this is not selected, please select and retry the MFA registration.

For **iOS** devices, go to:  
  

↳ _Settings > General > Date & Time > Time Zone_ and Turn on "_Set Automatically_". This automatically sets your date and time based on your time zone.

If you use Google Authentication, you should also change the Google chrome Authenticator plugin settings.

Select option to sync the clock with Google. See screen print below.

![](sys_attachment.do?sys_id=7b95905cdb754110fd63250913961914)
