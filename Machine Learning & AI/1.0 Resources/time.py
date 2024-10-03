import time

def myFunction():
    # function to run
    pass

startTime = time.time()  # start time
myFunction()
endTime = time.time()  # end time

totalTime = endTime - startTime  # Calculate total time
print(f"Total time: {totalTime} seconds")
