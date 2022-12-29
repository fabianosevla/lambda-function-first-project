import boto3
import json

s3 = boto3.resource('s3')

def lambda_handler (event, context):
 bucket_de_input = s3.Bucket('bucket-input-dados')
 bucket_de_output =s3.Bucket('bucket-output-dados')

 print(bucket_de_output)
 print(bucket_de_input)
 
 for obj in bucket_de_input.objects.filter(Prefix='images/',Delimiter='/'):
  dest_key=obj.key
  print(dest_key)
  print('copy file ' + dest_key)
  s3.Object(bucket_de_output.name, dest_key).copy_from(CopySource= {'Bucket': obj.bucket_name, 'Key': obj.key})
  print('delete file from bucket de input ' + dest_key)
  s3.Object(bucket_de_input.name, obj.key).delete()
