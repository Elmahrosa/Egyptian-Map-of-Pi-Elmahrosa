def export_map(fig, filename, format='png'):
    fig.savefig(f"{filename}.{format}", format=format)
    print(f"Map exported as {filename}.{format}")
