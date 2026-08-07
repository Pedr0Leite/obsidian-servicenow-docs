---
title: "Frequently asked questions - Google Maps setup"
aliases:
  - KB0782884
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782884
kb_number: KB0782884
last_modified: 2024-04-08
---

## Frequently asked questions - Google Maps setup

  

### Issue

Frequently asked questions - Google Maps setup

### Resolution

**1.** **Can I use default "gme-servicenow" client ID with no limits or do I have to obtain my own client ID?**  
gme-servicenow has limits. It is intended only for the customer to experiment and get exposure to the feature. But significant usage will require its own license as it's shared among all of our customers. So If necessary, obtain a Google Maps for a Work license key to cover the development use of the Google Maps API. We have changes in Orlando that will also support API key

[Set up Google Maps API](https://docs.servicenow.com/csh?topicname=set-up-google-maps-api.html&version=latest "Set up Google Maps API")

**2\. Also, what is the purpose of having my own map key? Since I have one provided by my client, but I don't have my customer's client ID.**

The purpose of having your own map key is that you can create map pages or use the default pages included with the plugin. Map pages define what data is displayed on the map and the appearance of the links.

Please check the below links

[Google maps setup](https://docs.servicenow.com/csh?topicname=p_NavigationAndUIConfiguration.html&version=latest "Google maps setup")

[Geolocation Google key](https://docs.servicenow.com/csh?topicname=r_GeolocationGoogleKey.html&version=latest "Geolocation Google key")

**3\. Can I use client ID gme-servicenow together with my customer's map key?**  
As stated from point #1 this should work but the client\_ID gme-servicenow has limitations. you might have to use your own client ID to avoid any usage limitations. 'gme-servicenow' is for the freebie version. Any customer using it for FSM definitely needs to get their own key

**4\. I have both API Key or client ID, which one should I use?**

If you have a client-id, you can change it in the Google Maps properties. If you have an API key you will need to wait for Orlando release. It will also be made available in earlier versions. You can contact Tech Support for additional info.

**5\. How can I gauge the limitations of the client ID and what are the steps to avoid limitations?**

Please check below links

[Maps Embed API Usage and Billing](https://developers.google.com/maps/documentation/embed/usage-and-billing#embed "Maps Embed API Usage and Billing")

[Usage Limits for Google Maps Platform Web Services](https://developers.google.com/maps/premium/previous-licenses/articles/usage-limits "Usage Limits for Google Maps Platform Web Services")

**6\. Map pages show "for development purpose only"**

You can navigate to the map pages and please navigate to **Developer Tools > Console from your browser** and you can see more information about the error. Sample screenshot below

![](sys_attachment.do?sys_id=fb32e8091b407414f34d33bc1d4bcbe1)

**Useful resources:**

[Maps Embed API Usage and Billing](https://developers.google.com/maps/documentation/embed/usage-and-billing#embed "Maps Embed API Usage and Billing")

[Google Maps Platform API Checker](https://chrome.google.com/webstore/detail/google-maps-platform-api/mlikepnkghhlnkgeejmlkfeheihlehne "Google Maps Platform API Checker")

[Google Maps shows “For development purposes only”](https://stackoverflow.com/questions/50977913/google-maps-shows-for-development-purposes-only "Google Maps shows “For development purposes only”")

[“FOR DEVELOPMENT PURPOSES ONLY” ERROR ON GOOGLE BASEMAPS](https://www.mapsmarker.com/kb/faq/for-development-purposes-only-error-on-google-basemaps/ "“FOR DEVELOPMENT PURPOSES ONLY” ERROR ON GOOGLE BASEMAPS")

[About Problem: Google Maps shows error ‘For development purposes only’](https://wordpress.org/support/topic/about-problem-google-maps-shows-error-for-development-purposes-only/ "About Problem: Google Maps shows error ‘For development purposes only’")

**7\. Which version of google maps should I use?**

You should be able to go with the current version. Please test by updating the version number and test in a sub prod environment before making the change in production.
