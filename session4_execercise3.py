from faker import Faker
import os, time
import threading

# Create a Faker object to generate random phrases
faker = Faker()

# Create a lock object to ensure only one thread writes to the file at a time
file_lock = threading.Lock()

def generate_phrase_and_save():

    # Specify the folder and file name
    folder_name = "output"
    file_name = "phrases.txt"
    file_path = os.path.join(folder_name, file_name)

    # Create the folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)

    # Generate a random sentence using Faker
    phrase = faker.sentence()

    # Open the file in append mode
    with open(file_path, "a") as file:
        # Create a log entry with the generated phrase
        log_entry = f"Saved: {phrase}\n"
        
        # Write the log entry to the file
        file.write(log_entry)


def main():
    # Acquire the file lock before writing to the file
    file_lock.acquire()
    # Iterate over each thread ID
    for thread_id in thread_ids:
    
        # Create a new thread to run the generate_phrase_and_save function
        # Pass the thread ID as an argument to the function
        thread = threading.Thread(target=generate_phrase_and_save, args=(thread_id,))
        
        # Append the created thread to the list of threads
        threads.append(thread)
        
        # Start the thread, beginning its execution
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
    
        # Join each thread, ensuring that the main thread waits for their completion
        thread.join()

    # Release the lock
    file_lock.release()

if __name__ == "__main__":
    main()



# List of thread IDs to create
thread_ids = [0, 1, 2, 3]

# List to hold the created thread objects
threads = []

