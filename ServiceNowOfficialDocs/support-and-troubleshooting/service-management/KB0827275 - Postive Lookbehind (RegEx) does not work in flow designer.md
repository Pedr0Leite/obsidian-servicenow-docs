---
title: "Postive Lookbehind (RegEx) does not work in flow designer"
aliases:
  - KB0827275
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827275
kb_number: KB0827275
last_modified: 2024-04-08
---

## Postive Lookbehind (RegEx) does not work in flow designer

  

### Issue

When a string is passed in via the flow action's inputs, and then used with JS Regex Object, it does not work.  

Observe the following piece of code:  
  

```
var stringToMatch = "asdf\r\nasd\r\nfasd\r\nf\r\nRequested User:Jason Smith (AD\\1122334455884444)jason.smith@test.com\r\nd\r\ndddddd";var pattern1 = "(?<=\Requested User:).*";var regEx1 = new RegExp(pattern1, 'j');var stringfound1 = (regEx1.test(stringToMatch)) ? regEx1.exec(stringToMatch).toString() : '';gs.info(stringfound1);
```

  
if the stringToMatch & pattern1 variables are defined from the flow action's input, and the regex code is inside a script step, the regex will fail to match the pattern and will not return anything

  

**STEPS TO REPRODUCE:**

1.  Create a flow action with two string inputs, once for the string and another for the regex pattern
2.  In the action create a script step where the above code is ran to match a pattern and have the script step return the match  
    
3.  Test and add the following as inputs  
    

  
  
string to search:  

```
line 1line 2Requested User:Jason Smith (AD\1122334455884444)jason.smith@test.comline 4
```

  
  
Regex pattern used:  

```
(?<=\Requested User:).*
```

  
  
4\. Run test  
5\. Observe in the context in the script test, there are no values in the runtime value outputs

### Cause

\\r in the regex pattern is causing conflict when translated to java  

### Resolution

you can use the following pattern instead:  

```
(?<=Requested User:).*
```
