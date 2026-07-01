---
title: Embedded lists for a record screen
description: Use an embedded list to place a list of information that is related to your current record within a segment on your record screen so that your users don't have to navigate to a related list.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/sg-embedded-list.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Record screen, Mobile screen types, Mobile screens, Mobile app components, Building mobile apps, Mobile Platform]
---

# Embedded lists for a record screen

Use an embedded list to place a list of information that is related to your current record within a segment on your [[form-screen|record screen]] so that your users don't have to navigate to a related list.

<table id="table_ryt_ynb_xlb"><tbody><tr><td>

Use embedded lists to display lists of related information in an easily accessible record screen segment rather than having your users navigate away to a related list. For example, you could add a list of records representing computer parts or software to your work order form.

 To create an embedded list on a record screen, you will first need to perform the following tasks:

 -   **Create a data item to contain the data for your embedded list**

You need a data item to store the data that appears in your embedded list. To create a data item, follow the process in [[sg-studio-create-data-item|Configure a standard data item]].

-   **Create a [[list-screen|list screen]] using that data item**

You need to configure a list to embed into your record screen. You can create this list using the process detailed in [[sg-configure-list-screen|List screen configuration]].

-   **Embed your list into your record screen**

For details on this process, see [[create-embedded-list-1|Configure an embedded list for a record screen]].


</td><td>

\[Omitted image "embedded-list.png"\] Alt text: Embedded list showing part records on a work order form.

</td></tr></tbody>
</table>

## Related

- [[sg-studio-create-data-item|Configure a standard data item]]
- [[sg-configure-list-screen|List screen configuration]]
- [[create-embedded-list-1|Configure an embedded list for a record screen]]
- [[form-screen|Record screen]]
- [[list-screen|List screen]]
