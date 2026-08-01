# Generated numeric regression tests — the migration-fidelity gate.
# `transcription` pins the node body to the spec expression at generation-time
# reference values; `physics_sanity` (where present) checks the computed value
# against the measured catalog constant (loose: loop corrections are real).
from gen.hamiltonjlucas_formularium_constants_messages_pb2 import Empty
from nodes.brassard_threshold import brassard_threshold


def test_brassard_threshold_transcription():
    result = brassard_threshold(None, Empty())
    assert result.formula_id == 'brassard_threshold'
    assert result.computes == 'S_IC_triv'
    assert result.tier == 'established'
    expected = 3.265986323710904
    assert abs(result.value / expected - 1.0) < 1e-9


def test_brassard_threshold_physics_sanity():
    result = brassard_threshold(None, Empty())
    catalog_value = 3.265986323710904  # measured, natural units
    assert abs(result.value / catalog_value - 1.0) < 0.25
