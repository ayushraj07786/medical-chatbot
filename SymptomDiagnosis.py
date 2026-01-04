from fuzzywuzzy import process
import pandas as pd
import sys

# Load the dataset
training = pd.read_csv('c:/Users/mayank.c/OneDrive - Optimus Information Inc/Desktop/Chatbot_Project/Chatbot/MedicalFiles/Training.csv')  # Ensure the file is in the same directory or provide the full path
cols = training.columns[:-1]  # Extract symptom columns
training['prognosis'] = training['prognosis'].str.strip()  # Clean up whitespace in prognosis column

def match_symptoms(user_symptoms, dataset_symptoms):
    """
    Match user-provided symptoms with the dataset symptoms using fuzzy matching.
    """
    matched_symptoms = []
    for symptom in user_symptoms:
        match = process.extractOne(symptom, dataset_symptoms)
        if match[1] > 70:  # Match threshold (e.g., 70%)
            matched_symptoms.append(match[0])
    return matched_symptoms

def predict_disease(matched_symptoms, dataset):
    """
    Predict the disease based on matched symptoms.
    """
    if not matched_symptoms:
        return "Healtho: No matching symptoms found. Please consult a doctor for further evaluation."

    # Filter dataset for rows where the matched symptoms are present
    symptom_columns = dataset.columns[:-1]
    filtered_data = dataset.copy()
    for symptom in matched_symptoms:
        filtered_data = filtered_data[filtered_data[symptom] == 1]

    if filtered_data.empty:
        return "Healtho: No disease matches your symptoms. Please consult a doctor for further evaluation."
    else:
        # Get the most common disease in the filtered data
        predicted_disease = filtered_data['prognosis'].mode()[0]
        response = f"Healtho: Based on your symptoms, you may have {predicted_disease}.\n"
        response += "Healtho: Matched symptoms:\n"
        for symptom in matched_symptoms:
            response += f"- {symptom}\n"
        return response

def main():
    """
    Main function to handle user input.
    """
    if len(sys.argv) < 2:
        print("Error: No input provided. Please provide symptoms as a comma-separated list.")
        return

    # Get the user input from the command-line arguments
    user_input = " ".join(sys.argv[1:])  # Combine all arguments into a single string
    user_symptoms = [symptom.strip() for symptom in user_input.split(',')]
    dataset_symptoms = list(cols)  # Columns from the dataset
    matched_symptoms = match_symptoms(user_symptoms, dataset_symptoms)
    response = predict_disease(matched_symptoms, training)

    # Print the response
    print("\n", response)

# Run the script
if __name__ == "__main__":
    main()