---
title: "Setting 'setSectionDisplay' function to 'false' does not hide the form section."
aliases:
  - KB0696583
tags:
  - servicenow
  - support-kb
  - client-scripts
  - GlideForm
  - ui-policy
  - g_form
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696583
kb_number: KB0696583
last_modified: 2025-07-15
---

## Setting 'setSectionDisplay' function to 'false' does not hide the form section.

  

### Issue

After setting the `g_form.setSectionDisplay` function to 'false' in a client script, it does not hide the form section on page load.

g\_form.setSectionDisplay('<section\_name>', false);

### Release

.

### Cause

There could be two causes for this:

1.  The setSectionDisplay function not working properly is due to how the section name is used within the function.
2.  There are mandatory fields within the section that is being hidden.

### Resolution

#### For #1

As per the documentation on [setSectionDisplay](https://docs.servicenow.com/bundle/sandiego-application-development/page/app-store/dev_portal/API_reference/GlideForm/concept/c_GlideFormAPI.html#r_GlideFormSetSectionDisplay_String_Boolean "setSectionDisplay"), the section name is in lowercase with an underscore replacing the first space in the name, and with the remaining spaces being removed.

For example:

"**Section Four is Here**" becomes "**section\_fourishere**".

Other non-alphanumeric characters, such as ampersand (&), are removed.

\*\*Section names can be found by using the getSectionNames() method.

#### For #2

It is expected behavior that if there are empty mandatory fields within the section being hidden the section itself will not be hidden. The reason is that users won't be able to see which mandatory fields to fill out if the section that contains them is hidden. If all mandatory fields have values then the section will hidden.

_\*note - In workspace forms, there was a defect where if the section contained any mandatory field, the section would not be hidden, even if the mandatory field had a value. The was resolved in Y release to match the UI16 behavior._

### Related Links

-   [GlideForm Client](https://docs.servicenow.com/csh?topicname=c_GlideFormAPI.html&version=latest "GlideForm Client")
-   [GlideForm - setSectionDisplay](https://docs.servicenow.com/bundle/sandiego-application-development/page/app-store/dev_portal/API_reference/GlideForm/concept/c_GlideFormAPI.html#r_GlideFormSetSectionDisplay_String_Boolean "GlideForm - setSectionDisplay")

## Related

- [[KB0697413 - In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()]]
- [[KB0711972 - oldValue returns empty value instead of the previous value for onChange client scripts]]
- [[KB0720671 - Generic error on form Submit canceled due to a script error - please contact your System Administrator]]
