---
aliases:
  - "Updating Store Apps Sucks"
area: "Install Stuff"
source: notion-export
tags:
  - store-apps
  - upgrade
  - ci-cd
  - background-scripts
  - install-stuff
---

# Updating Store Apps Sucks

Avoid the pain without this script
If you use the Upgrade Console in your instance you can update all of your apps as part of any upgrade (patch or family). I don't love everything about the process, but it is a very nice way to update all of your apps without running a script or doing them 1 by 1. As a bonus it captures the updates as part of an upgrade plan, so the app version you tested on Dev will be the same one that gets installed on Prod.

You can read more on the Docs page about it (scroll down to number 6).

If you need to update things between patches or otherwise want to ad-hoc update your apps read on...

The Pain
Every quarter or so, ServiceNow released updates to Store apps. This is usually a good thing. The bad part is that you also have to update them in your instance.

One...

At...

A...

Time...

In...

Each...

Instance...

It's painful.

Tools to make it better
However there is a Script Include that the Application Manager uses which you can call and trigger batch app updates. All you need is a payload. Fortunately this uses the same payload as the CI/CD REST endpoint for doing Batch updates

So I came up with a script that takes most of the pain out of this (use at your own risk, always review code some rando on the internet publishes and make sure you understand it before running it in your instance, follow your companies processes for deploying changes, particularly to Production).

Feel free to skip down and just grab the code.

There is a setting at the top to decide if you want to "check" the box for demo data, which just sets a flag in the payload. There is also one to tell it to check for available updates before running. This can make the script take a lot longer to run and will fill the logs with a lot of noise.

In order to build the payload, we need to figure out which apps need to be updated. To do this we look at the sys_store_app table, where they are stored. Sort order is really important here because the table may have many entries for the same app (one for each version that is compatible with your family release). so we check to see if the name is the same as the previous records name (because we only care about the highest version of each app) and skip it if it matches. Then we check to see if the installed version is the same as the latest version (which is conveniently stored on the record). From there the code is adding JSON objects to an Array and then wrapping that into a JSON object to make up the payload that the CI/CD API requires.

Since we are leveraging a Script include we don't need to worry about using a REST API, Authentication or dealing with the REST API Explorer (which you needed to do with the old version of this script). Once you hit Run Script, the code executes and will immediately start the process of updating any apps that need it. A link is provided to where you can monitor the progress. It can take a few minutes to get started, but your instance will figure out any dependancies and the appropriate order to install all the Apps and then proceed to install them starting the next one as soon as one completes.

You can see what is happening and track the progress of the install on the sys_batch_install_plan table (a link is provided when the code executes).

The Code

```jsx
/*----------------------------------------------------*/
/*                      AUTO                          */
/*  Have a bunch of apps that need to be updated?     */
/*  Run this and follow the directions in the output  */
/*  It will automaticallybuild and run a batch        */
/*  install of all of the needed updates.             */
/*                                                    */
/*         Latest code always available at            */
/*         https://snwizard.com/update-apps           */
/*                                                    */
/*----------------------------------------------------*/

//Want Demo Data with the app?
var loadDemoData = true;
var updateCheck = false; //this can take some time to run and adds a LOT of stuff to the log making the important bit harder to find

if (updateCheck) new sn_appclient.UpdateChecker().checkAvailableUpdates();

var prevName;
var appsArray = [];
var grSSA = new GlideRecord("sys_store_app");
grSSA.addEncodedQuery(
"install_dateISNOTEMPTY^hide_on_ui=false^vendor=ServiceNow^ORvendorISEMPTY^latest_version!="
);
grSSA.orderBy("name");
grSSA.orderBy("version");
grSSA.query();
while (grSSA.next()) {
var curName = grSSA.getValue("name");
var latestVersion = updateAvailable(grSSA);
if (curName == prevName) {
continue;
}
if (latestVersion) {
prevName = curName;
var appObject = {
displayName: curName,
id: grSSA.getUniqueValue(),
load_demo_data: loadDemoData,
type: "application",
requested_version: grSSA.getValue("latest_version"),
};
appsArray.push(appObject);
}
}

function updateAvailable(grSSA) {
var installedVersion = grSSA.getValue("version");
var latestVersion = grSSA.getValue("latest_version");
var installedArray = installedVersion.split(".");
var latestArray = latestVersion.split(".");
var len = Math.max(installedArray.length, latestArray.length);
for (var i = 0; i < len; i++) {
var installed = installedArray[i] ? parseInt(installedArray[i]) : 0;
var latest = latestArray[i] ? parseInt(latestArray[i]) : 0;
if (installed < latest) {
return true;
} else if (installed > latest) {
return false;
}
}
return false;
}
if (appsArray.length > 0) {
gs.info("\n\n------------------------------------------------\n\nLinks to track progress below the payload information\n\n(scroll down)\n\n-----------------------------------------------\n\n");
var appsPackages = {};
appsPackages.packages = appsArray;
appsPackages.name = "Update Apps";
var data = new global.JSON().encode(appsPackages);

var baseUrl = gs.getProperty("glide.servlet.uri");
var update = new sn_appclient.AppUpgrader().installBatch(data);
var updateObj = JSON.parse(update);
gs.info(
    "\n\n------------------------------------------------\n\nOpen the Batch install link to monitor the installation progress. It may take some time for the apps to all populate in the related list. After all apps have populated the install will start and the State will change to In progress.\n\nBatch install:\n" +
    baseUrl +
    "nav_to.do?uri=sys_batch_install_plan.do?sys_id=" +
    updateObj.batch_installation_id +
    "\n\nExecution tracker:\n" +
    baseUrl +
    "nav_to.do?uri=sys_progress_worker.do?sys_id=" +
    updateObj.execution_tracker_id +
    "\n\n-----------------------------------------------\n\n"
);
var grSBIP = new GlideRecord('sys_batch_install_plan');

if (grSBIP.get(updateObj.batch_installation_id)) {
grSBIP.setValue('notes','It may take some time for the apps to all populate in the related list below (you can refresh the list as needed to see them populating). \n\nAfter all apps have populated the install will start and the State (above) will change to In progress. \n\nWhen the batch is done the state will update to Installed');
grSBIP.update();
}
} else {
[gs.info](http://gs.info/)(
"\n\n-----------------------------------------------\n\nAll apps appear to be up-to-date. \n\nIf you think this is incorrect please try running this script again with updateCheck set to true. This will check the store for any new updates.\n(sometimes there are apps in the Application Manager that say that there are updates but you can't actually update them)\n\n-----------------------------------------------\n\n"
);
}
```

## Related

- [[Install Stuff]]
- [[Upgrade]]
- [[Update sets - Full Applications]]
- [[How to Backup All Development Work in 1 Click]]