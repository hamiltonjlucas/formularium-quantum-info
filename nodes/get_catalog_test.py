from gen.hamiltonjlucas_formularium_types_messages_pb2 import Empty
from nodes.get_catalog import get_catalog


def test_get_catalog():
    m = get_catalog(None, Empty())
    assert m.domain == 'quantum-info'
    assert len(m.formulas) == 6
    assert len(m.quantities) == 13
    ids = {f.id for f in m.formulas}
    assert len(ids) == 6
    assert all(f.expression.startswith('Eq(') for f in m.formulas)
