# hal_server

## Table of Contents

- [DCC Instance Detector](#dcc-instance-detector)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Example](#Example)
- [License](#license)

## DCC Instance Detector

This project provides functionality to detect and list running instances of various Digital Content Creation (DCC) software. The supported DCC tools are:

- **Maya**
- **Houdini**
- **Unreal Engine**
- **Blender**

## Features

- Detects running instances of Maya, Houdini, Unreal Engine, and Blender.
- Lists the Process IDs (PIDs) and names of running instances.
- Easy integration for detecting instances on a local machine.

## Requirements

- Python 3.x
- `subprocess` module (standard in Python)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/DCCInstanceDetector.git
   ```

## Example
```python


from InstanceDetector import DCCInstanceDetector

detector = DCCInstanceDetector()

# Detect instances for each DCC tool
detector.detect_maya_instances()
detector.detect_houdini_instances()
detector.detect_unreal_instances()
detector.detect_blender_instances()

# Print Maya instances
print("Maya Instances:")
for pid, name in detector.maya_instances:
    print(f"PID: {pid}, Name: {name}")

# Print Houdini instances
print("\nHoudini Instances:")
for pid, name in detector.houdini_instances:
    print(f"PID: {pid}, Name: {name}")

# Print Unreal instances
print("\nUnreal Instances:")
for pid, name in detector.unreal_instances:
    print(f"PID: {pid}, Name: {name}")

# Print Blender instances
print("\nBlender Instances:")
for pid, name in detector.blender_instances:
    print(f"PID: {pid}, Name: {name}")
```
Rez command to use it :

```bash
rez env hal_server -- echoInstances
```


## License
```text
Custom License Agreement

Copyright (c) 2024 Felix Benicourt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to use,
study, and modify the Software for personal, educational, or internal purposes,
subject to the following conditions:

1. Redistribution and Resale:
   - Redistribution, sublicensing, or resale of the Software, in whole or in part, 
     is strictly prohibited without prior written consent from the author.

2. Attribution:
   - This copyright notice and permission notice shall be included in all copies 
     or substantial portions of the Software.

3. No Warranty:
   - THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
     FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL 
     THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER 
     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING 
     FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
     IN THE SOFTWARE.
```





