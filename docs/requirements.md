# SmartChallan Requirements

## Functional Requirements

| ID | Requirement | Acceptance criterion |
|---|---|---|
| FR-01 | Capture input from a webcam | The user can start and stop a live camera feed. |
| FR-02 | Detect people and motorcycles | YOLOv8 results are filtered for person and motorcycle classes. |
| FR-03 | Detect violations | The system identifies no-helmet, triple-riding, and red-light violations when enabled. |
| FR-04 | Extract vehicle numbers | The system applies OCR to a motorcycle plate region and supplies a fallback plate when OCR is unavailable. |
| FR-05 | Preserve evidence | A snapshot is stored for every generated challan. |
| FR-06 | Generate challans | A structured PDF or text fallback contains the violation, plate, confidence, timestamp, fine, and challan ID. |
| FR-07 | Log and report results | Detection records are written to CSV and shown in dashboard statistics and tables. |
| FR-08 | Support demonstration | Demo mode produces representative violations without a physical camera. |

## Non-Functional Requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-01 | Performance | Use the YOLOv8 nano model and avoid OCR/PDF work unless a violation is detected. |
| NFR-02 | Usability | A first-time user can run the dashboard from the documented commands and use labelled controls. |
| NFR-03 | Reliability | Missing YOLO, OCR, camera, or PDF dependencies have graceful fallback/error paths where possible. |
| NFR-04 | Maintainability | Detection, PDF generation, UI, documentation, and tests are kept in separate modules/files. |
| NFR-05 | Error handling | Camera failures are shown in the dashboard; OCR and PDF snapshot failures do not crash the detection loop. |
| NFR-06 | Observability | Each generated challan records timestamp, violation, plate, confidence, snapshot, and challan ID. |
| NFR-07 | Resource efficiency | The application uses the lightweight YOLOv8n model and creates output directories only when needed. |

## Validation Strategy

Automated tests validate pure detection helpers and challan output. Manual validation covers webcam access, Streamlit interaction, demo mode, and visual quality of generated PDFs.