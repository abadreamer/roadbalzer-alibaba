import os;
import oss2;

endpoint = 'oss-me-central-1.aliyuncs.com';
bucket_name = 'roadbalzer-images';

def uploadImage(roadImagePath):
    access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID',)
    access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET',)
    # print('keys values:', access_key_id, access_key_secret);
    auth = oss2.Auth(access_key_id, access_key_secret);
    # print('after authentiate', );
    bucket = oss2.Bucket(auth, endpoint, bucket_name);
    # print('after access buket', );
    bucketPath = 'upload/{}'.format(roadImagePath);
    result = bucket.put_object_from_file(bucketPath, roadImagePath)
    print(result);


def downloadImage(roadImagePath):
    access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID',)
    access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET',)
    # print('keys values:', access_key_id, access_key_secret);
    auth = oss2.Auth(access_key_id, access_key_secret);
    # print('after authentiate', );
    bucket = oss2.Bucket(auth, endpoint, bucket_name);
    # print('after access buket', );
    bucketPath = 'upload/{}'.format(roadImagePath);
    # print(buketPath);
    result = bucket.get_object_to_file(bucketPath, roadImagePath);
    # print(result);
