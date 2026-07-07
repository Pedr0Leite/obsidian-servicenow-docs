---
title: "Open tinymce for journal"
aliases:
  - Open tinymce for journal
tags:
  - servicenow-dev-program
  - code-snippet
  - open-tinymce-for-journal
  - browser-bookmarklets
---

# tinymce journal editor Bookmarklet Modal

This script is a bookmarklet that injects a draggable modal into a form (or ui page with access to ScriptLoader api in the content frame) with a tiny mce editor and buttons to insert the html to the journal fields on the form.

The dependency for tinymce is loaded from the instance itself and a html field does not need to be present on the form. 

---

## 📸 Screenshots

### Modal Overview
![Modal Overview](tinymce.png)

---

## 🔧 How to Use

1. **Copy the minified script** on the first line of the *Open tinymce editor in modal for journal fields.js* file
2. **Create a bookmark** in your browser.
3. Paste the script into the bookmark's URL field.
4. Navigate to a ServiceNow form and click the bookmarklet.
5. Input formatted text into editor and click a button from the bottom to set the html to the corresponding journal field with the [code] tags

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Copy URL to ServiceNow Journal/README|Copy URL to ServiceNow Journal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create new update set/README|Create new update set]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Create story task/README|Create story task]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Highlight Mandatory fields on form/README|Highlight Mandatory fields on form]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Impersonation/README|Impersonation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Browser Bookmarklets/Load List with Query/readme|Load List with Query]]
