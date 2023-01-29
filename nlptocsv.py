# from sgnlp.models.emotion_entailment import (
#     RecconEmotionEntailmentConfig,
#     RecconEmotionEntailmentModel,
#     RecconEmotionEntailmentTokenizer,
#     RecconEmotionEntailmentPreprocessor,
#     RecconEmotionEntailmentPostprocessor,
# )

# config = RecconEmotionEntailmentConfig.from_pretrained(
#     "https://storage.googleapis.com/sgnlp/models/reccon_emotion_entailment/config.json"
# )
# model = RecconEmotionEntailmentModel.from_pretrained(
#     "https://storage.googleapis.com/sgnlp/models/reccon_emotion_entailment/pytorch_model.bin",
#     config=config,
# )
# tokenizer = RecconEmotionEntailmentTokenizer.from_pretrained("roberta-base")
# preprocessor = RecconEmotionEntailmentPreprocessor(tokenizer)
# postprocess = RecconEmotionEntailmentPostprocessor()

# input_batch = {
#     "emotion": ["happiness", "happiness"],
#     "target_utterance": ["Thank you very much .", "Thank you very much ."],
#     "evidence_utterance": [
#         "How can I forget my old friend ?",
#         "My best wishes to you and the bride !",
#     ],
#     "conversation_history": [
#         "It's very thoughtful of you to invite me to your wedding . How can I forget my old friend ? My best wishes to you and the bride ! Thank you very much .",
#         "It's very thoughtful of you to invite me to your wedding . How can I forget my old friend ? My best wishes to you and the bride ! Thank you very much .",
#     ],
# }
# input_dict = preprocessor(input_batch)
# raw_output = model(**input_dict)
# output = postprocess(raw_output)
# print(output)

# [{ "sentence": ['To', 'sum', 'it', 'up', ':', 'service', 'varies', 'from', 'good', 'to', 'mediorce', ',',
#             'depending', 'on', 'which', 'waiter', 'you', 'get', ';', 'generally', 'it', 'is', 'just',
#             'average', 'ok', '.'],
#             'aspects': [[5]],
#             'labels': [0]},

#             {'sentence': ['Everything', 'is', 'always', 'cooked', 'to', 'perfection', ',', 'the', 'service',
#             'is', 'excellent,', 'the', 'decor', 'cool', 'and', 'understated.'],
#             'aspects': [[8], [12]],
#             'labels': [1, 1]},

#             {'sentence': ['the', 'only', 'chicken', 'i', 'moderately', 'enjoyed', 'was', 'their', 'grilled',
#             'chicken', 'special', 'with', 'edamame', 'puree', '.'],
#             'aspects': [[8, 9], [2], [9]],
#             'labels': [1, 1, 1]}]

# Output from sgnlp is list of dictionaries
import csv
import os
import senticGCNBERT
os.chdir(r'C:\Users\User\Desktop')

list_output = senticGCNBERT.output

neutral = 0
negative = 0
positive = 0

# Counting the number of -1/0/1
for dict in list_output:
    labels_lst = dict["labels"]
    for num in labels_lst:
        if num == 0:
            neutral += 1
        elif num < 0:
            negative += 1
        else:
            positive += 1
            
# Set the header for the csv file
header = ["Negative", "Neutral", "Positive"]
data = [negative, neutral, positive]

# Writing the csv file
with open('sentiment2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerow(data)
    writer.writerow(["1234", "3473", "9083"])
    writer.writerow(["3434", "r3093", "d32d[]ld"])


print(positive)
print(negative)
print(neutral)
print(data)
