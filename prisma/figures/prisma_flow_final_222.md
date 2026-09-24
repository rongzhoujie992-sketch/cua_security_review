# PRISMA flow - final main CUA corpus

```mermaid
flowchart TD
  A["Captured search occurrences identified<br/>n = 18,371"] --> B["Duplicate occurrences removed<br/>n = 8,281"]
  B --> C["Records after global deduplication<br/>n = 10,090"]
  C --> D["Records screened<br/>n = 10,087"]
  C --> X0["Other pre-screening removals<br/>n = 3"]
  D --> E["Retained report records<br/>n = 466"]
  D --> X1["Screening exclusions<br/>n = 9,621"]
  E --> F["Alternate report versions consolidated<br/>n = 87"]
  F --> G["Reports sought for retrieval<br/>n = 379"]
  G --> H["Reports assessed for eligibility<br/>n = 378"]
  G --> X2["Reports not retrieved<br/>n = 1"]
  H --> I["Studies entering final review<br/>n = 285"]
  H --> X3["Full-text stage removals<br/>n = 93<br/>10 version resolutions + 83 initial exclusions"]
  I --> J["Main CUA corpus<br/>n = 222 studies"]
  I --> X4["Final review exclusions<br/>n = 63"]
```

Detailed exclusion reasons are reported in `reports/fulltext_exclusion_reason_summary_83.csv` and `reports/author_adjudication_exclusion_reason_summary.csv`. Study-level exclusions are listed in the corresponding ledgers.
