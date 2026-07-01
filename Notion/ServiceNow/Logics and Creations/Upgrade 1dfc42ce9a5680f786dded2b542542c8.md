---
aliases:
  - "Upgrade"
tags:
  - upgrade
  - cloning
  - data-preservation
  - mid-server
  - logics-and-creations
---

# Upgrade

Preserve data:

Data preservers

Sometimes, it is necessary to preserve some data on an instance targeted for cloning. For example, if the target is a MID Server, you must not overwrite the MID Server [ecc_agent] table. Preserved data is stored on the target instance before cloning begins and is restored on the target instance after cloning.

[https://docs.servicenow.com/bundle/orlando-platform-administration/page/administer/managing-data/con...](https://docs.servicenow.com/bundle/orlando-platform-administration/page/administer/managing-data/concept/data-preservation.html)

Exclude data:

[https://docs.servicenow.com/bundle/orlando-platform-administration/page/administer/managing-data/tas...](https://docs.servicenow.com/bundle/orlando-platform-administration/page/administer/managing-data/task/t_ExcludeATableFromCloning.html)

***Basically:***

Preserve means: keep what data is already there on the target instance, but add to it.

Exclude means: If no preserve, don't even bring data to the target instance, but instead make it empty. Otherwise, if perserved, but excluded, then keep what is there, but don't touch it.

## Related

- [[Logics and Creations]]
- [[How to Backup All Development Work in 1 Click]]
- [[Updating Store Apps Sucks]]
- [[Mid Server]]