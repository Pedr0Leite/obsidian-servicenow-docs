---
title: "pe-sp-simple-map"
aliases:
  - pe-sp-simple-map
tags:
  - servicenow-dev-program
  - code-snippet
  - pe-sp-simple-map
  - src
---

# Sp Simple Map

## Description

Simple Map is a widget which will quickly make you able to use all the available Google Maps APIs in Service Portal. The initial rendering is minimal, so you can easily enable and show what you need through the all available widget and directives options. The only requisite is to sign up on [Google Cloud](https://cloud.google.com/free/ "Google Cloud Platform Free Tier") and obtain a valid API key.

## Screenshots

![Customize your map style with the Google Styling Wizard - https://mapstyle.withgoogle.com/](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-sp-simple-map/images/pe-sp-simple-map-01.png)

![Sp Simple Map with style Retro](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-sp-simple-map/images/pe-sp-simple-map-02.png)

![Sp Simple Map with style Silver](https://raw.githubusercontent.com/platform-experience/serviceportal-widget-library/master/src/pe-sp-simple-map/images/pe-sp-simple-map-03.png)

## Installation

Download and install update set **[pe-sp-simple-map.u-update-set.xml](https://github.com/platform-experience/serviceportal-widget-library/blob/master/src/pe-sp-simple-map/pe-sp-simple-map.u-update-set.xml)**

After installation, the widget can be accessed via the `Service Portal > Widgets` section for use and customization.

Please replace the API Key in the Widget Dependency "x_pisn_sp_ng_map Google Map API key" with yours.

* SN Product Documentation - ['Load a customization from a single XML file'](https://docs.servicenow.com/bundle/newyork-application-development/page/build/system-update-sets/task/t_SaveAnUpdateSetAsAnXMLFile.html)

## Configuration

Available options:

* Origin

* Destination

* Current Position

* Current Position Image

* Travel Mode

### UI Dependencies

* [ngMap](https://rawgit.com/allenhwkim/angularjs-google-maps/master/build/docs/index.html)

* valid API key from [Google Cloud Platform](https://console.cloud.google.com/home/dashboard)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-big-link-to/README|pe-big-link-to]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-business-process-visualizer/README|pe-business-process-visualizer]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-card-scroll/README|pe-card-scroll]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-case-and-asset-map/README|pe-case-and-asset-map]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-cases-card/README|pe-cases-card]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal Widgets/serviceportal-widget-library/serviceportal-widget-library-master/src/pe-collapsible-form/README|pe-collapsible-form]]
