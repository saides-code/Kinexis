# Kinexis
Kinexis is an ever-expanding collection of software that utilizes the Kinect V1 sensor to create immersive and interactive visual performances. The project aims to explore the potential applications of Kinect technology in the field of art and entertainment. Most of the scripts are based on the OpenNI 2 SDK and were developed and tested using the official Microsoft Kinect v1.8 SDK and drivers. However, if you prefer, you can also use the open-source library [libfreenect](https://github.com/OpenKinect/libfreenect).

### Before you proceed
As a programming novice, I must advise that the codes in this collection are highly experimental and may not be reliable. It is recommended that these codes be used solely for experimentation purposes, and I do not advise their use in a production environment. Please note that these codes are distributed without any warranty, and their use is entirely at your own risk.

## 1. DepthMapper

DepthMapper is a Python script that uses a Kinect sensor to generate a real-time grayscale depth map.

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
- Customizable colors, depth range and post-processing

## 2. DepthCap

DepthCap is a Python script based on DepthMapper. The script opens the depth and color streams from the Kinect sensor and displays a preview with a color mapped depth overlayed on top of the color stream. The user can adjust the minimum and maximum depth values to display using trackbars. The script also allows the user to save the depth channel and color channel as TIFF files that are sized at 1280x960 pixels.

## Get started

### Install the necessary SDKs
- [Kinect for Windows SDK v1.8](https://www.microsoft.com/en-us/download/details.aspx?id=40278)
- [OpenNI 2 SDK](https://structure.io/openni)

### Install the necessary requirements
- With `pip install -r requirements.txt`

## Usage
- Run `depthcap.py`
- `s` key to save the depth channel and color channel as TIFF files in the `out` directory
- `i` key to invert the depth map
- `q` key to quit

## Please take note of
This code is experimental and could be very unreliable.
Other features are still under development:
- AI depth map enhancer (Custom trained CNN based on U-Net)
- Improved GUI

## License
This project is licensed under the [Mozilla Public License Version 2.0](https://github.com/saides-code/Kinexis/blob/main/LICENSE.md). If you use or modify this software, you must attribute the original creator in all copies or substantial portions of the software.