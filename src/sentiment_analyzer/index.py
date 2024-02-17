from scipy.special import softmax
import torch
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
import numpy as np
MODELS =["lxyuan/distilbert-base-multilingual-cased-sentiments-student", "cardiffnlp/twitter-roberta-base-sentiment-latest"]


results = {string: {model: {} for model in MODELS} for string in strings}
for transformer in MODELS:
    print(f"Using {transformer} model")
    
    tokenizer = AutoTokenizer.from_pretrained(transformer)
    model = AutoModelForSequenceClassification.from_pretrained(transformer)
    config = AutoConfig.from_pretrained(transformer)
    
    for text in strings:
       
        tokens = tokenizer(text, return_tensors="pt")
        result = model(**tokens)




        scores = result[0][0].detach().numpy()
        scores = softmax(scores)
        print(f"text: {text}")
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        for i in range(scores.shape[0]):
            l = config.id2label[ranking[i]]
            s = scores[ranking[i]]
            results[text][transformer][l]=np.round(float(s), 4)
            
            print(f"{i+1}) {l} {np.round(float(s), 4)}")
print(results)