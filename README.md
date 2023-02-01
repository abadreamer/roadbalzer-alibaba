# Alibab SA Hackathon - RoadBalzer team submission - Government Applications Theme


## Overview
The app helps municipalities to automatically detect visual pollution elements in street images.

## RoadBalzer team was able to utilize Alibaba cloud to deploy:
* Simple Web Interface that enables employees to upload street images
* ML Model: Model inference, detects visual pollution elements in given images,
* API and Backend code: Exposes backend API that interacts with (web interface, ML model, Object Storage and DB)
* DB: Stores the results of detection and enable it for further dashbaords and processing.
* Object storage: Stores the input images and output (with detected visual pollution)to enable fast retrieve.
* Dashboards: Gives an overview of the current state of detected visual pollution.

## Roadblazer team work:
* Develop ML model to detect visual pollution using a dataset published by SDAIA
* Integrate the model with Python web application to enable automatic detection
* Deploy the model on Alibaba cloud utilizing the following components:
1. ECS: Deploy ML model, deploy python application
2. OSS: Store images before and after processing
3. Absara PostgreSQL: Stores the detection results
4. VPC: Virtual Private Cloud NW to connect the application elements
5. API Gateway
6. Load balancer


## Usage
. initenv.sh

nohup flask --app apiroutes run --host=0.0.0.0 &

## Prerequisites
* Python 3.8.10
* PIP
* Flask
* postgresql driver


## Code modules
1. HTML Templates: Web HTML templates that enables user to interact with the application
2. APIs: Flask application that exposes application functionality as APIs 
3. Detection Module: Image Inference using the developed ML model
4. OSS Utilities: set of utilities that wraps OSS handling for upload and download of imaes

##Screenshots

![Main screen](https://user-images.githubusercontent.com/26005843/216072098-669cc35d-bc8f-4ba0-82db-18f8ecf22d6b.png)
![Result screen](https://user-images.githubusercontent.com/26005843/216072374-cbd49219-f837-4acc-b1ac-b87e7bea6ebf.png)
![Sample Inference 1](https://user-images.githubusercontent.com/26005843/216073049-b896be91-45c1-466f-9bc0-9786e4817cef.jpg)
![Sample Inference 2](https://user-images.githubusercontent.com/26005843/216073169-5a825bfc-04b9-4b2a-89ba-b152a6ab3ee9.jpg)




