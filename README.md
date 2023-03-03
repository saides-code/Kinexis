# Kinexis
Kinexis is a collection of software that utilizes the Kinect V1 sensor to create immersive and interactive visual performances. The project aims to explore the potential applications of Kinect technology in the field of art and entertainment. The current version of the collection includes a Python script called DepthMapper, which generates real-time grayscale depth maps using the Kinect sensor. The script is based on the OpenNI 2 SDK and can be used for experimentation purposes.

### Before you proceed
As a programming novice, I must advise that the codes in this collection are highly experimental and may not be reliable. It is recommended that these codes be used solely for experimentation purposes, and I do not advise their use in a production environment. Please note that these codes are distributed without any warranty, and their use is entirely at your own risk.

## 1. DepthMapper

DepthMapper is a Python script that uses a Kinect sensor to generate a real-time grayscale depth map. The script is based on the OpenNI 2 SDK. You can use the [libfreenect](https://github.com/OpenKinect/libfreenect) open source drivers instead of the Microsoft drivers if you wish.

## Get started

### Install the necessary SDKs
- [Kinect for Windows SDK v1.8](https://www.microsoft.com/en-us/download/details.aspx?id=40278)
- [OpenNI 2 SDK](https://structure.io/openni)

### Install the necessary requirements
- With `pip install -r requirements.txt`

## Usage
- Run `depthmapper.py`

## Please take note of
This code is experimental and could be very unreliable.
Other features are still under development:
- GPU / CUDA acceleration
- Native integration of open source drivers
- Customizable colors, depth range and post-processing
- An easy to use launcher for each scrpit with update functionality

## License
This project is licensed under the 
