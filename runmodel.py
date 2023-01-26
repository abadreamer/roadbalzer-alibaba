import os;
import sys;
import argparse;
import boto3;
from git import Repo; 
sys.path.append('./yolov7');
from yolov7 import detect;
from yolov7 import detectfn;


#check if yolov7 folder exists
def roadBalzerDetect(roadImagePath):
    yolov7FolderPath = './yolov7'
    if (os.path.exists(yolov7FolderPath)):
        print('yolov7 is installed');
    else:
        print('yolov7 is not installed')
        return -1;


    #check if model file exists
    s3_bucket_name = 'smartathon-submission'
    s3_model_path = 'model-v3/best3.pt'
    modelPath = './model3_roadblazer'
    isModelExists = os.path.isfile(modelPath)

    if (isModelExists):
        print('skip model "model3_roadblazer" download as it already exists');
    else:
        #init s3 server  
        print('Downloading roadblazer model from S3 ...')
        s3 = boto3.client('s3');
        # create an empty file and download the model to it 
        print('Downloading roadblazer model from S3 ...')
        with open('./model3_roadblazer', 'wb') as modelFile:
            s3.download_fileobj(s3_bucket_name, s3_model_path, modelFile);
        print(' roadblazer model downloaded successfully')

    runDetectwithOSCmd = False;

    if not runDetectwithOSCmd:
        detectfn.detectMain(source=roadImagePath, weights=modelPath, conf=0.25, imgsz=640, save_txt=True, classes=None);
    else:
        # python './yolov7/detect.py' --weights './best3.pt' --conf 0.25 --img-size 640 --source .\0a4f38c94dd63cd8e5b9209dc9892146.jpg
        detectCommand = "python .\yolov7\detect.py  --weights {weights1} --conf {conf} --img-size {imgsz} --save-txt --source {source} ";
        detectCommand = detectCommand.format(weights1=modelPath, conf=0.25, imgsz=640, source=roadImagePath);
        print(detectCommand);
        os.system(detectCommand);
    
    return 0;

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This program is to test the ML model developed by roadblazer team');
    parser.add_argument('--imagepath', default='0a4f38c94dd63cd8e5b9209dc9892146.jpg', type=str, help='Path of image to be used')
    args = parser.parse_args()
    if (os.path.isfile(args.imagepath) == False ):
        print("The given image path is not accessible");
        exit();
    roadBalzerDetect(args.imagepath)
