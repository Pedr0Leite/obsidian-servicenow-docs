---
title: "Managing large attachments — general guidelines"
aliases:
  - KB0563399
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563399
kb_number: KB0563399
last_modified: 2026-05-11
---

## Issue

  

We have seen some issues when customers increase the size limit of attachments that can be uploaded to instances. The default limit is 1GB as stated in [Limiting Attachment File Size](https://docs.servicenow.com/csh?topicname=r_AdministeringAttachments.html&version=latest "Limiting Attachment File Size"). The product documentation also states that increasing the limit can lead to issues in the user's session.

Such issues can be performance related. For example, the upload of a large file occupying a semaphore until that upload is complete. The same also applies when a user downloads that file. Should multiple users download the same file at about the same time, there are fewer semaphores available for every other transaction taking place on the instance. If there are no semaphores available for user sessions, this leads to an outage.

Capacity issues can also occur. With a large file limit it is possible that, in a given year, the attachments table will grow rapidly. This affects database size and the time it takes to do instance backups.

## Resolution

Here are some suggestions to reduce (if not avoid) over inflating the database size, depending on file types.  
  
**Videos**

As an example, you have a series of videos that you would like to embed within a knowledge base article. You could follow the steps in our documentation ([Embedding Video in HTML Fields](https://docs.servicenow.com/csh?topicname=t_EmbeddingVideoInHTMLFields.html&version=latest "Embedding Video in HTML Fields")), but that involves an upload of a potentially large file for a high quality video. On the other hand, you could create a corporate account on a video streaming service such as YouTube. The benefit of creating an account on a video streaming service is saving database capacity. Plus, the users can also control the quality depending on the bandwidth of their ISP (when working from home) for a smoother streaming experience.

![Video example of upload](/sys_attachment.do?sys_id=ba92d8548738439857288519dabb35eb "Video example of upload")

Additionally, if the video is intended for internal audiences, you can control the visibility so that only those with the links can view the video. Of course, instead of sharing the link, you can embed the video into the HTML of the knowledge base article.  

![Embedded video HTML video](/sys_attachment.do?sys_id=6e9298548738439857288519dabb35c4 "Embedded video HTML video")

  
**File Sharing**

The platform was not designed for file hosting and sharing. There are specialist services in this area, such as Box. Considering the sensitivity of your files, you can decide which files are uploaded to these services. Having a corporate account would allow you to keep files within an organization, retain control of security, and increase collaboration between peers.

If your organization has a policy against using cloud-hosting services, you can take an on-premise approach with tools such as [ownCloud](https://owncloud.org "ownCloud") (available for free). Using a cloud-hosting service gives you full control over which files are internal only, as well as having a dedicated server.  
  

**Attachment cleanup when archiving**

The ServiceNow platform currently has the ability to [archive records](https://docs.servicenow.com/csh?topicname=c_ArchiveData.html&version=latest "archive records"), such as inactive incidents or retired knowledge base articles. When archiving an inactive record, you can decide what happens to related records (for example, Reference fields or Document ID fields):

-   **Archive** – the related record is archived to the respective archive table (for example, ar\_attachment)
-   **Clear** – clear the relationship, but persist the related record's data in the original table
-   **Delete** – clear the relationship and delete the related record

Your organization (or national law) may have rules in place to dictate the retention of historical data depending on its type (for example, financial). This may have an impact on how you handle related records. If there are no policies or rules, you could potentially delete the attachments. Alternatively, archiving the attachments adds them to another table. This can affect the overall size of the database, but keeping the attachment table's size is still manageable while transaction times will not grow immensely.

<table class="noteTable" style="border: 1px solid rgb(224, 224, 224);" align="left"><tbody><tr><td style="vertical-align: middle; text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Disclaimer</strong>: The names of external services are only provided as examples and should not be seen as endorsements.</td></tr></tbody></table>
