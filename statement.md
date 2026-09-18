# SmartChallan Project Statement

**Author**: A Achal
**Registration No.**: 24BAI10839

## Problem Statement

Manual traffic enforcement cannot continuously monitor every road, and paper-based processing makes it difficult to identify violations, preserve evidence, and issue notices quickly. SmartChallan uses computer vision to detect common two-wheeler violations, read the vehicle number plate, and generate an evidence-backed e-challan.

## Scope

The project covers webcam-based monitoring, YOLOv8 person and motorcycle detection, heuristic helmet analysis, triple-riding detection, red-light colour analysis, number-plate OCR, CSV logging, and PDF challan generation. It is a proof-of-concept and does not connect to government databases, make legal enforcement decisions, or send messages to vehicle owners.

## Target Users

- Traffic enforcement teams reviewing camera footage
- Computer-vision students demonstrating an end-to-end ML application
- Researchers evaluating lightweight violation-detection workflows

## High-Level Features

1. Real-time camera feed with annotated detections
2. Demo mode for evaluation without camera hardware
3. No-helmet, triple-riding, and red-light violation detection
4. Number-plate OCR with a deterministic fallback format
5. Evidence snapshots and generated PDF e-challans
6. CSV-backed dashboard statistics and downloadable records