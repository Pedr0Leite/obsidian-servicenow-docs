---
aliases:
  - "getSimilarRecords Script"
tags:
  - ai-search
  - vector-search
  - scripting
  - troubleshooting
  - performance
---

# getSimilarRecords Script

Get Similar Records AIS Documentation

# Case Information

Case ID: CS9293768

Title: The AI search, such as getSimilarRecordsForCase, is not working properly

# Overview

The issue is related to failures and timeouts in the custom script U4getSimilarRecordsForCase, which performs semantic (vector) search using AIS.

The search runs over a very large dataset (~5.3M cases and ~9.8M embeddings), making performance highly sensitive to query configuration.

# Root Cause Analysis

The main issue was not a broken script, but how semantic search behaves under certain conditions.

The custom script combined semantic search with restrictive filters (e.g., resolution_code, state, product).

Instead of reducing the dataset, these filters made the search heavier, forcing AIS to scan more of the vector index.

This caused queries to exceed the default ~10-second timeout, resulting in SocketTimeoutException errors.

# Misconceptions

Misconception: Adding restrictive filters improves performance because it reduces the dataset.

Reality: In semantic search, filters do not shrink the search space; they add constraints after similarity evaluation.

This means the engine must search broadly first, then discard results that don't match filters.

Result: more traversal, deeper scans, and higher latency.

Misconception: Increasing documentMatchThreshold improves results quality safely.

Reality: Higher thresholds (e.g., 0.75) reduce recall drastically, filtering out relevant but non-identical records.

This leads to fewer results and forces deeper search, increasing timeout risk.

Misconception: Indexing only the title is sufficient for good semantic matching.

Reality: Title-only indexing uses short_description only, which is often too shallow.

Rich fields (description, notes, troubleshooting) significantly improve relevance but increase cost.

# Detailed Explanation of Key Concepts

Semantic Search Behavior:

AIS uses embeddings and approximate nearest neighbor (ANN) search to find similar records.

It searches for vectors that are semantically close in a high-dimensional space.

Filters are applied after similarity, not before.

Impact of Restrictive Filters:

A query like 'find similar records WHERE state=closed' forces AIS to:

1. Search broadly for similar vectors
2. Discard those not matching filters
3. Continue searching until enough valid results are found

This increases traversal depth and execution time.

documentMatchThreshold Trade-off:

Lower threshold (~0.5): more recall, faster results

Higher threshold (~0.75): higher precision but fewer matches, slower execution

Index Strategy Trade-off:

Title index: fast but shallow

Text index: rich but expensive

Best outcome requires balancing indexing richness and performance

# Fix Implemented

The following changes were applied to stabilize the feature:

- semanticIndex changed from ['title','text'] to ['title']
- documentMatchThreshold reduced from 0.75 to 0.50
- glide.ais.query.timeout increased from 10 to 20 seconds

# Results

After applying the fixes:

- The feature consistently returns similar records
- Timeout errors are no longer surfaced to users
- Overall stability improved

# Best Practices and Recommendations

1. Keep semantic queries broad: apply strict filters after retrieving results.
2. Use documentMatchThreshold around 0.5 for better recall.
3. Prefer lightweight indexes (title) when performance is critical.
4. Use richer indexes only when necessary and optimize them (chunk size, scoped sources).
5. Always implement fallback logic (e.g., keyword search) to avoid empty responses.
6. Monitor AIS query time and adjust timeout only as a workaround, not a fix.
7. Combine good query design with proper indexing — both are required for optimal results.

## Related

- [[AI Search]]
- [[AI Search – Considerations for Designing, Maintaining, and Sca]]
- [[AI Search Synonyms]]
- [[Now Assist in AI Search]]