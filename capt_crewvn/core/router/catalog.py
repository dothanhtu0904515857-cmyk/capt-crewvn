"""Loads role profiles and module definitions from YAML (no role logic is hard-coded in branches)."""

from functools import cache
from pathlib import Path

import yaml

from capt_crewvn.core.schemas.enums import RouterRole

PACKAGE_ROOT = Path(__file__).resolve().parents[2]
ROLES_DIR = PACKAGE_ROOT / "roles"
SKILLS_DIR = PACKAGE_ROOT / "skills"


@cache
def role_profiles() -> dict[RouterRole, dict]:
    profiles: dict[RouterRole, dict] = {}
    for path in sorted(ROLES_DIR.glob("*/*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        profiles[RouterRole(data["router_role"])] = data
    return profiles


@cache
def module_definitions() -> dict[str, dict]:
    modules: dict[str, dict] = {}
    for path in sorted(SKILLS_DIR.glob("*/*.module.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        modules[data["id"]] = data
    return modules
