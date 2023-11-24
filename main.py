from model import predict_sentiment

# Loop the inputs
while True:
    # Take the user input
    text = input("Your tweet (ctrl + c or z) to quit: ")
    print(predict_sentiment(text))