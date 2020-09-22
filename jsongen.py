import json
import os
import argparse

filedict = {}

def jsongen(dir, filename, url):
    files = os.listdir(dir)
    global filedict
    for file in files:
        if os.path.isdir(os.path.join(dir, file)):
            # we are only adding the directory to the basedir and the url
            # so we just need to add this to variable and call the recursion
            jsongen(os.path.join(dir, file), filename, url + file + "/")
            continue
        filedict[file] = url + file
    jsonv = json.dumps(filedict, indent=True)
    print(jsonv)
    with open(args.filename, "w") as f:
        f.write(jsonv)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Images link retrieval from Website")
    parser.add_argument("url", type=str, help="This is the link before the images")
    parser.add_argument("dir", type=str, help="This is the directory of the images")
    parser.add_argument("filename", type=str, help="Output filename. pls add .json ext at the end")
    args = parser.parse_args()
    jsongen(args.dir, args.filename, args.url)
