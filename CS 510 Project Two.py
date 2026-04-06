"""
    Class:   CS-510
    Author:  Amber Foster
    Date:    April 4, 2026

    Description:  Each function that needs to be completed has a comment at the top with
                  TODO written in it with instructions.

                  Within the function is a section with the comment #TODO where you will
                  insert your code as per the instructions.
"""

import os # Provides functions for interacting with the operating system for files, paths, directories
import psutil # requires pip install & Provides system and process utilities for CPU, memory, and disk stats
import sys # Provides access to system specific parameters and functions, including program exit handling
import threading # Enables creation and management of multiple threads for concurrent execution

"""
  Three provided Utility functions to use
"""

def printBlankLines(lines: int): # Prints a specified number of blank lines for cleaner output formatting
    for i in range(lines):
        print("")

def printMsg1(num): # Outputs the cube of the given number used by Thread 1
    print("Thread 1 cubed: {}" .format(num * num * num))


def printMsg2(num): # Outputs the square of the given number used by Thread 2
    print("Thread 2 squared: {}" .format(num * num))

"""
   TODO This function will display information about a file, size and file information.
   You can provide your own or use the projecttwo.txt file.

   Use psutil to get initial file information.
"""

def getFileDiskUsageStatistics() -> None:
    print("Getting Disk Statistics") # Added header for clean output formatting
    file_name = "./projecttwo.txt" # Defines the file the function will inspect or create
    
    #TODO INSERT YOUR CODE HERE
    # Part 1: Disk usage
    disk = psutil.disk_usage('/') # Retrieves total, used, and free disk space
    print(f"Total Disk Space: {disk.total / (1024**3):.2f} GB") # Converts bytes to GB
    print(f"Used Disk Space:  {disk.used / (1024**3):.2f} GB") # Displays used disk space
    print(f"Free Disk Space:  {disk.free / (1024**3):.2f} GB") # Displays free disk space
    
    # Part 2: File statistics
    if not os.path.exists(file_name): # Checks if the file exists
        with open(file_name, "w") as f: # Creates the file if missing
            f.write("This is a sample file for CS-510 Project Two.\n") # Writes sample text
            
    stats = os.stat(file_name) # Retrieves file metadata
    
    print("\nFile Information:") # Section header for readability
    print(f"  File Name:   {file_name}") # Displays file name
    print(f"  File Size:   {stats.st_size} bytes") # Displays file size in bytes
    print(f"  Created:     {stats.st_ctime}") # Displays creation timestamp
    print(f"  Last Modify: {stats.st_mtime}") # Displays last modified timestamp
    
    printBlankLines(2) # Adds spacing after section
    
"""
   TODO This should use psutil to retrieve standard and 
   virtual memory statistics
"""

def getMemoryStatistics() -> None:
    print("Getting Memory Statistics") # Section header for readability
    
    #TODO INSERT YOUR CODE HERE
    mem = psutil.virtual_memory() # Retrieves physical memory stats
    swap = psutil.swap_memory() # Retrieves virtual memory swap stats
    
    print("Physical Memory:") # Label for physical memory section
    print(f"  Total:     {mem.total / (1024**3):.2f} GB") # Total RAM
    print(f"  Used:      {mem.used / (1024**3):.2f} GB") # Used RAM
    print(f"  Available: {mem.available / (1024**3):.2f} GB") # Available RAM
    print(f"  Percent:   {mem.percent:.1f}%") # RAM usage percentage
    
    print("\nVirtual Memory (Swap):") # Label for swap memory section
    print(f"  Total:   {swap.total / (1024**3):.2f} GB") # Total swap space
    print(f"  Used:    {swap.used / (1024**3):.2f} GB") # Used swap
    print(f"  Free:    {swap.free / (1024**3):.2f} GB") # Free swap
    print(f"  Percent: {swap.percent:.1f}%") # Swap usage percentage
    
    printBlankLines(2) # Adds spacing after section

"""
   TODO This should use psutil to retrieve CPU statistics, including
   information on processes.
"""

