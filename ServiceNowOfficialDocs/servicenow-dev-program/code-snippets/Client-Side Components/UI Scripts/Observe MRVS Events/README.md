---
title: "Observe MRVS Events"
aliases:
  - Observe MRVS Events
tags:
  - servicenow-dev-program
  - code-snippet
  - observe-mrvs-events
  - ui-scripts
---

# Observe Multi-row variable set events

Using the MutationObserver API we can monitor changes to a multi-row variable set (i.e., new rows, deleted rows and updated rows).
This currently only works in the platform, not Workspace or Service Portal.

Use in a onLoad client script (Isolate script = false).  Sets up an observer on the named variable set and any changes are returned in the mutationList object.
Return value will list changes to the variable set.  For example:

```json
{
   "removed": [
      {
         "VM #": "2",
         "Name": "2",
         "row_number": 1,
         "row_id": "row_9652c56347f5311001612c44846d433f"
      }
   ]
}
```


```javascript

function onLoad() {
	
    setTimeout(function() {
	var mrvs = new MRVSUtils('name of multi-row-variable-set');
        var observer = new MutationObserver(function(mutationList, observer) {
            var modifiedData = mrvs.processMutations(mutationList);
            console.log(JSON.stringify(modifiedData, '', 3));
        });

        // create the observer looking for changes to the contents of the MRVS
        observer.observe($(mrvs.getTableID()), MRVSUtils.OBSERVER_CONFIG);

    }, 1000);

}
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Custom Change Schedule/README|Custom Change Schedule]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Disable Copy Paste For Portal/README|Disable Copy Paste For Portal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Display number of created records/README|Display number of created records]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Make OOB Attachment Mandatory/README|Make OOB Attachment Mandatory]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/PersistentAnnouncementBanner/README|PersistentAnnouncementBanner]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Scripts/Prevent right click on portals/README|Prevent right click on portals]]
