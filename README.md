# Project Title
A native and browser interface for Stable Diffusion based on Flutter (with flet). The goal of this project is to have a Stable Interface interface running on all platforms fully written in Python, making the developments of plugins easier than on a classic HTML WebUI or with native OS code.


## Appendix

The project currently runs on stable_diffusion.openvino instead of the classic Stable Diffusion library making us able to use the CPU instead of the GPU so the project can run on any computer during the development phase.

## Installation

#### Requirements
Python <= 3.9.0

#### Setup
```bash
   python -m pip install --upgrade pip
   pip install openvino-dev[onnx,pytorch]==2022.3.0
   pip install -r requirements.txt
```


    
## Usage/Examples

```bash
cd scripts/
python counter.py
```

