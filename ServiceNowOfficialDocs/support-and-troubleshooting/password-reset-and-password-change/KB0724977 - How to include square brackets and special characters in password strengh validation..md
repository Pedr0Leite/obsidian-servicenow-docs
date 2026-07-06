---
title: "How to include square brackets and special characters in password strengh validation."
aliases:
  - KB0724977
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724977
kb_number: KB0724977
last_modified: 2024-04-07
---

## How to include square brackets and special characters in password strengh validation.

  

### Issue

Out of the box password validation script will not check for special characters. Also, in special special characters, we need to handle square brackets(\[\] )differently since they have special meaning in regex.

Follow the below process to include special characters and square brackets(\[\]) in password validation.

### Release

All versions.

### Resolution

-   Password validation is done by the below script OOB:
    -   https://<Instance\_name>.service-now.com/nav\_to.do?uri=pwd\_cred\_store\_type.do?sys\_id=e611433fbf020100710071a7bf073921
-   Out of the box code the below regex to verify the password strength:
    -   ^(?=.\*\\d)(?=.\*\[a-z\])(?=.\*\[A-Z\]).{8,}
-   Note that all the special character can be placed in between \[\] except -(Hyphen) and the brackets themselves. Please provide escape sequence character \\ before \[, \] and -.
-   Change it to below regex to include special character along with square brackets\[\]:
    -    ^(?=.\*\\d)(?=.\*\[a-z\])(?=.\*\[A-Z\])(?=.\*\[\\\\\\\[\\\\\\\](){}?\\\\\\\\|,.<>;:!~\*\_@#$%^&+=\\-\]).{8,}$

### Related Links

The below regex tester can be used to test your regular expression.

[https://www.regextester.com/1969](https://www.regextester.com/1969)

Use the below online javascript tester to check if your code works:

[https://www.webtoolkitonline.com/javascript-tester.html](https://www.webtoolkitonline.com/javascript-tester.html)

**NOTE:** Above two links are external links and subject to change. ServiceNow will not take any responsibility of the content of the information in the above websites.
