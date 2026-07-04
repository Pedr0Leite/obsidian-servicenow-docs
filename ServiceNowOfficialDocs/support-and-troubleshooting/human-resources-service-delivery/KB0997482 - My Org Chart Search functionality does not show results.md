---
title: "My Org Chart Search functionality does not show results"
aliases:
  - KB0997482
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997482
kb_number: KB0997482
last_modified: 2025-09-03
---

## Issue

The search functionality does not always display results when we search by First Name or Last Name

## Resolution

If you are still using the Organization Chart (CD) functionality, please note that you can offer a better org chart experience with the new org chart functionality available in the Employee Center Pro application. The newer org chart provides an updated UI experience and more configuration capabilities than the older org chart available in the Content Publishing application. More information can be found here: [Organization chart](https://docs.servicenow.com/csh?topicname=employee-profile-org-chart.html&version=latest)

\----

The best solution is to ensure that the "User Display Configuration" \[sn\_cd\_user\_display\_configuration\] is configured correctly as per the [Organization Chart (CD)](https://docs.servicenow.com/csh?topicname=ec-org-chart-configuration.html&version=latest) documentation.

For example, if your User \[sys\_user\] records don't have related HR Profile \[sn\_hr\_core\_profile\] records, use a User Display Configuration pointing to the sys\_user table, searching in sys\_user might return records that don't have a related sn\_hr\_core\_profile. If the User Display Configuration is looking for a field on the HR Profile, it would fail to return anything.

\----

If that is still not working, as a workaround, two possible changes can be made to get the search working, but both will require making code changes to either the original widget or a copy of the widget. 

Changing the widget itself will prevent the widget from receiving any future updates, so our recommendation would be to make a copy of the widget, make the changes there and use the copied version on the portal for the time being. The steps for creating this copy are as follows:   
\- In the left nav go to Service Portal -> Widgets  
\- Search for "Organization Chart (CD)"  
\- Open the widget record  
\- In the top right click the "Clone Widget" button  
\- Go to the Org Chart page  
\- Remove the "Organization Chart (CD)" widget instance from the page and add a new widget instance using the copied version in the same place  
  
The first option is to remove the paging so all the matching users are returned at once. This is a simpler change but it could become a performance problem if the number of users in the system grows too large.

Steps for this are as follows:   
\- Open the record for the copied version of the widget  
\- In the "Server script" field, search for line:

`res.chooseWindow(10 * pg - 10, 10 * pg);`

\- Remove or comment out that line  
\- Update the widget and then test the search functionality again

  
The second option is a change to the client code for the widget to make additional calls for more users if none were returned in the first request. This is a slightly for involved change but won't have the same performance concerns as option 1. Steps are as follows:  
\- Open the record for the copied version of the widget  
\- In the "Link" field, find these line

```

if (data.orgChart && data.orgChart.searchRes) {
makeSearchRes(data.orgChart.searchRes);
more = (CONST.maxShowSearch * q.page) < data.orgChart.searchResCount;
}
```

\- and replace them with:

```
if (data.orgChart.searchRes.length > 0)
q.callback({
results: s.searchRes || [],
page: q.page + 1,
more: more
});
else if (more) {
q.page = q.page + 1;
s.searchForPerson(q);
}
```

or with:

```
if (more && data.orgChart.searchRes.length == 0) {
q.page = q.page + 1;
s.searchForPerson(q);
}
else {
q.callback({
results: s.searchRes || [],
page: q.page + 1,
more: more
});
}
```

\- Update the widget and then test the search functionality again.
