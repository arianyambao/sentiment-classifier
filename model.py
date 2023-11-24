# Import the necessary packages
import numpy as np
import torch.nn.functional as F
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from utils.preprocessing import preprocess_text

# Load the model
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# The labels are: Negative, Neutral, Positive 
# (Alphabetically arranged)
labels = ["negative", "neutral", "positive"]

# Let's create a function for inference
def predict_sentiment(text):
    # Preprocess the text and encode it
    cleaned_text = preprocess_text(text)
    encoded_input = tokenizer(cleaned_text, return_tensors='pt')

    # Do the actual prediction
    output = model(**encoded_input)
    probabilities = F.softmax(output.logits, dim=1)

    # Get the prediction
    index = np.argmax(probabilities.detach().numpy())
    confidence = np.round(probabilities.detach()
                            .numpy()[0][index] * 100, 2)

    
    # Return the outputs
    return {"model_output": labels[index], 
            "confidence_score":confidence}