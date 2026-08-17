# Integrated evidence-route map

```mermaid
flowchart TB
  subgraph MAIN["Main systematic CUA search"]
    M0["Records identified<br/>n = 18,371"] --> M1["Duplicate occurrences removed<br/>n = 8,281"]
    M1 --> M2["Records after global deduplication<br/>n = 10,090"]
    M2 --> M3["Records screened<br/>n = 10,087"]
    M2 --> X0["Other pre-screening removals<br/>n = 3"]
    M3 --> M4["Retained report records<br/>n = 466"]
    M3 --> X1["Screening exclusions<br/>n = 9,621"]
    M4 --> M5["Alternate report versions consolidated<br/>n = 87"]
    M5 --> M6["Reports sought for retrieval<br/>n = 379"]
    M6 --> X2["Reports not retrieved<br/>n = 1"]
    M6 --> M7["Reports assessed for eligibility<br/>n = 378"]
    M7 --> X3["Full-text stage removals<br/>n = 93"]
    M7 --> M8["Studies entering final review<br/>n = 285"]
    M8 --> X4["Final review exclusions<br/>n = 63"]
    M8 --> M9["Main CUA corpus<br/>n = 222 studies"]
  end

  F["Foundational route<br/>n = 12 sources"]

  subgraph TDES["TDES deployment-evidence route"]
    T0["TDES supplementary branch<br/>n = 9 sources"]
    TA["Academic sources<br/>n = 4"]
    TO["Official deployment documents<br/>n = 5"]
    T0 --> TA
    T0 --> TO
    TA --> TM((""))
    TO --> TM
  end

  M9 --> Z["Final evidence source base<br/>n = 243 sources<br/>222 + 12 + 4 + 5 = 243"]
  F --> Z
  TM --> Z
```

The TDES academic and official-document subroutes merge into one supplementary branch before entering the final evidence source base. The eight TDES re-extractions are already contained in the 222-study main corpus and do not add to the 243-source total.
