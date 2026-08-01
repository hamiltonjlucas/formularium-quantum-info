from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_constants_messages_pb2 import FormulaResult
from gen.messages_pb2 import GieFeasibilityRatioInput
from nodes.specs import FORMULAS

SPEC = FORMULAS['gie_feasibility_ratio']


def gie_feasibility_ratio(ax: AxiomContext, input: GieFeasibilityRatioInput) -> FormulaResult:
    """GIE repulsion feasibility ratio — established. Computes r_kick = -G_N*M_src*W_pkt*g_wva*m_probe*t_int/(hbar*x_sep**2) in natural units (GeV powers)."""
    # BEGIN GENERATED — do not hand-edit; run `formularium regen-node` after changing specs.py
    value = -input.G_N*input.M_src*input.W_pkt*input.g_wva*input.m_probe*input.t_int/(input.hbar*input.x_sep**2)
    # END GENERATED
    return FormulaResult(value=value, formula_id=SPEC.id,
                         computes=SPEC.computes, tier=SPEC.tier)
