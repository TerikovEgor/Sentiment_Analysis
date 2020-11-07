import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
from tensorflow.keras.models import load_model
import sys
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer('[ ,\.\?!";\:\|]', gaps = True)

model = load_model('muse_sent_v2.h5',custom_objects={'KerasLayer':hub.KerasLayer})
model.load_weights('muse_sent_w_v2.h5')
sw = open('sw_short.txt').read().split('\n')
			
def _clear(string):
    tokens = tokenizer.tokenize(string.lower())
    return ' '.join([i for i in tokens if i not in sw])
	
def detect(string):
    string_clr = _clear(string)
    res = model.predict([string])
    if res > 0.80:
        return {'string':string, 'sentiment':'positive'}
    elif res < 0.25:
        return {'string':string, 'sentiment':'negative'}
    else:
        return {'string':string, 'sentiment':'neutral'}

