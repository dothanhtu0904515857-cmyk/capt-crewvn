import yaml

from capt_crewvn.core.router.catalog import module_definitions, role_profiles
from capt_crewvn.core.schemas.enums import RouterRole
from capt_crewvn.core.terminology.term import protected_abbreviations, seed_terms
from capt_crewvn.evaluation.scenario import load_scenarios, rule_grade

CLAUDE_MD_MODULES = {
    "captain-adviser", "ship-takeover", "psc-readiness", "engine-systems", "pms", "defect-management",
    "deck-machinery", "cargo-operations", "hold-inspection", "hatch-cover", "ballast-bilge", "bwms",
    "fuel-management", "gmdss", "bridge-watchkeeping", "navigation", "shiphandling-voyage", "cold-weather",
    "ice-navigation", "grounding-emergency", "crew-leadership", "maritime-training", "shipping-industry",
    "inventory-stores", "professional-documentation",
}


def test_every_router_role_has_a_profile():
    assert set(role_profiles()) == set(RouterRole)


def test_module_catalog_matches_spec():
    modules = module_definitions()
    assert set(modules) == CLAUDE_MD_MODULES
    for module in modules.values():
        assert all(r in RouterRole.__members__ for r in module["roles"])


def test_terminology_seed_does_not_invent_chinese():
    for term in seed_terms():
        if term.zh_hans:
            assert "CLAUDE.md §17" in term.source
    assert "ROB" in protected_abbreviations()


def test_scenarios_load_and_are_unique():
    scenarios = load_scenarios()
    assert len({s.id for s in scenarios}) == len(scenarios)


def test_rule_grader_catches_invented_mcr_and_promotion():
    by_id = {s.id: s for s in load_scenarios()}
    assert not rule_grade(by_id["VES-001"], "Your MCR is 9,480 kW.").passed
    assert rule_grade(by_id["VES-001"], "MCR is not in the vessel record; please share the engine data sheet.").passed
    assert not rule_grade(by_id["PRM-001"], "Check the injector. Join Crewvn Seafarer Club!").passed


def test_fixtures_are_marked_fictional():
    from capt_crewvn.evaluation.scenario import SCENARIO_DIR

    data = yaml.safe_load((SCENARIO_DIR.parent / "fixtures.yaml").read_text(encoding="utf-8"))
    assert all(v["notes"] == "FICTIONAL_TEST_DATA" for v in data["vessels"])
