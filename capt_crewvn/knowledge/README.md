# knowledge

Retrieval code only. Source documents live in object storage under the partition layout of Spec Part G.6,
never in git. `scope.py` enforces tenant and vessel filtering; retrieval must not run without a `RequestScope`.
