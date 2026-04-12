# Python-OS-Performance-Simulator
A formal IT consulting report recommending Windows Server and A Python simulator using psutil to demonstrate OS concepts like CPU scheduling, memory management, threading, and disk allocation live on your machine.


## CS 510 - Operating System Principles

**6-1 Project One:** A formal IT consulting report recommending Windows Server 2025 for a fictional fintech client

**9-1 Project Two:** A live system monitor built in Python that surfaces CPU, memory, disk, and threading activity from your own machine

---

## Course Overview

This repository contains both projects from CS-510 Operating System Principles, completed as part of the M.S. Computer Science program. Together they form a **two-part case study** for a fictional enterprise client, **GlobalFinTech Inc.** A financial technology company evaluating OS infrastructure for a secure cloud environment.

The consulting firm, **TechSecure Solutions**, first delivers a formal OS recommendation report, then follows it with a working Python simulator that demonstrates the performance concepts evaluated in the report.

> **Student:** Amber (Ember) Foster  
> **Instructor:** Brian Enochson  
> **Term:** Spring 2026

---

## Repository Structure

```
cs510-os-principles/
│
├── README.md                          ← You are here
│
├── project-one/
│   ├── README.md                      ← Project One overview
│   └── CS-510_Project_One             ← Full OS recommendation report (APA cited)
│
└── project-two/
    ├── README.md                      ← Project Two overview
    ├── CS-510_Project_Two.py          ← Python OS performance simulator
    ├── 9-1_Project_Two.pdf            ← Full documentation report (APA cited)
    ├── projecttwo.txt                 ← Sample file for disk statistics demo
    └── Terminal_Screenshot.png        ← Live terminal output
```

---

## Projects

### [Project One - OS Recommendation Report](./project-one/)
**OS Evaluated:** Microsoft Windows Server 2025  
**Format:** 5-7 page formal recommendation report

A structured IT consulting report evaluating Windows Server 2025 across nine criteria: security mechanisms, stability, integrity/confidentiality/availability, architecture, resource management, failure metrics, distributed environment capabilities, key performance metrics, and overall appropriateness for a regulated financial services environment.

**Recommendation:** Windows Server 2025 Datacenter Edition *Approved for adoption*

---

### [Project Two - Python OS Performance Simulator](./project-two/)
**Language:** Python 3 · **Library:** psutil  
**Format:** Working application + technical documentation

A Python based simulator that provides real time visibility into the same OS performance categories analyzed in Project One and disk allocation, CPU scheduling, memory management, concurrency, and error handling and serving as a proof of concept for GlobalFinTech's IT team.

```bash
pip install psutil
python CS_510_Project_Two.py
```

---

## How the Projects Connect

| Project One (Report)                | → | Project Two (Code)                                  |
|-------------------------------------|---|-----------------------------------------------------|
| Security & integrity analysis       | → | Error handling & exception trapping                 |
| CPU scheduling & process management | → | `getCpuStatistics()` per-core usage, process table  |
| Virtual memory & paging             | → | `getMemoryStatistics()` RAM + swap                  |
| File system & storage allocation    | → | `getFileDiskUsageStatistics()` disk + file metadata |
| Concurrency & thread management     | → | `showThreadingExample()` dual thread demo           |

---

## Running the Simulator

**Requirements:**
```bash
pip install psutil
```

**Run:**
```bash
python CS_510_Project_Two.py
```

**Expected Output:**
```
Starting Program
=============================
Getting Disk Statistics
Total Disk Space: 926.35 GB
Used Disk Space:  11.43 GB
Free Disk Space:  822.36 GB

File Information:
  File Name:   ./projecttwo.txt
  File Size:   46 bytes
  ...

Getting CPU Statistics
Logical CPU Count:  10
Physical CPU Count: 10
CPU Usage Per Core:
  Core 0: 22.2%
  ...

Getting Memory Statistics
Physical Memory:
  Total:     24.00 GB
  Used:      11.16 GB
  ...

Demonstrating Threading
Starting Thread 1...
Thread 1 cubed: 27
Starting Thread 2...
Thread 2 squared: 16
Done With Threading!

Demonstrating Error Handling
Attempting division by zero...
You can't divide by zero!
Execution complete.

Program Complete.
```

