# smartathon hackathon - Road Blazer team submission 
This is a test program that enables testing of the model developef by Road Balzer the for smartathon hackathon theme1, 
Theme 1 is regarding the detection and evaluation of visual pollution elements on street imagery taken from a moving vehicle

## Usage
python .\runmodel.py --imagepath 0a4f38c94dd63cd8e5b9209dc9892146.jpg
-- imagepath: Path of image to be tested using the model

## Prerequisites
Python 3.8.10
PIP

## Overview
The program uses the model developed by roadblzer team as an input, and an image 
input:
1- model developed by roadblzer team as an input
2- Image given by the user containing visaul pollution elements 
output: 
1- Visual polution classes detected in the input image 
2- Resulting image with classes highlighted


## Description
1- Clone yolov7 from GitHub, install yolov7 prerequisites
2- Download our model from s3 bucket 
3- Run the detection
