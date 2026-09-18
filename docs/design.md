# SmartChallan Design Artefacts

## System Architecture

```mermaid
flowchart LR
    User[User] --> UI[Streamlit Dashboard]
    UI --> Camera[Webcam or Demo Frame]
    Camera --> Detector[ViolationDetector]
    Detector --> YOLO[YOLOv8 Person/Motorcycle Detection]
    Detector --> Rules[Violation Rules and OCR]
    Rules --> Evidence[Snapshot Storage]
    Rules --> Challan[Challan Generator]
    Challan --> PDFs[PDF/Text Challan]
    Rules --> Log[CSV Detection Log]
    PDFs --> UI
    Log --> UI
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Start camera or demo mode] --> B[Read frame]
    B --> C{YOLO model available?}
    C -->|Yes| D[Detect people and motorcycles]
    C -->|No| E[Use demo/fallback path]
    D --> F[Evaluate enabled violation rules]
    E --> F
    F --> G{Violation found?}
    G -->|No| B
    G -->|Yes| H[Read plate and save snapshot]
    H --> I[Generate challan]
    I --> J[Append CSV log and update dashboard]
    J --> B
```

## Use Case Diagram

```mermaid
flowchart LR
    Officer((Traffic reviewer))
    Officer --> UC1[Start or stop monitoring]
    Officer --> UC2[Choose active violations]
    Officer --> UC3[Review live alerts and statistics]
    Officer --> UC4[Download challan]
    System((SmartChallan))
    System --> UC5[Detect violation]
    System --> UC6[Generate evidence PDF]
```

## Component Diagram

```mermaid
flowchart TB
    App[app.py\nDashboard and orchestration]
    Detector[detector.py\nYOLO, rules, OCR]
    Generator[challan_generator.py\nPDF/text output]
    Storage[(CSV, snapshots, challans)]
    App --> Detector
    App --> Generator
    App --> Storage
    Detector --> Storage
    Generator --> Storage
```

## Sequence Diagram

```mermaid
sequenceDiagram
    actor User
    participant UI as Streamlit
    participant D as Detector
    participant G as Challan Generator
    participant S as Storage
    User->>UI: Start camera or demo
    UI->>D: detect(frame, threshold, active rules)
    D-->>UI: violations and annotated frame
    UI->>S: Save evidence snapshot
    UI->>G: generate_challan(details)
    G->>S: Write PDF or text fallback
    UI->>S: Append detection CSV record
    UI-->>User: Show alert, statistics, and download
```

## Storage Design

The CSV log uses the following schema:

| Column | Meaning |
|---|---|
| `timestamp` | Detection time |
| `violation` | Violation category |
| `plate` | OCR or fallback plate value |
| `confidence` | Model confidence |
| `challan_id` | Generated unique identifier |
| `snapshot` | Evidence image path |