# NammaSpace problem statement and submission contract

## What the official page says

Techfest, IIT Bombay describes Namma Space as an end-to-end intelligent spatial engine that converts standard smartphone captures of indoor spaces into interactive 3D digital twins. The target experience includes remote virtual walkthroughs, spatial point-of-interest (POI) search, and optimal non-colliding indoor path planning. The competition is staged as two online rounds followed by an on-site IIT Bombay finale. [1]

Round 1, **3D Reconstruction & Roaming**, asks teams to map their own indoor space under a custom standard operating procedure (SOP), then submit a technical abstract, proof-of-concept web viewer link, code repository, and a 3–5 minute demo video showing free roaming. Round 2 adds interactive POI tagging, search indexing, and obstacle-aware desktop navigation. Round 3 requires a fresh on-campus capture, reconstruction, POI annotation, deployment, a 10-minute live pitch, and a 5-minute technical Q&A. [1]

The page says solutions must be the team’s original work, open-source tools must comply with their licenses and be credited in the technical abstract, and supplementary links or drive materials must be organized inside a single master PDF in the submission folder. [1]

## Length audit

**Finding:** the public page retrieved on 29 October 2026 specifies the required artifact types and demo durations, but it does **not** specify a page limit, word limit, font, or file-size limit for the technical abstract or master PDF. This repository must not invent an official limit.

**Working target until the portal or organizers confirm otherwise:**

- Technical abstract/report: **6–8 pages**, excluding references and appendices. It should be readable as a self-contained technical document and should link to the repository, viewer, demo, capture SOP, and evaluation results.
- Master PDF: **2–4 pages**, containing the submission index, stable links, license/provenance notes, and reproducibility instructions. Keep it separate from the longer report only if the portal allows multiple PDFs; otherwise merge the report and index into one master PDF.
- Demo video: **3–5 minutes** for Round 1, as explicitly stated on the official page. [1]

**Open action:** before submission, check the authenticated competition portal and the latest organizer announcement for a superseding page/word/file-size constraint. Record the date and URL in the submission checklist. If the portal remains silent, use the working target above and prioritize completeness over padding.

## Acceptance checklist

- [ ] Capture SOP is written, repeatable, and tested by a second operator.
- [ ] Input images/video and any sensor metadata have documented consent and retention rules.
- [ ] Reconstruction runs without manual 3D modelling.
- [ ] Web viewer supports free roaming and a stable scene URL.
- [ ] POIs can be tagged, searched, and linked to geometry.
- [ ] Desktop pathfinding avoids marked obstacles and reports no-path cases.
- [ ] Repository is reproducible from a clean environment or documents unavoidable manual steps.
- [ ] Every third-party code, model, dataset, and font has a provenance and license entry.
- [ ] The technical abstract cites all open-source components.
- [ ] The master PDF contains all supplementary links.
- [ ] License review resolves whether any DUSt3R-dependent artifact is non-commercial only.

## References

[1]: https://techfest.org/competitions/nammaspace "Namma Space — Techfest, IIT Bombay"
