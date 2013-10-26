#coding: utf-8
import sys
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.cloudfront import CloudFrontConnection
import boto
import StringIO
import mimetypes
import json
import multiprocessing
import Queue
from boto.cloudfront.origin import S3Origin
boto.set_stream_logger('boto')
CONN = None
BUCKET = None


class G:
    pass

def setup():
    """
    config.jsonから読み込んでAWSに接続する。
    """
    with open("config.json","r") as f:
        config = json.load(f)
        AWS_ACCESS_KEY = config["AWS_ACCESS_KEY"]
        AWS_SECRET_KEY = config["AWS_SECRET_KEY"]
        BUCKET_NAME = config["BUCKET_NAME"]

        G.conn = S3Connection(
            aws_access_key_id = AWS_ACCESS_KEY,
            aws_secret_access_key= AWS_SECRET_KEY)
        G.bucket = G.conn.get_bucket(BUCKET_NAME)

def get_ctype(f):
    return mimetypes.guess_type(f)[0] or "application/x-octet-stream"

def put(filename):
    new_key = Key(G.bucket)
    new_key.key = filename
    new_key.set_metadata("Content-Type",get_ctype(filename))
    new_key.set_contents_from_filename(filename)


def clone(filename):
    key = G.bucket.get_key(filename)
    key.get_contents_to_filename(filename)

def delete(filename):
    G.bucket.delete_key(filename)


def show():
    buckets = G.bucket.list()
    for bucket in buckets:
        msg = """
        name: {0},
        size: {1},
        last_modified: {2},
        """.format(bucket.name,bucket.size,bucket.last_modified)
        print(msg)



def is_valid(cmd):
    valid_cmds = ["put","clone","show","delete"]
    if cmd in valid_cmds:
        return True

    print("valid cmd is {0}",(",").join(valid_cmds))
    return False



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("some")
    else:
        setup()
        if sys.argv[1] == "show":
            show()
            sys.exit()
        try:
            cmd = sys.argv[1]


            if is_valid(cmd):
                filename = sys.argv[2]
        except:
            print("doesn't exist")
            print("""
                  usage
                  python s3.py {put|clone|delete} "filename"
                  """)
            sys.exit()
        else:

            if cmd == "put":
                print("hello put")
                put(filename)
                print("done")
            elif cmd == "clone":
                print('hello clone')
                clone(filename)
                print("done")

