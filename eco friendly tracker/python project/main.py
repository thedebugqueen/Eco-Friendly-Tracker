# main.py  ""                          
# # Importing necessary libraries and modules
import csv                          
import datetime                     
import module1_water                
import module2_recycling            
import module3_energy               
import performance_analysis         
import random                       
import matplotlib.pyplot as plt     

def save_to_csv(filename, data):                                                     
    header = ['Date', 'Name', 'Module', 'Score', 'Recommendations']     
    
                                                                        
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)                
        
                                                                        
        if file.tell() == 0:
            writer.writeheader()
        
                                                                        
        for row in data:
            writer.writerow({
                'Date': row[0],                                     # Date of the entry
                'Name': row[1],                                     # Name of the user
                'Module': row[2],                                   # Module name (e.g., Water,Recycling)
                'Score': row[3],                                    # Score for that module
                'Recommendations': row[4]                           # Suggestions for improvement
            })


def read_csv(filename):
    """
    Reads data from a CSV file and returns it as a list of dictionaries.

    """
    try:
        with open(filename, 'r') as file:                               # Open the specified file in read mode.
            reader = csv.DictReader(file)                               # Create a DictReader object to read the file as dictionaries.
            data = [row for row in reader]                              # Iterate through the reader and store each row as a dictionary in a list.
        return data                                                     # Return the list of dictionaries containing the data.

    except FileNotFoundError:                                           # Handle the case where the file does not exist.
        print("CSV file not found. Please ensure the file exists.")     # Print an error message if the file is not found.
        return []                                                       # Return an empty list to indicate no data was read.

filename = "eco_friendly_data.csv"                                      # Specify the name of the CSV file to be read.
data = []                                                               # Initialize an empty list to store the data (if needed later in the program).

# Development Function to Plot Time-Series Data for a Specific Name

def plot_time_series_for_name(filename, name):
    """
    Plot time-series data for a specific individual based on their scores in different modules.

    Args:
        filename (str): The name of the CSV file to read data from.
        name (str): The name of the individual to filter and plot data for.
    """
    # Attempt to read the CSV file line by line.
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()       
    except FileNotFoundError:
                                           
        print(f"File '{filename}' not found.")
        return

                                                            
    header = lines[0].strip().split(',')                    # Split the first line into column names.
    data = [line.strip().split(',') for line in lines[1:]]  # Split the remaining lines into data rows.
                                                            
    name_data = [row for row in data if row[header.index('Name')].lower() == name.lower()]

    # If no data exists for the specified name, notify the user and exit the function.
    if not name_data:
        print(f"No data found for {name}.")
        return

                                                       
    scores_by_module = {}
    for row in name_data:
        date = row[header.index('Date')]               # Extract the date from the current row.
        module = row[header.index('Module')]           # Extract the module name.
        score = float(row[header.index('Score')])      # Convert the score to a floating-point number.

                                                        
        if module not in scores_by_module:
            scores_by_module[module] = []

                                                        
        scores_by_module[module].append((date, score))

    from datetime import datetime              # Import the datetime module for date handling.

                                               
    for module, entries in scores_by_module.items():
        scores_by_module[module] = sorted(entries, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))

                                            
    plt.figure(figsize=(10, 6))             
                                                                            
    for module, entries in scores_by_module.items():
        dates = [entry[0] for entry in entries]                             # Extract the list of dates.
        scores = [entry[1] for entry in entries]                            # Extract the list of scores.
        plt.plot(dates, scores, marker='o', label=f"{module} Score")        # Plot scores with markers.

  # Add a title and axis labels to the plot.
    plt.title(f"Time-Series Scores for {name}")  # Graph title indicating the individual.
    plt.xlabel("Date")                           # Label for the x-axis (dates).
    plt.ylabel("Score")                          # Label for the y-axis (scores).
    plt.xticks(rotation=45)                      # Rotate the x-axis labels for better readability.
    plt.legend()                                 # Add a legend to distinguish scores from different modules.
    plt.grid()                                   # Add a grid for easier visual analysis of the graph.
    plt.tight_layout()                           # Adjust layout to prevent label overlap.
    plt.show()                                   # Display the completed plot.


def display_feedback(module_name, score):
    """
    Display feedback based on the user's score for a specific module.
    """
    feedback = {
        "Water": [
            "Excellent water conservation habits!",
            "Consider reducing shower time to save more water.",
            "Turn off the tap while brushing your teeth.",
            "Great job checking for leaks regularly!",
            "Use a bucket instead of a hose for cleaning tasks.",
            "Install water-saving showerheads to reduce water usage.",
            "Run dishwashers and washing machines only with full loads.",
            "Avoid using running water to thaw frozen foods.",
            "Fix dripping taps promptly to avoid water wastage.",
            "Harvest rainwater for gardening and outdoor cleaning."
        ],
        "Recycling": [
            "Your recycling habits are commendable!",
            "Start separating recyclable materials for better waste management.",
            "Composting organic waste is a great practice!",
            "Recycle electronic waste properly at designated centers.",
            "Avoid single-use plastics to reduce waste.",
            "Participate in local recycling programs or drives.",
            "Reuse containers and jars for storage.",
            "Educate others about the importance of recycling.",
            "Purchase products made from recycled materials.",
            "Dispose of hazardous waste like batteries and paints responsibly."
        ],
        "Energy": [
            "Fantastic energy conservation practices!",
            "Switch to LED bulbs for better energy efficiency.",
            "Minimize light usage during the day by using natural light.",
            "Installing solar panels is a significant step towards sustainability!",
            "Unplug devices when not in use to prevent phantom energy loss.",
            "Use energy-efficient appliances to reduce consumption.",
            "Schedule high-energy tasks during off-peak hours.",
            "Consider using smart thermostats to optimize energy use.",
            "Limit the use of heaters and air conditioners when possible.",
            "Encourage family members to adopt energy-saving habits."
            \
        ]
    }
    
    messages = random.sample(feedback[module_name], 2)
    print(f"{module_name} Feedback:\n")
    for message in messages:
        print(f"- {message}")


