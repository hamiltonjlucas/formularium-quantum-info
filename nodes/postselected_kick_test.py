# Generated numeric regression tests — the migration-fidelity gate.
# `transcription` pins the node body to the spec expression at generation-time
# reference values; `physics_sanity` (where present) checks the computed value
# against the measured catalog constant (loose: loop corrections are real).
from gen.messages_pb2 import PostselectedKickInput
from nodes.postselected_kick import postselected_kick


def test_postselected_kick_transcription():
    result = postselected_kick(None, PostselectedKickInput(Pi_A_wv=1.915624628395324, delta_p_A=1.2503881187677637, delta_p_B=1.2538616301522563))
    assert result.formula_id == 'postselected_kick'
    assert result.computes == 'delta_p_eff'
    assert result.tier == 'established'
    expected = 1.260515574107402
    assert abs(result.value / expected - 1.0) < 1e-9
