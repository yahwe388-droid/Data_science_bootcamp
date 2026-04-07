import random


def simulate_crashes(days, crash_prob=0.045):
    if days <= 0:
        raise ValueError("Days must be a positive integer.")

    crashes = 0

    for _ in range(days):
        if random.random() < crash_prob:
            crashes += 1

    probability = crashes / days
    return crashes, probability