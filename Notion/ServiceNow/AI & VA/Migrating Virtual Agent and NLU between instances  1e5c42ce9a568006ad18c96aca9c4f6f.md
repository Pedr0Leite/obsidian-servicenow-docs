---
aliases:
  - "Migrating Virtual Agent and NLU between instances"
tags:
  - virtual-agent
  - nlu
  - update-sets
  - migration
---

# Migrating Virtual Agent and NLU between instances with update sets

**Migrating Virtual Agent with update sets**

The primary guidance for migrating VA topics between instances is to create a scoped app and to build your custom Virtual Agent topics in that scoped app. You can then publish the scoped app as an update set (xml format) and upload it in another instance. Below is another way to migrate several Virtual Agent topics without using a scoped app. A popular use case is migrating your Virtual Agent topics and NLU models from a sub-prod instance to prod.

**Setup**

If you haven't already, download the '[**Add to Update Set**](https://developer.servicenow.com/connect.do#!/share/contents/9824957_add_to_update_set_utility?v=7.3&t=PRODUCT_DETAILS)' utility the ServiceNow developer site. This makes migrating VA topics easier in that it automatically includes dependent tables needed to migrate. The utility itself is also an update set. To install it to your instance, navigate to "Retrieved Update Sets" in your instance and click "Upload Update set from XML" at the bottom. Upload the xml file. After uploading the file, click into the record, click "Preview" to make sure there are no errors, then click "Commit Upload."

[](https://www.servicenow.com/community/image/serverpage/image-id/85451iAEBAD574681B4A2D/image-size/large?v=v2&px=999)

To check that the installation is successful, navigate to "sys_cs_topic.list". Click into any topic. At the very bottom you should see "Related Links || Add to Update Set".

[](https://www.servicenow.com/community/image/serverpage/image-id/85452i9B7846BD9DD44982/image-size/large?v=v2&px=999)

**Migrating Virtual Agent topics**

1. Navigate to Local Update Sets. Create a new update set, and click "Submit and Make Current."

[](https://www.servicenow.com/community/image/serverpage/image-id/85453i652B02D28796A611/image-size/large?v=v2&px=999)

1. Navigate to "sys_cs_topic.list". Click into a topic you want to migrate, and click on "Add to Update Set" at the bottom. You may receive a banner saying that batched update sets was used. This usually the case when multiple scopes are being added, e.g. adding a scope containing an attached NLU model.

[](https://www.servicenow.com/community/image/serverpage/image-id/85454i2668FB8672B45E6C/image-size/large?v=v2&px=999)

1. Once you are done adding VA topics to the Update Set, navigate back to the Local Update Set table and find your update set. As per above, you may see more than one update set with the created name. Look for the "Batch Parent" update set, and click into it. Change the drop-down from "in progress" to "Complete". Then click "Export Update Set (Batch) to XML."

[](https://www.servicenow.com/community/image/serverpage/image-id/85455i7E60C333E76B58D9/image-size/large?v=v2&px=999)

1. Open the other instance where the topics are to go in. Navigate to "Retrieved Update Sets" and click "Import Update Set from XML". Select the XML file created above and click "Upload". The update set or update set batch should now appear in the Update Set table.

[](https://www.servicenow.com/community/image/serverpage/image-id/85462iBFB419B84CF3573A/image-size/large?v=v2&px=999)

1. Open the parent update set record and click "Preview Update Set"on the top right. If you run into errors, see the "Preview Problems" tab below. To skip the errors, click "Accept remote update." Then click "Commit" on the top right.

[](https://www.servicenow.com/community/image/serverpage/image-id/85461iA00CEA23F2352FF6/image-size/large?v=v2&px=999)

1. Verify that your topic(s) are migrated by navigating to sys_cs_topic, or view in VA Designer.

[](https://www.servicenow.com/community/image/serverpage/image-id/85458i62965258F68F7B6F/image-size/large?v=v2&px=999)

**Notes:** the topic's NLU model and intent may have to be re-binded. You can also add your topic from sys_cs_topic_language to the update set to include the NLU bindings.

**Migrating NLU models with update sets**

The process has been updated in the Vancouver release. It is covered in this Academy video:

[https://www.youtube.com/watch?v=ejo8Vcjq_BA](https://www.youtube.com/watch?v=ejo8Vcjq_BA)

## Related

- [[VA - Basic Arch and ACLs]]
- [[50+ (Un)documented Virtual Agent variables (vaInpu]]
- [[Knowledge graph enhancing Virtual Agent search]]
- [[Automation Discovery]]