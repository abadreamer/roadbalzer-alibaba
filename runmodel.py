import os;
import sys;
import argparse;
import ossutils;
import csv;

sys.path.append('./yolov7');
from yolov7 import detect;
from yolov7 import detectfn;

pollutionClasses = ['Graffiti', 'Faded Signage', 'Potholes', 'Garbage', 
                    'Construction Road', 'Broken Signage', 'Bad Billboard',
                    'Sand on Road', 'Clutter sidewalk', 'Unkept Facade'];

# def uploadImage(roadImagePath):
#     endpoint = 'oss-me-central-1.aliyuncs.com';
#     access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID',)
#     access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET',)
#     # print('keys values:', access_key_id, access_key_secret);
#     auth = oss2.Auth(access_key_id, access_key_secret);
#     # print('after authentiate', );
#     bucket = oss2.Bucket(auth, endpoint, 'roadbalzer-images');
#     # print('after access buket', );
#     buketPath = 'upload/{}'.format(roadImagePath);
#     result = bucket.put_object_from_file(buketPath, roadImagePath)
#     print(result);


# def downloadImage(roadImagePath):
#     endpoint = 'oss-me-central-1.aliyuncs.com';
#     access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID',)
#     access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET',)
#     # print('keys values:', access_key_id, access_key_secret);
#     auth = oss2.Auth(access_key_id, access_key_secret);
#   exit  # print('after authentiate', );
#     bucket = oss2.Bucket(auth, endpoint, 'roadbalzer-images');
#     # print('after access buket', );
#     buketPath = 'upload/{}'.format(roadImagePath);
#     # print(buketPath);
#     # imgObj = bucket.get_object(buketPath);
#     # content_got = b''
#     # for chunk in imgObj:
#     #     content_got += chunk
#     result = bucket.get_object_to_file(buketPath, roadImagePath);
#     # print(result);

def parseLabels(detectPath, imageFileName):
    labelsFileName = imageFileName[0:imageFileName.rindex('.')]+'.txt';
    labelsFilePath = os.path.join(detectPath, 'exp', 'labels', labelsFileName);
    # detectionLabel =' ';
    detectionLabels ='';
    detectedClasses = [];
    if (os.path.isfile(labelsFilePath) == True ):
        with open(labelsFilePath, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar=' ')
            detectionLabels = 'Image have following Visual Pollution Classes: '
            for row in spamreader:
                # detectionLabels = detectionLabels + detectionLabel.format(pollutionClasses[int(row[0])]);
                detectionLabels = detectionLabels + pollutionClasses[int(row[0])] + "\n";
                detectedClasses.append(pollutionClasses[int(row[0])]);
    return detectedClasses;
    
def roadBalzerDetect(roadImagePath, imageFileName):
    #check if yolov7 folder exists
    yolov7FolderPath = './yolov7'
    if (os.path.exists(yolov7FolderPath)):
        print('yolov7 is accessible');
    else:
        print('yolov7 is not accessible')
        return -1;


    #check if model file exists
    # oss-me-central-1.aliyuncs.com
    modelPath = './model3_roadblazer'
    isModelExists = os.path.isfile(modelPath)

    if (isModelExists):
        # print('skip model "model3_roadblazer" download as it already exists');
        pass
    else:
        print('model is not accessible')
        return -1;
    
    useDetectFn = True;
    detectPath = 'detectOutput/'

    if useDetectFn:
        print('starting detect')
        detectfn.detectMain(source=roadImagePath, weights=modelPath, conf=0.25, imgsz=640, 
                             save_txt=True, classes=None, exist_ok=True, project=detectPath);
        outputImage = os.path.join(detectPath, 'exp', imageFileName);
        if (os.path.isfile(outputImage) == True ):
            print("detect succeeded: ", outputImage);
            ossutils.uploadImage(outputImage);
            return parseLabels(detectPath, imageFileName);
        else:
            print("detect failed or detected image is not accessible");
    else:
        # python './yolov7/detect.py' --weights './best3.pt' --conf 0.25 --img-size 640 --source .\0a4f38c94dd63cd8e5b9209dc9892146.jpg
        detectCommand = "python ./yolov7/detect.py  --weights {weights1} --conf {conf} --img-size {imgsz} --save-txt --source {source} ";
        detectCommand = detectCommand.format(weights1=modelPath, conf=0.25, imgsz=640, source=roadImagePath);
        print(detectCommand);
        os.system(detectCommand);
    return '';

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This program is to test the ML model developed by roadblazer team');
    parser.add_argument('--imagepath', default='0a4f38c94dd63cd8e5b9209dc9892146.jpg', type=str, help='Path of image to be used')
    args = parser.parse_args()
    if (os.path.isfile(args.imagepath) == False ):
        print("The given image path is not accessible");
        exit();
    # roadBalzerDetect(args.imagepath)
    downloadImage(args.imagepath);
