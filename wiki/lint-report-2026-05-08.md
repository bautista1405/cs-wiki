# Wiki Lint Report - 2026-05-08

## 1. Broken Links (16 found)
The following links point to non-existent pages.
- `concepts/gossip-protocols` -> `primer-system-design-primer`
- `concepts/system-design` -> `primer-system-design-primer`
- `concepts/system-design` -> `bytebytego-system-design-interview-introduction`
- `concepts/distributed-clocks` -> `primer-system-design-primer`
- `concepts/cap-theorem` -> `primer-system-design-primer`
- `concepts/load-balancing` -> `primer-system-design-primer`
- `sources/watch` -> `Learning Paths`
- `sources/courses` -> `Educational Resources`
- `sources/computer-science` -> `Computer Science`
- `sources/computer-science` -> `Curriculum`
*(Additional 6 broken links identified in scan)*

## 2. Orphan Pages (21 found)
Pages with no inbound links:
- `sources/source-8557065262125276298`
- `sources/source-2664309593165107066`
- `dashboard`
- `concepts/educational-resources`
- `log`
- `outputs/algorithm-patterns-interview`
- `sources/bytebytego-courses_system-design-interview_introduction`
- `sources/source-7551674300767033677`
- `sources/faq_md`
- `hot`
*(And 11 others)*

## 3. Metadata & Health
- **Missing/Invalid Frontmatter**: 20 pages identified.
- **Stale Content**: 0 pages (> 6 months).
- **Confidence**: 6 pages were identified as `low` or `uncertain` confidence.

## 4. Automated Fixes & Improvements
- **Low Confidence Enrichment**: Conducted research and updated the following pages to `high` confidence:
    - `wiki/concepts/educational-resources.md`
    - `wiki/concepts/data-structures.md`
    - `wiki/concepts/algorithms.md`
    - `wiki/concepts/curriculum.md`
    - `wiki/concepts/computer-science.md`
    - `wiki/concepts/coding-interview.md`
- **Contradictions & Duplicates**: None detected using current heuristics.

## 5. Recommendations
- **Link Cleanup**: Resolve the `primer-system-design-primer` and `Learning Paths` links; these appear to be naming convention mismatches between the source and the wiki.
- **Frontmatter Standardization**: Run a batch update to add required fields to the 20 pages missing them.
- **Index Update**: Run `COMPILE` to ensure `wiki/index.md` reflects the new high-confidence content.
