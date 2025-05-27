import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, Button
import numpy as np

def create_interactive_map(data):
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(data['x'], data['y'], c=data['digit'], cmap='viridis', s=100, alpha=0.7)

    # Add a color bar
    cbar = plt.colorbar(scatter, ax=ax, label='Digits of Pi')
    
    # Set titles and labels
    plt.title('Interactive Egyptian Map of Pi', fontsize=16)
    plt.xlabel('X Coordinate', fontsize=14)
    plt.ylabel('Y Coordinate', fontsize=14)

    # Add a cursor for interactivity
    cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

    # Function to display digit information on hover
    def on_hover(event):
        if event.inaxes == ax:
            # Get the index of the nearest point
            distances = np.sqrt((data['x'] - event.xdata) ** 2 + (data['y'] - event.ydata) ** 2)
            index = np.argmin(distances)
            digit_info = f'Digit: {data["digit"][index]}'
            ax.set_title(digit_info, fontsize=16)

    # Connect the hover event
    fig.canvas.mpl_connect('motion_notify_event', on_hover)

    # Add zoom and pan functionality
    ax.set_xlim(min(data['x']) - 1, max(data['x']) + 1)
    ax.set_ylim(min(data['y']) - 1, max(data['y']) + 1)

    # Add a button to reset the view
    resetax = plt.axes([0.8, 0.01, 0.1, 0.05])
    button = Button(resetax, 'Reset View', color='lightgoldenrodyellow', hovercolor='0.975')
    
    def reset_view(event):
        ax.set_xlim(min(data['x']) - 1, max(data['x']) + 1)
        ax.set_ylim(min(data['y']) - 1, max(data['y']) + 1)
        plt.draw()

    button.on_clicked(reset_view)

    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = {
        'x': np.random.rand(100) * 10,
        'y': np.random.rand(100) * 10,
        'digit': np.random.randint(0, 10, 100)
    }
    create_interactive_map(sample_data)
