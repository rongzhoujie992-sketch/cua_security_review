# Contribution-Role Annotation

This layer classifies each HPAT-positive study's non-exclusive contribution to threat, evaluation, and safeguard research. Only `central` labels support role-comparative summaries. A study can be central to more than one role; the three role counts are not a partition of the corpus. `other` is derived only when no role is central.

The layer covers 91 HPAT-positive studies (273 study-by-role records). Independent role annotations were compared and adjudicated under the frozen role definitions; the independent labels and agreement calculations are retained in `reliability/`.

The role labels apply at the study level. They are linked to HPAT records by `study_id` and are deliberately not duplicated into individual transitions.
