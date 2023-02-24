# Kinexis
A set of software for visual performances that utilizes the Kinect V1 sensor to create immersive and interactive experiences.

## 1. DepthMapper

DepthMapper is a Python script that uses a Kinect sensor to generate a grayscale depth map in real-time. The script can leverages NVIDIA CUDA GPU acceleration to improve performance, and can be run on Windows or Linux.

## Get started

### Install the appropriate drivers for your system
- [Microsoft drivers](https://www.microsoft.com/en-us/download/details.aspx?id=44561) (Windows)
- [OpenKinect drivers](https://github.com/OpenKinect/libfreenect) (Linux)

### Install the necessary requirements
- With `pip install -r requirements.txt`

## Usage
- Run the `depthmapper.py` script to use the CPU version.
- Run the `depthmapper_cuda.py` script to use the experimental CUDA version (requires an NVIDIA GPU).

## License
This project is licensed under the 
