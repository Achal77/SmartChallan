# Project Report - SmartChallan Traffic Violation Detection System

**Author**: A Achal
**Registration No.**: 24BAI10839
**Course**: Computer Vision
**Submission Type**: Bring Your Own Project (BYOP)

## Cover Page

**Project**: SmartChallan - Traffic Violation Detection System  
**Author**: A Achal  
**Registration No.**: 24BAI10839  
**Course**: Computer Vision  
**Submission**: Bring Your Own Project (BYOP)

---

## 1. Problem Statement

In this project I focused on three common two-wheeler violations: no helmet, triple riding, and jumping a red light. A person reviewing camera footage has to notice the event, identify the vehicle, save evidence, and prepare a record. That process is slow when done for every frame.

My aim was to build a small proof-of-concept that can:

- detect the selected violations from a camera frame
- extract a vehicle number when the image is readable
- save the evidence and create a challan record

---

## 2. Reason for Choosing the Problem

I chose this problem because it combines object detection, image processing, OCR, storage, and a user interface in one project. It also gives a clear output to demonstrate: an annotated image, a log entry, and a generated challan. This is a classroom prototype, not an official traffic system.

---

## 3. Objectives

1. Read frames from a webcam or use a demo frame.
2. Detect three violation types using computer vision rules.
3. Try to read the number plate with OCR.
4. Generate a PDF challan with the detection details.
5. Display the results in a Streamlit dashboard.

---

## 4. Functional Requirements

1. Capture frames from a webcam or generate a demonstration frame.
2. Detect people and motorcycles using YOLOv8.
3. Detect no-helmet, triple-riding, and red-light violations.
4. Extract a vehicle number with OCR or a fallback plate generator.
5. Save evidence snapshots and generate PDF e-challans.
6. Record timestamp, violation, plate, confidence, challan ID, and snapshot path in CSV.
7. Display live alerts, statistics, detection history, and downloadable challans.

## 5. Non-Functional Requirements

- **Performance**: YOLOv8n is selected for near-real-time CPU inference; OCR and PDF generation run only for detected violations.
- **Usability**: Streamlit provides labelled controls, live feedback, demo mode, and documented setup commands.
- **Reliability**: YOLO and OCR imports have graceful fallbacks, while camera failures are reported in the dashboard.
- **Maintainability**: Detection, orchestration, challan generation, documentation, and tests are separated into focused files.
- **Error handling**: Invalid or unavailable image regions return fallback plate values, and snapshot embedding failures do not stop PDF generation.
- **Observability**: Every generated challan is paired with a CSV record and evidence path.

## 6. System Architecture and Design

The application uses a modular pipeline: the Streamlit dashboard obtains a frame, `ViolationDetector` performs object detection and rule evaluation, and `challan_generator.py` creates the evidence notice. CSV files, snapshots, and challans provide simple persistent storage for this proof-of-concept.

The architecture, workflow, use-case, component, sequence, and storage diagrams are maintained in [docs/design.md](docs/design.md). The detailed requirement matrix is in [docs/requirements.md](docs/requirements.md).

## 7. Approach & Methodology

### 7.1 Object Detection — YOLOv8

I used **YOLOv8n** (nano variant) from Ultralytics as the primary detection backbone. It was chosen because:

- Pre-trained on COCO dataset — detects `person` and `motorcycle` out of the box
- Fast enough for near-real-time inference (~30 FPS on CPU with nano model)
- Easy Python API with minimal setup

The detection pipeline:
1. Each frame from the webcam is passed to YOLOv8
2. Detected bounding boxes are filtered for `person` (class 0) and `motorcycle` (class 3)
3. Spatial overlap between persons and motorcycles is calculated to associate riders with vehicles

### 7.2 Dataset Description

The prototype uses the pretrained COCO object-detection dataset through the YOLOv8n model. The relevant COCO classes are `person` (class 0) and `motorcycle` (class 3). No private student data or personally identifying dataset is stored in this repository. The demo mode uses synthetic frames and fixed sample records so the workflow can be evaluated without a camera.

### 7.3 Violation Logic

**No Helmet:**
The top 25% of each detected rider's bounding box is treated as the "head region." A brightness (HSV Value channel) heuristic determines if a helmet is present — helmets tend to be darker and more uniform in colour than bare heads.

**Triple Riding:**
The count of persons whose bounding box overlaps significantly (>20% IoU) with a motorcycle bounding box is computed. If 3 or more persons are associated with one motorcycle, a triple riding violation is flagged.

**Red Light Jump:**
The upper-centre region of the frame (where traffic signals typically appear) is analysed in HSV colour space. If red pixels exceed 4% of the ROI area and a motorcycle is detected, a red light jump violation is raised.

### 7.4 Number Plate OCR

The bottom 20% of each motorcycle's bounding box is cropped as the number plate region. The region is:
1. Converted to grayscale
2. Upscaled 2× for better OCR resolution
3. Binarised using Otsu's thresholding
4. Passed to **pytesseract** with restricted character set (`A-Z`, `0-9`)

A fallback random plate generator ensures the demo always works without Tesseract installed.

### 7.5 PDF Challan Generation

**fpdf2** was used to generate structured PDF challans containing:
- Challan ID, timestamp, vehicle number, violation type
- AI confidence score
- Fine amount (as per Motor Vehicles Act, 2019)
- Evidence snapshot embedded in the PDF
- Authority footer and payment instructions

