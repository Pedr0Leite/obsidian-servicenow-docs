---
title: "Ensuring that Inbound Email Actions always work regardless of text case sensitivity"
aliases:
  - KB0535584
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535584
kb_number: KB0535584
last_modified: 2026-04-22
---

## Ensuring that Inbound Email Actions always work regardless of text case sensitivity

  

### Issue

Sometimes an Inbound Email action will not behave as expected, because the string comparisons it uses are case-sensitive, and the incoming email's text does not match upper- and lower-case characters exactly. There are two places where case-sensitive string comparisons are important:

1.  For early product families, **Inbound Email Configuration** properties that determine when an email should be treated as a **Reply** or a **Forward**.
2.  Custom scripts that you write, which contain case-sensitive string comparisons.

### Release

Since Calgary/Dublin

### Resolution

# Procedure for Ensuring Inbound Email Configuration Matches Upper- and Lower-case

In current releases, the reply and forward prefixes perform case-insensitive comparisons.

# Procedure for Ensuring Your Custom Scripts Work with Case-Insensitive Text

If your Inbound Email action scripts contain Javascript patterns similar to the following, then it is best practice to review your code for possible case-sensitivity issues. An example of case-sensitive Javascript looks like this:

**Bad practice, because indexOf() requires perfect case-sensitive comparison:**

if (yourVariable.indexOf("Incident Opened") != -1) {  
    // Do something important here, based on text "Incident Opened"    // The problem is that "Incident **O**pened" will not match  
}

**Best practice:**

if (yourVariable**.toLowerCase()**.indexOf("**i**ncident **o**pened") != -1) {  
    // This will match "Incident Opened", "**i**ncident Opened", "Incident **o**pened", etc.  
}
