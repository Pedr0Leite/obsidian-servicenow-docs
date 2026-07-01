---
aliases:
  - "AI Search Synonyms"
tags:
  - ai-search
  - synonyms
  - search-relevancy
---

# AI Search Synonyms

[AI Search’s Synonym](https://docs.servicenow.com/csh?version=latest&topicname=synonyms-ais) feature is extremely powerful but requires a careful eye and an awareness of the content before configuring. The first thing to note is that AI Search’s Synonyms act identically to the [dictionary definition](https://en.wikipedia.org/wiki/Synonym). Unless the two terms can be substituted for each other in a sentence, they should not be used.

The recommendation is to be reactive instead of proactive in most cases. While it could be helpful to add a few entries to get started, the administrator should review the ‘Queries with no results’ to get a better understanding of the audience's search patterns. The configuration is done on a per [profile](https://docs.servicenow.com/csh?version=latest&topicname=defining-search-profiles-ais) basis and the administrator can associate more than one Synonym dictionary to a given Search Profile.

**Key Considerations for Synonym Functionality:** 

- Synonym terms and their payload carry equal weight for relevancy
- Synonym terms and their payload are bidirectional
- The synonym term: *'cat'* with payload '["*animal*"]’ will cause queries with *cat* to expand to *animal* and queries with *animal* to expand to *cat*.
- Matches occur on both term and payload.
    - Meaning if you have the following configured: term*: benefit;* payload*: [“401k”, “ESPP”]* and an additional term*: ESPP;* payload*: [“Employee Stock Purchase Plan”, “stock”]*

**A search for: *ESPP* will match on ESPP, *benefit*, *employee stock purchase plan*, and *stock* which could lead to a noisy search experience.** 

**General Synonym Guidelines:**

**Do:**

1. Use the dictionary form of the word. For nouns, use the singular form. For verbs, the infinitive.

2. Include brand names and proprietary software/hardware if such terms would be universally applicable to the searches

3. Include units and their abbreviations that are relevant to the IT domain.

**Example:**

gigabits per second ↔ Gbps

4. Flag 2-letter acronyms and other short acronyms/terms ambiguous in meaning for review.

**Examples:**

AA ↔ anti-aliasing

dB ↔ database

**DO NOT:**

1. DO NOT include terms pairs where one is a subcategory of the other.

**Example:** 

Chromebook ↔ laptop

2. DO NOT include terms that share the same parent class but are not strictly synonymous:

**Example:**

Microsoft Windows 10 ↔ Red Hat Enterprise Linux 6

3. DO NOT include quantities + unit pairs for arbitrary quantities.

**Examples:**

10 gigabits ↔ ten gigabits

2 sides ↔ two sides

However, if the quantity is part of a finite set pertinent to the domain, as in the case of standards, it may be included.

**Examples:**

- 5G ↔ fifth generation
- BT4.0 ↔ Bluetooth 4.0

4. DO NOT include misspellings of words that are not valid synonyms.

**Example:**

accessory ↔ accessary (not synonymous)

However, *valid* spelling variants may be included.

5. DO NOT include definitions or descriptions of terms. These are likely to contribute noise to search results.

**Examples:**

client ↔ computer connected to a server

firewall ↔ designed to block or prevent attacks

enterprise-grade ↔ self-assessing your application for enterprise adoption

6. DO NOT include related words or phrases that are not strictly synonyms:

**Examples:**

authorization ↔ proxy

blueprint ↔ schema

capability ↔ predisposition

conferencing ↔ talk

cyber ↔ mechanized

dynamic ↔ functional

files ↔ file management app

automated ↔ real-time

The team hopes this helps. Please feel free to ask questions about synonyms here.

[Dictionary Term form • Zurich ServiceNow AI Platform Administration • Docs | ServiceNow](https://www.servicenow.com/docs/r/platform-administration/ai-search/dictionary-term-form-ais.html)

## Related

- [[AI Search]]
- [[AI Search – Considerations for Designing, Maintaining, and Sca]]
- [[getSimilarRecords Script]]
- [[Now Assist in AI Search]]