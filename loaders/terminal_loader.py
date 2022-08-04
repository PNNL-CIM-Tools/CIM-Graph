from __future__ import annotations

from typing import List

from gridappsd_cim import Terminal, ConductingEquipment


def load_terminals_by_conducting_equipment(conducting: str | ConductingEquipment) -> List[Terminal]:
    return [Terminal(mRID="foo")]
