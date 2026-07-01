---
aliases:
  - "Engagement Messenger"
tags:
  - engagement-messenger
  - csm
  - service-portal
  - javascript
  - install-stuff
---

# Engagement Messenger

[https://github.com/dylanlindgren/servicenow-em-demo](https://github.com/dylanlindgren/servicenow-em-demo)

![Untitled](Engagement%20Messenger/Untitled.png)

<script>
function loadScript(url) {
return new Promise((resolve, reject) => {
const script = document.createElement('script');
script.src = url;
script.onload = resolve;
script.onerror = reject;
document.body.appendChild(script);
});
}

```
    loadScript('<https://ABC.service-now.com/script/sn_csm_ec.jsdbx>')
        .then(() => {
            console.log('PL - Script loaded successfully');
             SN_CSM_EC.init({
moduleID: "<https://CBA/#3493bf578706e11012a5cbbc8bbb3513>",
loadFeature: SN_CSM_EC.loadEMFeature(),
enableRecommendations: true

```

});
})
.catch((error) => {
console.error('PL - Error loading script:', error);
});
</script>

## Related

- [[Install Stuff]]
- [[Enable Engagement Messenger on a website when thir]]
- [[Multi-provider SSO]]
- [[SAML Errors and Fixes (Multiple Provider SSO)]]