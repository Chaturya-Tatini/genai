# genai - Copilot Test Documentation

## Overview

This repository contains the script `copilot_test.py`, which was generated and refined with the help of GitHub Copilot. This README documents the experience of using Copilot, details of any modifications made to the script, how the script was tested, and instructions for running it.

---

## Copilot Experience

### 1. Code Generation

- **Initial Prompt:** I asked Copilot to create a Python script that prints the system uptime for different operating systems.
- **Generated Code:** Copilot produced a script that:
    - Uses the `platform` module to detect the OS.
    - For Windows, uses `net stats srv` to get uptime and parses the output.
    - For Linux and macOS (Darwin), uses the `uptime` command.
    - Handles exceptions and unsupported operating systems.

### 2. Modifications

- **Review:** The generated code was clear and concise.
- **Changes:** No major modifications were needed. I reviewed the error handling to ensure it prints useful messages in case of command failure.
- **Why:** The script already covered the required functionality for Windows, Linux, and macOS.

### 3. Testing

- **Environment:** I tested the script on both Linux and Windows environments.
- **How:**
    - Ran the script directly with `python copilot_test.py`.
    - Verified that the correct command is executed for each OS.
    - Checked that the output matches expected uptime formats.
    - Tested error handling by temporarily renaming the `uptime` command to simulate failure (Linux).
- **Results:** The script correctly detected the OS and printed the uptime or an error message accordingly.

---

## How to Run the Script

1. **Requirements**
    - Python 3.x
    - No additional libraries required (uses standard library).

2. **Steps**

    ```bash
    # Clone the repository or download copilot_test.py
    git clone https://github.com/Chaturya-Tatini/genai.git
    cd genai

    # Run the script
    python copilot_test.py
    ```

    - On **Windows**: The script uses `net stats srv` (may require admin privileges).
    - On **Linux/macOS**: The script uses the `uptime` command.

---

## Submission

- **GitHub repository link:** [https://github.com/Chaturya-Tatini/genai](https://github.com/Chaturya-Tatini/genai)
- **Included files:**
    - `copilot_test.py`
    - `README.md`

---
