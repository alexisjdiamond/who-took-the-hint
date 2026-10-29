# Who Took the Hint?

*Applying Methods of Causal Inference to Evaluate Chain of Thought Monitorability*

Alexis Diamond, Minerva University. Agent Evaluation Science symposium, New York, November 2026.

- **[Paper (PDF)](who-took-the-hint.pdf)**
- **[Online supplement (PDF)](who-took-the-hint-online-supplement.pdf)**: Appendices A.2, A.4, B.1–B.4, C and D. Section numbers match the references in the paper; Appendices A.1, A.3, A.5, A.6, B.5 and E are printed with the paper.
- **[Long-form version (PDF)](who-took-the-hint-full.pdf)**: the full paper, with the appendices in the body and later related work. The two PDFs above are the symposium version, fixed as of October 2026 apart from the corrections noted below; this one is kept up to date.

**Note on versions.** The symposium PDFs are corrected relative to the version submitted to the symposium in October 2026. Section 5.2 and Appendices A.3 and A.5 previously said that the width of the recall interval is set by the base rate; that holds only when the monitor's flag rate is below the floor. What the base rate governs is whether a lower bound above zero is available at all, which requires the flag rate to exceed the base rate. Appendix D's readings of two published results have also been corrected, and it now cites the companion paper at https://github.com/alexisjdiamond/who-would-have-complied-anyway. R_effect is now described as the share whose output the cue changed rather than the complier share, the Bürger et al. attribution is corrected, and the concurrent Fu et al. (2026) is cited. The conclusions are unchanged.

The `latex-source/` folder (if present) contains the LaTeX source for both documents; compile `main.tex` and `supplement.tex` with XeLaTeX. The `arxiv-source/` folder contains the source for the long-form version; compile `main.tex` with pdfLaTeX (the bibliography is in `main.bbl`).
