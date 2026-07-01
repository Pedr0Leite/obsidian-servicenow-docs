---
aliases:
  - "Scripted Extension Point"
tags:
  - scripted-extension-point
  - script-include
  - scripting
  - design-pattern
---

# Scripted Extension Point

Yesterday I was reviewing some code in a vendor app, noticed a call with

```jsx
GlideScriptedExtensionPoint().getExtensions(..)
```

and I found myself asking, how do scripted extension points work?

**BENEFIT:**  It's possible to define a script include that declares methods as an "interface" and register other script includes to handle those methods with different implementations for different circumstances. Kind of like a generic script include that says what kind of work can be done, with some related script includes that actually do the work. The practical result is, an app developer can deploy an extension point to open up a spot where other developers can plug in their own script include to handle a particular circumstance.

**SCOPE:**  The scope of my experience is limited here. I reviewed work that others have built, and I built one sample project. *Mostly I just tried to condense the details down to the simplest explanation that could help me remember how it works.*

**OVERVIEW:**1. In the `[sys_extension_point]` table, define a script include to serve as interface definition (method signatures and their return types).2. On the record you made in step #1, use "Create Implementation" button to generate a copy of the interface script include, then edit the generated file to handle a specific circumstance.

- you can do this multiple times to create alternate versions of the script include with same method names but different implementations.
- each include has a boolean method which can tell if its applicable to the current situation.
- For example, a **handles()** method, can initialize internal variables if needed, then returns a boolean to the caller, true if it applies or false signals to ignore it. Note, some people choose different names for this boolean method. I've also seen it as, "shouldRun()" and other names.
- `//silly example where my include has an array of things to care about, //and I return true when the param received appears in there
handles: function(somethingToEvaluate) {return thingsThatICareAbout.some(function(a) {return a == somethingToEvaluate;});};// make method return true when this script include is relevant, should be used`

3. Create a wrapper script to call the implemented script include(s)

- wrapper asks for a list of the "extensions" for a script include name
- loops thru each "extension" calling the boolean "handles()" method, followed by other desired method if handles() returns true.
- For Example in your wrapper script:
    
    ```jsx
    var myExtensionPoint = "InboundTaskUtil";
    var relatedScriptIncludes = new GlideScriptedExtensionPoint().getExtensions(myExtensionPoint);
    
    for (var i = 0; i < relatedScriptIncludes.length; i++) {
    
        /* NOTICE--I DONT KNOW WHICH SCRIPT INCLUDE IM RUNNING. I CALL THEM ALL, ASKING EACH ONE
            IF IT "HANDLES" MY NEED, AND WHEN ONE RETURNS TRUE I CONTINUE DOING MORE WORK WITH IT */
        var ImplScriptInclude = relatedScriptIncludes[i];
        if (ImplScriptInclude.handles(requestBody.company)) {
    
            gs.info(ImplScriptInclude.type + " is handing.." + requestBody.company);
    
            ...DO THE MAIN STUFF YOUR SCRIPT NEEDS TO DO...
    
            var resultSysID = ImplScriptInclude.importTask(requestBody);
    
            // How will you end?
            // Return to caller after one script include has handled it?
            // Store some result from each one, and return at the end?
            // ..it's up to you
        }
        else {
            gs.info(ImplScriptInclude.type + " is NOT handing.." + requestBody.company);
        }
    }
    ```
    

**USE CASE:**  There are many use cases but the one I'm envisioning is when there are multiple different customer integrations for the same table, each with different rules.

**CREDITS:**  Other people's work that I reviewed to help me understand the layout of this includes:

Travis Toulson blog article: [Are Extension Points Worth It](https://codecreative.io/blog/are-extension-points-worth-it/)*Travis' article is interesting because he covers some earlier alternative ways that crafty developers achieved similar behaviors, before scripted extension points came to the platform.*

Cory Seering community article: [Extension Points and their uses](https://community.servicenow.com/community?id=community_blog&sys_id=83caf8c01bc8e4503222ea89bd4bcb97)*Cory's article is interesting because its much more detailed, covers additional types of extension points, and he probably has the most insight, since he helped create the extension point features for Servicenow!*

Additionally, I also reviewed content previously shared by [Maria Gabriela Ochoa Perez Waechter](https://community.servicenow.com/community?id=community_user_profile&user=fed09a21db981fc09c9ffb651f961944), so she gets some credit too.

[Links](Scripted%20Extension%20Point/Links%20319c42ce9a5680e6ba01c7c715665ea1.md)

## Related

- [[Server and Client Side Scripts]]
- [[Script include Advance structure - Inheritance]]
- [[Links]]