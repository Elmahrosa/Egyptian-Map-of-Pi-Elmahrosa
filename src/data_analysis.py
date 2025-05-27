import numpy as np
import matplotlib.pyplot as plt
&nbsp;
&nbsp;

def analyze_pi_digits(digits):
    unique, counts = np.unique(digits, return_counts=True)
    frequency = dict(zip(unique, counts))
&nbsp;
&nbsp;

    plt.bar(frequency.keys(), frequency.values())
    plt.title('Frequency Distribution of Pi Digits')
    plt.xlabel('Digits')
    plt.ylabel('Frequency')
    plt.show()
