from capt_crewvn.core.terminology.importers.crewvn_trilingual import consolidate, parse

SAMPLE = (
    "Trang PDF Mục STT   Việt   English   中文（简体）   Pinyin\n"
    "7          1.1.1 1     Bánh lái                    Rudder              舵         Duò\n"
    "7          1.1.4 4     Vây giảm lắc                Bilge keel          舭龙骨       Bǐ lóng gǔ\n"
    "\f"
    "1. Rudder → Bánh lái → 舵 → Duò\n"
    "4. Bilge keel → Vây giảm lắc → 减摇鳍 → Jiǎnyáo qí\n"
    "\f"
    "6. Bilge keel – Vây giảm lắc – 舭龙骨 – Bǐ lóng gǔ\n"
)


def test_parses_tables_and_both_entry_orders():
    records, unparsed = parse(SAMPLE)
    assert not unparsed
    assert {(r["en"], r["vi"], r["zh"]) for r in records} >= {
        ("Rudder", "Bánh lái", "舵"),
        ("Bilge keel", "Vây giảm lắc", "减摇鳍"),
    }
    assert {r["page"] for r in records} == {1, 2, 3}


def test_conflicting_renderings_are_kept_not_resolved():
    terms = {t["canonical_en"]: t for t in consolidate(parse(SAMPLE)[0])}
    keel = terms["Bilge keel"]
    assert keel["zh_hans"] == "舭龙骨"  # most frequent in the source, not chosen by the importer's own knowledge
    assert keel["status"] == "NEEDS_REVIEW"
    assert [v["value"] for v in keel["source_variants"]["zh_hans"]] == ["舭龙骨", "减摇鳍"]
    assert terms["Rudder"]["status"] == "IMPORTED"
