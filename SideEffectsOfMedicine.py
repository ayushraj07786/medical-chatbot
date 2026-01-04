import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('c:/Users/mayank.c/OneDrive - Optimus Information Inc/Desktop/Chatbot_Project/Chatbot/MedicalFiles/SideEffectsOFMedicine.csv')

# Function to get substitutes, side effects, and use cases for a given medicine
def get_medicine_details(medicine_name):
    # Search for the medicine in the 'name' column and all 'substitute' columns (case-insensitive)
    medicine_row = df[
        df['name'].str.contains(medicine_name, case=False, na=False) |
        df[['substitute0', 'substitute1', 'substitute2', 'substitute3', 'substitute4']].apply(
            lambda x: x.str.contains(medicine_name, case=False, na=False).any(), axis=1
        )
    ]
    
    if not medicine_row.empty:
        # Extract substitutes
        substitutes = medicine_row[['name', 'substitute0', 'substitute1', 'substitute2', 'substitute3', 'substitute4']].values.flatten()
        substitutes = list(dict.fromkeys([sub.strip() for sub in substitutes if pd.notna(sub)]))  # Remove NaN values, duplicates, and strip whitespace
        
        # Extract side effects
        side_effects = medicine_row[[col for col in df.columns if col.startswith('sideEffect')]].values.flatten()
        side_effects = list(dict.fromkeys([effect.strip() for effect in side_effects if pd.notna(effect)]))  # Remove NaN values, duplicates, and strip whitespace
        
        # Extract use cases
        uses = medicine_row[['use0', 'use1', 'use2', 'use3', 'use4']].values.flatten()
        uses = list(dict.fromkeys([use.strip() for use in uses if pd.notna(use)]))  # Remove NaN values, duplicates, and strip whitespace
        
        # Format the response
        response = f"Substitutes: {', '.join(substitutes)}\n"
        response += f"Side Effects: {', '.join(side_effects)}\n"
        response += f"Uses: {', '.join(uses)}"
        return response
    else:
        return "No matching medicine found. Please check the name and try again."

# Chatbot interface
def chatbot():
    print("Welcome to the Medicine Chatbot!")
    print("Type 'exit' to quit.")
    
    while True:
        # Get user input
        user_input = input("\nEnter the name of the medicine: ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get medicine details
        response = get_medicine_details(user_input)
        print("\n", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()