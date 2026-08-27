---
aliases:
  - "send_spec_email_to_users"
area: "Scripts"
source: custom
tags:
  - notifications
  - event-queue
  - interaction
  - csm
  - localization
  - scripts
---

# send_spec_email_to_users

Loops `interaction` records and, for each one with no completed CSAT survey (`asmt_assessment_instance`) and an active assigned user, fires a language-specific notification event (`gs.eventQueue`) picked from a `preferred_language → event name` map — so a Spanish-speaking agent gets `Interaction.notif.es` while an English one gets `Interaction.notif.en`. Also tracks already-notified users to avoid duplicate sends within the run.

```javascript
var mainQuery = "";

var excludeUser = [];

var hashDict = {

    "en": "Interaction.notif.en",
    "pt": "Interaction.notif.pt",
    "fr": "Interaction.notif.fr",
    "it": "Interaction.notif.it",
    "de": "Interaction.notif.de",
    "es": "Interaction.notif.es",
    "pl": "Interaction.notif.pl",
    "zt": "Interaction.notif.zt",
    "zh": "Interaction.notif.zh",
    "nl": "Interaction.notif.nl",
};
 
 
var gr = new GlideRecord("interaction");

gr.addEncodedQuery(mainQuery);

gr.query();
 
while (gr.next()) {

    var surveys = new GlideRecord('asmt_assessment_instance');
    surveys.addQuery('trigger_id',gr.sys_id);
    surveys.addQuery('state', 'completed');
    surveys.query();
    var count = surveys.getRowCount();

var userGr = new GlideRecord("sys_user");
userGr.addQuery("active", true);
userGr.addQuery("sys_id", gr.assined_to);
userGr.query();

var countUser = userGr.getRowCount();

    if (count < 1 && countUser > 0 && excludeUser.indexOf(gr.opened_for.sys_id + "") == -1) {

        var eventName = hashDict[gr.opened_for.preferred_language];
        gs.eventQueue(eventName, gr, "", "");
        excludeUser.push(gr.opened_for.sys_id + "");

    }

}
```

## Related

- [[Email]]
- [[Now Assist Q&A using Dynamic Translation]]
