---
aliases:
  - "Guarded Scripts"
tags:
  - knowledge-base
  - platform
  - security
  - server-side-scripting
  - sandbox
---

# Guarded Scripts

You thought on upcoming rollout KB2944435 Server-Side JavaScript Sandbox Replacement?
Question
My boss just assigned me to review the upcoming security feature that will force admins/developers to review the flagged scripts under Incompatible Guarded Scripts to make a change in the script(by moving the code to the script include) or exempt them before it gets to Phase 3, where it will block the flagged scripts from executing if not changed or exempted. What are your thought on that new feature? It mentioned Sandbox, and I want to make sure if that only applies to sandbox instances or applies to all kinds of instances, including production?

EDIT: I have pasted the KB2944435 because I do not have access to the link to that article since it seems to be only accessible to business accounts.

Quick Summary
What you need to know: ServiceNow is enhancing instance security by restricting the type of code that can run in server-side sandbox contexts (such as filters and default values). Simple scripts (basic function calls and expressions) will continue to work with no changes. Complex scripts (those using variables, if/else logic, loops, or multiple statements) will need to be moved into a script include. Your instance automatically identifies affected scripts in the Incompatible Guarded Scripts list (once on a version identified in the Rollout Schedule below) — no setup needed. Client-side JavaScript and code inside script includes are not affected. On upgraded cloud instances, enforcement for authenticated traffic phases in automatically over approximately four weeks, with automatic exemptions to protect existing functionality. On-premises instances begin detection automatically but require administrators to advance to each enforcement phase manually.

Am I Affected?
If your instance uses any of the following, you may have scripts that need updating:

javascript: prefixes in filters or conditions

Dynamic default values with more than a simple function call

AMB or RecordWatcher conditions with complex expressions

The fastest way to check: Navigate to the Incompatible Guarded Scripts list on your instance. If there are entries, those scripts need attention.

Note: The Incompatible Guarded Scripts list is only available on instances running the versions identified in the Rollout Schedule below.

What Is Changing
Background
Today, certain areas of ServiceNow allow server-side JavaScript to run in a protected environment called the sandbox. This includes places where code runs on behalf of potentially untrusted users, such as filters and default values.

ServiceNow is releasing guarded script to enhance instance security. Guarded script will block JavaScript except for a small set of operations — primarily simple expressions and function calls.

What Guarded Script Does Not Allow
Guarded script accepts only a single, simple expression. The following JavaScript features are not supported inside the sandbox:

Variable declarations (var, let, const)

Control flow (if, switch, for, while)

Function declarations

Assignment operators (=)

Multiple statements — only a single expression is allowed per script

Note: This change only affects server-side scripts that run inside the sandbox. Client-side JavaScript is not affected. Code inside script includes is also not affected, because script includes run in the application scope, outside the sandbox.
Why This Is Happening
The current sandbox allows JavaScript from potentially untrusted sources — including unauthenticated users — to run on the server. JavaScript is a powerful and flexible language, and that flexibility creates security risk. Even with restrictions in place, the broad nature of JavaScript means there is always the possibility of new vulnerabilities.

Guarded script drastically reduces the attack surface by allowing only a small set of operations.

Rollout Schedule
Release	Target Date
Zurich Patch 9	May 5, 2026
Australia Patch 2	May 5, 2026
Yokohama Patch 13	May 5, 2026
Zurich Patch 7b	May 14, 2026
Yokohama Patch 12 HF1b	May 14, 2026
Brazil	September 10, 2026
Default Behavior by Instance Type
Transaction Type	Instance Type	Guarded Script Behavior
Unauthenticated / guest	All instances	Fully enforced immediately
Authenticated	New instances	Fully enforced immediately
Authenticated	Upgraded instances (cloud)	Phased enforcement over ~4 weeks (see below)
Authenticated	Upgraded instances (on-premises)	Detection begins automatically; enforcement requires manual advancement
In plain terms: Guest traffic is fully protected as soon as your instance is upgraded. For authenticated traffic on upgraded cloud instances, enforcement phases in automatically over approximately four weeks. The system detects incompatible scripts and creates exemptions for them before enabling enforcement, so existing functionality continues to work. On-premises administrators control the pace of enforcement manually.

Phased Enforcement for Authenticated Traffic
Note: Guest (unauthenticated) traffic is fully protected as soon as your instance is upgraded. The phased rollout described below applies only to authenticated traffic.
After your instance is upgraded, guarded script enforcement for authenticated transactions advances through three phases. On cloud instances, this happens automatically. Before each phase transition, the system creates exemptions for any incompatible scripts it has detected, so those scripts continue to work.

