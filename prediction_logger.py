import json

def save_predictions(predictions, filename):
    #writes the data 
    with open(filename, "w") as file:
        json.dump(predictions,file,indent=4)
        


#reads the data

def load_predictions(filename):
    try:
        with open(filename , "r") as file:
            data = json.load(file)
            if  not isinstance(data,list):
                print("invalid data sturcture")
                return None
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("check the content or filename")
        return None


def add_prediction(new_prediction, filename):
    existing_data = load_predictions(filename)
    if existing_data is None:
        print("Unable to load predictions. Saving cancelled.")
        return None
    for prediction in existing_data:
        if prediction["url"] == new_prediction["url"]:
            print("Prediction already exists")
            return 
    existing_data.append(new_prediction)
    save_predictions(existing_data,filename)
    print("prediction added successfully")
    

def get_user_prediction():
    while True:
            url = input("Enter URL: ").strip()
            if url:
                break
            else:
                print("enter valid URL")
    
    while True:
    
            prediction = input("Enter prediction: ").strip().lower()
            if prediction in ["legitimate" ,"phishing"]:
                prediction = prediction.capitalize()
                break
            else:
                print("enter either legitimate or phishing")
            
    while True:
        try:
            confidence = float(input("Enter confidence: "))
            if confidence >=0 and confidence <=1:
                break
            else:
                print("invalid value")
        except ValueError:
            print("Please enter a valid number")
            

    new_prediction = {
        "url":url,
        "prediction": prediction,
        "confidence" : confidence
    }
    

    # Return the dictionary
    return new_prediction
    
while True:
    print("\n===== AI Prediction Logger =====")
    print("1. Add prediction")
    print("2. View all predictions")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Collect and add a prediction
        new_prediction = get_user_prediction()
        add_prediction(new_prediction,"predictions.json")
        

    elif choice == "2":
        # Load and display predictions
        saved_data = load_predictions("predictions.json")
        print(saved_data)
    elif choice == "3":
        # Exit the loop
        break

    else:
        print("Invalid choice")
