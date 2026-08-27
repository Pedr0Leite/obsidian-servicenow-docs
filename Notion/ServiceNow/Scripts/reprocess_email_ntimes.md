---
aliases:
  - "reprocess_email_ntimes"
area: "Scripts"
source: custom
tags:
  - email
  - sysevent
  - background-scripts
  - testing
  - scripts
---

# reprocess_email_ntimes

Load-test / repro script: creates a `sys_email` "Email Impersonator" record from/to a given address N times, and for each one raises an `email.read` `sysevent` to force reprocessing. Used to reproduce inbound-email-volume bugs or verify inbound email actions under repeated load, with a `gs.sleep(2500)` throttle between iterations.

```javascript
//VIA EMAIL IMPERSONATOR
var nTimes = 51;
var alreadyDone = 0;
var from = ""; //EMAIL FROM
var to = ""; //EMAIL TO

while (alreadyDone <= nTimes) {
  //amount of emails you want to generate
  var evt = new GlideRecord("sysevent");
  function process_email(id) {
    var evt = new GlideRecord("sysevent");
    evt.initialize();
    evt.process_on = gs.nowDateTime();
    evt.name = "email.read";
    evt.parm1 = id;
    evt.insert();
    gs.print("Event sysid: " + evt.sys_id);
  }

  var email = new GlideRecord("sys_email");
  email.newRecord();
  email.direct = to;
  email.received_type = "new";
  email.recipients = to;
  email.content_type = "Email Impersonator";
  email.user = from; // Add from email
  var user_id = "";
  var usr = new GlideRecord("sys_user");
  usr.addQuery("email", from);
  usr.query();

  if (usr.next()) {
    user_id = usr.sys_id;
  }
  if (user_id != "") {
    email.user_id = user_id;
  }
  gs.print("UserID: " + user_id);
  email.subject = "Testing Email Loop"; //EMAIL SUBJECT HERE
  email.insert();
  process_email(email.sys_id);
  gs.sleep(2500);
  alreadyDone++;
}
```

## Related

- [[Email]]
