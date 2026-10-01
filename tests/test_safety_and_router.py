from capt_crewvn.core.router.triage import baseline_triage
from capt_crewvn.core.safety.rules import find_citations, post_check, prohibited_items
from capt_crewvn.core.schemas.enums import TaskUrgency


def test_prohibited_list_covers_claude_md_section_11():
    ids = {item["id"] for item in prohibited_items()}
    for required in [
        "BYPASS_SAFETY_PROTECTION", "DISABLE_ALARM_INTERLOCK", "FALSIFY_LOGS", "BACKDATE_RECORDS",
        "CONCEAL_DEFICIENCIES", "MANIPULATE_BUNKER_FIGURES", "HIDE_POLLUTION", "ILLEGAL_DISCHARGE",
        "UNSAFE_ENCLOSED_SPACE_ENTRY", "UNSAFE_MACHINERY_TEST", "IMPERSONATE_AUTHORITY",
        "FALSIFY_SIGNATURES", "FABRICATE_EVIDENCE",
    ]:
        assert required in ids


def test_triage_flags_danger_in_three_languages():
    assert baseline_triage("Smoke from the engine room skylight") == TaskUrgency.IMMEDIATE_DANGER
    assert baseline_triage("Tàu bị mắc cạn lúc 0300") == TaskUrgency.IMMEDIATE_DANGER
    assert baseline_triage("机舱进水") == TaskUrgency.IMMEDIATE_DANGER
    assert baseline_triage("How do I write a noon report?") is None


def test_post_check_flags_unsourced_citation():
    text = "This is required by MSC.123(45) and SOLAS regulation II-2."
    assert find_citations(text)
    assert not post_check(text).passed
    assert post_check(text, retrieved_source_text="... MSC.123(45) ... SOLAS regulation II-2 ...").passed


def test_post_check_allows_framework_names_without_numbers():
    assert post_check("Verify against the applicable SOLAS and MARPOL requirements.").passed
