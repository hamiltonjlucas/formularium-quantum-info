import math

from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_constants_messages_pb2 import FormulaResult
from gen.hamiltonjlucas_formularium_constants_messages_pb2 import Empty
from nodes.specs import FORMULAS

SPEC = FORMULAS['brassard_threshold']


def brassard_threshold(ax: AxiomContext, input: Empty) -> FormulaResult:
    """Brassard trivialization threshold — established. Computes S_IC_triv = 4*sqrt(6)/3 in natural units (GeV powers)."""
    # BEGIN GENERATED — do not hand-edit; run `formularium regen-node` after changing specs.py
    value = (4/3)*math.sqrt(6)
    # END GENERATED
    return FormulaResult(value=value, formula_id=SPEC.id,
                         computes=SPEC.computes, tier=SPEC.tier)
