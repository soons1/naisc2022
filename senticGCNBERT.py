from sgnlp.models.sentic_gcn import(
    SenticGCNBertConfig,
    SenticGCNBertModel,
    SenticGCNBertEmbeddingConfig,
    SenticGCNBertEmbeddingModel,
    SenticGCNBertTokenizer,
    SenticGCNBertPreprocessor,
    SenticGCNBertPostprocessor
)

import scrape

tokenizer = SenticGCNBertTokenizer.from_pretrained("bert-base-uncased")

config = SenticGCNBertConfig.from_pretrained(
    "https://storage.googleapis.com/sgnlp/models/sentic_gcn/senticgcn_bert/config.json"
)

model = SenticGCNBertModel.from_pretrained(
    "https://storage.googleapis.com/sgnlp/models/sentic_gcn/senticgcn_bert/pytorch_model.bin",
    config=config
)

embed_config = SenticGCNBertEmbeddingConfig.from_pretrained("bert-base-uncased")

embed_model = SenticGCNBertEmbeddingModel.from_pretrained("bert-base-uncased",
    config=embed_config
)

preprocessor = SenticGCNBertPreprocessor(
    tokenizer=tokenizer, embedding_model=embed_model,
    senticnet="https://storage.googleapis.com/sgnlp/models/sentic_gcn/senticnet.pickle",
    device="cpu")

postprocessor = SenticGCNBertPostprocessor()

processed_inputs, processed_indices = preprocessor(main.inputs)
raw_outputs = model(processed_indices)

post_outputs = postprocessor(processed_inputs=processed_inputs, model_outputs=raw_outputs)

print(post_outputs[0])
# {'sentence': ['To', 'sum', 'it', 'up', ':', 'service', 'varies', 'from', 'good', 'to', 'mediorce', ',',
#               'depending', 'on', 'which', 'waiter', 'you', 'get', ';', 'generally', 'it', 'is', 'just',
#               'average', 'ok', '.'],
#  'aspects': [[5]],
#  'labels': [0]}

print(post_outputs[1])
# {'sentence': ['Everything', 'is', 'always', 'cooked', 'to', 'perfection', ',', 'the', 'service',
#               'is', 'excellent,', 'the', 'decor', 'cool', 'and', 'understated.'],
#  'aspects': [[8], [12]],
#  'labels': [1, 1]}

print(post_outputs[2])
# {'sentence': ['the', 'only', 'chicken', 'i', 'moderately', 'enjoyed', 'was', 'their', 'grilled',
#               'chicken', 'special', 'with', 'edamame', 'puree', '.'],
#  'aspects': [[8, 9], [2], [9]],
#  'labels': [1, 1, 1]}

'''
inputs = [
    {  # Single word aspect
        "aspects": ["service"],
        "sentence": "To sum it up : service varies from good to mediorce , depending on which waiter you get ; generally it is just average ok .",
    },
    {  # Single-word, multiple aspects
        "aspects": ["service", "decor"],
        "sentence": "Everything is always cooked to perfection , the service is excellent, the decor cool and understated.",
    },
    {  # Multi-word aspect
        "aspects": ["grilled chicken", "chicken"],
        "sentence": "the only chicken i moderately enjoyed was their grilled chicken special with edamame puree .",
    },
]
'''
