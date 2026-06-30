---
title: User sensitive data logs
description: You can view the top 100 activity logs for specific real-time protection policies that contain the most sensitive data from the last month.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/data-privacy-classic/user-sensitive-data-logs.html
release: australia
product: Data Privacy \(Classic\)
classification: data-privacy-classic
topic_type: task
last_updated: "2026-06-25"
reading_time_minutes: 1
breadcrumb: [Real time protection, Data privacy, Data Privacy, Platform Privacy]
---

# User sensitive data logs

You can view the top 100 activity [[logs|logs]] for specific real-time protection [[ca-policies|policies]] that contain the most sensitive data from the last month.

## About this task

Role required: data\_privacy\_admin

## Procedure

1.  Navigate to **All** &gt; **System Security** &gt; **[[data-privacy-landing|Data privacy]]** &gt; **[[real-time-protection|Real time protection]]** &gt; **[[real-time-protection-policies|Real time protection policies]]**.

2.  Select **View logs** under the real-time protection policy that you want to view logs for.

3.  The report that displays shows the top 100 activity logs from the last month, sorted into the following information:

<table id="table_phv_pxf_m3c"><thead><tr><th>

Field

</th><th>

Definition

</th></tr></thead><tbody><tr><td>

Table

</td><td>

Table configured in the policy where user sensitive data was detected and alerted or blocked.

</td></tr><tr><td>

Column

</td><td>

Column configured in the policy where user sensitive data was detected and alerted or blocked.

</td></tr><tr><td>

Data pattern

</td><td>

Which sensitive data was alerted or blocked.

</td></tr><tr><td>

User

</td><td>

Username of the user who entered sensitive data.

</td></tr><tr><td>

Action

</td><td>

Which action was taken, either Alert or Block.

</td></tr></tbody>
</table>

## Related

- [[logs|Logs]]
- [[ca-policies|Policies]]
- [[data-privacy-landing|Data Privacy]]
- [[real-time-protection|Real time protection]]
- [[real-time-protection-policies|Real time protection policies]]
