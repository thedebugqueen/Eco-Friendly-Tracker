
def collect_recycling_data():    
    """
    Collect user data related to recycling habits and waste generation.

    Returns:
        tuple: Contains the following user inputs:
            - plastic_waste (float): Kilograms of plastic waste generated per week.
            - glass_waste (float): Kilograms of glass waste generated per week.
            - organic_waste (float): Kilograms of organic waste generated per week.
            - separates_waste (str): Whether the user separates waste for recycling (yes/no).
            - composting (str): Whether the user composts organic waste (yes/no).
            - electronics_recycled (str): Whether the user recycles electronic waste (yes/no).
    """
    print("\nRecycling Management Module")
    
                                                                     
    plastic_waste = input("How many kilograms of plastic waste do you generate per week? (Enter a positive number): ")
    while not plastic_waste.replace('.', '', 1).isdigit() or float(plastic_waste) < 0:
        print("Invalid input. Please enter a positive number.")
        plastic_waste = input("How many kilograms of plastic waste do you generate per week? (Enter a positive number): ")
    plastic_waste = float(plastic_waste)

                                                                      
    glass_waste = input("How many kilograms of glass waste do you generate per week? (Enter a positive number): ")
    while not glass_waste.replace('.', '', 1).isdigit() or float(glass_waste) < 0:
        print("Invalid input. Please enter a positive number.")
        glass_waste = input("How many kilograms of glass waste do you generate per week? (Enter a positive number): ")
    glass_waste = float(glass_waste)

    
    organic_waste = input("How many kilograms of organic waste do you generate per week? (Enter a positive number): ")
    while not organic_waste.replace('.', '', 1).isdigit() or float(organic_waste) < 0:
        print("Invalid input. Please enter a positive number.")
        organic_waste = input("How many kilograms of organic waste do you generate per week? (Enter a positive number): ")
    organic_waste = float(organic_waste)

                                                                   
    while True:
        separates_waste = input("Do you separate your waste for recycling? (Yes/No): ").lower()
        if separates_waste in ['yes', 'no']:
            break
        print("Invalid input. Please answer with 'Yes' or 'No'.")

    
    while True:
        composting = input("Do you compost organic waste? (Yes/No): ").lower()
        if composting in ['yes', 'no']:
            break
        print("Invalid input. Please answer with 'Yes' or 'No'.")

   
    while True:
        electronics_recycled = input("Do you recycle electronic waste? (Yes/No): ").lower()
        if electronics_recycled in ['yes', 'no']:
            break
        print("Invalid input. Please answer with 'Yes' or 'No'.")

    # Return collected user inputs.
    return plastic_waste, glass_waste, organic_waste, separates_waste, composting, electronics_recycled


def calculate_recycling_score(plastic_waste, glass_waste, organic_waste, separates_waste, composting, electronics_recycled):
    """
    Calculate a recycling score based on the user's waste generation and recycling habits.

    Args:
        plastic_waste (float): Kilograms of plastic waste generated per week.
        glass_waste (float): Kilograms of glass waste generated per week.
        organic_waste (float): Kilograms of organic waste generated per week.
        separates_waste (str): Whether the user separates waste for recycling (yes/no).
        composting (str): Whether the user composts organic waste (yes/no).
        electronics_recycled (str): Whether the user recycles electronic waste (yes/no).

    Returns:
        tuple: 
            - score (int): The calculated recycling score (minimum 0).
            - recommendations (list): A list of recommendations to improve recycling habits.
    """
    # Start with a maximum score of 100.
    score = 100
    
    # Deduct points based on the amount of waste generated.
    score -= plastic_waste * 5        # Plastic waste reduces the score by 5 per kilogram.
    score -= glass_waste * 3          # Glass waste reduces the score by 3 per kilogram.
    score -= organic_waste * 2        # Organic waste reduces the score by 2 per kilogram.
    
    # Deduct points for not following good recycling practices.
    if separates_waste != 'yes':
        score -= 20                       # Deduction for not separating waste.
    if composting != 'yes':
        score -= 15                       # Deduction for not composting organic waste.
    if electronics_recycled != 'yes':
        score -= 10                       # Deduction for not recycling electronic waste.
    
    # Generate recommendations based on user inputs.
    recommendations = []
    if plastic_waste > 5:
        recommendations.append("Reduce your plastic waste by using reusable bags and containers.")
    if glass_waste > 5:
        recommendations.append("Consider reusing or recycling glass containers.")
    if organic_waste > 5:
        recommendations.append("Try to minimize food waste by planning meals effectively.")
    if separates_waste != 'yes':
        recommendations.append("Start separating your waste for proper recycling.")
    if composting != 'yes':
        recommendations.append("Compost your organic waste to reduce landfill contribution.")
    if electronics_recycled != 'yes':
        recommendations.append("Recycle your electronic waste properly at designated centers.")
    if plastic_waste > 10:
        recommendations.append("Avoid single-use plastics and opt for sustainable alternatives.")
    if glass_waste > 10:
        recommendations.append("Participate in local glass recycling programs.")
    if organic_waste > 10:
        recommendations.append("Use leftover food creatively to minimize organic waste.")
    if score < 50:
        recommendations.append("Educate yourself on recycling best practices to improve your habits.")
    if score < 30:
        recommendations.append("Consider joining a community recycling initiative.")
    
    # Ensure the score does not go below 0 and return the score with recommendations.
    return max(0, score), recommendations
