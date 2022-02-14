'''

Test to extract embeddings from wav2vec2 models

'''

import torch
import fairseq
from pprint import pprint
import json
cp_path = '/path/to/model/checkpoint_3540_400000.pt'
model, cfg, task = fairseq.checkpoint_utils.load_model_ensemble_and_task([cp_path])
model = model[0]
#model.eval()

print("cfg.model.quantize_input:", cfg.model.quantize_input)
print("cfg.model.quantize_targets:", cfg.model.quantize_targets)

wav_input_16khz = torch.randn(1,10000)


outputs = model.extract_features(wav_input_16khz, padding_mask=None)
z = outputs["x"]
# if the model was run with cfg.model.quantize_input = True, then z here will be quantized


# z = model.feature_extractor(wav_input_16khz)

#c = model.feature_aggregator(z)
c = model.forward(wav_input_16khz, mask=False, features_only=True)
print("-------------------------------------\n")
print("This is the output from passing a random 16kHz sequence to model.feature_extractor \n")
print("-------------------------------------\n")
# print(z)

print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("This is the output from passing a random 16kHz sequence to model.forward \n")
print("-------------------------------------\n")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print(z.shape)
# print(z_quantized.shape)
