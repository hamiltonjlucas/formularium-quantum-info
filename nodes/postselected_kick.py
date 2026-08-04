from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_types_messages_pb2 import FormulaResult
from gen.messages_pb2 import PostselectedKickInput
from nodes.specs import FORMULAS

SPEC = FORMULAS['postselected_kick']


def postselected_kick(ax: AxiomContext, input: PostselectedKickInput) -> FormulaResult:
    """Effective momentum transfer after postselection (repulsive gravity witness) — established. Computes delta_p_eff = -Pi_A_wv*(delta_p_A - delta_p_B) + delta_p_B in natural units (GeV powers)."""
    # BEGIN GENERATED — do not hand-edit; run `formularium regen-node` after changing specs.py
    value = -input.Pi_A_wv*(input.delta_p_A - input.delta_p_B) + input.delta_p_B
    # END GENERATED
    return FormulaResult(value=value, formula_id=SPEC.id,
                         computes=SPEC.computes, tier=SPEC.tier)
