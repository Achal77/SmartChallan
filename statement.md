# SmartChallan Project Statement

**Author**: A Achal
**Registration No.**: 24BAI10839

## Problem Statement

Checking traffic footage manually takes time. It is also easy to lose the connection between a violation, the vehicle number, and the evidence image. I built SmartChallan to test a small automated workflow for these tasks. The program reads a camera frame, checks for selected two-wheeler violations, reads a plate when possible, and creates a challan record.

## Scope

The project covers webcam monitoring, YOLOv8 person and motorcycle detection, a brightness-based helmet check, triple-riding detection, red-light colour analysis, number-plate OCR, CSV logging, and PDF generation. It is a classroom prototype. It does not connect to government databases, make legal decisions, or contact vehicle owners.

## Target Users

- A traffic reviewer checking camera footage
- Students demonstrating a computer vision application
- Anyone testing a small traffic-monitoring prototype

## High-Level Features

1. Real-time camera feed with annotated detections
2. Demo mode for evaluation without camera hardware
3. No-helmet, triple-riding, and red-light violation detection
4. Number-plate OCR with a deterministic fallback format
5. Evidence snapshots and generated PDF e-challans
6. CSV-backed dashboard statistics and downloadable records