
# Python Server Monitor

## Overview

Python Server Monitor is a command-line application that simulates server monitoring by classifying user-provided statuses without connecting to live servers.

Users provide a server status through the command line, and the application returns the corresponding health label: `Healthy`, `Down`, or `Unknown`.

This project demonstrates how Python can be used in DevOps automation to process server statuses, handle command-line inputs, and classify operational states.

## Usage 

To run the application, open the terminal and execute the Python script with a server status argument.

Example command:

```bash
python main.py running
```

Expected output:

```text
Healthy
```
