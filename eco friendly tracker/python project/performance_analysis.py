import matplotlib.pyplot as plt                                # Importing the Matplotlib library for creating visualizations.

def calculate_overall_score(water_score, recycling_score, energy_score):
    """
    Calculate the overall score by averaging scores from all modules.
    """
    return (water_score + recycling_score + energy_score) / 3   # Return the average score


def visualize_personal_scores(water_score, recycling_score, energy_score, overall_score):
    """
    Visualize personal scores for all modules using a bar chart.
    """
    modules = ['Water', 'Recycling', 'Energy', 'Overall']         # List of module names for labeling the x-axis.
    scores = [water_score, recycling_score, energy_score, overall_score]  # Corresponding scores for the modules.

# Create a bar chart with the module scores
    plt.bar(modules, scores, color=['blue', 'green', 'orange', 'red'])
    plt.title('Personal Performance Scores')       # Title of the chart.
    plt.ylabel('Scores')                           # Label for the y-axis.
    plt.ylim(0, 100)                               # Set the range of the y-axis to be between 0 and 100
    plt.show()                                     # Display the chart

