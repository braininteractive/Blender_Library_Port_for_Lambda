try:
 import bpy
except ImportError:
 from bpy_lambda import bpy
import bpy_lambda
import sys
import math
import json
import os, zipfile
import boto3
import botocore
import urllib.parse
from botocore.client import Config
import s3transfer
import base64
import time
from PIL import Image


s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
s31 = boto3.client('s3', config=Config(signature_version='s3v4'))

//Test Code For Lambda Libraries

def lambda_handler(event, context):
    blender=bpy._version_;
    
	return {"Blender Version": blender  }

if __name__ == "__main__":
	lambda_handler(42, 42)

