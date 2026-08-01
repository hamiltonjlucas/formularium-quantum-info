"""Formularium quantum-info — the source of truth for this package's formulas.

Edit entries here directly (tier, provenance, notes, or the expression itself).
After changing an `expression`, run `formularium regen-node <pkg-dir> <formula-id>`
to re-derive the node's arithmetic; `formularium check-specs` (pre-commit) verifies
node bodies stay consistent with these specs.
"""

from dataclasses import dataclass

DOMAIN = 'quantum-info'


@dataclass(frozen=True)
class FormulaSpec:
    id: str
    name: str
    expression: str          # sympy-parseable "Eq(lhs, rhs)" — THE formula
    symbols: list[str]       # every catalog symbol the expression touches
    input_symbols: list[str] # RHS free symbols, sorted — the node's input fields
    computes: str            # str(lhs): what the node's FormulaResult.value is
    tier: str                # established | derived | conjecture
    provenance: str
    refs: list[str]
    notes: str
    dimensional_check: str
    domain: str = DOMAIN


@dataclass(frozen=True)
class QuantitySpec:
    symbol: str
    name: str
    mass_dim: float
    kind: str                # parameter | coupling | observable | derived
    notes: str


FORMULAS: dict[str, FormulaSpec] = {
    'brassard_threshold': FormulaSpec(
        id='brassard_threshold',
        name='Brassard trivialization threshold',
        expression='Eq(S_IC_triv, 4*sqrt(6)/3)',
        symbols=['S_IC_triv'],
        input_symbols=[],
        computes='S_IC_triv',
        tier='established',
        provenance="Brassard et al., PRL 96, 250401 (2006): noisy super-quantum boxes above 4 sqrt(2/3) are distillable by majority-vote repetition (a concatenated-code argument) until communication complexity collapses, via van Dam's trick -- any distributed Boolean function as a GF(2) inner product, evaluated with one transmitted bit at the PR point.",
        refs=['quant-ph/0508042', 'quant-ph/0501159'],
        notes='Above this threshold the ratio of accessible information to transmitted capacity diverges -- correlations counterfeiting bandwidth -- which is the regime where Lemma 0 (the provable fragment of the no-counterfeiting target theorem) is staked. The interval (2 sqrt(2), 4 sqrt(2/3)] remains open, shared with the communication-complexity literature.',
        dimensional_check='consistent (mass_dim 0)',
    ),
    'gie_feasibility_ratio': FormulaSpec(
        id='gie_feasibility_ratio',
        name='GIE repulsion feasibility ratio',
        expression='Eq(r_kick, -g_wva*G_N*M_src*m_probe*W_pkt*t_int/(hbar*x_sep**2))',
        symbols=['G_N', 'M_src', 'W_pkt', 'g_wva', 'hbar', 'm_probe', 'r_kick', 't_int', 'x_sep'],
        input_symbols=['G_N', 'M_src', 'W_pkt', 'g_wva', 'hbar', 'm_probe', 't_int', 'x_sep'],
        computes='r_kick',
        tier='established',
        provenance='Eq. (11) of arXiv:2602.12266, with Delta p = hbar/W_pkt for a Gaussian probe packet and delta_p_eff = -g * delta_p_A.',
        refs=['arXiv:2602.12266'],
        notes="The measurable signal in units of quantum noise. Notable for the catalog's map: G_N and hbar appear TOGETHER with laboratory-scale quantities in one dimensionless observable -- the signature of a genuinely quantum- gravitational (though non-Planckian) experiment. Paper's benchmark sets: {M=2e-8 kg, m=Cs atom, W=10 um, T=0.1 s, x_A=50 um, g=1e3} or {M=1e-14 kg, m=1e-20 kg, W=0.1 um, T=0.5 s, x_A=0.4 um, g=1e2}, both reaching |r_kick| ~ 2e-3. Main confound to exclude: Casimir-Polder.",
        dimensional_check='consistent (mass_dim 0)',
    ),
    'postselected_kick': FormulaSpec(
        id='postselected_kick',
        name='Effective momentum transfer after postselection (repulsive gravity witness)',
        expression='Eq(delta_p_eff, delta_p_B - (delta_p_A - delta_p_B)*Pi_A_wv)',
        symbols=['Pi_A_wv', 'delta_p_A', 'delta_p_B', 'delta_p_eff'],
        input_symbols=['Pi_A_wv', 'delta_p_A', 'delta_p_B'],
        computes='delta_p_eff',
        tier='established',
        provenance='Quantum interference of force (Correa-Cenni-Saldanha 2018, verified with photons 2025) applied to the gravitational two-branch kick; Eqs. (5) and (8) of arXiv:2602.12266. Identical result in Schrodinger (wavepacket interference) and Heisenberg (weak value of Delta p-hat) pictures.',
        refs=['arXiv:2602.12266', 'Quantum 2.112 (Correa et al. 2018)', 'PRA 112.012213 (Militani et al. 2025)', 'PRA 100.022101 (Cenni et al. 2019)'],
        notes="With the negative weak value Pi_A_wv = -alpha/(beta-alpha), this is delta_eff = delta_B - alpha(delta_A - delta_B)/(beta - alpha), which is NEGATIVE (repulsion) when alpha(delta_A - delta_B)/(beta - alpha) > delta_B -- although both branch forces are attractive. A classical (unsuperposed) gravitational field can produce no such sign flip: repulsion requires interference of two distinct states of the field, so observing it witnesses gravity's quantum nature (GIE tier: speculative research). Electrostatic analogue: effective same-sign attraction between electrons (Cenni 2019).",
        dimensional_check='consistent (mass_dim 1)',
    ),
    'tsirelson_bound': FormulaSpec(
        id='tsirelson_bound',
        name='Tsirelson bound from information causality',
        expression='Eq(S_Tsirelson, 2*sqrt(2))',
        symbols=['S_Tsirelson'],
        input_symbols=[],
        computes='S_Tsirelson',
        tier='established',
        provenance='Tsirelson 1980; information causality implies the bound exactly (Pawlowski et al., Nature 461, 1101 (2009))',
        refs=['Nature 461, 1101 (2009)'],
        notes='Also recovered by macroscopic locality and local orthogonality, so the capacity reading is not privileged by the bound alone. Geometry-as-bandwidth clause (iv) CONJECTURES the identity of information causality with the covariant entropy bound (correlations cannot counterfeit bandwidth); the target theorem - no consistent subadditive region-capacity function in any IC-violating GPT - is Debt 2, with frozen-definitions protocol. Provable fragment (Lemma 0) above the Brassard threshold 4 sqrt(2/3) ~ 3.266; the interval (2 sqrt(2), 4 sqrt(2/3)] is open, shared with the field.',
        dimensional_check='consistent (mass_dim 0)',
    ),
    'tsirelson_from_chsh': FormulaSpec(
        id='tsirelson_from_chsh',
        name='Tsirelson bound from the operator norm',
        expression='Eq(S_Tsirelson, sqrt(2)*S_CHSH_cl)',
        symbols=['S_CHSH_cl', 'S_Tsirelson'],
        input_symbols=['S_CHSH_cl'],
        computes='S_Tsirelson',
        tier='established',
        provenance="Tsirelson 1980: for observables with A^2 = B^2 = 1, the CHSH operator satisfies S^2 = 4 - [A,A'][B,B']; each commutator has norm at most 2, so ||S||^2 <= 8 -- the quantum maximum is sqrt(2) times the classical bound, saturated by a singlet with measurement axes 45 degrees apart.",
        refs=[],
        notes="The sqrt(2) enhancement is the entire quantum/classical CHSH gap. Information causality (Pawlowski et al. 2009) derives the same ceiling from Shannon's toolkit (chain rule + data processing for mutual information); geometry-as-bandwidth clause (iv) conjectures that ceiling and the covariant entropy bound are one fact.",
        dimensional_check='consistent (mass_dim 0)',
    ),
    'weak_value_projector': FormulaSpec(
        id='weak_value_projector',
        name='Weak value of the branch projector (GIE postselection)',
        expression='Eq(Pi_A_wv, -alpha_sup/(beta_sup - alpha_sup))',
        symbols=['Pi_A_wv', 'alpha_sup', 'beta_sup'],
        input_symbols=['alpha_sup', 'beta_sup'],
        computes='Pi_A_wv',
        tier='established',
        provenance='Aharonov-Albert-Vaidman weak value <f|Pi_A|i>/<f|i> evaluated for pre-selection alpha|A> + beta|B> and postselection (-|A> + |B>)/sqrt(2); Eq. (6) of arXiv:2602.12266.',
        refs=['arXiv:2602.12266', 'PRL 60.1351 (Aharonov-Albert-Vaidman 1988)', 'RMP 86.307 (Dressel et al. 2014)'],
        notes='For real 0 < alpha < beta the weak value is negative -- outside the [0,1] spectrum of a projector. This anomalous value is what lets an ensemble of postselected probes acquire momentum OPPOSITE to every force present. Diverges as beta - alpha -> 0 (weak-value amplification), while the postselection probability |<f|i>|^2 = (beta-alpha)^2/2 -> 0.',
        dimensional_check='consistent (mass_dim 0)',
    ),
}


