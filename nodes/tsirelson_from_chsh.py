import math

from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_types_messages_pb2 import FormulaResult
from gen.messages_pb2 import TsirelsonFromChshInput
from nodes.specs import FORMULAS

SPEC = FORMULAS['tsirelson_from_chsh']


def tsirelson_from_chsh(ax: AxiomContext, input: TsirelsonFromChshInput) -> FormulaResult:
    """Tsirelson bound from the operator norm — established. Computes S_Tsirelson = sqrt(2)*S_CHSH_cl in natural units (GeV powers)."""
    # BEGIN GENERATED — do not hand-edit; run `formularium regen-node` after changing specs.py
    value = math.sqrt(2)*input.S_CHSH_cl
    # END GENERATED
    return FormulaResult(value=value, formula_id=SPEC.id,
                         computes=SPEC.computes, tier=SPEC.tier)
