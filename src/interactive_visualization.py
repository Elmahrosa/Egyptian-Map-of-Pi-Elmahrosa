import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
&nbsp;
&nbsp;

def create_interactive_map(data):
    fig, ax = plt.subplots()
    scatter = ax.scatter(data['x'], data['y'], c=data['digit'], cmap='viridis')
&nbsp;
&nbsp;

    cursor = Cursor(ax, useblit=True, color='red', linewidth=1)
&nbsp;
&nbsp;

    plt.colorbar(scatter, label='Digits of Pi')
    plt.title('Interactive Egyptian Map of Pi')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()
