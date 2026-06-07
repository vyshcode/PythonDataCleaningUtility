# Python Data Cleaning Utility

A Python-based text processing utility designed to automate data cleaning, standardize formatting, and eliminate duplicate records with production-grade efficiency and error handling.

## Core Functional Features
* **Lightning-Fast Deduplication:** Utilizes high-performance hashing structures to isolate and remove redundant entries across high-volume streams instantly.
* **Fault-Tolerant Error Handling:** Gracefully catches malformed or corrupted lines (such as missing separation boundaries) without interrupting the stream execution.
* **Text Standardization:** Neutralizes erratic spacing anomalies, strips trailing tabs, and forces systematic title capitalization across multi-word fields (e.g., transforming `jOhN dOe` into `John Doe`).
* **Format Normalization:** Enforces case-insensitive constraints across email data structures to maintain strict relational dataset integrity.
* **Memory-Efficient I/O:** Safely handles incoming raw data line-by-line, minimizing memory consumption for large file sets before outputting structured data.

## Architectural Concepts Applied
* **Contextual File Streaming:** Simultaneous management of read/write file streams using a unified, safe Python `with open()` block.
* **O(1) Lookup Optimization:** Replacing linear list lookups with hash set collections (`set()`) for near-instantaneous duplication tracking.
* **Exception Handling Patterns:** Implementation of isolated `try/except` safety blocks to handle structural mutations and `ValueError` occurrences gracefully.
* **Real-time Stream Tracking:** Leveraging `enumerate()` counters to supply precise line-by-line diagnostics and human-readable feedback during processing.

## Execution Guide

### 1. Project Structure
Ensure your project files are organized inside your workspace directory like this:
```text
PythonDataCleaningUtility/
│
├── Cleaner.py
├── dirty_data.txt
└── README.md
```
### 2. Local Execution
Ensure your terminal is navigated inside the project folder, then execute the script:

```bash
python Cleaner.py