def main():
    """
    Main function to run the Eco-Friendly Tracker.
    Collects data, calculates scores, provides feedback, and visualizes results.
    """
    print("Welcome to the Eco-Friendly Tracker!\n")  

    # Get the current date for logging.
    date = datetime.date.today().isoformat()

    
    water_data = module1_water.collect_water_data()                                        # Collect water usage data.
    water_score, water_recommendations = module1_water.calculate_water_score(*water_data)  # Calculate score and recommendations.

    display_feedback("Water", water_score)   # Display water module feedback.
    for rec in water_recommendations:
        print(f"- {rec}")                    # Print each recommendation.

    
    recycling_data = module2_recycling.collect_recycling_data()                                                # Collect recycling data.
    recycling_score, recycling_recommendations = module2_recycling.calculate_recycling_score(*recycling_data)  # Calculate score and recommendations.

    display_feedback("Recycling", recycling_score)  # Display recycling module feedback.
    for rec in recycling_recommendations:
        print(f"- {rec}")                           # Print each recommendation.

    
    energy_data = module3_energy.collect_energy_data()                                          # Collect energy usage data.
    energy_score, energy_recommendations = module3_energy.calculate_energy_score(*energy_data)  # Calculate score and recommendations.

    display_feedback("Energy", energy_score)  # Display energy module feedback.
    for rec in energy_recommendations:
        print(f"- {rec}")                     # Print each recommendation.


    overall_score = performance_analysis.calculate_overall_score(water_score, recycling_score, energy_score)

    personal_scores = {  # Store individual scores in a dictionary.
        'Water': water_score,
        'Recycling': recycling_score,
        'Energy': energy_score,
        'Overall': overall_score
    }



    # --- Visualization ---
    performance_analysis.visualize_personal_scores(water_score, recycling_score, energy_score, overall_score)


                                       
    water_recommendations_str = ""     # Initialize an empty string.
    for rec in water_recommendations:  # Loop through each recommendation in the list.
        water_recommendations_str += rec + ", "  # Append each recommendation followed by a comma and space.
    water_recommendations_str = water_recommendations_str.rstrip(", ")  # Remove the trailing comma and space.

                                           
    recycling_recommendations_str = ""      # Initialize an empty string.
    for rec in recycling_recommendations:   # Loop through each recommendation in the list.
        recycling_recommendations_str += rec + ", "  # Append each recommendation followed by a comma and space.
    recycling_recommendations_str = recycling_recommendations_str.rstrip(", ")  # Remove the trailing comma and space.

                                           
    energy_recommendations_str = ""        # Initialize an empty string.
    for rec in energy_recommendations:     # Loop through each recommendation in the list.
        energy_recommendations_str += rec + ", "  # Append each recommendation followed by a comma and space.
    energy_recommendations_str = energy_recommendations_str.rstrip(", ")  # Remove the trailing comma and space.

                                         
    data.append([date, name, 'Water', water_score, water_recommendations_str])

                                        
    data.append([date, name, 'Recycling', recycling_score, recycling_recommendations_str])

                                        
    data.append([date, name, 'Energy', energy_score, energy_recommendations_str])

    # Save all the collected data to the CSV file.
    save_to_csv(filename, data)


                                                   
    with open("consumption_log.csv", "a") as f:    # Open the file in append mode.
                                                  
        f.write(f"{date},{water_score},{recycling_score},{energy_score},{overall_score}\n")  
        
     
    print("\nThank you for completing the tracker.")
    

# Set the file name where user data is stored.
filename = "eco_friendly_data.csv"

# Read the existing data from the specified CSV file.
existing_data = read_csv(filename)
                                           
name = input("Enter your name: ").lower()                     

# Check if the name already exists in the data.
name_exists = False                        # Initialize a flag to track if the name exists.
for row in existing_data:
                                           
    if row['Name'].lower() == name:
        name_exists = True                 # Set the flag to True if a match is found.
        break                              # Exit the loop once a match is found.

                                           
if name_exists:
    print(f"Welcome back, {name}!")        # Greet returning users.
    main()                                 # Run the main functionality of the program.
    plot_time_series_for_name(filename, name)  # Plot the time-series data for the user.
else:
    print(f"Hello, {name}! Let's get started.")  # Greet new users.
    main()                                       # Run the main functionality of the program.

    