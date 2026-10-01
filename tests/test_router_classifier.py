from capt_crewvn.core.providers.scripted import ScriptedProvider
from capt_crewvn.core.router.classifier import llm_route, match_modules, route, rule_route
from capt_crewvn.core.schemas.enums import Department, RouterRole, TaskUrgency


def test_takeover_in_three_languages():
    for text in ("Prepare ship takeover of main engine", "Chuẩn bị nhận tàu", "接船检查"):
        assert "ship-takeover" in match_modules(text), text


def test_department_comes_from_role_profile():
    d = rule_route("main engine defect", RouterRole.SECOND_ENGINEER, vessel_id="V-FICT-1", company_id="C-FICT")
    assert d.department == Department.ENGINE
    assert set(d.modules[:2]) == {"defect-management", "engine-systems"}
    assert d.missing_context == []


def test_danger_routes_to_emergency_first_and_asks_for_vessel():
    d = rule_route("Tàu mắc cạn, cần làm gì ngay", RouterRole.MASTER)
    assert d.urgency == TaskUrgency.IMMEDIATE_DANGER and d.immediate_danger
    assert d.modules[0] == "grounding-emergency"
    assert "vessel" in d.missing_context


def test_no_match_falls_back_to_captain_adviser():
    assert rule_route("hello", RouterRole.MASTER).modules == ["captain-adviser"]


def test_study_question_from_cadet():
    assert rule_route("Giải thích SMCP là gì", RouterRole.CADET).urgency == TaskUrgency.STUDY


def test_word_boundary_for_english():
    assert "fuel-management" not in match_modules("the problem is the robot")


def test_llm_can_add_modules_and_raise_urgency():
    provider = ScriptedProvider(['{"modules": ["bwms", "made-up"], "urgency": "URGENT", "task_type": "troubleshooting"}'])
    d = route("system alarm keeps tripping", RouterRole.CHIEF_ENGINEER, provider=provider)
    assert d.modules[0] == "bwms" and "made-up" not in d.modules
    assert "captain-adviser" not in d.modules
    assert d.urgency == TaskUrgency.URGENT and d.task_type == "troubleshooting"
    assert provider.received[0][0].role == "system"


def test_llm_cannot_lower_detected_danger():
    base = rule_route("fire in engine room", RouterRole.CHIEF_ENGINEER)
    d = llm_route("fire in engine room", base, ScriptedProvider(['{"modules": [], "urgency": "STUDY"}']))
    assert d.urgency == TaskUrgency.IMMEDIATE_DANGER and d.immediate_danger


def test_invalid_llm_output_keeps_rule_decision():
    base = rule_route("Chuẩn bị nhận tàu", RouterRole.MASTER)
    assert llm_route("x", base, ScriptedProvider(["not json"])) == base
    assert llm_route("x", base, ScriptedProvider(['{"urgency": "PANIC"}'])).urgency == base.urgency
