---
title: "Browse near a person is providing an option to select the reservation dates only for 7 days."
aliases:
  - KB1338750
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1338750
kb_number: KB1338750
last_modified: 2026-06-09
---

## Browse near a person is providing an option to select the reservation dates only for 7 days.

  

### Issue

Reserve a workplace item such as a room for a single or recurring meeting and also we can browse rooms based on near by a person.  
The issue is the dates that can be selected only for 7 days in start and actual end date.

Steps to reproduce:  
1.Navigate to Workplace Core and open the Workplace service portal.  
2.In workplace service portal homepage we can find the make a reservation.  
3.Select the option browse near a person.  
4.We can find that it is allowing dates only for 7 days.

### Release

every

### Cause

This is an expected behaviour as per the configuration set in below script include.  
https://<instance-name>.service-now.com/sys\_script\_include.do?sys\_id=b77f2d1dc3511010cc7060bf4b40dd67

### Resolution

To change the restriction for more than 7 days please do customize below script include.  
https://<instance-name>.service-now.com/sys\_script\_include.do?sys\_id=b77f2d1dc3511010cc7060bf4b40dd67

Note: Please do note that adding more no of days might block room for more days and cause an behaviour impact.
