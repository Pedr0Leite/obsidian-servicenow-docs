---
title: "How to find references to a report on Homepages and Non responsive Dashboards using JavaScript"
aliases:
  - KB0749182
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749182
kb_number: KB0749182
last_modified: 2024-04-07
---

## How to find references to a report on Homepages and Non responsive Dashboards using JavaScript

  

### Issue

# Introduction

* * *

Sometimes it may be useful to find usages of a report on Homepages and non responsive Dashboards. For example, you may want to remove or redesign a report, but want to measure the impact. The script in this article will search for Homepages and Dashboards that have this report.

If an instance is using a responsive dashboard, the following script might not give accurate results because responsive dashboards use sys\_grid\_canvas and sys\_grid\_canvas\_pane tables to store contents on the dashboard. 

# Usage

* * *

The function in the script takes one argument. This should be a string containing the sys ID of the report (sys\_report record) you are looking for. This script should be run via the Scripts - Background module.

# The Script

**Version for homepages and non-responsive dashboards:**

* * *

findReportReferences('c8b0bce8db25b3003869ff041d961975'); //sys\_id for the report
function findReportReferences(report) {
    var pp = new GlideRecord('sys\_portal\_preferences');
    pp.addQuery('value', report);
    pp.query();
    while (pp.next()) {
        var page = new GlideRecord('sys\_portal\_page');
        page.get(pp.portal\_section.page);
        var tabs = new GlideRecord('pa\_tabs');
        tabs.addQuery('page', page.sys\_id);
        tabs.query();

        // No PA tabs, it's just a homepage
        if (tabs.getRowCount() < 1) {
            gs.info("Homepage: " + page.title);
            continue;
        }

        // PA tabs exist, it's on a dashboard
        while (tabs.next()) {
            var m2m = new GlideRecord('pa\_m2m\_dashboard\_tabs');
            m2m.addQuery('tab', tabs.sys\_id);
            m2m.query();
            while (m2m.next()) {
                gs.info("Dashboard: " + m2m.dashboard.name);
            }
        }
    }
}

* * *

**Version for responsive dashboards:  
  
**var reports = \['01266b8bdb0cf7c46538f7adae9619d0'\]; // list of report sysIDs  
var dashboards = \[\];  
reports.forEach(function(report) {  
    dashboards = dashboards.concat(getDashboardsForAReport(report))  
    dashboards = dashboards.filter(function (elem, index, me) { // remove any duplicates exists  
        return index === me.indexOf(elem);  
    });  
})  
gs.log(JSON.stringify(dashboards.join()));  
// +++++++++++++++   helper functions   +++++++++++++++  
function getDashboardsForAReport(sysId) {  
    var paSysReport = new GlideRecordSecure('sys\_report');  
    var paGaugeReport = new GlideRecordSecure('sys\_gauge');  
    var tabs = \[\];  
    if (sysId && paSysReport.get(sysId))  
    tabs = \_getTabsFromWidget(sysId);  
    if (paGaugeReport.get('report', sysId))  
    tabs = tabs.concat(\_getTabsFromWidget(paGaugeReport.getValue('sys\_id')));  
    tabs = tabs.filter(function (elem, index, me) { // remove any duplicates exists  
        return index === me.indexOf(elem);  
    });  
    var dashboards = \[\];  
    tabs.forEach(function (tab) {  
        dashboards = dashboards.concat(\_getDashboardFromTab(tab.tabUniqueId))  
    });  
    dashboards = dashboards.filter(function (elem, index, me) { // remove any duplicates exists  
        return index === me.indexOf(elem);  
    });  
    return dashboards;  
}  
function \_getTabsFromWidget(sysId) {  
    // fetch tabs  
    var paTabs = null;  
    var tabs = \[\];  
    var gridCanvasPaneList = \[\];  
    var record = null;  
    var i = 0;  
    var sysGridCanvasPane = null;  
    var pref = new GlideRecord('sys\_portal\_preferences');  
    pref.addQuery('value', sysId);  
    pref.query();  
    var portalSections = \[\];  
    while (pref.next())  
        portalSections.push(pref.getValue("portal\_section"));  
    for (i = 0; i < portalSections.length; i++) {  
        sysGridCanvasPane = new GlideRecord('sys\_grid\_canvas\_pane');  
        sysGridCanvasPane.addQuery('portal\_widget', portalSections\[i\]);  
        sysGridCanvasPane.query();  
        while (sysGridCanvasPane.next())  
            gridCanvasPaneList.push(sysGridCanvasPane.getValue('grid\_canvas'));  
    }  
    for (i = 0; i < gridCanvasPaneList.length; i++) {  
        paTabs = new GlideRecordSecure('pa\_tabs');  
        paTabs.addQuery('canvas\_page', gridCanvasPaneList\[i\]);  
        paTabs.query();  
        while (paTabs.next()) {  
            record = {  
                id: paTabs.getValue('sys\_id'),  
                tabUniqueId: paTabs.getValue('sys\_id'),  
                name: paTabs.getDisplayValue('name'),  
            };  
            tabs.push(record);  
        }  
    }  
    return tabs;  
}  
function \_getDashboardFromTab(tabID) {  
    var dashboards = \[\];  
    var dashBoardTab = new GlideRecordSecure('pa\_m2m\_dashboard\_tabs');  
    var padDashboard = new GlideRecordSecure('pa\_dashboards');  
    var record = null;  
    dashBoardTab.addQuery('tab', '=', tabID);  
    dashBoardTab.query();  
    while (dashBoardTab.next()) {  
        dashboards.push(dashBoardTab.getDisplayValue('dashboard.sys\_id'));  
    }  
    return dashboards;  
}
