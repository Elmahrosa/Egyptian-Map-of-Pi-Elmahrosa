import numpy as np
import matplotlib.pyplot as plt

def analyze_pi_digits(digits):
    # Calculate frequency of each digit
    unique, counts = np.unique(digits, return_counts=True)
    frequency = dict(zip(unique, counts))
    
    # Calculate additional statistics
    total_digits = len(digits)
    mean = np.mean(counts)
    median = np.median(counts)
    mode = unique[np.argmax(counts)]
    
    # Create a bar plot for frequency distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(frequency.keys(), frequency.values(), color='skyblue', edgecolor='black')

    # Add data labels on top of the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    # Set titles and labels
    plt.title('Frequency Distribution of Pi Digits', fontsize=16)
    plt.xlabel('Digits', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(np.arange(0, 10, 1))  # Set x-ticks for digits 0-9
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display statistics on the plot
    stats_text = f'Total Digits: {total_digits}\nMean: {mean:.2f}\nMedian: {median:.2f}\nMode: {mode}'
    plt.figtext(0.15, 0.85, stats_text, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

    # Show the plot
    plt.show()

    # Optionally, return the frequency dictionary for further analysis
    return frequency

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration (first 100 digits of Pi)
    pi_digits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 
                 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 
                 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 0, 2, 8, 8, 4, 1, 9, 
                 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 0, 2, 8, 8, 4, 1, 9, 7]
    
    analyze_pi_digits(pi_digits)
