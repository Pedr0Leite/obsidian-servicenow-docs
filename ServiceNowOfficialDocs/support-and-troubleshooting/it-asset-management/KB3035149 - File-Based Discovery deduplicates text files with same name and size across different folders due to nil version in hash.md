---
title: "File-Based Discovery deduplicates text files with same name and size across different folders due to nil version in hash"
aliases:
  - KB3035149
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3035149
kb_number: KB3035149
last_modified: 2026-05-21
---

## File-Based Discovery deduplicates text files with same name and size across different folders due to nil version in hash

  

## Issue

File-Based Discovery creates only one Unidentified File Set record for text files with the same name and size located in different folders. This occurs because the deduplication hash does not include the file path, and text files always have a nil version.

## Symptoms

-   Two text files with the same name and size in different directories result in only one Unidentified File Set record
-   File path is not considered in deduplication
-   Customer expects separate records for files in different locations
-   No errors logged — deduplication is silent

## Cause

The FBD deduplication logic computes a SHA256 hash using: **file\_name + '.' + file\_version (if not nil) + '.' + file\_size**. A business rule prevents insertion of records with matching hashes.

File path is intentionally excluded from the hash per **PRB1613464**.

For text files (.txt), the VersionResolver cannot extract version information because it relies exclusively on Windows PE VERSIONINFO metadata embedded in binary files (.exe, .dll). With path excluded and version absent, two text files sharing the same name and size produce identical hashes and are treated as the same file.

This is working as designed.

## Resolution

1.  This is working as designed. File path exclusion from the hash was a deliberate fix under **PRB1613464**.
2.  FBD can differentiate versions for .exe and .dll files because they carry embedded VERSIONINFO metadata.
3.  FBD cannot look at the contents inside a file to determine the version, nor can it use the file path as a determining factor.
4.  For use cases requiring file version tracking across locations for auditing purposes, consider using **Event Management** instead of Discovery.
5.  See also **KB2977718** for the full FBD deduplication chain documentation.
