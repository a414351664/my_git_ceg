import pandas as pd
import jsonlines
import json
import numpy as np
from tqdm import tqdm

source_path = 'valid.src'
predict_path = 'predict_predtrain.txt'
tgt_path = 'valid.tgt'
predict_save = 'pred_pretrain.tsv'
source = []
pred = []
tgt = []
# read saved file
with open(source_path, 'r', encoding='utf-8') as infile:
    for i in infile.readlines():
        source.append(i)
with open(predict_path, 'r', encoding='utf-8') as infile:
    for i in infile.readlines():
        pred.append(i)
with open(tgt_path, 'r', encoding='utf-8') as infile:
    for i in infile.readlines():
        tgt.append(i)

assert len(source) == len(tgt) and len(tgt) == len(pred)
with open(predict_save, 'w', encoding='utf-8') as writer:
    for i in range(len(source)):
        sources = source[i].strip()
        prediction = pred[i].strip()
        target = tgt[i].strip()
        writer.write(sources + '\t' + prediction + '\t' + target + '\n')
print(predict_save)
