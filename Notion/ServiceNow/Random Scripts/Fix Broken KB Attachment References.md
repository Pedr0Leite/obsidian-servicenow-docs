---
aliases:
  - "Fix Broken KB Attachment References"
area: "Random Scripts"
tags:
  - background-scripts
  - fix-script
  - attachments
  - glide-record
  - glide-sys-attachment
  - knowledge-base
  - random-scripts
---

# Fix Broken KB Attachment References

Fix Script / Background Script — re-parents orphaned KB attachment references.

**Problem:** KB articles reference attachments inline via HTML like `.../sys_attachment.do?sys_id=<32-char-hex>` (or the HTML-encoded `&#61;` form), but that attachment's `sys_attachment.table_sys_id` may point at a **different** record (e.g. copied from another article, or the article was cloned).

**Fix:** for every referenced attachment that does NOT belong to the current record, clone it onto the current record and rewrite the HTML to point at the new attachment's sys_id instead of the original.

Run scope: needs read/write on `kb_template_how_to` (or whatever table is in `hashMap`) and `sys_attachment`.

```javascript
var hashMap = [
    {
        'active': false,
		'table': 'kb_knowledge',
        'bodyField': 'text',
		'encQuery': 'textLIKE/sys_attachment.do?sys_id^active=true^workflow_state=published'
    },
    {
        'active': true,
        'table': 'kb_template_how_to',
        'bodyField': 'kb_instructions',
		'encQuery': 'kb_instructionsLIKE/sys_attachment.do?sys_id^active=true^workflow_state=published'
    },
    {
        'active': false,
        'table': 'u_kb_template_px_standard_template',
        'bodyField': 'u_kb_body',
		'encQuery': 'u_kb_bodyLIKE/sys_attachment.do?sys_id^active=true^workflow_state=published'
    },
    {
        'active': false,
        'table': 'kb_template_faq',
        'bodyField': 'text',
		'encQuery': 'textLIKE/sys_attachment.do?sys_id^active=true^workflow_state=published'
    },
    {
        'active': false,
        'table': 'kb_template_known_error_article',
        'bodyField': 'kb_workaround',
		'encQuery': 'kb_workaroundLIKE/sys_attachment.do?sys_id^active=true^workflow_state=published'
    },
    {
        'active': false,
        'table': 'kb_template_what_is',
        'bodyField': 'kb_explanation',
		'encQuery': 'kb_explanationLIKE/sys_attachment.do?sys_id^active=true^workflow_state=published'
    }
];

var updatedArticleNumbers = [];

hashMap.forEach(function (x) {
	if(x.active){
		var grKK = new GlideRecord(x.table);
		if(x.table )
		grKK.addEncodedQuery(x.encQuery);
		grKK.query();

		while (grKK.next()) {
			var htmlContent = grKK.getValue(x.bodyField);
			var targetRecord = grKK.getValue('sys_id');
			gs.info('targetRecord: ' + targetRecord);

			var attachSysIdsArr = extractAttachmentSysIds(htmlContent);
			gs.info('Referenced attachments: ' + JSON.stringify(attachSysIdsArr));

			var updatedHtml = htmlContent;
			var htmlChanged = false;

			attachSysIdsArr.forEach(function (attachSysId) {
				if (checkIfAttachBelongs(attachSysId, targetRecord)) {
					// Already correctly parented to this record — nothing to do.
					return;
				}

				gs.info('Attachment ' + attachSysId + ' does NOT belong to ' + targetRecord + ' — cloning.');

				var newAttachmentSysId = copySingleAttachment(attachSysId, x.table, targetRecord);

				if (newAttachmentSysId) {
					// Replace every occurrence of the old sys_id with the new one
					// in this article's body (HTML-encoded '=' is &#61; per the source regex).
					var oldRef = new RegExp(attachSysId, 'g');
					updatedHtml = updatedHtml.replace(oldRef, newAttachmentSysId);
					htmlChanged = true;
				}
			});

			if (htmlChanged) {
				grKK.setValue(x.bodyField, updatedHtml);
				grKK.setWorkflow(false);
				grKK.autoSysFields(false);
				grKK.update();
				gs.info('Updated ' + x.bodyField + ' on ' + targetRecord + ' with re-pointed attachment references.');
				updatedArticleNumbers.push(grKK.getValue('number'));
			}
		}
	}
});

gs.info('Unit4 - Fix knowledge attachments - There were ' + updatedArticleNumbers.length + ' articles fixed today. Article Numbers: ' + updatedArticleNumbers.join(', '));

function extractAttachmentSysIds(htmlString) {
    if (!htmlString) return [];

    // Matches the specified prefix and captures the 32-character hex sys_id
    // Accepts both the HTML-encoded '=' (&#61;) and the literal '=' form.
    var regex = /\/sys_attachment\.do\?sys_id(?:&#61;|=)([0-9a-f]{32})/gi;
    var sysIds = [];
    var match;

    while ((match = regex.exec(htmlString)) !== null) {
        sysIds.push(match[1]);
    }

    return sysIds;
}

// Returns true if the given attachment sys_id is already parented
// (table_sys_id) to targetRec — i.e. no fix needed.
function checkIfAttachBelongs(attachSysId, targetRec) {
    var attachGr = new GlideRecord('sys_attachment');
    attachGr.addQuery('sys_id', attachSysId);
    attachGr.addQuery('table_sys_id', targetRec);
    attachGr.setLimit(1);
    attachGr.query();

    return attachGr.next();
}

// Clones a single attachment onto targetTable/targetSysId and returns the
// new attachment's sys_id.
function copySingleAttachment(sourceAttachmentSysId, targetTable, targetSysId) {
    // 1. Get the target record
    var targetGR = new GlideRecord(targetTable);
    if (!targetGR.get(targetSysId)) {
        gs.error('Target record not found: ' + targetSysId);
        return null;
    }

    // 2. Get the specific source attachment record
    var sourceAttachmentGR = new GlideRecord('sys_attachment');
    if (!sourceAttachmentGR.get(sourceAttachmentSysId)) {
        gs.error('Source attachment not found: ' + sourceAttachmentSysId);
        return null;
    }

    var fileName = sourceAttachmentGR.getValue('file_name');
    var contentType = sourceAttachmentGR.getValue('content_type');

    // 3. Stream the content from the source attachment onto the target record
    var gsa = new GlideSysAttachment();
    var newAttachmentSysId = gsa.writeContentStream(
        targetGR,
        fileName,
        contentType,
        gsa.getContentStream(sourceAttachmentSysId)
    );

    gs.info('Copied attachment ' + sourceAttachmentSysId + ' -> new attachment ' + newAttachmentSysId);
    return newAttachmentSysId;
}

```

## Related
- [[GlideSysAttachmentGlobalAPI|GlideSysAttachment - Global]]
- [[c_GlideSysAttachmentScopedAPI|GlideSysAttachment - Scoped]]
- [[Ler anexos excel via BG]] — sibling script, same `GlideSysAttachment`/`getContentStream` pattern for reading attachment content
