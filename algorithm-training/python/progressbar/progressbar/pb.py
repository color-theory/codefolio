def print_progress(iteration, loops, n):
		progress = (iteration) / loops
		bar_length = 50
		filled_length = int(bar_length * progress)
		bar = "=" * filled_length + "-" * (bar_length - filled_length)
		percent = progress * 100
		percent_string = f"{percent:3.2f}".zfill(5)
		print(f"\r|{bar}| {percent_string}% Running sequential search for size of {n} elements {loops} times...", end="")