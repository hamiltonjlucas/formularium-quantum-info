from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_constants_messages_pb2 import FormulaResult
from gen.messages_pb2 import WeakValueProjectorInput
from nodes.specs import FORMULAS

SPEC = FORMULAS['weak_value_projector']


def weak_value_projector(ax: AxiomContext, input: WeakValueProjectorInput) -> FormulaResult:
    """Weak value of the branch projector (GIE postselection) — established. Computes Pi_A_wv = -alpha_sup/(-alpha_sup + beta_sup) in natural units (GeV powers)."""
    # BEGIN GENERATED — do not hand-edit; run `formularium regen-node` after changing specs.py
    value = -input.alpha_sup/(-input.alpha_sup + input.beta_sup)
    # END GENERATED
    return FormulaResult(value=value, formula_id=SPEC.id,
                         computes=SPEC.computes, tier=SPEC.tier)
