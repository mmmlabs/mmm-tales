import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Helper Functions to Calculate and Plot Contributions
def plot_contributions(df, coefs, model_name="Model"):
    """
    Plots the contributions of a model as a percentage of total contributions.
    
    Parameters:
    df (DataFrame): DataFrame containing the variables that were used to create the model.
    coefs (dict or list): A dictionary or list of coefficients where the keys or indices match the columns of the DataFrame.
    model_name (str): The name of the model (used in the title of the plot).
    """
    # If coefs is a list or ndarray, convert it to a dictionary
    if isinstance(coefs, (list, np.ndarray)):
        coefs = dict(zip(df.columns, coefs))
    
    # Calculate the contributions of each variable
    contributions = {var: coefs[var] * df[var].sum() for var in coefs.keys()}
    
    # Calculate total contributions
    total_contributions = sum(contributions.values())
    
    # Calculate contributions as percentages
    contributions_pct = {k: (v / total_contributions) * 100 for k, v in contributions.items()}
    
    # Convert to a DataFrame for easier plotting
    contributions_df = pd.DataFrame(list(contributions_pct.items()), columns=['Variable', 'Contribution (%)'])
    
    # Keep the order of variables as in the DataFrame, but reverse the order for plotting
    contributions_df['Variable'] = pd.Categorical(contributions_df['Variable'], categories=df.columns, ordered=True)
    contributions_df = contributions_df.sort_values('Variable', ascending=False)
    
    # Plot the contributions as a horizontal bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.barh(contributions_df['Variable'], contributions_df['Contribution (%)'], color='lightcoral')
    
    # Add the percentage labels at the end of each bar
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                 f'{bar.get_width():.0f}%', 
                 va='center')
    
    plt.xlabel('Contribution (%)')
    plt.title(f'Variable Contributions as % of Total Contributions ({model_name})')
    plt.show()

# Function to plot contributions from all models
def calculate_contributions(df, coefs):
    """
    Calculates the contributions of each variable in a model.
    
    Parameters:
    df (DataFrame): DataFrame containing the variables that were used to create the model.
    coefs (dict or list): A dictionary or list of coefficients where the keys or indices match the columns of the DataFrame.
    
    Returns:
    contributions_pct (dict): A dictionary of contributions as percentages of total contributions.
    """
    # If coefs is a list or ndarray, convert it to a dictionary
    if isinstance(coefs, (list, np.ndarray)):
        coefs = dict(zip(df.columns, coefs))
    
    # Calculate the contributions of each variable
    contributions = {var: coefs[var] * df[var].sum() for var in coefs.keys()}
    
    # # Calculate total contributions
    # total_contributions = sum(contributions.values())
    
    # # Calculate contributions as percentages
    # contributions_pct = {k: (v / total_contributions) * 100 for k, v in contributions.items()}
    
    return contributions
    
def plot_multi_model_contributions(contributions_pct, df_columns, model_name="Model"):
    """
    Plots the contributions of multiple models as grouped horizontal bar charts.
    
    Parameters:
    contributions_pct (dict of lists): A dictionary where keys are model names and values are dictionaries of contributions as percentages of total contributions.
    df_columns (Index): The columns of the DataFrame to ensure the order of variables.
    model_name (str): The name of the combined plot.
    """
    # Convert the dictionary into a DataFrame for easier plotting
    contributions_df = pd.DataFrame(contributions_pct)
    
    # Ensure the order of variables matches the DataFrame columns
    contributions_df.index = pd.Categorical(contributions_df.index, categories=df_columns, ordered=True)
    contributions_df = contributions_df.sort_index()

    # Plot the contributions as grouped horizontal bar charts
    contributions_df.plot(kind='barh', figsize=(12, 7))

    # Add labels and title
    plt.ylabel('Variable')
    plt.xlabel('Contribution (%)')
    plt.title(f'Contributions % ({model_name})')
    plt.legend(title="Model")
    plt.tight_layout()
    plt.show()