QUANTITIES: dict[str, QuantitySpec] = {
    'M_src': QuantitySpec(
        symbol='M_src',
        name='GIE source mass',
        mass_dim=1,
        kind='parameter',
        notes="Mass of the 'source' particle prepared in a spatial superposition alpha|A> + beta|B> in gravitationally-induced-entanglement (GIE) proposals (Marletto-Vedral / Bose et al. 2017; Saldanha-Marletto-Vedral 2026). Nanodiamond-scale in current proposals, ~1e-14 kg.",
    ),
    'Pi_A_wv': QuantitySpec(
        symbol='Pi_A_wv',
        name='weak value of the branch-A projector',
        mass_dim=0,
        kind='derived',
        notes='Aharonov-Albert-Vaidman weak value <Pi_A>_W = <f|Pi_A|i>/<f|i> of the projector |A><A| between the pre-selected source state alpha|A> + beta|B> and the postselected (-|A> + |B>)/sqrt(2). Lies OUTSIDE [0,1] (it is negative here) -- the anomalous-weak-value regime that makes effective repulsion possible.',
    ),
    'W_pkt': QuantitySpec(
        symbol='W_pkt',
        name='probe wavepacket width',
        mass_dim=-1,
        kind='parameter',
        notes='Position-space Gaussian width of the probe, phi(x) ~ exp(-x^2/W^2); the initial momentum uncertainty is Delta p = hbar / W. The weak-value formalism requires the branch kicks to be much smaller than this uncertainty.',
    ),
    'alpha_sup': QuantitySpec(
        symbol='alpha_sup',
        name='source superposition amplitude (branch A)',
        mass_dim=0,
        kind='parameter',
        notes='Amplitude of branch |A> in the source preparation alpha|A> + beta|B> (taken real, alpha^2 + beta^2 = 1). Repulsion needs beta > alpha with the (-|A> + |B>)/sqrt(2) postselection.',
    ),
    'beta_sup': QuantitySpec(
        symbol='beta_sup',
        name='source superposition amplitude (branch B)',
        mass_dim=0,
        kind='parameter',
        notes='Amplitude of branch |B> in the source preparation alpha|A> + beta|B>. Tuning beta - alpha -> 0+ makes pre- and post-selected states nearly orthogonal, driving the weak value (and the anomalous kick) arbitrarily large at the price of postselection probability |<f|i>|^2 -> 0.',
    ),
    'delta_p_A': QuantitySpec(
        symbol='delta_p_A',
        name='branch-A momentum kick',
        mass_dim=1,
        kind='derived',
        notes='The gravitational momentum kick delta_p_grav evaluated for the source in branch |A> (separation x_A). The nearer branch in the Saldanha-Marletto-Vedral scheme, so delta_p_A > delta_p_B.',
    ),
    'delta_p_B': QuantitySpec(
        symbol='delta_p_B',
        name='branch-B momentum kick',
        mass_dim=1,
        kind='derived',
        notes='The gravitational momentum kick delta_p_grav evaluated for the source in branch |B> (separation x_B > x_A), the weaker of the two superposed attractions.',
    ),
    'delta_p_eff': QuantitySpec(
        symbol='delta_p_eff',
        name='postselected effective momentum transfer',
        mass_dim=1,
        kind='derived',
        notes='The momentum shift of the probe wavepacket conditioned on a successful postselection of the source. Can be NEGATIVE (effective gravitational repulsion) although both branch kicks are attractive -- destructive interference of the two shifted wavepackets. A classical gravitational field can never produce this sign; that is the witness.',
    ),
    'g_wva': QuantitySpec(
        symbol='g_wva',
        name='weak-value amplification factor',
        mass_dim=0,
        kind='parameter',
        notes="Amplification factor g in delta_p_eff = -g * delta_p_A: how many times the anomalous (repulsive) kick exceeds the bare branch kick, set by the near- orthogonality of pre- and post-selection. g ~ 1e2-1e3 in the paper's feasibility estimates, paid for by postselection probability ~ 1e-3.",
    ),
    'm_probe': QuantitySpec(
        symbol='m_probe',
        name='GIE probe mass',
        mass_dim=1,
        kind='parameter',
        notes="Mass of the 'probe' wavepacket that registers the gravitational kick from the superposed source. In the Saldanha-Marletto-Vedral single-superposition scheme the probe needs NO spatial superposition of its own -- only a large momentum uncertainty (atom or BEC, ~1e-25 to 1e-20 kg).",
    ),
    'r_kick': QuantitySpec(
        symbol='r_kick',
        name='kick-to-uncertainty ratio',
        mass_dim=0,
        kind='observable',
        notes="The experimental figure of merit delta_p_eff / Delta p: the anomalous momentum shift in units of the probe's initial momentum uncertainty (Delta p = hbar/W_pkt for a Gaussian packet). Measurable when |r_kick| is greater than or of order 1e-3. The genuine dimensionless knob of the tabletop quantum-gravity witness -- and it contains G_N and hbar together.",
    ),
    't_int': QuantitySpec(
        symbol='t_int',
        name='gravitational interaction time',
        mass_dim=-1,
        kind='parameter',
        notes='Duration T over which the superposed source and the probe interact gravitationally before the source is interfered and postselected. Bounded above by the probe wavepacket spread time tau = m W^2 / (2 hbar).',
    ),
    'x_sep': QuantitySpec(
        symbol='x_sep',
        name='source-probe separation',
        mass_dim=-1,
        kind='parameter',
        notes='Distance between the probe (at x = 0) and a branch location of the superposed source (x_A or x_B). Assumed much larger than the position wavefunction widths of both particles.',
    ),
}
