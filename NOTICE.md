# Third-Party Data, Models & References

This project's own source code is licensed under the **PolyForm Noncommercial
License 1.0.0** (see [LICENSE](LICENSE)). That noncommercial restriction is not
incidental — it is required to stay consistent with the terms of the training
data below, which permit **noncommercial use only**. Do not relicense this
project under permissive (e.g. MIT/Apache) terms while it depends on this data.

The following third-party materials are used by, referenced by, or informed this
project. Each carries its own license; those terms govern the corresponding
material and are **in addition to** this project's own license.

---

## Training / evaluation data

### RSNA 2024 Lumbar Spine Degenerative Classification dataset (RSNA-LSDD)

- Source (competition): <https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification>
- Source (open data mirror): <https://registry.opendata.aws/rsna-lumbar-spine-degenerative-classification-dataset/>
- Provider: Radiological Society of North America (RSNA)
- Terms: **Noncommercial use only** (academic research and education). Users must
  not attempt to re-identify or contact any individual who may be a subject of
  the data. The competition's official rules and data-use agreement on Kaggle
  are the controlling terms — review and accept them before using the data.
- Note: The dataset itself is **not** redistributed in this repository. It must
  be obtained directly from the sources above under their terms.

---

## Reference notebooks / prior work

### RSNA Lumbar Spine Analysis

- Author: Satya Prakash Shukl
- Source: <https://www.kaggle.com/code/satyaprakashshukl/rsna-lumbar-spine-analysis>
- Use: Exploratory analysis and modeling approach that informed this pipeline.
- License: As published on Kaggle (Kaggle notebooks are commonly released under
  the Apache License 2.0). Confirm the license shown on the notebook page and
  retain attribution to the author for any derived code.

---

## Models & tooling (referenced in the pipeline)

These are integrated or planned integrations; each is governed by its own
upstream license, obtained from its respective distributor:

- **YOLOv8** (Ultralytics) — AGPL-3.0 / Ultralytics Enterprise License.
- **Qwen2-VL** (or other local VLM) — governed by the model's own license card.
- **pydicom**, **numpy**, **OpenCV** — their respective open-source licenses.

Review each upstream license before commercial or redistribution use. Note in
particular that some of these (e.g. YOLOv8 under AGPL-3.0) impose their own
copyleft or noncommercial-style obligations independent of this project.
