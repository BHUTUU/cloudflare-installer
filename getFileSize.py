from __future__ import print_function
import sys,os
from sys import getsizeof
import requests, time, re
# # number of bytes in a megabyte
# MBFACTOR = float(1 << 20)
# # response = requests.head(sys.argv[1], allow_redirects=True)
# def getsize():
#     response = requests.head("https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe", allow_redirects=True)
#     size = int(response.headers.get('content-length', 0))
#     return size/MBFACTOR
# def download():
#     response = requests.get("https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe0", allow_redirects=True)

# def addDownloader(url, filename):
#     req = requests.get(url, stream=True)
#     if req.headers['Content-Length']:
#         total_size = int(req.headers['Content-Length'])
#         print(total_size)
#     else:
#         total_size = None
  
#     if 'Content-Disposition' in req.headers.keys():
#         fname = re.findall("filename=(.+)", req.headers["Content-Disposition"])[0]
#     else:
#         fname = url.split("/")[-1]
#     with open(fname, 'wb') as fileobj:
#         for chunk in req.iter_content(chunk_size=1024):
#             if chunk:
#                 fileobj.write(chunk)
#                 current_size = int(os.path.getsize(filename))
#                 percentg = round((current_size / total_size)*100)
#                 print(percentg)
# addDownloader("https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe", "Git-2.40.0-64-bit.exe")

def addDownloader(url, filename, oldPercentage, limitPercentage, message):
    percentageDifference = limitPercentage - oldPercentage
    percentIncreament = float(percentageDifference / 100)
    percentRecord = 0
    req = requests.get(url, stream=True)
    if req.headers['Content-Length']:
        total_size = int(req.headers['Content-Length'])
        print(total_size)
    else:
        total_size = None
    if 'Content-Disposition' in req.headers.keys():
        fname = re.findall("filename=(.+)", req.headers["Content-Disposition"])[0]
    else:
        fname = url.split("/")[-1]
    with open(fname, 'wb') as fileobj:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                fileobj.write(chunk)
                current_size = int(os.path.getsize(filename))
                percentg = round((current_size / total_size)*100)
                if percentg > percentRecord:
                    oldPercentage+=percentIncreament
                    print(round(oldPercentage), message)
                    percentRecord=percentg

addDownloader("https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe","Git-2.40.0-64-bit.exe", 20, 50, "downloadind github")