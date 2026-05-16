# PythonDataCleaningUtility
A Python based text processing utility designed to automate data cleaning, standardize formatting, and eliminate duplicate records.

# Core Functional Features
* **Data Deduplication:** Tracks unique identification criteria across streams to isolate and remove redundant entries.
* **Text Standardization:** Neutralizes erratic spacing anomalies and forces systematic title capitalization (e.g., transforming `jOhN` into `John`).
* **Format Normalization:** Enforces case-insensitive constraints across email records to maintain dataset integrity.
* **File I/O Operations:** Dynamically handles streaming data from raw text inputs and maps structured records into isolated output environments.

# Architectural Concepts Learned
* **Stream & File Management:** Implementation of contextual file mapping using Python's primitive `with open()` protocols.
* **String Parsing Optimization:** Processing unstructured string schemas using native tokenization (`.split()`) and sanitization methods (`.strip()`, `.capitalize()`).
* **Linear Filtering Logic:** Utilizing conditional execution branches and transient data structures (lists) to handle real-time duplicate control.

# Execution Guide
To run this utility locally, ensure your working directory contains both `Cleaner.py` and the target dataset `dirty_data.txt`, then execute:

```bash
python Cleaner.py
