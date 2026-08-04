import math

from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_types_messages_pb2 import FormulaResult
from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.specs import FORMULAS

SPEC = FORMULAS['tsirelson_bound']


def tsirelson_bound(ax: AxiomContext, input: Empty) -> FormulaResult:
    """Tsirelson bound from information causality — established. Computes S_Tsirelson = 2*sqrt(2) in natural units (GeV powers)."""
    # BEGIN GENERATED — do not hand-edit; run `formularium regen-node` after changing specs.py
    value = 2*math.sqrt(2)
    # END GENERATED
    return FormulaResult(value=value, formula_id=SPEC.id,
                         computes=SPEC.computes, tier=SPEC.tier)
