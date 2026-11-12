# docs/_generated - generated facts

Machine-produced documents. **Never hand-edit**: each file names the command that
writes it, and a check fails when the content and the producer disagree.

| File | Producer | Contract |
| --- | --- | --- |
| [`gate-timings.md`](gate-timings.md) | `./run.sh bench` | Wall time per gate arm, before/after, with the arm commands and the setup costs that are not arms. |
| [`gate-baseline.json`](../../docs/_generated/gate-baseline.json) | recorded once by hand at the pre-change commit | The "before" receipt `gate-timings.md` renders. Never re-measured, never rewritten by the bench arm. |

Timings are host-specific: they are evidence for "this arm costs seconds, that one
costs minutes", not a service-level target. The `docs` arm only checks that the
timings table covers exactly the arms `./run.sh` exposes.
