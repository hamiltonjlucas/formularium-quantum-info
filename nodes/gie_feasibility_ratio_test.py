# Generated numeric regression tests — the migration-fidelity gate.
# `transcription` pins the node body to the spec expression at generation-time
# reference values; `physics_sanity` (where present) checks the computed value
# against the measured catalog constant (loose: loop corrections are real).
from gen.messages_pb2 import GieFeasibilityRatioInput
from nodes.gie_feasibility_ratio import gie_feasibility_ratio


def test_gie_feasibility_ratio_transcription():
    result = gie_feasibility_ratio(None, GieFeasibilityRatioInput(G_N=6.70883074614254e-39, M_src=0.6550856815791929, W_pkt=0.9417041752677979, g_wva=1.2239759807302737, hbar=1.000000000016944, m_probe=1.001619208090617, t_int=0.9470931422019505, x_sep=1.5360579120908329))
    assert result.formula_id == 'gie_feasibility_ratio'
    assert result.computes == 'r_kick'
    assert result.tier == 'established'
    expected = -2.0366316600954175e-39
    assert abs(result.value / expected - 1.0) < 1e-9
