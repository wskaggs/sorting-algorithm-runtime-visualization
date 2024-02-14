from algorithms import insertion_sort, merge_sort
from random import shuffle
from time import perf_counter
import matplotlib.pyplot as plt


def visualize_sorting_algorithm_runtime() -> None:
    """
    Experimentally collect and visualize the runtimes for various sorting algorithms

    :return: None
    """
    # Configurations for the analysis
    algorithms = {"insertion sort": insertion_sort, "merge sort": merge_sort}
    input_sizes = list(range(1, 101))
    trials = 10

    # Run the runtime analysis
    runtime_analysis = {algorithm_name: [] for algorithm_name in algorithms}

    for algorithm_name, algorithm in algorithms.items():
        for input_size in input_sizes:
            lst = list(range(input_size))
            total_time = 0

            for _ in range(trials):
                shuffle(lst)
                start_time = perf_counter()
                algorithm(lst)
                total_time += perf_counter() - start_time

            runtime_analysis[algorithm_name].append(total_time / trials)

    # Visualize the collected data
    plt.title("Sorting Algorithm Runtime vs. Input Size")
    plt.xlabel("Input Size")
    plt.ylabel("Average Runtime (seconds)")

    for algorithm_name, runtimes in runtime_analysis.items():
        plt.plot(input_sizes, runtimes, label=algorithm_name)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    visualize_sorting_algorithm_runtime()
