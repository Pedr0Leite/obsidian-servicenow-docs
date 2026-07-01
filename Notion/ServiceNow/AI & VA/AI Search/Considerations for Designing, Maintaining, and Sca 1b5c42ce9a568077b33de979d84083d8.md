---
aliases:
  - "AI Search – Considerations for Designing, Maintaining, and Sca"
area: "AI & VA"
source: notion-export
tags:
  - ai-search
  - search-relevancy
  - scaling
  - governance
---

# Considerations for Designing, Maintaining, and Scaling the Solution

Follow recommendations to avoid lost opportunities and an inability to take full advantage of your investment.

## Maintaining the Search Experience

The following are a few ways through which we can maintain the search experience on par with the expectations:

1. For queries with no clicks, use Result Improvement rules to promote and
boost relevant search results displayed on top. If no content is
available, create the same based on the frequency of the query asked.
2. Add user context to some queries by adding appropriate rules to trigger
them. This would help users to get back only data relevant to them.
3. Have a process to collect and approve synonyms that can be added to the AI
Search configuration. You may also need to add/remove stop words, while
others may warrant adding a new one.
4. Click position improvement may be achieved by document boosting and related rules.
5. Disable the generation of suggestions from specific search strings to keep
expletives from appearing in search results or to prevent disclosure of
personal or secure information.

## Maximizing Relevancy

How
 do you improve search results? While machine learning–based relevancy 
will automatically optimize AI Search results over time, the following 
techniques may be used to maximize relevancy. They are handy for 
bootstrapping, while user interactions are not yet available to learn 
from. AI Search relies on various content features to maintain a good 
relevancy ranking of search result documents. These include:

- **Document freshness** — how recently the document was created and/or updated.
- **Document popularity** — how often the document has been viewed.
- **Title match** — how well the query matches the document’s title.
- **Content match** — how well the query matches the document’s body content.
- **Tags match** — how well the query matches the document’s tags.
- **Tags popularity** — the popularity of the document’s tags.

## Introducing New Changes to AI Search Configuration

There
 needs to be a process to introduce new AI Search configuration changes 
that must go into production. Although the exact process of change will 
be different for different organizations, in general:

1. Once
the queries that need improvement are identified, they may optionally be logged into the project management software and assigned to business
unit SMEs along with the team managing AI Search for tracking and
collaboration.
2. The identified queries can then be improved
either in sub-prod instance and tested by a set of trusted experts
before they are moved to production via an update set or directly be
updated in production instances in case of minor changes (like boosting, promoting, or blocking some documents) provided the team is comfortable with it.

## Related

- [[AI Search]]
- [[AI Search Synonyms]]
- [[getSimilarRecords Script]]
- [[Now Assist in AI Search]]