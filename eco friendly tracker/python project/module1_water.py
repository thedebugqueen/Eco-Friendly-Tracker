
# collects data from the user about their water usage habits and behaviors.
def collect_water_data():
    print("\nWater Conservation Module")
    
    shower_time = input("How many minutes do you spend in the shower? (Enter a positive integer): ")
    while not shower_time.replace('.', '', 1).isdigit() or float(shower_time) < 0:
        print("Invalid input. Please enter a positive integer.")
        shower_time = input("How many minutes do you spend in the shower? (Enter a positive integer): ")
    shower_time = float(shower_time)

    showers_per_week = input("How many times do you shower per week? (Enter a positive integer): ")
    while not showers_per_week.replace('.', '', 1).isdigit() or float(showers_per_week) < 0:
        print("Invalid input. Please enter a positive integer.")
        showers_per_week = input("How many times do you shower per week? (Enter a positive integer): ")
    showers_per_week = float(showers_per_week)

    washing_machine_use = input("How many times do you use the washing machine per week? (Enter a positive integer): ")
    while not washing_machine_use.replace('.', '', 1).isdigit() or float(washing_machine_use) < 0:
        print("Invalid input. Please enter a positive integer.")
        washing_machine_use = input("How many times do you use the washing machine per week? (Enter a positive integer): ")
    washing_machine_use = float(washing_machine_use)

    dishwasher_use = input("How many times do you use the dishwasher per week? (Enter a positive integer): ")
    while not dishwasher_use.replace('.', '', 1).isdigit() or float(dishwasher_use) < 0:
        print("Invalid input. Please enter a positive integer.")
        dishwasher_use = input("How many times do you use the dishwasher per week? (Enter a positive integer): ")
    dishwasher_use = float(dishwasher_use)

    while True:
        tap_running = input("Do you leave the tap running while brushing teeth? (Yes/No) ").lower()
        if tap_running in ['yes', 'no']:
            break
        print("Invalid input. Please answer with 'Yes' or 'No'.")

    while True:
        leaks_checked = input("Do you regularly check for water leaks? (Yes/No) ").lower()
        if leaks_checked in ['yes', 'no']:
            break
        print("Invalid input. Please answer with 'Yes' or 'No'.")
    
    return shower_time, showers_per_week, washing_machine_use, dishwasher_use, tap_running, leaks_checked



def calculate_water_score(shower_time, showers_per_week, washing_machine_use, dishwasher_use, tap_running, leaks_checked):
    """
    Calculate a water conservation score based on the user's water usage habits.

    Args:
        shower_time (int): Minutes spent in the shower.
        showers_per_week (int): Number of showers per week.
        washing_machine_use (int): Weekly washing machine usage count.
        dishwasher_use (int): Weekly dishwasher usage count.
        tap_running (str): Whether the tap is left running while brushing teeth (yes/no).
        leaks_checked (str): Whether the user checks for water leaks regularly (yes/no).

    Returns:
        tuple: 
            - score (int): The calculated water conservation score (minimum 0).
            - recommendations (list): A list of recommendations to improve water conservation.
    """
                                                                           
    score = 100
    
                                                                           
    score -= shower_time * showers_per_week * 0.5                          # Deduct based on total shower time per week.
    score -= washing_machine_use * 2                                       # Deduct 2 points for each use of the washing machine.
    score -= dishwasher_use * 1.5                                          # Deduct 1.5 points for each use of the dishwasher.
    
    # Deduct additional points for inefficient water usage behaviors.
    if tap_running == 'yes':
        score -= 10               # Deduct 10 points if the tap is left running while brushing teeth.
    if leaks_checked != 'yes':
        score -= 15               # Deduct 15 points if the user does not check for leaks regularly.

    # Initialize an empty list to store recommendations for improvement.
    recommendations = []
    
    # --- Generate recommendations based on user data ---
    if shower_time > 15:
        recommendations.append("Reduce your shower time to save water.")
    if showers_per_week > 7:
        recommendations.append("Limit the number of showers you take per week.")
    if washing_machine_use > 5:
        recommendations.append("Use the washing machine less frequently or ensure full loads.")
    if dishwasher_use > 3:
        recommendations.append("Run the dishwasher only when it is fully loaded.")
    if tap_running == 'yes':
        recommendations.append("Turn off the tap while brushing your teeth or washing dishes.")
    if leaks_checked != 'yes':
        recommendations.append("Check for leaks in taps, pipes, and toilets to prevent water wastage.")
    if score < 50:
        recommendations.append("Consider installing water-efficient fixtures and appliances.")
    if shower_time > 15:
        recommendations.append("Install a water-saving showerhead to reduce water usage.")
    if washing_machine_use > 5:
        recommendations.append("Choose an energy-efficient washing machine for lower water consumption.")
    if dishwasher_use > 5:
        recommendations.append("Rinse dishes lightly before using the dishwasher instead of prewashing them.")
    
    # Ensure the score does not go below 0 and return the score with recommendations.
    return max(0, score), recommendations
