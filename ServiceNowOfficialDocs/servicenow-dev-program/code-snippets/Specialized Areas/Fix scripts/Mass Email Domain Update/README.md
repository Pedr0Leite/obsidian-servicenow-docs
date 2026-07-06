---
title: "Mass Email Domain Update"
aliases:
  - Mass Email Domain Update
tags:
  - servicenow-dev-program
  - code-snippet
  - mass-email-domain-update
  - fix-scripts
---

# Update User Email Domain in ServiceNow

This script finds all users in the **`sys_user`** table whose email addresses contain an old domain (e.g. `bad_domain.com`) and replaces it with a new domain (e.g. `new_domain.com`) using **regular expressions**.

---

## Purpose

To bulk–update user email domains safely and efficiently without manual edits.

Example use case:
 When your organization migrates from `@bad_domain.com` to `@new_domain.com`, this script updates all users automatically.

---

## Example
| Old Email              | New Email              |
|-------------------------|------------------------|
| alice@bad_domain.com    | alice@new_domain.com   |
| bob@bad_domain.com      | bob@new_domain.com     |
| carol@bad_domain.com    | carol@new_domain.com   |

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Adjust Variable Order on Catalog Item/README|Adjust Variable Order on Catalog Item]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
