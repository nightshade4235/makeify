# Clean-room and licensing plan

## Why this is required

The official DUSt3R repository states that its code is distributed under **CC BY-NC-SA 4.0** and that pretrained checkpoints also depend on the licenses of their training datasets and base checkpoints. The README lists datasets with non-commercial, research-only, or other specific terms. [1] The Creative Commons legal code grants reproduction and adaptations only for NonCommercial purposes, requires attribution, and applies ShareAlike conditions to shared adaptations. [2]

This creates a practical boundary: a public repository, a competition submission, job consideration, or a future product may not all have the same legal character. The word “non-commercial” is context-dependent. The team should obtain a written determination from the relevant rights holder or counsel before using DUSt3R code/checkpoints in anything intended for commercial advantage, production, paid work, or transfer to an employer.

This document is an engineering control plan, not legal advice.

## Two-track strategy

### Track A — non-commercial research baseline

Use the official DUSt3R code and weights only after recording acceptance of the upstream license and every applicable checkpoint/dataset condition. Keep it in a separate environment and directory. Label outputs as research artifacts. Do not copy upstream source into the clean-room implementation, and do not mix upstream weights with a model that is represented as independently trained.

### Track B — independent implementation

Define the public behavior needed by NammaSpace, then implement a reconstruction adapter from public papers, public mathematical descriptions, and independently created code. Train or obtain weights whose licenses permit the intended use. The implementation may be compatible at the API level, but must not reproduce protected source expression or upstream model files. A clean-room process reduces provenance risk; it is not a blanket commercial-use permission and does not resolve patents, trademarks, data rights, privacy, or third-party licenses.

## Separation protocol

1. **Specification team:** may read the paper, public documentation, benchmark descriptions, and observed input/output behavior. It writes behavior-level specifications, test cases, equations, and acceptance criteria without copying source code or source comments.
2. **Implementation team:** receives only the approved specification, test fixtures created by the team, and permissively licensed dependencies. It must not access the upstream repository, checkpoint files, or copied snippets while implementing.
3. **Independent review:** compare behavior against the specification and held-out fixtures. Reviewers check provenance, commit history, dependency licenses, and generated artifacts.
4. **Evidence archive:** retain dated specifications, contributor attestations, source inventory, hashes, data consents, model cards, and decision records. Do not retain or redistribute upstream materials merely to prove separation.
5. **Release gate:** block publication when a dependency has unclear commercial terms, when a checkpoint’s dataset conditions are not satisfied, when attribution is missing, or when code provenance cannot be explained.

## Provenance rules

- Every dependency has a pinned version, source URL, license, copyright notice, and intended use.
- Every model has a source URL, checksum, training-data statement, usage restriction, and whether it is used in Track A or Track B.
- Every dataset has consent/terms, geographic/privacy constraints, and a retention policy.
- Generated scene captures are owned and shared only under a documented consent and competition policy.
- Do not describe the whole repository as “open source” if any bundled model, dataset, or asset is non-commercial or source-available only.
- Keep the repository’s own original code under a separate license chosen by the team. Do not apply the team license to third-party material.

## Release matrix

| Artifact | Research-only competition evaluation | Commercial deployment | Required action |
|---|---:|---:|---|
| Upstream DUSt3R code | Possibly, subject to CC BY-NC-SA terms | Not assumed | Confirm scope in writing or replace |
| Upstream DUSt3R checkpoint | Additional dataset/base-model terms | Not assumed | Audit each model and dataset |
| Clean-room adapter code | Depends on dependencies and provenance | Potentially, if all rights clear | License review and patent/data/privacy review |
| Team capture data | Consent and venue rules apply | Consent and contract review | Minimize, redact, and document |
| Browser viewer | Depends on bundled assets/models | Depends on all bundled assets/models | Separate code from restricted artifacts |

## Immediate decision

For the competition build, keep DUSt3R behind a replaceable adapter and publish a “research baseline” configuration only after the team confirms the competition context is non-commercial under the applicable license. For anything connected to paid work, job deliverables, productization, or commercial advantage, use the clean-room or a commercially permissive reconstruction stack and obtain written counsel/rights-holder review.

## References

[1]: https://github.com/naver/dust3r "naver/dust3r — license, checkpoints, and dataset notes"
[2]: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International — legal code"
[3]: https://guides.nyu.edu/software-reproducibility/licensing "NYU Libraries — licensing research software"
