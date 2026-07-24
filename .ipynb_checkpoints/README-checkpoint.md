# Lumbar Spine Diagnostic

An end-to-end, multi-stage AI diagnostic pipeline built to analyze personal lumbar spine MRIs **locally**. It ingests raw DICOM scans, automatically locates the five lumbar discs (L1–S1), crops the regions of interest, and produces a structured clinical readout of stenosis severity — all on your own machine, with no data leaving your device.

> ⚠️ **Disclaimer:** This is a personal research and learning project. It is **not** a medical device and is not intended for clinical diagnosis. Always consult a qualified radiologist or physician.

## Architecture

The pipeline runs in four stages:

| Stage | Tooling | What it does |
| --- | --- | --- |
| **1. Data Wrangling** | `pydicom`, `numpy` | Extracts and normalizes raw DICOM files into high-contrast 8-bit grayscale images. |
| **2. Target Detection** | YOLOv8 | A fast object detector, trained on Kaggle coordinate data, instantly locates the exact _x_ and _y_ pixels of the five lumbar discs (L1–S1). |
| **3. Image Processing** | OpenCV | Automatically crops the scans and draws bounding boxes around the regions of interest. |
| **4. Clinical Evaluation** | Local VLM (e.g. Qwen2-VL) | Feeds the tightly cropped, localized slices into a Vision-Language Model to classify stenosis severity and emit a structured medical readout. |

```
DICOM  →  Normalize  →  YOLOv8 detect  →  Crop + box  →  VLM classify  →  Structured readout
(raw)     (8-bit img)    (L1–S1 coords)   (OpenCV)       (Qwen2-VL)        (severity)
```

## Why local?

Medical imaging is sensitive. Every stage — detection, cropping, and language-model evaluation — runs on-device so that personal MRI data is never uploaded to a third-party service.

## Project layout

```
.
├── main.py                 # Entry point
├── src/
│   └── extract_data.py     # Stage 1: DICOM extraction & normalization
├── pyproject.toml
└── README.md
```

## Getting started

Requires **Python 3.13+**. This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run
uv run main.py
```

## Data & References

Detection is trained on the coordinate labels from the RSNA 2024 lumbar spine challenge, and the analysis approach draws on published community notebooks.

- **Dataset / competition:** [RSNA 2024 Lumbar Spine Degenerative Classification](https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification) — DICOM MRI series with per-level coordinate labels and stenosis severity grades for L1–S1.
- **Reference notebook:** [RSNA Lumbar Spine Analysis](https://www.kaggle.com/code/satyaprakashshukl/rsna-lumbar-spine-analysis) by Satya Prakash Shukl — exploratory analysis and modeling approach that informed this pipeline.

## License

This project's source code is licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE) — you may use, modify, and share it for **any noncommercial purpose**, but not commercially.

This restriction is deliberate: the RSNA 2024 training data this pipeline is built on is licensed for **noncommercial use only**. See [NOTICE.md](NOTICE.md) for the full list of third-party data, models, and references and their respective license terms.

## Status

🚧 **Work in progress.** The DICOM extraction and normalization stage is under active development; the detection, cropping, and VLM evaluation stages are being built out.
