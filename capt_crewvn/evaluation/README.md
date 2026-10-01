# Maritime safety evaluation

- `scenarios/*.yaml`: scenario sets (Spec Part K). `blocking: true` scenarios must pass before any release
  or provider switch.
- `fixtures.yaml`: synthetic vessels, marked FICTIONAL_TEST_DATA.
- `scenario.py`: loader and rule grader. Rubric and human review are added in Phase 6.

Scenarios are reviewed by the owner (owner decision N.1-9).
