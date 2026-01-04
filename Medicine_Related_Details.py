import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('c:/Users/mayank.c/OneDrive - Optimus Information Inc/Desktop/Chatbot_Project/Chatbot/MedicalFiles/medquad.csv')

# Function to search for answers based on user question
def get_answers_by_question(user_question):
    # Split the user question into words
    words = user_question.split()
    
    # Search for any word in the focus_area column (case-insensitive)
    results = df[df['focus_area'].str.contains('|'.join(words), case=False, na=False)]
    
    # Check if any results were found
    if not results.empty:
        return f"Here is some information about your question : \n{results['answer'].to_string(index=False)}"
    else:
        return "No matching focus area found. Sorry, I can't help with that."

# Chatbot interface
def chatbot():
    print("Welcome to the MedQuad Chatbot!")
    print("Type 'exit' to quit.")
    
    while True:
        # Get user input
        user_input = input("\nAsk your question: ")
        
        # Exit condition
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get the answers for the matching focus area
        response = get_answers_by_question(user_input)
        print("\n", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()