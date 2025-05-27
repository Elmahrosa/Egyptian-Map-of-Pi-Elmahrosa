def customize_map(ax, color_map='viridis'):
    scatter = ax.collections[0]
    scatter.set_array(color_map)
    plt.draw()
