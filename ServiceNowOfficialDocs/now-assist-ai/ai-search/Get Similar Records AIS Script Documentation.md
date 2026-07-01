# Get Similar Records AIS Documentation

## Case Information

- **Case ID:** CS9293768
- **Title:** The AI search, such as `getSimilarRecordsForCase`, is not working properly

## Overview

The issue is related to failures and timeouts in the custom script `U4getSimilarRecordsForCase`, which performs semantic (vector) search using AIS.

The search runs over a very large dataset (~5.3M cases and ~9.8M embeddings), making performance highly sensitive to query configuration.

## Root Cause Analysis

The main issue was not a broken script, but how semantic search behaves under certain conditions.

The custom script combined semantic search with restrictive filters (e.g., `resolution_code`, `state`, `product`). Instead of reducing the dataset, these filters made the search heavier, forcing AIS to scan more of the vector index.

This caused queries to exceed the default ~10-second timeout, resulting in `SocketTimeoutException` errors.

## Misconceptions

### Misconception 1
**Adding restrictive filters improves performance because it reduces the dataset.**

**Reality:**
Filters do not shrink the search space; they add constraints after similarity evaluation.

Result:
- More traversal
- Deeper scans
- Higher latency

### Misconception 2
**Increasing `documentMatchThreshold` improves result quality safely.**

**Reality:**
Higher thresholds (for example 0.75) reduce recall drastically and can increase timeout risk.

### Misconception 3
**Indexing only the title is sufficient for semantic matching.**

**Reality:**
Title-only indexing is fast but shallow. Rich fields such as descriptions, notes and troubleshooting content improve relevance but increase cost.

## Detailed Explanation of Key Concepts

### Semantic Search Behavior

AIS uses embeddings and Approximate Nearest Neighbor (ANN) search to find semantically similar records.

Search process:
1. Search broadly for similar vectors.
2. Apply filters after similarity evaluation.
3. Continue searching until enough valid records are found.

### Restrictive Filter Impact

Filters are evaluated after similarity matching and can increase traversal depth and execution time.

### documentMatchThreshold Trade-off

| Threshold | Effect |
|------------|---------|
| ~0.50 | Better recall, faster results |
| ~0.75 | Higher precision, fewer matches, slower execution |

### Index Strategy Trade-off

| Index Type | Characteristics |
|------------|----------------|
| Title | Fast but shallow |
| Text | Rich but expensive |

Best results require balancing performance and relevance.

## Fix Implemented

The following changes were applied:

```text
semanticIndex: ['title','text'] -> ['title']
documentMatchThreshold: 0.75 -> 0.50
glide.ais.query.timeout: 10s -> 20s
```

## Results

After applying the fixes:

- Similar records are consistently returned.
- Timeout errors are no longer surfaced to users.
- Overall stability improved.

## Best Practices and Recommendations

1. Keep semantic queries broad.
2. Apply strict filtering after retrieval.
3. Use `documentMatchThreshold` around 0.5 for better recall.
4. Prefer lightweight indexes when performance is critical.
5. Use richer indexes only when necessary.
6. Implement fallback logic such as keyword search.
7. Monitor AIS query execution times.
8. Treat timeout increases as a workaround rather than a root-cause fix.
9. Balance query design and indexing strategy.

---

**Source:** Get Similar Records AIS Script Documentation

Reference: turn2search3
