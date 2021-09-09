MODEL_PATH=~/data1/jiao_data/gec_output
VOCAB_PATH=~/data1/jiao_data/gec_output/vocabulary
INPUT_FILE=/home/v-weipeng/data1/jiao_data/gec_data/valid.src
OUTPUT_FILE=/home/v-weipeng/data1/jiao_data/gec_output
python predict.py --model_path $MODEL_PATH --vocab_path $VOCAB_PATH --input_file $INPUT_FILE --output_file $OUTPUT_FILE
