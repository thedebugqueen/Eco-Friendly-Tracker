
def collect_energy_data():
    print("\nEnergy Consumption Module")
    white_goods_use = input("How many times do you use white goods per week? (Enter a positive integer): ")
    while not white_goods_use.replace('.', '', 1).isdigit() or float(white_goods_use) < 0:
        print("Invalid input. Please enter a positive integer.")
        white_goods_use = input("How many hours do you use white goods per week? (Enter a positive integer): ")
    white_goods_use = float(white_goods_use) 

    charging_time = input("How many hours do you charge devices per week? (Enter a positive number): ")
    while not charging_time.replace('.', '', 1).isdigit() or float(charging_time) < 0:
        print("Invalid input. Please enter a positive number.")
        charging_time = input("How many hours do you charge devices per week? (Enter a positive number): ")
    charging_time = float(charging_time)

    appliance_usage = input("How many hours do you use other appliances per week? (Enter a positive number): ")
    while not appliance_usage.replace('.', '', 1).isdigit() or float(appliance_usage) < 0:
        print("Invalid input. Please enter a positive number.")
        appliance_usage = input("How many hours do you use other appliances per week? (Enter a positive number): ")
    appliance_usage = float(appliance_usage)

    light_usage = input("How many hours do you use lights per week? (Enter a positive number): ")
    while not light_usage.replace('.', '', 1).isdigit() or float(light_usage) < 0:
        print("Invalid input. Please enter a positive number.")
        light_usage = input("How many hours do you use lights per week? (Enter a positive number): ")
    light_usage = float(light_usage)
    while True:
        led_bulbs = input("Do you use LED bulbs? (Yes/No) ").lower()
        if led_bulbs in ['yes', 'no']:
            break
        print("Invalid input. Please answer with 'Yes' or 'No'.")

    while True:
        solar_panels = input("Do you use solar panels? (Yes/No) ").lower()
        if solar_panels in ['yes', 'no']:
            break
        print("Invalid input. Please answer with 'Yes' or 'No'.")
    return white_goods_use, charging_time, appliance_usage, light_usage, led_bulbs, solar_panels 



def calculate_energy_score(white_goods_use, charging_time, appliance_usage, light_usage, led_bulbs, solar_panels):
    score = 100
    score -= white_goods_use * 2  # Deduct 2 points for each hour of white goods usage.
    score -= charging_time * 1.5  # Deduct 1.5 points for each hour of charging devices.
    score -= appliance_usage * 2   # Deduct 2 points for each hour of other appliance usage
    score -= light_usage * 0.5   # Deduct 0.5 points for each hour of light usage.
    
    # Deduct additional points for not using LED bulbs.
    if led_bulbs != 'yes':
        score -= 10
        # Deduct additional points for not using solar panels.
    if solar_panels != 'yes':
        score -= 15
    
    recommendations = [] # Initialize an empty list to store recommendations
    
 # Provide recommendations based on the user's data
    if white_goods_use > 5:
        recommendations.append("Use energy-efficient appliances to reduce energy consumption.")
    if charging_time > 4:
        recommendations.append("Unplug chargers when devices are fully charged.")
    if appliance_usage > 10:
        recommendations.append("Limit the use of high-energy-consuming appliances.")
    if light_usage > 10:
        recommendations.append("Turn off lights when not in use.")
    if led_bulbs != 'yes':
        recommendations.append("Switch to LED bulbs for better energy efficiency.")
    if solar_panels != 'yes':
        recommendations.append("Consider installing solar panels to generate renewable energy.")
    if score < 70:
        recommendations.append("Conduct an energy audit to identify areas for improvement.")
    if light_usage > 20:
        recommendations.append("Use motion sensors for lights to reduce unnecessary usage.")
    if charging_time > 6:
        recommendations.append("Invest in smart chargers that automatically stop charging.")
    if white_goods_use > 10:
        recommendations.append("Schedule laundry and dishwashing during off-peak hours.")
    if score < 50:
        recommendations.append("Explore government incentives for energy-saving home upgrades.")
    
    # Ensure the score does not drop below 0 and return the score and recommendations.
    return max(0, score), recommendations
