import pandas as pd

input_file = '../org_data_abs/valid.tsv'
src_file = '../org_data_abs/valid.src'
tgt_file = '../org_data_abs/valid.tgt'
# abstracts = pd.read_csv(train_file, sep='\t')
sources = []
tgts = []
with open(input_file, 'r', encoding='utf-8') as infile:
    for index in infile.readlines():
        tmp_list = index.strip().split('\t')
        tmp_list = list(filter(lambda x: '|||' in x, [i for i in tmp_list]))
        source = tmp_list[0].split('|||')[0]
        for j, abs in enumerate(tmp_list):
            if j == 0 or 'Most important meaning Flawless language' in abs.split('|||')[0]:
                tgts.append(abs.split('|||')[1])
                sources.append(source)
with open(src_file, 'w', encoding='utf-8') as outfile:
    for i in sources:
        outfile.write(i)
        outfile.write('\n')
with open(tgt_file, 'w', encoding='utf-8') as outfile:
    for i in tgts:
        outfile.write(i)
        outfile.write('\n')
# for index, abstract in abstracts.iterrows():
#     print(abstract)
