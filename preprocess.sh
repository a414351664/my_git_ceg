#!/bin/bash
DATA_PAY=~/data1/jiao_data/gec_data
python utils/preprocess_data.py -s $DATA_PAY/train.src -t $DATA_PAY/train.tgt -o $DATA_PAY/post_train.txt

python utils/preprocess_data.py -s $DATA_PAY/valid.src -t $DATA_PAY/valid.tgt -o $DATA_PAY/post_val.txt

python utils/preprocess_data.py -s $DATA_PAY/test.src -t $DATA_PAY/test.tgt -o $DATA_PAY/post_test.txt
