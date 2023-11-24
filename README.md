# Sentiment Classifier Using Roberta
Model used was referenced from: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment (54M training). Please take note that when running the models, it may take a few seconds to load the model.

# Installing dependencies
Before using the scripts, make sure to install the necessary packages
```
pip install -r requirements.txt
```

# Using locally
To use the app locally:
```
python main.py
```

# Using via API (simple version)
To use the app via API fashion:
1. Initialize the uvicorn 
```
uvicorn api:app
```
2. On another python instance (or on your POSTMAN), just make a POST request. For example:
```
import requests
requests.post("http://127.0.0.1:8000/predict_sentiment", json={'text': 'i love fried chicken'}).json()
```

# Using via Streamlit (with UI)
Alternatively, here's a publicly available instance: https://sentiment-classifier-yg7n4regykx2nktztqdk4n.streamlit.app/

Remember that this may take a few seconds to a few minutes to launch locally
```
streamlit run streamlit_app.py
```
