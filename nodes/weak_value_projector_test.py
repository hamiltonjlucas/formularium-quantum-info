# Generated numeric regression tests — the migration-fidelity gate.
# `transcription` pins the node body to the spec expression at generation-time
# reference values; `physics_sanity` (where present) checks the computed value
# against the measured catalog constant (loose: loop corrections are real).
from gen.messages_pb2 import WeakValueProjectorInput
from nodes.weak_value_projector import weak_value_projector


def test_weak_value_projector_transcription():
    result = weak_value_projector(None, WeakValueProjectorInput(alpha_sup=0.8880872161663722, beta_sup=0.6500315644267479))
    assert result.formula_id == 'weak_value_projector'
    assert result.computes == 'Pi_A_wv'
    assert result.tier == 'established'
    expected = 3.7305865652697308
    assert abs(result.value / expected - 1.0) < 1e-9
