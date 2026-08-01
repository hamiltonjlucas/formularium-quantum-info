# Generated numeric regression tests — the migration-fidelity gate.
# `transcription` pins the node body to the spec expression at generation-time
# reference values; `physics_sanity` (where present) checks the computed value
# against the measured catalog constant (loose: loop corrections are real).
from gen.messages_pb2 import Empty
from nodes.tsirelson_bound import tsirelson_bound


def test_tsirelson_bound_transcription():
    result = tsirelson_bound(None, Empty())
    assert result.formula_id == 'tsirelson_bound'
    assert result.computes == 'S_Tsirelson'
    assert result.tier == 'established'
    expected = 2.8284271247461903
    assert abs(result.value / expected - 1.0) < 1e-9


def test_tsirelson_bound_physics_sanity():
    result = tsirelson_bound(None, Empty())
    catalog_value = 2.8284271247461903  # measured, natural units
    assert abs(result.value / catalog_value - 1.0) < 0.25
