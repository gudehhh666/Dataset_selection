from datasets import load_dataset
# from transformers import 
import json


# gsm8k_data = load_dataset('/dfs/data/sda/xmwang/data/gsm8k/main')
# print(gsm8k_data['test'])

# humaneval_data = load_dataset('/dfs/data/sda/xmwang/data/openai_humaneval')
# print(humaneval_data['test'])

# commonsenseqa_data = load_dataset('/dfs/data/sda/xmwang/data/commonsense_qa')
# print(commonsenseqa_data['test'])


json_file = '/dfs/data/sda/xmwang/FewCLUE/datasets/chid/test.jsonl'

data_dict = []

with open(json_file, 'r', encoding='utf-8') as f:
    for line in f:
        data_dict.append(line)

print(data_dict[0])


def convert_hf_to_json(dataset, datadir):
    out_file = datadir
    with open(out_file, 'w', encoding='utf-8') as f:
        for row in dataset:
            # print(row)
            f.write(json.dumps(row)+ '\n')
        
        
# convert_hf_to_json(gsm8k_data['test'], '/dfs/data/sda/xmwang/Dataset_slection/convert_data/gsm8k.jsonl')

# convert_hf_to_json(humaneval_data['test'], '/dfs/data/sda/xmwang/Dataset_slection/convert_data/humaneval.jsonl')

convert_hf_to_json(data_dict, '/dfs/data/sda/xmwang/Dataset_slection/convert_data/chid.jsonl')
