"""
progressbar.py

A simple progress bar for Python
Available Functions:
- print_progress(iteration, loops, n, algo_name="algorithm"): Print the bar
"""


def print_progress(iteration, loops, n, algo_name="algorithm"):
    """
    Print the progress bar

    Parameters:
    iteration: int: The current iteration
    loops: int: The total number of loops
    n: int: The size of the data
    algo_name: str: The name of the algorithm
    """
    progress = (iteration) / loops
    bar_length = 50
    filled_length = int(bar_length * progress)
    bar_graphic = "=" * filled_length + "-" * (bar_length - filled_length)
    percent = progress * 100
    percent_string = f"{percent:6.2f}".zfill(5)
    print(f"\r|{bar_graphic}| {percent_string}% Running {
          algo_name} for size of {n} elements {loops} times...", end="")
