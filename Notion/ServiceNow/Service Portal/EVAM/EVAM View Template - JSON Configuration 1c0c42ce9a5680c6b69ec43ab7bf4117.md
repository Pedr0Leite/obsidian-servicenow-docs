---
aliases:
  - "EVAM View Template - JSON Configuration"
area: "Service Portal"
source: notion-export
tags:
  - service-portal
  - evam
  - ui-builder
  - json
  - now-experience
---

# EVAM View Template - JSON Configuration

If you’ve setup an

[EVAM data resource](https://docs.servicenow.com/bundle/quebec-servicenow-platform/page/administer/evam/concept/evam-overview.html)

for the UI Builder or followed along with @Brad Tilton's

[blog](https://developer.servicenow.com/blog.do?p=/post/quebec-ui-builder-evam/)

, you’ll know that as part of the setup steps, you have to configure a View Template [sys_ux_composite_data_template] using some JSON *magic*.

After some trial and error, I’ve managed to map the JSON from the 
sample provided at the bottom of the View Template configuration page to
 the data displayed in the Data Set component (using User [sys_user] table as an example) as follows…

**Static Values**

[](https://www.servicenow.com/community/image/serverpage/image-id/152955i01CB40864B40B6B1/image-size/large?v=v2&px=999)

**Mappings**

[](https://www.servicenow.com/community/image/serverpage/image-id/152957i15E437A89B0E744C/image-size/large?v=v2&px=999)

[](https://www.servicenow.com/community/image/serverpage/image-id/152971i495E844AFD90AE19/image-size/large?v=v2&px=999)

Here’s the View Template [sys_ux_composite_data_template] JSON used:

```markup
{
    "component": "now-card-evam-record",
	"staticValues": {
		"highlightedHeaderIcon": {
			"translatable": false,
			"key": "user-outline"
		},
		"highlightedHeaderBkgColor": {
			"translatable": false,
			"key": "critical"
		},
		"subtitleIcon": {
			"translatable": false,
			"key": "calendar-fill"
		},
		"imageType": {
			"translatable": false,
			"key": "image"
		},
		"subtitleImageType": {
			"translatable": false,
			"key": "avatar"
		},
		"detailLabelOne": {
			"translatable": true,
			"key": "Email address"
		},
		"detailLabelTwo": {
			"translatable": true,
			"key": "Works for"
		},
		"detailLabelThree": {
			"translatable": true,
			"key": "Business phone"
		}
	},
	"mappings": {
		"highlightedHeaderLabel": "title",
		"textHeaderLabel": "department",
		"titleLabel": "name",
		"imageURL": "avatar",
		"subtitle": "user_name",
		"subtitleAvatarName": "name",
		"subtitleAvatarURL": "avatar",
		"detailValueOne": "email",
		"detailValueTwo": "company",
		"detailValueThree": "phone"
	},
	"actionMappings": {
		"clickAction": "navigation"
	}
}

```

## A few things to note

1. **detailLabelThree and detailValueThree do NOT appear when using *Grid* view with Card Height of *Small***
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/152975iD1398116A5777896/image-size/large?v=v2&px=999)
    
    Small card:
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/152961i646617180F053F6E/image-size/large?v=v2&px=999)
    
2. **Remove subtitleAvatarURL from the mappings to remove the duplicate image**
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/152959i07210C17CD046F2D/image-size/large?v=v2&px=999)
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/152973i2A6AC505FC6527F7/image-size/large?v=v2&px=999)
    
3. **To get rid of it entirely, remove subtitleImageType from static values too**
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/152963iF41462C6E64832F0/image-size/large?v=v2&px=999)
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/152969i565F7930A02E25BA/image-size/large?v=v2&px=999)
    
4. **Options for the *key* value for highlightedHeaderBkgColor see the options listed under [the sidebar property of the now-card component](https://developer.servicenow.com/dev.do#!/reference/now-experience/quebec/now-components/now-card/api):**
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/152965iF40EBD2FEA4AFA9C/image-size/large?v=v2&px=999)
    
    [](https://www.servicenow.com/community/image/serverpage/image-id/152967i21BC090C13C2B987/image-size/large?v=v2&px=999)
    

I anticipate that ServiceNow will eventually make it easier to 
configure the View Template via a GUI, instead of via JSON - perhaps in 
some manner like the [Mobile Card Builder](https://community.servicenow.com/community?id=community_blog&sys_id=6bb491a91b007410fc3233bc1d4bcb4a).

But until then, I hope this has been a handy resource.

## Related
- [[EVAM Navigation – Untitled]]

- [[EVAM]]
- [[Changing the AI Search navigation on Employee Cent]]
- [[ServiceNow – Service Portal]]