New instances ship with full enforcement because out-of-the-box scripts have been revised to be compatible with guarded script. Upgraded instances, however, may have customizations that rely on the existing sandbox behavior, so a phased approach is used to give the system time to detect incompatible scripts in your environment and create exemptions for them before enforcement begins.

Phase Overview
Phase	Duration	What Happens
Phase 1 — Detection	2 weeks	The system silently analyzes authenticated scripts for compatibility with guarded script syntax rules. Incompatible scripts are recorded in the Incompatible Guarded Scripts list. No change to how scripts execute.
Phase 2 — Syntax Enforcement	2 weeks	Guarded script syntax rules are enforced for authenticated scripts. The system also detects scripts that use restricted APIs, but does not block them — API violations are recorded but execution continues. Exemptions created at the end of Phase 1 ensure previously detected scripts continue to work.
Phase 3 — Full Enforcement	Permanent	Full guarded script enforcement for all authenticated transactions, including API restrictions. Scripts that violate restrictions are blocked unless exempted. Exemptions created at the end of Phase 2 ensure previously detected scripts continue to work.
Automatic Exemptions
Before each phase transition, the system reviews scripts that were logged to the Incompatible Guarded Scripts list during that phase and creates a guarded script exemption for each one. At the end of Phase 1, this covers scripts with syntax incompatibilities. At the end of Phase 2, this covers scripts with API incompatibilities. Exempted scripts continue to run in the existing JavaScript sandbox runtime, bypassing guarded script restrictions. This means any script that ran during the detection windows will continue to work after each enforcement step.

Important: Only scripts that actually execute during a detection phase are captured. If you have scripts that run infrequently — such as quarterly reports or annual processes — they may not be detected automatically. Review the Incompatible Guarded Scripts list and test critical but rarely-used workflows before Phase 3 to ensure they are covered.
On-Premises Instances
On-premises instances enter Phase 1 automatically after upgrade — detection begins immediately. However, the system does not advance to Phase 2 or Phase 3 automatically. Administrators must advance to each phase manually when ready.

ServiceNow provides the GlideGuardedScript script include to advance or reset the enforcement phase. Administrators can run these methods from a Background Script:

Method	Purpose
new GlideGuardedScript().resetToPhase1()	Return the instance to Phase 1 (detection only).
new GlideGuardedScript().advanceToPhase2()	Advance the instance to Phase 2.
new GlideGuardedScript().advanceToPhase3()	Advance the instance to Phase 3 (full enforcement).
Administrators who prefer automatic advancement may enable it by setting com.glide.script.sandbox.ks.watchdog.auto.advance to true.

Enforcement Phase Properties
The following system properties control the enforcement phase system (the "ks" in the property names refers to KittyScript, the internal name for the guarded script language and runtime):

Property	Description	Default
com.glide.script.sandbox.ks.watchdog.phase	Current enforcement phase (1, 2 , or 3).	1 (upgraded) / 3 (new)
com.glide.script.sandbox.ks.watchdog.phase.duration.days	Duration in days for Phase 1 and Phase 2. Set to -1 to pause phase advancement.	14
com.glide.script.sandbox.ks.watchdog.auto.advance	Whether phases advance automatically. Set to false on on-premises instances.	true (cloud) / false (on-prem)

Note: The property com.glide.script.kittyscript.validation.mode is deprecated and no longer controls enforcement behavior on instances with the enforcement phase system. If you previously set this property, it can be removed.

Finding Affected Scripts
Your instance automatically detects and records scripts that are not compatible with guarded script. No configuration is needed — this happens as soon as the feature is active.

Where to Look: The Incompatible Guarded Scripts List
Every script that fails guarded script validation is recorded in the Incompatible Guarded Scripts list. Each entry shows:

The script (normalized, so variations of the same logic appear as one entry)

The scope the script was running in

Transaction type (authenticated or unauthenticated)

The endpoint that triggered it

The origin (table name, URL, or stack trace)

A count of how many times that script has been encountered

Because scripts are deduplicated by their normalized form, the list stays manageable even on high-traffic instances. Many real-world invocations of the same logic collapse into a single row. As such, there is no default retention policy applied to the table — if growth is a concern, add a table cleaner to maintain the table within acceptable limits.

How to Fix Affected Scripts
For each script in the Incompatible Guarded Scripts list, you have two options.

