---
title: "Normalize many Software Discovery Models"
aliases:
  - KB2655054
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2655054
kb_number: KB2655054
last_modified: 2025-11-27
---

## Normalize many Software Discovery Models

  

The Content Library automatically normalizes 85-98% of software records out of the box, but the remaining percentage can include thousands of records. [Manual normalization](https://www.servicenow.com/docs/csh?topicname=t_EditASoftwareDiscModel.html&version=latest) is possible, but it can be time consuming.

1\. Opt-in to ITAM / SAM Content Service

Validate if you are [opt-in to the ITAM Content Service](https://www.servicenow.com/docs/csh?topicname=c_SAMContentService.html&version=latest) and opt-in if it meets your requriements. When opt-in, unnormalized software installation data is shared from your organization with ServiceNow, allowing for automatic content updates based on your unique software installation footprint.

2\. Submit a Content Request

[Submit a Content Request](https://www.servicenow.com/docs/csh?topicname=content-request-itam.html&version=latest) through the Support portal with the records directly attached. The ITAM Content team will normalize the records and add the normalization to the Content Library, which is delivered to your instance through content updates. This is also recommended for customers who are opt-in to the Content Service as updates will be provided for the requested records.

When submitting the request, [export the Discovery Models from the list](https://www.servicenow.com/docs/csh?topicname=export-list-data.html&version=latest) and attach the file to the request.

As requests with a large number of records may span several content update cycles. We recommend you prioritise the records most relevant to your requirements. This can be done by considering the Publisher / Product, such as by spend, or the number of related Software Installations.

If data is added to the Content Library for any manually normalized records, [a normalization suggestion](https://www.servicenow.com/docs/csh?topicname=normalization-suggestions.html&version=latest) will be created, providing the option to revert to the out of the box normalization values.

3\. [Pattern Normalization Rules](https://www.servicenow.com/docs/csh?topicname=t_AddAPatternNormRule.html&version=latest)

Rules can be created to normalize similar records in bulk.

4\. [Machine Learning Normalization](https://www.servicenow.com/docs/csh?topicname=ml-learning-sam.html&version=latest)

Machine learning normalization can be used to use normalize the version, full version, and edition fields.