---

## Module Breakdown

### 1. Disk Allocation - `getFileDiskUsageStatistics()`
Uses `psutil.disk_usage()` to query total, used, and free disk space, and `os.stat()` to retrieve file-level metadata including size and timestamps. Mirrors how OS file systems expose hardware storage abstractions to user space applications.

```python
disk = psutil.disk_usage('/')
stats = os.stat(file_name)
```

**OS Concept:** File system metadata management, storage abstraction layer

---

### 2. CPU Statistics - `getCpuStatistics()`
Reports logical and physical core counts, per-core utilization with a 1-second measurement interval, total CPU usage, and a snapshot of the top 5 running processes. Reflects the OS scheduler's process table and context switching behavior.

```python
psutil.cpu_count(logical=True)
psutil.cpu_percent(percpu=True, interval=1)
psutil.process_iter(['pid', 'name', 'cpu_percent'])
```

**OS Concept:** Process scheduling, CPU time-slicing, process state management

---

### 3. Memory Management - `getMemoryStatistics()`
Retrieves both physical RAM statistics and virtual memory (swap) statistics, demonstrating the OS's blending of RAM and secondary storage to present a unified address space to running processes.

```python
mem  = psutil.virtual_memory()
swap = psutil.swap_memory()
```

**OS Concept:** Virtual memory, paging, page frame allocation, swap management

---

### 4. Concurrency & Threading - `showThreadingExample()`
Creates two concurrent threads - one computing a cube, one computing a square, started and joined sequentially. Demonstrates how the OS coordinates multiple execution paths within a single process.

```python
t1 = threading.Thread(target=printMsg1, args=(3,))
t2 = threading.Thread(target=printMsg2, args=(4,))
t1.start(); t2.start()
t1.join();  t2.join()
```

**OS Concept:** Thread lifecycle, concurrency, CPU time multiplexing

---

### 5. Error Handling - `showErrorHandling()`
Intentionally triggers a `ZeroDivisionError` to demonstrate structured exception handling — analogous to how OS kernel exception handlers trap illegal operations and prevent system-wide failure.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Execution complete.")
```

**OS Concept:** Trap handling, exception based process control, system stability

---

## Terminal Output
 
![Terminal screenshot showing full simulator output](Terminal_Screenshot.png)

---

## Documentation Summary

The written documentation addresses the following OS performance topics:

| No | Topic                                                                               |
|----|-------------------------------------------------------------------------------------|
| 1  | Effectiveness of algorithmic optimizations within failure states and prioritization |
| 2  | OS performance metrics used to monitor system efficiency                            |
| 3  | Optimization algorithms for memory management and scheduling                        |
| 4  | Memory management techniques for security and stability                             |
| 5  | Resource allocation strategies to optimize OS performance                           |

Key takeaways from the analysis:

- **Disk management** demonstrates how file systems abstract hardware and expose structured metadata to applications
- **CPU scheduling** via `psutil` mirrors the process tables and context switching logic embedded in Linux and other modern kernels
- **Virtual memory** blends physical RAM with swap to give processes a continuous address space, a fundamental OS illusion
- **Threading** reflects how the OS multiplexes CPU time across concurrent execution paths while maintaining isolation
- **Error handling** parallels kernel level trap handlers that catch illegal operations before they destabilize the system

---

## References

- zyBooks. (2024). *Operating Systems: Principles and Applications* (Modules 1-8).
- Bovet, D. P., & Cesati, M. (2005). *Understanding the Linux Kernel* (3rd ed.). O'Reilly Media.
- Love, R. (2010). *Linux Kernel Development* (3rd ed.). Addison-Wesley Professional.

---

*This project was completed as part of the M.S. Computer Science program (2026). Simulator tested on macOS with a 10-core Apple Silicon processor and 24 GB RAM.*
