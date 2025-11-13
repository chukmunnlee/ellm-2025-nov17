print('The following script will preload all datasets and models to be used in the workshops')

import torch, nltk
from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from sentence_transformers import SentenceTransformer


print('Loading dataset...')
data = [ "facebook/ExploreToM", "knkarthick/dialogsum" ]

for d in data:
   print(f'\t{d}')
   load_dataset(d)

print('Loading models...')
data = [ 'google/flan-t5-base', 'google/flan-t5-small']
for d in data:
   print(f'\t{d}')
   AutoModelForSeq2SeqLM.from_pretrained(d)

print('Loading pre-trained models...')
data = [ 'truocpham/flan-dialogue-summary-checkpoint' ]
for d in data:
   print(f'\t{d}')
   AutoModelForSeq2SeqLM.from_pretrained(d, torch_dtype=torch.bfloat16)

print('Loading embedding models...')
data = [ 'BAAI/bge-small-en-v1.5', 'all-MiniLM-L6-V2' ]
for d in data:
    print(f'\t{d}')
    SentenceTransformer(d)

print('Preloading NLTK...')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


