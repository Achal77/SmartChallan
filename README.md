# SmartChallan - Traffic Violation Detection System

SmartChallan is my computer vision project for detecting common traffic violations from a webcam. It uses YOLOv8 for people and motorcycle detection, OpenCV for image processing, Tesseract for number plates, and Streamlit for the dashboard.

**Student**: A Achal  
**Registration No.**: 24BAI10839

---

## Features

| Feature | Description |
|---|---|
| Person and motorcycle detection | YOLOv8 detects the two COCO classes used by the project |
| No-helmet detection | Checks the upper part of a detected rider |
| Triple-riding detection | Counts people overlapping a motorcycle box |
| Red-light detection | Checks for red pixels in the upper centre of the frame |
| Number-plate OCR | Uses Tesseract on the bottom part of a motorcycle box |
| Challan generation | Saves a PDF with the detection details and evidence image |
| Dashboard | Shows the feed, statistics, log, and saved challans |
| Demo mode | Runs the workflow without a webcam |

---

## Tools Used

- **Python 3.10+**
- **OpenCV** – Video capture & image processing
- **YOLOv8** (Ultralytics) – Object detection
- **pytesseract** – OCR for number plate reading
- **fpdf2** – PDF challan generation
- **Streamlit** – Web dashboard
- **Pandas** – Detection logging

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/Achal77/SmartChallan.git
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR (for number plate reading)
- **Windows**: Download from https://github.com/UB-Mannheim/tesseract/wiki
- **Linux**: `sudo apt install tesseract-ocr`
- **Mac**: `brew install tesseract`

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## Running the Project

### With a webcam:
1. Click **▶ Start Camera**
2. Point camera at traffic (or yourself to test)
3. Violations are detected automatically
4. PDF challans appear in the **Saved Challans** tab

### Without a webcam (demo):
1. Click **🎭 Demo Mode**
2. The system simulates 3 violations
3. PDFs are generated instantly — download from the Challans tab

## Tests

Run the validation suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The tests cover violation colour mapping, bounding-box overlap, fallback plate
formatting, submission identity, storage schema, and PDF/text challan generation.
The camera and YOLO paths require
the optional runtime dependencies listed in `requirements.txt`.

## Project Documents

- Project scope and target users: [statement.md](statement.md)
- Functional and non-functional requirements: [docs/requirements.md](docs/requirements.md)
- Architecture and UML-style diagrams: [docs/design.md](docs/design.md)
- Detailed implementation report: [PROJECT_REPORT.md](PROJECT_REPORT.md)

---

## Project Structure

```
e-challan-system/
│
├── app.py                  # Streamlit dashboard (main entry point)
├── detector.py             # YOLOv8 violation detection logic
├── challan_generator.py    # PDF challan generation (fpdf2)
│
├── snapshots/              # Auto-saved violation screenshots
├── challans/               # Generated PDF challans
├── logs/
│   └── detections.csv      # Detection history log
│
├── requirements.txt
├── .gitignore
├── config.py                # Project identity and runtime configuration
├── storage.py               # CSV log persistence
├── statement.md             # Problem, scope, users, and high-level features
├── README.md
├── docs/
│   ├── design.md            # Architecture and UML-style diagrams
│   └── requirements.md      # Functional and non-functional requirements
└── tests/
      └── test_core.py         # Automated validation tests
```

---

## Processing Flow

```
Live Camera Feed
      │
      ▼
YOLOv8 Object Detection
  ├── Detect motorcycles
  └── Detect persons
      │
      ▼
Violation Analysis
  ├── Count riders per motorcycle  →  Triple Riding
  ├── Analyse head region          →  No Helmet
  └── Check signal colour (HSV)   →  Red Light Jump
      │
      ▼
Number Plate OCR (pytesseract)
      │
      ▼
Generate PDF Challan (fpdf2)
      │
      ▼
Log to CSV + Display in Dashboard
```

---

## Fine Table Used by the Demo

| Violation | Fine (INR) |
|---|---|
| No Helmet | ₹1,000 |
| Triple Riding | ₹1,000 |
| Red Light Jump | ₹5,000 |

---

## Limitations

- Number plate OCR accuracy depends on image quality and lighting
- Helmet detection uses a brightness heuristic; a custom-trained model would improve accuracy
- Red light detection requires the signal to be visible in frame
- Future: SMS/Email alert to vehicle owner, integration with RTO database

---

## Author

**A Achal**
This is a Bring Your Own Project (BYOP) submission for the Computer Vision course.

---

## 📄 License

MIT License – free to use and modify.
