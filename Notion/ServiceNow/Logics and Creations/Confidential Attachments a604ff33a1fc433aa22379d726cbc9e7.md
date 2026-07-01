---
aliases:
  - "Confidential Attachments"
tags:
  - attachments
  - acl
  - custom-table
  - glideajax
  - client-scripts
---

# Confidential Attachments

A way to hide certain attachments

- [ ]  Custom table
- [ ]  

![Untitled](Confidential%20Attachments/Untitled.png)

```jsx
function abrirAnexo() {
    var sysID = g_form.getUniqueValue();
    var description = g_form.getValue('description');
    var shortDescription = g_form.getValue('short_description');

    var ajax = new GlideAjax('anexosConfidenciaisUtils');
    ajax.addParam('sysparm_name', 'recordExist');
    ajax.addParam('sysparm_id', sysID);
    ajax.getXML(getAnexo);

    function getAnexo(response) {
        var answer = response.responseXML.documentElement.getAttribute("answer");
        answer = (answer == 'false') ? false : answer;
		var title = getMessage('adicione_anexos_confidenciais');
        var gmf = new GlideModalForm(title, 'x_cttrd_fujitsu_pr_anexos_confidenciais');
        gmf.setOnloadCallback(function() {
            //Resize the modal window
            jQuery(".modal-content").css("width", "50%").css("margin", "0 auto");
        });
        if (answer) {
            gmf.setSysID(answer); //Pass in sys_id to edit existing record, -1 to create new record
        }
		//Set the header on the Anexos Confidenciais record
        gmf.setPreference("sysparm_titleless", "false");
        gmf.setPreference('sysparm_query', 'parent=' + sysID + '^description=' + description + '^short_description=' + shortDescription);
        gmf.render();
    }
}
```

Don’t forget to create the custom table:

- [ ]  ACLs of the table

![Untitled](Confidential%20Attachments/Untitled%201.png)

## Related

- [[Logics and Creations]]
- [[Security & ACL]]
- [[Enabling Report View ACLs]]
- [[Possible Ways for Making an Attachment Mandatory S]]