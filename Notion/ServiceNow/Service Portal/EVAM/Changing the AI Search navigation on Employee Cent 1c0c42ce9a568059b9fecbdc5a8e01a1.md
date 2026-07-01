---
aliases:
  - "Changing the AI Search navigation on Employee Cent"
area: "Service Portal"
source: notion-export
tags:
  - service-portal
  - evam
  - ai-search
  - employee-center
  - navigation
---

# Changing the AI Search navigation on Employee Center [How-To]

## Changing the navigation URL on Employee Center

In this technical How To article, we'll cover the configuration steps
 needed to change the behavior of the navigation when a user clicks on a
 search result.

In this use case, the current behavior for Knowledge articles is that the KB sys_id is used to navigate to the KB page.

We want to change the URL to use the KB number (for example KB000001) instead, so the new URL uses the *sysparm_article* URL parameter instead of the *sys_id*.

Note that in this use case, the widget on the KB page is built OOB to
 handle both the URL with the sys_id and the KB number so we'll focus on
 the AI Search configuration without reworking any widget.

[](https://www.servicenow.com/community/image/serverpage/image-id/88476i9C8255C4D0F87D90/image-size/large?v=v2&px=999)

---

### Finding the EVAM configuration

Navigate to the **Portals** list, then open the **Employee Center** record.

Scroll to the bottom of the form and open the Search Results Configuration record.

[](https://www.servicenow.com/community/image/serverpage/image-id/88477i2698F292D68E37D7/image-size/large?v=v2&px=999)

On this page, open the **EVAM View Config Bundle M2Ms** tab and open the **Taxonomy Portal Search Bundle** record (click on the label, not the icon).

[](https://www.servicenow.com/community/image/serverpage/image-id/88484i45F044647131E808/image-size/large?v=v2&px=999)

Scroll through the list and open the **Taxonomy - Knowledge Search Results** record.

[](https://www.servicenow.com/community/image/serverpage/image-id/88474iEF51B9A34178C614/image-size/large?v=v2&px=999)

Tip 1: EVAM View Config drives how search results are displayed and what actions can be taken.

To
 find which EVAM View Config record drives the search results you're 
looking to modify, filter by table and look at the Condition field. If 
there aren't any records, it means the Default Search Results record 
will be used.

Tip
 2: If you are creating new EVAM View Config records, make sure they are
 part of a Bundle and linked to the Portal via the EVAM Definition.

On the **Taxonomy - Knowledge Search Results** record form (it's an **EVAM View Config** record), make sure that the **Number** is available in the list of **Table Fields**.

[](https://www.servicenow.com/community/image/serverpage/image-id/88479i0E1B9A044EC057E2/image-size/large?v=v2&px=999)

[Untitled](Changing%20the%20AI%20Search%20navigation%20on%20Employee%20Cent/Untitled%201c0c42ce9a5680968865d2b3085d94b9.csv)

### Changing the EVAM configuration

From the **Taxonomy - Knowledge Search Results** record form, scroll to the **EVAM View Config Action Assignment M2Ms** related list and open the **navigation**
 record by clicking on the label (not the icon). To make the next few 
steps more manageable we recommend opening that record in a new browser 
tab.

[](https://www.servicenow.com/community/image/serverpage/image-id/88481i436DE2B220491129/image-size/large?v=v2&px=999)

The **Navigation** record is opened (it's an **Action Assignment** record), then open the record in the **Specify client action** field. To make the next few steps more manageable we recommend opening that record in a new browser tab.

[](https://www.servicenow.com/community/image/serverpage/image-id/88492i856775960EEB8A4E/image-size/large?v=v2&px=999)

The **Navigation** record is opened in a new tab (it's an **Action Payload Definition** record). Change the **Key** and **Label** fields to match the picture below. Then click **Insert and Stay** to create a new record.

Key: KB_NAVIGATION

Label: kb_navigation

Then, change the **Payload** field and Save.

Payload:

{

"table": "{{table}}",

"sysparm_article": "{{number}}",

"url": "{{navigation_url}}"

}

[](https://www.servicenow.com/community/image/serverpage/image-id/88485iA30BE5D80EB9300E/image-size/large?v=v2&px=999)

Make sure that the **Action Payload Mappings** and **Action Payload Fields** show the new **Payload** parameters.

[](https://www.servicenow.com/community/image/serverpage/image-id/88488iCBBC891B3E215D9F/image-size/large?v=v2&px=999)

Go back to the previous browser tab showing the **Navigation** record (the **Action Assignment** record). Change the **Action label**, **Action name** and **Specify client action** and click **Insert and Stay**.

Action label: KB Navigation

Action name: kb_navigation

Specify client action: kb_navigation

[](https://www.servicenow.com/community/image/serverpage/image-id/88478i8A168B008E670898/image-size/large?v=v2&px=999)

Go back to the previous browser tab showing the **Taxonomy - Knowledge Search Results** record form (it's an **EVAM View Config** record), scroll to the **EVAM View Config Action Assignment M2Ms** related list, click **Link Existing** and select the kb_navigation **Declarative Action** then **Submit**.

[](https://www.servicenow.com/community/image/serverpage/image-id/88482iF1B6FDD29DEDDCD9/image-size/large?v=v2&px=999)

The **Taxonomy - Knowledge Search Results** record has now 2 records on the **EVAM View Config Action Assignment M2Ms** related list.

[](https://www.servicenow.com/community/image/serverpage/image-id/88486iCFF5087C7BFD6BE4/image-size/large?v=v2&px=999)

While still on the **Taxonomy - Knowledge Search Results** record form, open the record in the **View Template** field.

[](https://www.servicenow.com/community/image/serverpage/image-id/88491i7AF6C2DFD77AD7F7/image-size/large?v=v2&px=999)

Modify the value **actionMappings** in the **Template** field.

[](https://www.servicenow.com/community/image/serverpage/image-id/88490i4809B4175A61B1EB/image-size/large?v=v2&px=999)

Template:

"actionMappings": {

"clickAction": "kb_navigation"

}

[Untitled](Changing%20the%20AI%20Search%20navigation%20on%20Employee%20Cent/Untitled%201c0c42ce9a568032929df956f55397dc.csv)

### Changing the navigation behavior

Navigate to **Search Results Actions** and open the **Knowledge** record for Employee Center.

[](https://www.servicenow.com/community/image/serverpage/image-id/88483i581F7DDD0053F33C/image-size/large?v=v2&px=999)

Edit the **Action name** value to be **kb_navigation**, then **Save**.

[](https://www.servicenow.com/community/image/serverpage/image-id/88487i7DE9AD6864EA9B14/image-size/large?v=v2&px=999)

Check that the parameters we created for the **Action Payload Definition** record are now displayed in the **Payload query parameters** field.

[](https://www.servicenow.com/community/image/serverpage/image-id/88495i4B76D27640727759/image-size/large?v=v2&px=999)

Open Employee Center and start a new search, open a KB result and notice that the URL now uses the **number** parameter.

[](https://www.servicenow.com/community/image/serverpage/image-id/88494i29246BB7435B221D/image-size/large?v=v2&px=999)

[Untitled](Changing%20the%20AI%20Search%20navigation%20on%20Employee%20Cent/Untitled%201c0c42ce9a56800f839bcb2c58ffeb4e.csv)

### References

[Untitled](Changing%20the%20AI%20Search%20navigation%20on%20Employee%20Cent/Untitled%201c0c42ce9a5680b7a2e0d7e7afd690a3.csv)

## Related
- [[Sharepoint integration]]
- [[Search Sources]]

- [[EVAM]]
- [[EVAM Navigation – Untitled]]
- [[EVAM View Template - JSON Configuration]]
- [[AI Search]]