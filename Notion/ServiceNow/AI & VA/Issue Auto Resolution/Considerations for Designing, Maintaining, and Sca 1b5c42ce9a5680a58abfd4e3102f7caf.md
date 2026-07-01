---
aliases:
  - "Issue Auto Resolution – Considerations for Designing, Maintaining, and Sca"
tags:
  - issue-auto-resolution
  - virtual-agent
  - itsm
  - upgrades
---

# Considerations for Designing, Maintaining, and Scaling the Solution

## Upgrading to Future Releases

Customized
 scripts such as Script Includes, Business Rules, Client Scripts, 
Virtual Agent Topic Scripts, etc., may cause Issue Auto Resolution to 
stop working when upgrading to a new release. Therefore, it is 
recommended that all customizations be reverted to their out-of-the-box 
state and then selectively apply all previous updates over the 
out-of-the-box release version.

## Activate Plugin

Starting
 in the Tokyo release, Issue Auto Resolution processing depends on ITSM 
Roles (com.snc.itsm.roles) plugin to be enabled on instance. The Virtual
 Agent user needs the plugin to interact with the incident, Issue Auto 
Resolution Context records, and end user. If this plugin is inactive, 
customers would need to activate the plugin for Issue Auto Resolution to
 function fully.

## Check Product Documentation

Issue
 Auto Resolution is a new and evolving solution, so be sure to check the
 release notes and documentation around new features and adjust the 
processes, especially around tuning and monitoring Issue Auto Resolution
 performance, to take advantage of the latest features.

## Related

- [[Issue Auto Resolution]]
- [[VA - Basic Arch and ACLs]]
- [[Task Intelligence – Considerations for Designing, Maintaining, and Sca]]