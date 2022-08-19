#!/usr/bin/env python3
import pickle

f= open("/home/zj/_github_/folder_proj/mmaction2/data/posec3d/ntu60_xsub_val.pkl",mode="rb")
content =pickle.load(f)
print(content[0])
f.close()

