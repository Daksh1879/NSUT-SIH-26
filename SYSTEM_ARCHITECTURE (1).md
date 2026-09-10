# System Architecture — Legal Metrology Compliance Checker

## High-level flow

```text
User
  |
  v
Frontend (web UI)
  |
  v
Backend API
  |
  +--> cv_service  --> OCR Region Extraction (text + bounding boxes)
  |
  +--> classifier  --> Declaration Classification (MRP, net qty, MFG date, etc.)
  |
  +--> engine (rule_engine) --> Rule Evaluation
  |        ^
  |        |
  |     rules / legalmetrology_part3 (Legal Metrology PCR rule definitions)
  |
  v
Compliance Report (violations, compliance score, status)
  |
  v
Frontend (results display)
```

Core pipeline can also be run standalone via `main.py` (CLI), bypassing the web layer entirely — useful for testing and batch scans.

```text
main.py --input ocr.json --weight 500
   |
   v
schemas.OCRRegion / BoundingBox   (load_ocr_json)
   |
   v
classifier.classify_regions       (raw OCR text -> declaration fields)
   |
   v
engine.run_rule_engine            (declarations + product_context -> ComplianceReport)
   |
   v
Console summary + optional JSON report (--output)
```

## Components

### Frontend
Web interface where a user uploads a product package image (or OCR data) and views the compliance report — violations, compliance score, and suggested corrections — once the backend finishes processing.

### Backend API
Receives the uploaded image/request, orchestrates the pipeline (`cv_service` → `classifier` → `engine`), and returns the structured compliance report to the frontend.

### cv_service
Computer-vision layer that processes the raw product image and produces OCR output — text regions with bounding boxes, confidence, estimated font size, and language — matching the `OCRRegion` / `BoundingBox` schema consumed by `main.py` and the classifier.

### classifier
Takes the raw OCR regions and classifies each one into a Legal Metrology declaration field (e.g. MRP, net quantity, manufacturer/packer name and address, manufacturing date, consumer care details, country of origin, unit sale price).

### engine (rule_engine)
Evaluates the classified declarations against the Legal Metrology Packaged Commodities Rules, using the product context (e.g. declared net weight). Produces a `ComplianceReport` containing a summary, a list of violations (rule ID, field, violation type, penalty class, description, suggested correction), a compliance score (0–100), and an overall compliant / non-compliant status.

### rules / legalmetrology_part3
Rule definitions and reference data encoding the actual Legal Metrology (Packaged Commodities) Rules that the rule engine checks declarations against.

### schemas
Shared data structures (e.g. `OCRRegion`, `BoundingBox`) used across the OCR, classification, and rule-engine stages to keep the pipeline's data contract consistent.

### Scripts
Utility/automation scripts supporting the project (e.g. data prep, batch runs, testing helpers) outside the core request/response pipeline.

### tests
Automated test suite (pytest) validating the classifier and rule engine logic.

### main.py
Command-line entry point that runs the classification + rule-engine pipeline directly against an OCR JSON file, without the frontend/backend web layer — prints a compliance summary to the console and can optionally write a JSON report.

## Data flow summary
1. A product package image is captured/uploaded via the **Frontend**.
2. The **Backend API** receives it and calls the **cv_service** to run OCR, producing text regions with bounding boxes.
3. The **classifier** maps each OCR region to a Legal Metrology declaration field.
4. The **engine**, using rules from **rules / legalmetrology_part3**, checks the declarations for missing, incorrect, or non-compliant information.
5. A **compliance report** (violations, score, status) is generated and returned to the **Frontend** for display to the user.

---
> **Note:** This document was reconstructed from the repository's folder structure (`Backend`, `Frontend`, `Scripts`, `classifier`, `cv_service`, `engine`, `legalmetrology_part3`, `rules`, `schemas`, `tests`) and the working CLI pipeline in `main.py`. Please review and adjust component descriptions/connections (especially inside `Backend`, `Frontend`, and `cv_service`) to exactly match your implementation details before final submission, since those folders weren't directly readable during this pass.
