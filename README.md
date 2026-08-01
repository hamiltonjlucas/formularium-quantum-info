# formularium-quantum-info

**Formularium** quantum-info formulas as [Axiom](https://dev.axiomide.com) compute nodes —
part of an axiom-native physics catalog where the packages themselves are the source
of truth (6 formulas in this domain).

Each node takes the formula's right-hand-side symbols as `double` inputs in **natural
units** (ħ = c = 1, GeV powers) and returns the shared
`formularium-types.FormulaResult {value, formula_id, computes, tier}`. The `GetCatalog`
node returns this package's full `DomainCatalog` (formula specs + referenced quantities)
for catalog assembly.

| Node | Formula | Tier | Computes |
|---|---|---|---|
| `BrassardThreshold` | Brassard trivialization threshold | established | `S_IC_triv = 4*sqrt(6)/3` |
| `GieFeasibilityRatio` | GIE repulsion feasibility ratio | established | `r_kick = -G_N*M_src*W_pkt*g_wva*m_probe*t_int/(hbar*x_sep**2)` |
| `PostselectedKick` | Effective momentum transfer after postselection (repulsive gravity witness) | established | `delta_p_eff = -Pi_A_wv*(delta_p_A - delta_p_B) + delta_p_B` |
| `TsirelsonBound` | Tsirelson bound from information causality | established | `S_Tsirelson = 2*sqrt(2)` |
| `TsirelsonFromChsh` | Tsirelson bound from the operator norm | established | `S_Tsirelson = sqrt(2)*S_CHSH_cl` |
| `WeakValueProjector` | Weak value of the branch projector (GIE postselection) | established | `Pi_A_wv = -alpha_sup/(-alpha_sup + beta_sup)` |

Input field names preserve catalog symbol spelling (`M_W`, not `m_w`) — fidelity over
proto naming convention, by design.

The machine-readable source of truth is [`nodes/specs.py`](nodes/specs.py); node
arithmetic is generated from it and kept consistent by `formularium check-specs`.
Part of the [Formularium](https://github.com/hamiltonjlucas/formularium) project,
migrated from the file-based *unified-theory* catalog.

License: Apache-2.0.
