---
title: Toggle character count display for form fields in Grants Management
description: Toggle the character count for form fields in the Grants Management to display the remaining number of characters available in the text field.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/government-industry/psds-gmp-config-show-character-count.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Foundation, Grants Management, Playbooks and Solutions, Configure agent workspaces, Configure, Public Sector Digital Services \(PSDS\)]
---

# Toggle character count display for form fields in Grants Management

Toggle the character count for form fields in the Grants Management to display the remaining number of characters available in the text field.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **System Properties** &gt; **UI Properties**.

2.  Select **Character counter for text area \(journal and multi line text fields\)**.

    \[Omitted image "psds-config-gmp-character-counter-field.png"\] Alt text: Show character count prompt.

    When this property is set to true, the character counter will appear under the text area, displaying the remaining number of characters available in the text field. Once the character limit is reached, the entire text may not be saved.

3.  Navigate to a playbook form activity and verify that the character counter is visible.

    \[Omitted image "psds-gmp-character-count.png"\] Alt text: Program information activity.

    The character count is visible under the text area.


**Parent Topic:**[[psds-config-gmp-foundation|Configure Grants Management]]

**Previous topic:**[[psds-config-gmp-internal-team-default-roles|Configure read/write access roles for the Grants Management internal program team]]

**Next topic:**[[psds-config-gmp-setup-retention-policy|Configure a retention policy for grant cases in Grants Management]]

## Related

- [[psds-config-gmp-foundation|Configure Grants Management]]
- [[psds-config-gmp-internal-team-default-roles|Configure read/write access roles for the Grants Management internal program team]]
- [[psds-config-gmp-setup-retention-policy|Configure a retention policy for grant cases in Grants Management]]
