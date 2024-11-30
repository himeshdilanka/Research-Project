import joblib

# Load the saved model (if needed)
model_filename = 'stress_management_model.pkl'
classifier = joblib.load(model_filename)

def categorize_age(age):
    """
    Categorize age into Teenagers or Young Adults
    
    :param age: Integer representing the person's age
    :return: Age group category as a string
    """
    if 13 <= age <= 19:
        return 'Teenagers'
    elif 20 <= age <= 28:
        return 'Young Adults'
    else:
        return 'Unknown'

def categorize_stress_level(stress_score):
    """
    Categorize stress level based on a numerical score
    
    :param stress_score: Integer representing stress level (0-10)
    :return: Stress level category as a string
    """
    if stress_score <= 3:
        return 'Low Stress'
    elif 3 < stress_score <= 7:
        return 'Moderate Stress'
    else:
        return 'High Stress'

def get_music_therapy_recommendation(age_group, gender, stress_level):
    """
    Retrieve personalized music therapy recommendations
    """
    therapy_recommendations = {
        'Teenagers': {
            'Female': {
                'High Stress': {
                    'Drumming': {'duration': 15, 'description': 'for high stress relief'},
                    'Singing': {'duration': 12, 'description': 'to help with emotional connection and brain activity'},
                    'VAT': {'duration': 13, 'description': 'to calm the body and mind'}
                },
                'Moderate Stress': {
                    'Drumming': {'duration': 10, 'description': 'for energy release'},
                    'Singing': {'duration': 15, 'description': 'to promote connection and brain repair'},
                    'VAT': {'duration': 13, 'description': 'for relaxation'}
                },
                'Low Stress': {
                    'Drumming': {'duration': 10, 'description': 'for energy activation'},
                    'Singing': {'duration': 12, 'description': 'to reinforce positive brain activity'},
                    'VAT': {'duration': 15, 'description': 'to enhance relaxation and body repair'}
                }
            },
            'Male': {
                'High Stress': {
                    'Drumming': {'duration': 15, 'description': 'to release built-up stress and trauma'},
                    'Singing': {'duration': 10, 'description': 'to connect and stimulate brain function'},
                    'VAT': {'duration': 12, 'description': 'to calm the body and mind'}
                },
                'Moderate Stress': {
                    'Drumming': {'duration': 10, 'description': 'to release some tension'},
                    'Singing': {'duration': 14, 'description': 'to promote brain repair'},
                    'VAT': {'duration': 13, 'description': 'to relax the body'}
                },
                'Low Stress': {
                    'Drumming': {'duration': 10, 'description': 'to activate energy'},
                    'Singing': {'duration': 12, 'description': 'to maintain a positive mood'},
                    'VAT': {'duration': 14, 'description': 'to enhance relaxation'}
                }
            }
        },
        'Young Adults': {
            'Female': {
                'High Stress': {
                    'Drumming': {'duration': 14, 'description': 'to release high stress'},
                    'Singing': {'duration': 11, 'description': 'to boost brain function'},
                    'VAT': {'duration': 12, 'description': 'to relax the body'}
                },
                'Moderate Stress': {
                    'Drumming': {'duration': 12, 'description': 'to release moderate stress'},
                    'Singing': {'duration': 13, 'description': 'to enhance brain activity'},
                    'VAT': {'duration': 13, 'description': 'for overall relaxation'}
                },
                'Low Stress': {
                    'Drumming': {'duration': 10, 'description': 'to activate energy'},
                    'Singing': {'duration': 14, 'description': 'to enhance emotional connection'},
                    'VAT': {'duration': 15, 'description': 'to deepen relaxation'}
                }
            },
            'Male': {
                'High Stress': {
                    'Drumming': {'duration': 15, 'description': 'to release tension and trauma'},
                    'Singing': {'duration': 10, 'description': 'to stimulate brain activity'},
                    'VAT': {'duration': 12, 'description': 'to calm and soothe the body'}
                },
                'Moderate Stress': {
                    'Drumming': {'duration': 12, 'description': 'to release stress'},
                    'Singing': {'duration': 12, 'description': 'to enhance brain function'},
                    'VAT': {'duration': 13, 'description': 'to relax'}
                },
                'Low Stress': {
                    'Drumming': {'duration': 10, 'description': 'for gentle energy activation'},
                    'Singing': {'duration': 14, 'description': 'for emotional health'},
                    'VAT': {'duration': 14, 'description': 'to deepen relaxation'}
                }
            }
        }
    }

    try:
        return therapy_recommendations[age_group][gender][stress_level]
    except KeyError:
        return None

def get_personalized_music_therapy(age, gender, stress_score):
    """
    Function to get personalized music therapy recommendations
    without interactive input
    """
    # Validate inputs
    if not (isinstance(age, int) and 0 < age):
        return {"error": "Invalid age"}
    
    if gender not in ['Male', 'Female']:
        return {"error": "Invalid gender"}
    
    if not (isinstance(stress_score, int) and 0 <= stress_score <= 10):
        return {"error": "Invalid stress score"}

    # Categorize inputs
    age_group = categorize_age(age)
    stress_level = categorize_stress_level(stress_score)

    # Check if age group is valid
    if age_group == 'Unknown':
        return {"error": f"No recommendations for age {age}"}

    # Get recommendations
    recommendations = get_music_therapy_recommendation(age_group, gender, stress_level)

    # Prepare response
    response = {
        "personalizedTherapyDetails": f"""--- Personalized Music Therapy for {age} year old {gender} ---
Age Group: {age_group}
Stress Level: {stress_level}

Drumming Therapy:
  Duration: {recommendations['Drumming']['duration']} minutes
  Purpose: {recommendations['Drumming']['description']}

Singing Therapy:
  Duration: {recommendations['Singing']['duration']} minutes
  Purpose: {recommendations['Singing']['description']}

VAT Therapy:
  Duration: {recommendations['VAT']['duration']} minutes
  Purpose: {recommendations['VAT']['description']}"""
    }

    return response

# Interactive version for console use
def interactive_music_therapy():
    """
    Interactive function to get personalized music therapy recommendations
    """
    while True:
        try:
            # Get age input
            while True:
                age = int(input("Enter your age: "))
                if age > 0:
                    break
                print("Please enter a valid age.")

            # Get gender input
            while True:
                gender = input("Enter your gender (Male/Female): ").strip().capitalize()
                if gender in ['Male', 'Female']:
                    break
                print("Please enter either 'Male' or 'Female'.")

            # Get stress score input
            while True:
                stress_score = int(input("Enter your stress level (0-10): "))
                if 0 <= stress_score <= 10:
                    break
                print("Please enter a stress score between 0 and 10.")

            # Get and display recommendations
            result = get_personalized_music_therapy(age, gender, stress_score)
            
            # Check if there's an error
            if 'error' in result:
                print(result['error'])
            else:
                print(result['personalizedTherapyDetails'])

            # Ask if user wants to continue
            another = input("\nDo you want to get another recommendation? (yes/no): ").lower()
            if another != 'yes':
                print("Thank you for using the Music Therapy Recommendation System. Stay calm and take care!")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values for age and stress level.")

# Run the interactive recommendation system
if __name__ == "__main__":
    interactive_music_therapy()