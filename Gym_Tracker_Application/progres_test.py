from progress.bar import ChargingBar
import time

# Function to simulate a time-consuming task
def simulate_task(duration):
    time.sleep(duration)

# Number of iterations for your task
total_iterations = 100

# Create a progress bar
progress_bar = ChargingBar('Processing', max=total_iterations)

# Perform the task in a loop
for iteration in range(total_iterations):
    # Simulate a time-consuming task
    simulate_task(0.01)

    # Update the progress bar
    progress_bar.next()

# Finish the progress bar
progress_bar.finish()

print("Task completed!")