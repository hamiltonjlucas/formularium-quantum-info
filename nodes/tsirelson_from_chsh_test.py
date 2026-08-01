# Generated numeric regression tests — the migration-fidelity gate.
# `transcription` pins the node body to the spec expression at generation-time
# reference values; `physics_sanity` (where present) checks the computed value
# against the measured catalog constant (loose: loop corrections are real).
from gen.messages_pb2 import TsirelsonFromChshInput
from nodes.tsirelson_from_chsh import tsirelson_from_chsh


def test_tsirelson_from_chsh_transcription():
    result = tsirelson_from_chsh(None, TsirelsonFromChshInput(S_CHSH_cl=2.0))
    assert result.formula_id == 'tsirelson_from_chsh'
    assert result.computes == 'S_Tsirelson'
    assert result.tier == 'established'
    expected = 2.8284271247461903
    assert abs(result.value / expected - 1.0) < 1e-9


def test_tsirelson_from_chsh_physics_sanity():
    result = tsirelson_from_chsh(None, TsirelsonFromChshInput(S_CHSH_cl=2.0))
    catalog_value = 2.8284271247461903  # measured, natural units
    assert abs(result.value / catalog_value - 1.0) < 0.25
