# Automated E-Commerce Price Monitor & System Analytics Engine
A production-grade, highly resilient backend utility architecture written in Python. This system features an automated tracking simulator that generates high-volume transaction logs under volatile network conditions, paired with an optimized, high-performance analytics processor to parse and analyze market metrics.

## Architecture Overview
The system is structurally isolated into two distinct, decoupled pipelines to ensure clean separation of concerns:

1. **The Ingestion Pipeline (`monitor.py`):** Simulates an active web scraper fetching live pricing metrics for targeted product identifiers. To mimic real-world distributed infrastructure, it implements robust error-handling mechanisms that safely intercept and log network faults (e.g., HTTP timeouts, server disconnects) without risking a systemic runtime crash.
2. **The Analytics Processor (`analyzer.py`):** A high-performance parsing engine that processes raw unstructured logs. By utilizing optimized Regular Expressions (`regex`) and dynamic Hash Maps, it aggregates and structures time-series financial statistics seamlessly.

## Technical Design & Algorithmic Complexity
### Time Complexity: $O(N)$
The analytics engine reads the system logs sequentially in a single pass. For a log file containing $N$ rows, the time complexity is strictly linear, $O(N)$. Lookups, structural insertion, and value updates inside the product metric dictionary operate at a constant time complexity of $O(1)$ due to the underlying Hash Map data structure.

### Space Complexity: $O(U)$
The space complexity scales strictly with the number of unique tracking units ($U$) mapped in memory, rather than the total size of the log file $N$. This ensures an incredibly low memory footprint even when parsing millions of records.

### Cross-Platform Data Integrity
The application explicitly enforces global **UTF-8 compliance** during file operations (`encoding="utf-8"`). This safeguards the data pipeline against environment-specific character mapping limitations across varying operating systems (e.g., Windows CP1252 codec constraints).

## Project Structure

text
PriceMonitor/
│
├── monitor.py          # Data ingestion simulator & system logger
├── analyzer.py         # O(N) log parser & analytics aggregator
├── tracking_logs.txt   # Unstructured log file output (Generated)
└── Market_Report.md    # Compiled markdown performance report (Generated)
