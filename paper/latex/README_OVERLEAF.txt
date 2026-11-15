BRIDGE-AI | HPDC-Net IEEE Article (4 pages)
==========================================

CONTENTS
  main.tex                           IEEE two-column LaTeX manuscript (English)
  figures/confusion_baseline.pdf     Confusion matrix reconstructed from observed counts
  figures/confusion_proposed.pdf     Confusion matrix reconstructed from observed counts
  figures/efficiency.pdf             Plot of relative resource requirements
  make_figures.py                    Recreates the figures from the experiment values

OVERLEAF
1. Open https://www.overleaf.com/ and create a blank project.
2. Upload all contents of this ZIP, retaining the figures/ subdirectory.
3. Ensure the main document is main.tex and set compiler to pdfLaTeX.
4. Compile. The verified result is a 4-page, two-column IEEE paper.
5. Edit the author affiliation, institution, any coauthor names, and email.

SCIENTIFIC NOTES BEFORE SUBMISSION
- This paper describes the ACTUALLY EXECUTED ten-class TOMATO experiment,
  not the original Week-2 proposal's three-class POTATO and augmentation experiment.
  Align the topic/proposal with your supervisor before submission.
- Published paper reports approximately 0.52M params and 0.06 GFLOPs;
  released notebook reproduced locally has 764,376 params and 1.0147 GMACs.
  These units are not numerically equated in the paper.
- Reported test metrics are from the user-run saved local checkpoints,
  not independent author reruns in this deliverable.
- Single run per model; the +1 correct image is not statistically significant.
- The official code and dataset must be properly linked in the final GitHub repo,
  along with baseline/proposed scripts, logs, requirements, splits and seeds.

VERIFIED SOURCES
- HPDC-Net: https://doi.org/10.1038/s41598-025-08788-4
- Official code: https://github.com/ZahidFarooqKhan/HPDC-Net
- Dataset: https://doi.org/10.17632/tywbtsjrjv.1  (CC0 1.0)
