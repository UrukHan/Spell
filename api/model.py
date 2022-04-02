from transformers import AutoModelForSeq2SeqLM, T5TokenizerFast
import torch
import subprocess


gpu_memory_info = subprocess.check_output("nvidia-smi --query-gpu=memory.free --format=csv", shell=True)

gpus = {}
num = '0123456789'
g_num = 0
g_mem = ''
mess = str(gpu_memory_info)
for i in range(len(mess)):
  if mess[i] in num: 
    g_mem += mess[i]
    if mess[i+1] not in num:
      gpus[g_num] = g_mem
      g_num += 1
      g_mem = ''

use_gpu = 0
gpu_mem = 0
for i in gpus.keys():
  if gpu_mem < int(gpus[i]):
    gpu_mem = int(gpus[i])
    use_gpu = i

class BERT_MODEL():

  def __init__(self):
    if torch.cuda.is_available():
      if use_gpu == 0:
        self.device = torch.device('cuda')
      else:
        self.device = torch.device('cuda:' + use_gpu)
    else:
      self.device = torch.device('cpu')
      print('CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU')

    self.MODEL_NAME = 'UrukHan/t5-russian-spell'
    self.MAX_INPUT = 256

    self.tokenizer = T5TokenizerFast.from_pretrained(self.MODEL_NAME)
    self.model = AutoModelForSeq2SeqLM.from_pretrained(self.MODEL_NAME).to(self.device)

  # input = ['сеглдыя хорош ден', 'когд а вы прдет к нам в госи']
  # input = 'сеглдыя хорош ден'

  def predict(self, input):
    task_prefix = "Spell correct: "         
    if type(input) != list: input = [input]
    encoded = self.tokenizer(
    [task_prefix + sequence for sequence in input],
    padding="longest",
    max_length=self.MAX_INPUT,
    truncation=True,
    return_tensors="pt",
    )
    predicts = self.model.generate(**encoded.to(self.device))   
    predicts = self.tokenizer.batch_decode(predicts, skip_special_tokens=True)
    return predicts