---
title: "SAM - Reconciliation fails/completes partially with error : 'RhinoStackOverflowException: Maximum JavaScript call depth of 1000 exceeded"
aliases:
  - KB2636830
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2636830
kb_number: KB2636830
last_modified: 2026-05-22
---

## SAM - Reconciliation fails/completes partially with error : 'RhinoStackOverflowException: Maximum JavaScript call depth of 1000 exceeded''

  

### Issue

The SAM Reconciliation process fails with the following error:  
"org.mozilla.javascript.RhinoStackOverflowException: Maximum JavaScript call depth of 1000 exceeded".

You may also notice messages such as : 'Inferring allocated install suites for the Publisher \[publisher name\]'

### Release

All

### Cause

This likely indicates that this has something to do with how the software suites are configured is wrong. This may be customer configured, or from the  out-of-box SAM Content service data, or a conflicting combination.

-   The Stackoverflow error indicates that the code seems to use up more stack space than expected. The limit is huge, so something must be wrong. This is because of the recursive execution of the code caused by cyclic suite definitions.
-   The following is an example of a cyclic suite :

Suite A is the parent of suite B  
Suite B is the parent of Suite A

Suite definitions are configured in the following tables:

-   cmdb\_m2m\_suite\_model
-   samp\_m2m\_suite\_entitlement\_def

Customers are allowed to make suite configurations in the cmdb\_m2m\_suite\_model table (OOTB configurations from samp\_m2m\_suite\_entitlement\_def are also in this table) while suite configurations from Content are updated in the samp\_m2m\_suite\_entitlement\_def table. If cyclic suites as mentioned above are present in either of this table, this will cause recursion and stack overflow error which will in turn cause the reconciliation to fail.

The following script can be used to determine if there any cyclic suites present on a customer instance : Change the table name accordingly. NOTE: this is read-only and does not delete any records - only prints if any cyclic suites are present.

```
// Background Script: detect cycles in the suite relation table
(function () {
// Use the constant if available; fall back to the table name string if not.
var SUITE_TABLE = 'cmdb_m2m_suite_model'
// field names (adjust here if your dictionary uses different names)
var PARENT_FIELD = 'suite_parent';
var CHILD_FIELD = 'suite_child';

/**
* DFS: starting from `startNode`, follow edges startNode -> neighbor where record has suite_parent = current
* Return true if we can reach `targetNode`.
*/
function pathExists(startNode, targetNode) {
if (!startNode || !targetNode) return false;

var stack = [startNode];
var visited = Object.create(null);
visited[startNode] = true;

while (stack.length > 0) {
var curr = stack.pop();

// Expand neighbors: all records with suite_parent = curr
var suiteGr = new GlideRecord(SUITE_TABLE);
suiteGr.addQuery(PARENT_FIELD, curr);
suiteGr.query();

while (suiteGr.next()) {
var neighbor = suiteGr.getValue(CHILD_FIELD);
if (!neighbor) continue;

// Found a path back to targetNode
if (neighbor === targetNode) {
return true;
}

if (!visited[neighbor]) {
visited[neighbor] = true;
stack.push(neighbor);
}
}
}
return false;
}

var total = 0;
var cycles = 0;

var gr = new GlideRecord(SUITE_TABLE);
gr.query();
while (gr.next()) {
total++;

var parent = gr.getValue(PARENT_FIELD);
var child = gr.getValue(CHILD_FIELD);
var id = gr.getUniqueValue();

// Skip incomplete rows
if (!parent || !child) continue;

// Self-loop
if (parent === child) {
cycles++;
gs.warn('[SELF-LOOP] record=' + id + ' parent=' + parent + ' child=' + child);
continue;
}

// Check if this edge (parent -> child) closes a cycle:
// i.e., is there a path from child back to parent?
if (pathExists(child, parent)) {
cycles++;
gs.warn('[CYCLE] record=' + id + ' parent=' + parent + ' child=' + child);
}
}

gs.info('Suite cycle scan complete. Records scanned = ' + total + ', cycles found = ' + cycles);
})();
```

### Resolution

Ensure no cyclic suite definitions in the table : cmdb\_m2m\_suite\_model and samp\_m2m\_suite\_entitlement\_def and rerun reconciliation.

You can delete records manually from cmdb\_m2m\_suite\_model but for samp\_m2m\_suite\_entitlement\_def you would need to raise a content request.

Focus on direct cyclic suites such as A-> B, B-> A

If the fault is with SAM Content, then be sure to open a support case to report the issue, after searching our knowledge base in case we are already aware.

### Related Links

In one example, SAM Content included bad data for Quest Software, which caused this problem: [KB2606560 Software Asset Management - SAM Reconciliation For Quest Publisher- Failing with "org.mozilla.javascript.RhinoStackOverflowException: Maximum JavaScript call depth of 1000 exceeded" error.](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2606560)

ServiceNow also has a Problem recorded, still open as of May 2026, to try and avoid this sort of thing happening in the first placce:  
PRB1956893 SAM - Reconciliation fails/completes partially with error : 'RhinoStackOverflowException: Maximum JavaScript call depth of 1000 exceeded''