def getCpuStatistics() -> None:
    print("Getting CPU Statistics") # Section header
    
    #TODO INSERT YOUR CODE HERE
    print(f"Logical CPU Count:  {psutil.cpu_count(logical=True)}") # Number of logical CPUs
    print(f"Physical CPU Count: {psutil.cpu_count(logical=False)}") # Number of physical cores
    
    print("\nCPU Usage Per Core:") # Label for per core usage
    per_core = psutil.cpu_percent(percpu=True, interval=1) # Retrieves CPU usage for each core
    for i, pct in enumerate(per_core): # Loops through each core
        print(f"  Core {i}: {pct:.1f}%") # Displays usage for each core
        
    total = psutil.cpu_percent(interval=1) # Retrieves total CPU usage
    print(f"\nTotal CPU Usage: {total:.1f}%") # Displays total CPU usage
    
    print("\nSample Processes (up to 5):") # Label for process list
    try:
        processes = list(psutil.process_iter(['pid', 'name', 'cpu_percent']))[:5] # Gets first 5 processes
        for proc in processes: # Loops through each process
            info = proc.info # Extracts process info dictionary
            print(f"  PID {info['pid']}: {info['name']} – {info['cpu_percent']}% CPU") # Displays process info
    except (psutil.NoSuchProcess, psutil.AccessDenied): # Handles permission or missing process errors
        print("  Unable to retrieve process information.")
        
    printBlankLines(2) # Adds spacing after section
    
"""
   TODO This function will show multi threading capabilities.

   Two threads should be created.
    
   One used to call the function "printMsg1" provided above.

   A second thread should call the function "printMsg2" provided above.
"""

def showThreadingExample() -> None:
    print("Demonstrating Threading") # Section header
    
    #TODO INSERT YOUR CODE HERE
    t1 = threading.Thread(target=printMsg1, args=(3,)) # Creates thread 1 to run printMsg1
    t2 = threading.Thread(target=printMsg2, args=(4,)) # Creates thread 2 to run printMsg2
    
    print("Starting Thread 1...") # Status message
    t1.start() # Starts thread 1
    
    print("Starting Thread 2...") # Status message
    t2.start() # Starts thread 2
    
    t1.join() # Waits for thread 1 to finish
    t2.join() # Waits for thread 2 to finish
    
    print("Done With Threading!") # Confirms both threads finished
    printBlankLines(2) # Adds spacing after section
    
"""
   TODO This function shows system error handling.

   Since out of memory, or out of disk space errors are difficult to create,
   we will use a divide by zero error and show the error handling being executed.
"""

def showErrorHandling() -> None:
    print("Demonstrating Error Handling") # Section header
    try:
        
        #TODO Insert your code here to cause a divide by zero error
        print("Attempting division by zero...") # Status message
        result = 10 / 0 # Intentional divide by zero error
        
    except ZeroDivisionError: # Catches divide by zero
        print("You can't divide by zero!")
        
    except MemoryError: # Catches memory allocation errors
        print("Memory Error!")
        
    else:
        print("Result is", res) # Runs only if no error occurs
        
    finally:
        print("Execution complete.") # Always runs
        
    printBlankLines(2) # Adds spacing after section
    
"""
   Main function, does not require modification.

   This calls the specific functions.
"""

def main() -> int:
    print("Starting Program") # Initial startup message indicating program execution has begun
    print("=============================") # Visual separator for cleaner, readable console output
    
    getFileDiskUsageStatistics() # Calls disk statistics function
    
    getCpuStatistics() # Calls CPU statistics function
    
    getMemoryStatistics() # Calls memory statistics function
    
    showThreadingExample() # Calls threading demonstration
    
    showErrorHandling() # Calls error handling demonstration
    
    print("Program Complete.") # Final status message indicating all functions have finished running
    return 0 # Returns 0 to signal successful program execution to the operating system
    
if __name__ == '__main__':
    sys.exit(main()) # Runs main() and exits cleanly
    