### 7.6 Dashboard

**Streamlit** was used for the frontend because it allows rapid development of data apps with Python. The dashboard includes:
- Live annotated camera feed
- Real-time violation alert banner
- Detection statistics (total challans, per-violation counts)
- Configurable confidence threshold and active violation selection
- Detection log table (CSV-backed)
- Downloadable PDF challans

---

## 8. Key Design Decisions

| Decision | Rationale |
|---|---|
| YOLOv8n (nano) over larger models | Speed > accuracy on CPU; nano is sufficient for proof-of-concept |
| Brightness heuristic for helmet | No custom-labelled dataset available; heuristic works as a baseline |
| HSV colour space for red light | More robust to lighting changes than RGB thresholding |
| fpdf2 over ReportLab | Simpler API, no external font dependencies, sufficient for structured documents |
| Streamlit over Flask/React | Faster to build; appropriate for a data-heavy CV dashboard |
| CSV logging over SQL | Simpler dependency stack; adequate for the project scope |
| Demo mode | Allows evaluation without physical camera hardware |

---

## 9. Challenges Faced

**Challenge 1 – No custom helmet dataset**
A custom-trained YOLO model for helmet detection would significantly improve accuracy. Without labelled data, a heuristic approach was used. This is a known limitation and a clear direction for future improvement.

**Challenge 2 – OCR accuracy on number plates**
Tesseract was designed for printed text and struggles with low-resolution, angled, or dirty number plates. Upscaling and binarisation improved results, but accuracy in poor lighting conditions remains a limitation. Dedicated ANPR (Automatic Number Plate Recognition) models like OpenALPR or PaddleOCR would perform better.

**Challenge 3 – Red light detection without a signal in frame**
The colour-based approach requires the traffic signal to be visible in the camera frame. In real deployments, the camera position relative to the signal matters greatly.

**Challenge 4 – Real-time performance**
Running YOLOv8 + OCR + PDF generation in a tight loop caused latency. This was resolved by only triggering OCR and PDF generation on confirmed violations (not every frame) and using the YOLOv8 nano model.

---

## 10. Results

In demo mode, the system successfully:
- Detected 3 simulated violations simultaneously
- Generated 3 distinct PDF challans with correct information
- Logged all detections to CSV
- Displayed live statistics on the dashboard

With a webcam and adequate lighting:
- Person and motorcycle detection works reliably at >50% confidence threshold
- Number plate OCR produces partial plate numbers in most cases
- Red light detection is effective when the signal is within the frame's upper centre

---

## 11. Testing Approach

Automated validation is implemented with Python's standard `unittest` framework and can be run with:

```bash
python -m unittest discover -s tests -v
```

The suite checks detector overlap logic, violation colour coverage, helmet helper behaviour, fallback plate formatting, submission identity, storage schema, and required challan fields. The current automated run contains **7 passing tests**. Manual testing covers camera start/stop, demo mode, dashboard controls, CSV logging, evidence snapshots, and PDF downloads.

## 12. Evaluation Methodology

The system is evaluated in two modes:

1. **Deterministic validation**: unit tests verify pure helper functions, identity configuration, log schema, fallback plate format, and challan field content.
2. **Workflow validation**: demo mode verifies the complete path from frame creation to violation annotation, evidence snapshot, challan generation, CSV logging, and dashboard display. Webcam evaluation is performed under adequate lighting with a confidence threshold of 0.5.

The prototype is assessed for functional completion rather than production accuracy. The main limitations are the heuristic helmet classifier, colour-based red-light detector, OCR sensitivity to image quality, and the lack of a custom labelled helmet dataset.

## 13. What I Learned

1. **YOLOv8 was easy to try** — loading a pretrained model took only a few lines. Most of my work was in connecting its output to the violation rules and the dashboard.

2. **Heuristics are a valid starting point** — not every CV problem requires a custom model. Colour-space analysis and geometric reasoning can solve real problems effectively.

3. **OCR on real-world images is hard** — good lighting, a frontal angle, and a clean plate are important. This was the part that gave the least consistent results.

4. **Streamlit is powerful for CV prototyping** — combining image display, controls, and data tables in one Python file is very productive.

5. **System design matters as much as the model** — logging, evidence capture, PDF generation, and the dashboard together make this a usable system, not just a detection script.

---

## 14. Future Improvements

- Train a custom YOLOv8 model on a labelled helmet/no-helmet dataset (e.g., from Roboflow)
- Integrate a dedicated ANPR model (PaddleOCR or OpenALPR) for better plate reading
- Connect to the Vahan RTO database API to fetch owner details from plate number
- Add SMS/email alert to the vehicle owner using Twilio/SendGrid
- Deploy on a Raspberry Pi with a Pi Camera for edge deployment
- Add speed estimation using frame-to-frame displacement

---

## 15. References

- Ultralytics YOLOv8 Documentation — https://docs.ultralytics.com
- OpenCV Documentation — https://docs.opencv.org
- pytesseract — https://pypi.org/project/pytesseract
- fpdf2 — https://py-fpdf2.readthedocs.io
- Motor Vehicles (Amendment) Act, 2019 — fine amounts
- MoRTH Road Accidents in India 2022 Report

---

*I prepared this report for my Computer Vision BYOP submission.*