Option 1 (Recommended): Move Logic Into a Script Include
The cleanest fix is to take the complex logic out of the sandbox script and put it in a script include. Script includes run outside the sandbox and are not restricted by guarded script. Then, your sandbox script just calls the script include with a simple one-line expression.

Example
Before (this will fail guarded script — it uses a variable and conditional logic):

var priority = current.priority;
if (priority == 1) { gs.beginningOfToday(); }
else { gs.endOfLastWeek(); }
After — Script Include (create a new script include called MyDateHelper):

var MyDateHelper = Class.create();
MyDateHelper.prototype = {
initialize: function() {},
getRelevantDate: function(priority) {
if (priority == 1) {
return gs.beginningOfToday();
} else {
return gs.endOfLastWeek();
}
},
type: 'MyDateHelper'
};
After — Sandbox script (this is what replaces the original — one simple line):

new MyDateHelper().getRelevantDate(current.priority)
Key point: The sandbox script is now just a single function call — exactly the kind of simple expression guarded script allows. All the complex logic lives safely in the script include.
Option 2 (Last Resort): Create an Exemption
If rewriting a script is not practical, an administrator can exempt it. Exempted scripts bypass guarded script and continue to run in the existing JavaScript sandbox runtime.

Exemptions are created from the Incompatible Guarded Scripts list — select the script entry and create the exemption from there. Only administrators can create or remove exemptions. The system may also create exemptions automatically during enforcement phase transitions. Automatic exemptions work the same way — the exempted script runs in the existing JavaScript sandbox runtime. You can review and manage all exemptions, whether created manually or automatically, from the exemptions list.

Note that the exemption table is not an app table and changes are not tracked in update sets. To move exemptions between machines, manually export and import them.

Use exemptions sparingly. Each exemption is a script that continues to run with the existing, broader permissions.

Recommended Actions
On cloud instances, enforcement phases in automatically and the system creates exemptions for detected scripts. The following steps help you prepare proactively and ensure full coverage.

For Cloud Instances
Review the Incompatible Guarded Scripts list during Phase 1. Once your instance is upgraded, detection begins immediately. Navigate to the list to see which scripts have been flagged.

Exercise infrequently-used workflows. Trigger quarterly, annual, or other rarely-used processes on a sub-production instance so they are detected and exempted before the phase transitions.

Fix incompatible scripts where practical. For each entry, either rewrite it (move complex logic to a script include) or confirm that it has an exemption. Scripts rewritten to use simple expressions no longer need an exemption.

Review automatic exemptions after Phase 2 begins. The system creates exemptions before each phase transition. Review them to confirm they are expected, and plan to remediate the underlying scripts over time.

Monitor after Phase 3. Once full enforcement is active, continue checking the Incompatible Guarded Scripts list. Any script that was not detected during Phases 1 and 2 (because it did not run during those windows) will be blocked and recorded there. Create a manual exemption for any that surface, then remediate them.

To pause automatic phase advancement, set com.glide.script.sandbox.ks.watchdog.phase.duration.days to -1. This freezes the current phase until you set the property back to a positive value.
For On-Premises Instances
Allow Phase 1 detection to run. After upgrading, your instance enters Phase 1 automatically. Let it run long enough to capture incompatible scripts. A longer detection window catches more infrequent workflows but delays the onset of protection. ServiceNow defaults to two weeks per phase and recommends this as a starting point.

Review the Incompatible Guarded Scripts list. Exercise all critical workflows — including infrequent ones — and review the detected scripts.

Fix or exempt each incompatible script. Rewrite scripts where practical; create exemptions for the rest.

Advance to Phase 2. When ready, run new GlideGuardedScript().advanceToPhase2() from a Background Script. The system will create exemptions for any remaining detected scripts before enforcement begins. Allow Phase 2 to run using the same duration considerations as Phase 1 to catch API-level incompatibilities.

Advance to Phase 3. Once you are confident all scripts are covered, run new GlideGuardedScript().advanceToPhase3() to enable full enforcement. The system will create exemptions for any API-incompatible scripts detected during Phase 2 before full enforcement begins. To roll back to detection-only at any time, run new GlideGuardedScript().resetToPhase1().

Note: On-premises administrators can enable automatic phase advancement by setting com.glide.script.sandbox.ks.watchdog.auto.advance to true.

## Related

- [[Platform]]
- [[Knowledge Base Articles]]
- [[Security & ACL]]
- [[Script include Advance structure - Inheritance]]