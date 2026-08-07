---
title: "[SAMP - Removal Candidate] The worknotes are not getting updated or not showing in activity on table Removal Candidate (samp_sw_reclamation_candidate)"
aliases:
  - KB0716642
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0716642
kb_number: KB0716642
last_modified: 2024-04-07
---

## \[SAMP - Removal Candidate\] The worknotes are not getting updated or not showing in activity on table Removal Candidate (samp\_sw\_reclamation\_candidate)

  

### Issue

# Symptoms

* * *

The worknotes are not getting updated or not showing in activity on table Removal Candidate (samp\_sw\_reclamation\_candidate).

# Release

* * *

Jakarta or later..

# Cause

* * *

Here the issue is not updating the worknotes. Originally the worknotes are getting updated but it is not being shown on the activity log. Reason for this is auditing is not enabled on it and it is expected that the journal fields work only on audited tables.

[https://docs.servicenow.com/csh?topicname=r\_JournalFields.html&version=latest](https://docs.servicenow.com/csh?topicname=r_JournalFields.html&version=latest)

# Resolution

* * *

Turn on auditing for this table and this can be very simple as below:

#1 Turn on Auditing on tables:

[https://docs.servicenow.com/csh?topicname=audited-tables-2.html&version=latest](https://docs.servicenow.com/csh?topicname=audited-tables-2.html&version=latest)

#2 Add the Additional comments field on the form layout and then remove it:

-   Change the application to "Software Asset Management Professional"
-   Now open one of the record on Removal Candidate able and right click on header and select form layout and add the field.

[![](/sys_attachment.do?sys_id=258c64aedb42b450e515c22305961997)](https://docs.servicenow.com/csh?topicname=basic-form-administration.html&version=latest)

![](/sys_attachment.do?sys_id=298c64aedb42b450e515c2230596199c)

[https://docs.servicenow.com/csh?topicname=basic-form-administration.html&version=latest](https://docs.servicenow.com/csh?topicname=basic-form-administration.html&version=latest)

# Additional Information

* * *

[https://docs.servicenow.com/csh?topicname=t\_AddAReclCandidate.html&version=latest](https://docs.servicenow.com/csh?topicname=t_AddAReclCandidate.html&version=latest)

[https://docs.servicenow.com/csh?topicname=basic-form-administration.html&version=latest](https://docs.servicenow.com/csh?topicname=basic-form-administration.html&version=latest)

[https://docs.servicenow.com/csh?topicname=audited-tables-2.html&version=latest](https://docs.servicenow.com/csh?topicname=audited-tables-2.html&version=latest)

[https://docs.servicenow.com/csh?topicname=r\_JournalFields.html&version=latest](https://docs.servicenow.com/csh?topicname=r_JournalFields.html&version=latest)
