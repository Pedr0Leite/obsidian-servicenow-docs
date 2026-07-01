---
aliases:
  - "Using Applicability in Next Experience Themes to s"
area: "System Properties"
source: notion-export
tags:
  - system-properties
  - next-experience
  - theming
  - ui-builder
  - workspace
---

# Using Applicability in Next Experience Themes to show different colors based on role

## Quick Links

[Theme Builder Store App](https://store.servicenow.com/sn_appstore_store.do#!/store/application/c8d18ffa2b695cec36b671673e27938d/1.0.1?referer=%2Fstore%2Fsearch%3Flistingtype%3Dallintegrations%25253Bancillary_app%25253Bcertified_apps%25253Bcontent%25253Bindustry_solution%25253Boem%25253Butility%25253Btemplate%26q%3Dtheme%2520builder&sl=sh)

[Theme Builder Product Documentation](https://docs.servicenow.com/csh?version=latest&topicname=configuring-next-experience-with-theme-builder)

[Next Experience Academy Session #6: Introducing Theme Builder](https://www.servicenow.com/community/next-experience-events/next-experience-academy-session-6-introducing-theme-builder/ev-p/2434763)

[Creator Toolbox: Theme Builder in Utah](https://www.youtube.com/watch?v=MEzCfNIZSW4)

---

## The Compositional Theme Data Model

This article will discuss what the applicability field is in Next 
Experience themes and how you can use it to show different styles to 
users based on personas. Before we jump into to creating our own UX 
Styles, let's discuss the Compositional Theme Data Model.

At a high level, our previous Legacy Theming Data Model was really 
just one stylesheet that encompassed a JSON object of CSS Variables. You
 could extend from other themes, but everything was still located in a 
hierarchical manner and mainly on one stylesheet. This approach was 
suitable for instances on Core UI and using workspaces that launched 
independently of other experiences because all the stylesheet had to do 
was apply styling to that one workspace. When Next Experience UI is 
turned on, configurable workspace experiences are wrapped within Next 
Experience, and now we're beginning to work with multiple applications 
in tandem so a hierarchical model no longer suited this scenario as 
we're now applying styling to multiple experiences.

With the introduction of Next Experience UI in San Diego we 
introduced the concept of a compositional theming data model. Using a 
compositional model, we're no longer using one large stylesheet to apply
 to our experiences, instead we're using a combination of stylesheets to
 compile our overall theme. The diagram below is an example of a theme 
that has multiple stylesheets.

[](https://www.servicenow.com/community/image/serverpage/image-id/239170iC92C6CCA191C5F78/image-size/large?v=v2&px=999)

---

## Applicability

With the knowledge that one core color style can be applied to the 
instance as a default and this color style applies to both Next 
Experience UI and configurable workspaces, how do we implement default 
colors based upon personas? A typical use case is applying different 
coloring to workspaces to differentiate the workspace.

You can do this with with a style using the Applicability field.  Applicability
 is specified to override the base theme. Users who meet the 
applicability constraints see those overrides in their theme rather than
 the base style. For example, a style with different colors can be 
applied to managers. Users who meet the manager applicability will see 
different colors in the Next Experience UI, which overrides the base 
system theme values. Administrators do not have to copy or create an 
entire theme with changes for the applicable audience.

Audience is a term used in multiple places in the platform, but for 
the purposes of theming, it is to the persona the style applies to. 
You'll also see the concept of [Audiences used with UI Builder pages](https://docs.servicenow.com/csh?version=latest&topicname=add-audiences), which also point to the same Audience table.

**Note: Leaving the Applicability constraint to empty will apply the style to all users.**

---

## Example

In this article, we're going to use the
 example of an Itil user versus a Customer Service Agent user and show 
how the workspaces can be different colors based upon the persona.

### Before Getting Started

If you haven't worked with themes before, or need more information on the fundamentals of the theming model check out this [article](https://www.servicenow.com/community/next-experience-articles/next-experience-ui-theming-fundamentals/ta-p/2332045)
 to get started. This article is going to start with a custom theme 
already implemented with Theme Builder. I've created a theme called 
SodaCo Utah, and Theme Builder automatically created the four associated
 styles I needed for the theme.

Here's a screenshot of what you should already have prior to using the following steps:

[](https://www.servicenow.com/community/image/serverpage/image-id/239171i9FCBBBD3EBC6687F/image-size/large?v=v2&px=999)

### 

### Create an Applicability Color Style for the CSM User

In this example, we want Customer Service Agents to have a default 
color palette of greens. We're going to use very basic CSS Variables to 
compose our theme, but these variables are not extensive and more 
granularity can be introduced if you choose.

1. In the **All** menu navigate to **Now Experience Framework > Theme Management > Themes** and locate the theme applied to your instance.

Under the Compositional: App Theme and **Insert a New row...**

2. In the **Applicability** column, choose CSM - Agent. 
This is an out-of-the-box audience that is shipped with CSM Configurable
 Workspace. You may or may not have the audience you want to used 
defined, if you have custom roles or other roles, you can create an 
audience at this point.

3. In the Order column, select a higher order than 0, such as 1. This
 means this style will be evaluated before the default Colors style with
 an order of 0. *This does differ from ordering in other areas of the platform, where 0 is considered a higher order than 1.*

4. In the **Style** column, a new style is going to be 
used for this example, but you may have a style you want to reuse. Be 
sure that the type of the style aligns with what you want to use, for 
example, you don't want to use a Variant style as a Core style, as 
changing it on the Theme record will apply the change to all themes the 
style is associated with.

Here's the example JSON used:

```jsx
{
    "base": {
        "--now-color--neutral": "127,175,92",
        "--now-color--primary": "57,145,48",
        "--now-color--secondary": "127,175,92",
        "--now-color_chrome--brand": "57,145,48"
    },
    "properties": {
        "--now-color_brand--neutral": "127,175,92",
        "--now-color_brand--primary": "57,145,48",
        "--now-color_brand--secondary": "127,175,92"
    }
}
```

[](https://www.servicenow.com/community/image/serverpage/image-id/239179i1F34C6C2D30883A3/image-size/large?v=v2&px=999)

5. Under the **Type** column, select the Core type. This
 means the style will apply by default, and will not be a user 
selectable variant in the User Preferences pane.

### Create an Applicability Color Style for the ITIL User

In this example, we want Service Operations ITIL users to have a 
default color palette of blues. We're going to use very basic CSS 
Variables to compose our theme, but these variables are not extensive 
and more granularity can be introduced if you choose.

1. In the **All** menu navigate to **Now Experience Framework > Theme Management > Themes** and locate the theme applied to your instance.

Under the Compositional: App Theme and **Insert a New row...**

2. In the **Applicability** column, choose SOW ITIL 
Audience. This is an out-of-the-box audience that is shipped with 
Service Operations Workspace. You may or may not have the audience you 
want to used defined, if you have custom roles or other roles, you can 
create an audience at this point.

3. In the Order column, select a higher order than 0, such as 1. This
 means this style will be evaluated before the default Colors style with
 an order of 0. *This does differ from ordering in other areas of the platform, where 0 is considered a higher order than 1.*

4. In the **Style** column, a new style is going to be 
used for this example, but you may have a style you want to reuse. Be 
sure that the type of the style aligns with what you want to use, for 
example, you don't want to use a Variant style as a Core style, as 
changing it on the Theme record will apply the change to all themes the 
style is associated with.

Here's the example JSON used:

### 

`{
    "base": {
        "--now-color--neutral": "204,204,204",
        "--now-color--primary": "1,152,253",
        "--now-color--secondary": "128,201,250",
        "--now-color_chrome--brand": "1,152,253"
    },
    "properties": {
        "--now-color_brand--neutral": "204,204,204",
        "--now-color_brand--primary": "1,152,253",
        "--now-color_brand--secondary": "128,201,250"
    }
}`

[](https://www.servicenow.com/community/image/serverpage/image-id/239181i9BAFDB98B75AB79F/image-size/large?v=v2&px=999)

5. Under the **Type** 
column, select the Core type. This means the style will apply by 
default, and will not be a user selectable variant in the User 
Preferences pane.

Here's an example of our theme after adding these two additional core styles. **Note:
 You can see the styles being applied to Admin, so if you don't want 
them to apply to Admin, you'll have to create another style for your 
Admin audience.**

[](https://www.servicenow.com/community/image/serverpage/image-id/239182i720B32482626A13D/image-size/large?v=v2&px=999)

So let's see a YouTube video of all of this in action, in this video 
I'll run through the steps and impersonate three different users 
(sn_customerservice_agent, itil, and one without those roles) to show 
how different default colors can be applied by role.

[https://youtu.be/kuvL7zlUbsU](https://youtu.be/kuvL7zlUbsU)

## Related
- [[Workspace for a custom app forms]]

- [[System Properties]]
- [[Workspace App Shell UX Page Properties]]
- [[ServiceNow – Service Portal]]