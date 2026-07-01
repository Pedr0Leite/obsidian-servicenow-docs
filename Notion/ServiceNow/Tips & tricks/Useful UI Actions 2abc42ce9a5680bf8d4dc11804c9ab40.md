---
aliases:
  - "Useful UI Actions"
tags:
  - ui-actions
  - tips-and-tricks
  - workspace
  - g-modal
---

# Useful UI Actions

# **What are UI Actions?**

UI Actions are custom actions users can perform on records in the ServiceNow interface. They are typically associated with forms and lists and appear as buttons or context menu options. UI Actions allow users to initiate specific actions, such as creating records, updating fields, running scripts, or navigating to related pages, directly from the ServiceNow interface. They can be configured to execute client-side or server-side scripts to perform desired operations. UI Actions help users work faster and more efficiently by giving them quick access to common ServiceNow functions.

Please refer to the [ServiceNow documentation pages](https://docs.servicenow.com/csh?topicname=c_UIActions.html&version=latest) for more information about UI Actions.

# **Open Scan Finding related Record in List View**

In most of the cases, a finding record of an Instance Scan (table **scan_finding**) will reference the identified source record, and you can open that source record as usual. The problem here are source records from the **sys_attachment** table. These cannot be opened in the form view. Instead, ServiceNow starts a download of the underlying file. However, this takes away the possibility of examining the **sys_attachment** record in more detail in order to understand the cause of the finding.

Therefore, the following UI Action (related link in form view and context option in list view) will open the referenced record in the list view, thus allowing to add the required columns for more information.

### **UI Action**

| **Table** | **scan_finding** |
| --- | --- |
| **Form link** | true |
| **List Context Menu** | true |
| **Client** | true |
| **Onclick** | `openSourceRecordInListView()` |
| **Condition** | `gs.hasRole('scan_user')` |
| **Script** | `function openSourceRecordInListView() {
  
  var _grScanFinding = new GlideRecord('scan_finding');
  
  _grScanFinding.addQuery('sys_id', rowSysId || g_form.getUniqueValue());
  _grScanFinding.query();

  if (_grScanFinding.next()) {
    var _strSourceTableName   = _grScanFinding.source_table.toString();
    var _strSourceRecordSysID = _grScanFinding.source.toString();
  
    g_navigation.openPopup(
      '/' + _strSourceTableName + '_list.do?sysparm_query=sys_id=' + 
      _strSourceRecordSysID
    );
  }
}` |

# **Open Attachment-related Record from List View**

Basically, an attachment record at table sys_attachment is associated with a related record. For example, an Excel file attached to a data source. That relationship is designed as a Document ID reference at table sys_attachment. And because of records in the sys_attachment table do not have a form view, it is impossible to open the referenced record from the list view. Instead, you have to open the related target table manually and lookup the target record via its Sys ID which is a pretty bad user experience. Therefore, I built a list action for the context menu, allowing me to open the target record with a mouse click.

### **UI Action**

| **Table** | **sys_attachment** |
| --- | --- |
| **List Context Menu** | true |
| **Client** | true |
| **Onclick** | `openRelatedRecord()` |
| **Condition** | `!current.table_name.nil() && !current.table_sys_id.nil() && 
!current.table_name.startsWith('invisible.') && 
current.table_name != 'sys_attachment'` |
| **Script** | `function openRelatedRecord() {

  var _grRecord = new GlideRecord('sys_attachment');
  
  _grRecord.addQuery('sys_id', rowSysId);
  _grRecord.query();

  if (_grRecord.next()) {
    var _strTableName   = _grRecord.table_name.toString();
    var _strRecordSysID = _grRecord.table_sys_id.toString();

    if (_strTableName.startsWith('ZZ_YY')) {
      _strTableName = _strTableName.substring(5);
    }
    
    g_navigation.openPopup('/' + _strTableName + '.do?sys_id=' + _strRecordSysID);
  }
}` |

# **Open Metadata Snapshot-related Records**

In ServiceNow, we can add pure data records to an application via [action "Create Application Files"](https://docs.servicenow.com/csh?topicname=t_IncludeApplicationData.html&version=latest). These records are stored at table **sys_metadata_link** and thus associated to a certain application.

However, just as with the **sys_attachment** table, ServiceNow has forgotten to provide a UI Action that allows the original data record to be opened directly in the form as well as list view.

### **UI Action**

| **Table** | **sys_metadata_link** |
| --- | --- |
| **Form link** | true |
| **List Context Menu** | true |
| **Client** | true |
| **Onclick** | `openRelatedRecord()` |
| **Condition** | `new GlideRecord(current.tablename.toString()).get(current.documentkey.toString())` |
| **Script** | `function openRelatedRecord() {

  var _grRecord = new GlideRecord('sys_metadata_link');
  
  _grRecord.addQuery('sys_id', rowSysId || g_form.getUniqueValue());
  _grRecord.query();

  if (_grRecord.next()) {
    var _strTableName   = _grRecord.tablename.toString();
    var _strRecordSysID = _grRecord.documentkey.toString();
    
    g_navigation.openPopup('/' + _strTableName + '.do?sys_id=' + _strRecordSysID);
  }
}` |

# **Create Application Files on Form View**

In a list view of a non-artifact table (table NOT inheriting from **sys_metadata**) you have the list [action "Create Application Files"](https://docs.servicenow.com/csh?topicname=t_IncludeApplicationData.html&version=latest). This is always super helpful if you want to add pure data records to an application (for example technical users for integrations) for easier transfer to the next instance and make sure those records definitely exist in the target instance.

Unfortunately, that action is not available in the form view. However, with a slight modification of the original UI Action you also make it available for the form view.

### **UI Action**

| **Table** | **global** |
| --- | --- |
| **Form context menu** | true |
| **Client** | true |
| **Onclick** | `popAddMetadataDialog();` |
| **Condition** | `!current.isMetadata() && 
current.canCreate() && 
!SNC.MetadataLinkUtil.isTableMetadataLinkExempt(current.getTableName())` |
| **Script** | `function popAddMetadataDialog() {	
  var dialog = new GlideModal('add_selected_metadata_link_dialog');

  dialog.setTitle(
    new GwtMessage().getMessage('Create Application File from Record')
  );
  dialog.setPreference('current_table', g_form.getTableName());
  dialog.setPreference('sys_id_list', g_form.getUniqueValue());
  dialog.render();
}` |

# **Open in Instance**

How often have you opened any configuration record in one instance and then the same record on a different instance for comparison reasons? Or the same for list views? A button that allows us to open the current URL on another instance would therefore be extremely helpful. And this is exactly what the following UI action offers.

[MaikSkoddow_0-1717394024557.png](https://www.servicenow.com/community/image/serverpage/image-id/361718iF36ED11DD2E90FEB/image-size/large?v=v2&px=999)

### **UI Action**

| **Table** | **global** |
| --- | --- |
| **Form button** | true |
| **List banner button** | true |
| **Client** | true |
| **Onclick** | `openInInstance()` |
| **Condition** | `gs.hasRole("admin") && !RP.isRelatedList() && RP.getParameterValue("sysparm_view") != 'sys_ref_list'` |
| **Script** | `function openInInstance() {
  var _gm                     = new GlideModal();
  var _strCurrentInstanceHost = top.location.host;
  var _objInstanceProperties  = {
    'DEV': {
      color: '#b32400',
      host : 'mycompany-dev.servicenow.com'
    },
    'TEST': {
      color: '#b38300',
      host : 'mycompany-test.servicenow.com'
    },
    'PROD': {
      color: '#302f4b',
      host : 'mycompany-prod.servicenow.com'
    }
  };

  var _arrHtml = 
  ['<div style="display: flex; justify-content: space-evenly; gap: 10px;">'];

  for (var _strInstanceName in _objInstanceProperties) {
    var _strInstanceHost  = _objInstanceProperties[_strInstanceName]['host'];
    var _strInstanceColor = _objInstanceProperties[_strInstanceName]['color'];
    var _strInstanceUrl = 
      g_navigation.getURL().replace(_strCurrentInstanceHost, _strInstanceHost);

    if (_strInstanceHost !== _strCurrentInstanceHost) {
      _arrHtml.push(
        '<a href="' + _strInstanceUrl + 
        '" target="_blank" ' + 
        'class="btn btn-lg btn-primary" style="background-color: ' + 
        _strInstanceColor + '; flex-grow: 1">' + _strInstanceName + '</a>'
      );
    }
  }

  _arrHtml.push('</div>');
  _gm.setTitle('Open in Instance')
  _gm.renderWithContent(_arrHtml.join(''));
}` |

# **Lookup syslog Records in a dedicated Time Range**

The **`syslog`** table in ServiceNow serves as a centralized repository for log entries generated by various system functions and their child tables. This consolidation can make it challenging to trace specific log entries back to their originating scripts or transactions, especially when logs from different processes are intermingled.

To address this challenge, I have developed the UI Action **"Lookup Records in Time Range"**. This feature provides two complementary methods to refine your log searches:

1. **Time Range Selection:** Choose from predefined time intervals to expand your search window both forward and backward from the current log entry's timestamp. This approach helps in capturing all relevant logs that occurred around the same time frame.
2. **Transaction-Based Filtering:** Limit the search results to log entries associated with the same transaction as the currently viewed log. This method ensures that you retrieve logs that are contextually linked to the specific process or script execution.

By clicking on the **"Search"** button, the system performs the lookup in a new tab, presenting you with a filtered list of log entries that match your specified criteria. This functionality enhances your ability to diagnose issues by providing a clearer view of related log activities, thereby improving the efficiency of your troubleshooting processes.

[MaikSkoddow_0-1737381213371.png](https://www.servicenow.com/community/image/serverpage/image-id/413556iAA40CA48CB745EAB/image-size/large?v=v2&px=999)

### **UI Action**

You can download it from the attached file [sys_ui_action_e1ddae045ca1de102f83db37de3d1987.xml](https://www.servicenow.com/community/s/cgfwn76974/attachments/cgfwn76974/developer-kb/9186/1/sys_ui_action_e1ddae045ca1de102f83db37de3d1987.xml)

# **Open record in selected Workspace**

I liked [Ahmed Drar's idea](https://www.servicenow.com/community/csm-articles/encouraging-cs-agents-to-embrace-csm-workspace/ta-p/3185926) of having a UI action in the Classic UI that opens the current record in a Workspace. But why focus on just one Workspace? There are several dozen Workspaces in ServiceNow, and the number is growing rapidly. Even when developing custom Workspaces, it would be helpful to open a specific record in a selected Workspace. So I added a preselection of Workspaces to the UI action. The list is pulled from the table **sys_ux_registry_m2m_category**, which is also the basis for the list of workspaces in the header. This operation is performed using a client-side [**fetch**](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch) call, saving me an additional script include that would have to be called via [**GlideAjax**](https://www.servicenow.com/docs/csh?topicname=c_GlideAjaxAPI.html&version=latest). You can get the finished UI action from my page "My collected list of useful UI actions".

[MaikSkoddow_0-1740545148498.png](https://www.servicenow.com/community/image/serverpage/image-id/422088iE67B90DB95014482/image-size/large?v=v2&px=999)

### **UI Action**

| **Table** | **task** (change if required) |
| --- | --- |
| **Form Button** | true |
| **Client** | true |
| **Onclick** | `openInWorkspace()` |
| **Condition** | Add a condition that matches your context and your requirements. |
| **Script** | `function openInWorkspace() {

  const _strTableName         = g_form.getTableName();
  const _strSysID             = g_form.getUniqueValue();
  const _gmWorkspaceSelection = new GlideModal('workspace_selection', false, 600);
  
  top.window.openWorkspace = () => {
    const _objSelectedWorkspace = 
      document.querySelector('input[name="workspace"]:checked'); 

    if (_objSelectedWorkspace === null) {
      alert('Please select a Workspace!');
    }
    else {
      g_navigation.openPopup(
        '/now/' + _objSelectedWorkspace.value + 
        '/record/' + _strTableName + '/' + _strSysID
      );
    }
  }

  top.window.closeWorkspaceSelection = () => _gmWorkspaceSelection.destroy();  

  fetch(
    '/api/now/table/sys_ux_registry_m2m_category' + 
    '?sysparm_query=' + encodeURIComponent('page_registry.active=true^ORDERBYpage_registry.title') +
    '&sysparm_fields=page_registry.title,page_registry.path' +
    '&sysparm_ck=' + window.g_ck
  )
  .then(response => {return response.json()})
  .then(data => {
    if (Array.isArray(data.result)) {
      var _arrHTML = [];

      _arrHTML.push('<table border="0" style="border-spacing:10px;border-collapse:separate;">');

      data.result.forEach(function(objData) {
        _arrHTML.push('<tr>');
        _arrHTML.push('<td>');
        _arrHTML.push('<input type="radio" name="workspace" value="');
        _arrHTML.push(objData['page_registry.path']);
        _arrHTML.push('">');
        _arrHTML.push('</td><td>');
        _arrHTML.push(objData['page_registry.title']);
        _arrHTML.push('</td>');
        _arrHTML.push('</tr>');
      });

      _arrHTML.push('</table>');
      _arrHTML.push('<div class="modal-footer">');
      _arrHTML.push('<span class="pull-right">');
      _arrHTML.push('<button class="btn btn-default" onClick="top.window.openWorkspace();return false;">');
      _arrHTML.push('Open');
      _arrHTML.push('</button>');
      _arrHTML.push('<button class="btn btn-primary" onClick="top.window.closeWorkspaceSelection()">');
      _arrHTML.push('Close');
      _arrHTML.push('</button>');
      _arrHTML.push('</span>');
      _arrHTML.push('</div>');

      _gmWorkspaceSelection.setTitle('Open record in selected Workspace');
      _gmWorkspaceSelection.setBackdropStatic(true);
      _gmWorkspaceSelection.setPreference("focusTrap", true);
      _gmWorkspaceSelection.renderWithContent(_arrHTML.join(''));
    }
    else {
      alert('No workspaces available to open the current record!')
    }
  });
}` |

## Related

- [[Tips & tricks]]
- [[How to use UI Actions in Workspaces]]
- [[Workspace for a custom app forms]]