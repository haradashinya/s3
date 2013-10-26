import os
import sys

aws_access  = os.environ.get("AWS_ACCESS_KEY").strip()
aws_secret = os.environ.get("AWS_SECRET_KEY").strip()
def write():

    print(aws_secret)
    data = ""
    """
    setup your config.json
    """
    if os.path.exists("config.json"):
        print("""this data is already exists, can't replace it. please remove it
              if you do so""")
        sys.exit()
    with open("config.json","w") as f:
        if data != "":
            print("this data is already exists")
        body = """
{"AWS_ACCESS_KEY":"%s",
"AWS_SECRET_KEY":"%s",
"BUCKET_NAME": "your bucket name" }
        """ % (aws_access,aws_secret)
        print(body) # f.write(body)
        f.write(body)

if __name__ == "__main__":
    write()
    print("done")
