# Deploying NLP model using FastAPI server and Docker

## NLP model
The application takes a list of sentences and returns sentence embedding for each. The app uses sBERT framework and paraphrase-distilroberta-base-v1 model. 

Read more about sBERT: https://www.sbert.net/.

Read more about model: https://huggingface.co/sentence-transformers/paraphrase-distilroberta-base-v1

## How to run
run in your console:
> docker-compose up --build

