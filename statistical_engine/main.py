from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes


def run_statistical_analysis():
    print("=== STATISTICAL ANALYSIS ===\n")

    data = [10, 20, 30, 40, 50]
    engine = StatEngine(data)

    print(f"Data: {data}\n")

    print(f"Mean: {engine.get_mean():.2f}")
    print(f"Median: {engine.get_median():.2f}")
    print(f"Mode: {engine.get_mode()}")
    print(f"Sample Variance: {engine.get_variance():.2f}")
    print(f"Population Variance: {engine.get_variance(is_sample=False):.2f}")
    print(f"Standard Deviation: {engine.get_standard_deviation():.2f}")
    print(f"Outliers: {engine.get_outliers()}")

    print("\n")


def run_simulation():
    print("=== MONTE CARLO SIMULATION (LLN DEMO) ===\n")

    for days in [100, 10000, 100000]:
        crashes, prob = simulate_crashes(days)

        print(f"Days: {days}")
        print(f"Crashes: {crashes}")
        print(f"Simulated Probability: {prob:.5f}")
        print("-" * 40)


if __name__ == "__main__":
    run_statistical_analysis()
    run_simulation()