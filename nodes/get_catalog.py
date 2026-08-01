from gen.axiom_context import AxiomContext
from gen.hamiltonjlucas_formularium_constants_messages_pb2 import DomainCatalog, Empty
from nodes.specs import DOMAIN, FORMULAS, QUANTITIES


def get_catalog(ax: AxiomContext, input: Empty) -> DomainCatalog:
    """The Formularium quantum-info domain catalog: every formula spec and the quantities they reference."""
    m = DomainCatalog(domain=DOMAIN)
    for f in FORMULAS.values():
        m.formulas.add(
            id=f.id, name=f.name, expression=f.expression, symbols=f.symbols,
            input_symbols=f.input_symbols, computes=f.computes, tier=f.tier,
            provenance=f.provenance, refs=f.refs, notes=f.notes,
            dimensional_check=f.dimensional_check, domain=f.domain,
        )
    for q in QUANTITIES.values():
        m.quantities.add(symbol=q.symbol, name=q.name, mass_dim=q.mass_dim,
                         kind=q.kind, notes=q.notes)
    return m
