# Smartathon Hackathon - RoadBalzer team submission 
This test program enables the trying of the ML Model developed by RoadBalzer team for smartathon hackathon theme1. 
Theme 1 concerns detecting and evaluating visual pollution elements on street imagery taken from a moving vehicle.

## Usage
python .\runmodel.py --imagepath 0a4f38c94dd63cd8e5b9209dc9892146.jpg

-- imagepath: Path of the image to be tried using the model

## Prerequisites
* Python 3.8.10
* PIP

## Overview
The program uses the model developed by RoadBalzer  team as an input and an image 
Input:

1. ML Model developed by RoadBalzer team 
2. Image containing visual pollution elements (user input)

Output: 
1. Visual pollution classes detected in the input image 
2. Resulting image with classes highlighted


## Description of the code
1. Clone yolov7 from GitHub, install yolov7 prerequisites
2. Download our model from S3 bucket 
3. Run the detection
