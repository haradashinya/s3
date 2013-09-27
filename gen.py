import os
import sys
def write():
    """
    setup your config.json
    """
    if os.path.exists("foo.json"):
        print("""this data is already exists, can't replace it. please remove it
              if you do so""")
        sys.exit()
    with open("foo.json","w") as f:
        if data != "":
            print("this data is already exists")
        body = """
{
"AWS_ACCESS_KEY":"your access key",
"AWS_SECRET_KEY":"your secret key",
"BUCKET_NAME": "your bucket name"
}
        """.strip()
        f.write(body)

if __name__ == "__main__":
    write()
    print("done")
