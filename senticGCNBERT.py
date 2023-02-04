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

processed_inputs, processed_indices = preprocessor(scrape.nlpmodelinputs)
raw_outputs = model(processed_indices)

nlpmodeloutputs = postprocessor(processed_inputs=processed_inputs, model_outputs=raw_outputs)
