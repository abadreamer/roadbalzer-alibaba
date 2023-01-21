import boto3;
import os;
import sys;
from git import Repo; 

#check if yolov7 folder exists
yolov7Git = 'https://github.com/WongKinYiu/yolov7.git'
yolov7FolderPath = './yolov7'
isYolov7Exists = os.path.exists(yolov7FolderPath);
if (isYolov7Exists):
    print('skip "yolov7" download as it already exists');
else:
    print('Downloading yolov7 from github ...')
    Repo.clone_from(yolov7Git, yolov7FolderPath)
    print('installin yolv7 requirements')
    os.system("pip install -r ./yolov7/requirements.txt")

sys.path.append('./yolov7');
from yolov7 import detect;



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
    s3 = boto3.client('s3', aws_access_key_id='AKIASQSBFOHHI5Q7NQ4N',
    aws_secret_access_key= '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');
    # create an empty file and download the model to it 
    print('Downloading roadblazer model from S3 ...')
    with open('./model3_roadblazer', 'wb') as modelFile:
        s3.download_fileobj(s3_bucket_name, s3_model_path, modelFile);
    print(' roadblazer model downloaded successfully')

# road_image_path = '0a4f38c94dd63cd8e5b9209dc9892146.jpg'
road_image_path = input("Please enter image path: ")
# detect.detect(weights=modelPath, conf=0.25, imgsz=640, source=road_image_path);


detectCommand = "python .\yolov7\detect.py  --weights {weights1} --conf {conf} --img-size {imgsz} --source {source}";
detectCommand = detectCommand.format(weights1=modelPath, conf=0.25, imgsz=640, source=road_image_path);
print(detectCommand);

os.system(detectCommand);


# python './yolov7/detect.py' --weights './best3.pt' --conf 0.25 --img-size 640 --source .\0a4f38c94dd63cd8e5b9209dc9892146.jpg
