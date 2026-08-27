---
title: "Customization Support FAQ and Guidelines"
aliases:
  - KB0728414
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0728414
kb_number: KB0728414
last_modified: 2026-04-30
---

## Issue

# What is a Customization?

A customization is an extension or modification of a ServiceNow feature that requires custom coding and some form of implementation outside the "out of the box" context (OOB).

Examples:

-   Change in scripting from the available OOB features, which creates a sys\_update\_xml record showing that it was customized
-   New script not owned and not directly supported by ServiceNow.
-   Changing UI Action
-   Creating lookup tables by modifying code

#### How do you know if you have a customization?

Your questions/requests may include things like:

-   "I need xyz created"  
    -   I need to link a quotation for 10 cables to different servers.
    -   The problem is that from the form I can only select a Parent server.
    -   I need to proceed like with the Aoftware license to link the total cables to different servers until the total is empty. How do I do that?
-   "What code do I need to create xyz?"
-   "This code doesn't work, but it did before the upgrade." (Revert back to OOB, and schedule jobs to be run.)
-   "Something is broken (may be a customization)"
-   "This code is not working as expected." 

### What is a Configuration change?

This is different from a **configuration change,** using native ServiceNow capabilities and tools in the system to change its behavior or features to address business needs. Any changes to the configurable data which changes the functionality of the application are considered as a _configuration change_ and are supported by ServiceNow unless otherwise documented.

Examples:

-   Adding an ACL
-   Changing a system Property
-   Something like glide.ui.escape\_text being set to _false_.

Any configuration should be a data-driven change and should be easy to revert without any changes to the ServiceNow code base. 

### Differentiating among Customizations, Implementations, Configurations

-   Different to OOB feature
-   Creator of customization is responsible for updating and maintaining that code after the upgrade

<table style="border-collapse: collapse; width: 100%; height: 52px;" border="1"><tbody><tr style="height: 13px;"><td style="width: 20%; height: 13px;">&nbsp;</td><td style="width: 20%; height: 13px;">Key Differentiator</td><td style="width: 20%; height: 13px;">Is</td><td style="width: 20%; height: 13px;">Is not</td><td style="width: 20%; height: 13px;">Example</td></tr><tr style="height: 13px;"><td style="width: 20%; height: 13px;">Customization</td><td style="width: 20%; height: 13px;"><ul><li>Different to OOB feature</li><li>Creator of customization is responsible for updating and maintaning that code including after upgrade.</li></ul><p>&nbsp;</p></td><td style="width: 20%; height: 13px;">A customization is a modification of a ServiceNow OOB feature or adding a new feature.</td><td style="width: 20%; height: 13px;">Tweaking properties or parameters in order to use a functionality.</td><td style="width: 20%; height: 13px;">Suppose a custom script include used a glide record API call that used to work and now does not function as documented.</td></tr><tr style="height: 13px;"><td style="width: 20%; height: 13px;">Implementation</td><td style="width: 20%; height: 13px;"><ul><li>How to Questions</li><li>Best Practice configurations</li><li>Troubleshooting of custom code</li></ul></td><td style="width: 20%; height: 13px;">An Implementation is setting up SN platform as per the design to get users and/or organizations ready for the Go-Live.</td><td style="width: 20%; height: 13px;">Support educating a feature/function or suggesting best practices.</td><td style="width: 20%; height: 13px;">&nbsp;A customer reports that the attachment pop-up progress bar does not stop spinning when they try to attach a file. Support discovers this is caused by an upgrade conflict with a UI page that has been offered from the base system by a partner.&nbsp;</td></tr><tr style="height: 13px;"><td style="width: 20%; height: 13px;">Configuration</td><td style="width: 20%; height: 13px;">Adjusting available system properties or settings of OOB features or products.</td><td style="width: 20%; height: 13px;">A configuration change is where we use native ServiceNow capabilities and tools in the system to change its behavior or features to address busines needs.&nbsp;</td><td style="width: 20%; height: 13px;">A code change that results in the creation of a version difference.&nbsp;</td><td style="width: 20%; height: 13px;">Adding an ACL or changing a system property. Any changes to the configurable data which changes the functionality of the application are considered as a configuration change and are supported by ServiceNow unless otherwise documented, such as glide.ui.escape_text being set to false.&nbsp;</td></tr></tbody></table>

#### What happens if you decide to customize code that is part of a baseline installation?

-   You will need to maintain that code going forward
-   You will be responsible for making sure that functionality still works after an upgrade 

#### How your admin can check to see if you have customizations on your system

1.  If you have a new feature implemented by your own dev group or by your partner, check to see if this feature is owned by your company:

1.  -   Review the "created by/updated" by field of one of the records involved (script include, business rule, etc) and cross-reference it with the name of the person with your sys\_user table.
    -   If you find that user in the sys\_user table, it means that the customization is owned by your company (though it may have been a partner or ServiceNow professional services that did the work).

2.  To identify where your company customized OOB objects, the system adds a corresponding record in the _Customer Updates_ \[sys\_update\_xml\] table. The table maintains the current version information for all objects that have been customized. The upgrade process will skip changes to objects that have entries in this table. The upgrade process does not skip objects if only excluded fields have changed.

### Things to consider if you decide to customize

-   New releases come every six months introducing new features, bug fixes, etc  
    -   If you are OOB, no problem.
    -   For configurations, these may last a couple days.
    -   For customizations, it could take months and impact your future upgrade if previous upgrade was not yet complete.
    -   Upgrades could break custom code
    -   If heavily customized, you may miss out on upgrades, along with new features, bug fixes, etc.

#### Best Practices for Customizations

-   [Link to Customization Best Practices](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/success/quick-answer/customization-best-practices.pdf)

#### Handling customizations from your company’s perspective

-   If the feature is fully customized, reach out to the person who built this new feature or one of your technical resources to check the customization.  
    -   After review, if the initial analysis is believed to be an issue with a specific supported/documented functionality from ServiceNow, create a case with Technical Support and highlight the specific line of code or functionality that should be working and what the expected result is.
-   If an OOB feature was overwritten by customizations, review the OOB version of the object and compare it with your own version.  
    -   If an OOB feature is updated by a company, the expectation is that for each upgrade any of those customizations are checked against the upgrade history log and review all the skip updates on any of those OOB objects (scripts/properties/feature).
    -   As the ServiceNow platform evolves, it is possible you will need to compare the OOB files with your customization(s) and merge the new OOB updates with your customization. Once the code has been merged into the out of box version of the object, thorough testing should be done to ensure it is functioning as expected.

Please refer to the documentation: [Resolve a skipped update set and set a resolution status.](https://docs.servicenow.com/csh?topicname=t_ResolveASkippedUpdate.html&version=latest "documentation to resolve a skipped update set and set a resolution status.")

#### Need help with Customizations?

-   Review or post in our [Community](https://community.servicenow.com/community) site, for guidance on implementations and ideas on how to accomplish non-OOB functionality. 

For assistance with building customizations, please engage your sales representative to put you in touch with our Professional Services team who is specialized in helping with implementations/customizations or guide you to one of our supported partners.

-   [Find a partner](https://www.servicenow.com/partners/find-a-partner.html "Find a partner")
-   [Expert Services](https://www.servicenow.com/services/expert-services.html "Expert Services")

## Resolution
