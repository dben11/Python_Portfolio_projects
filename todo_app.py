import json



#Define an empty python data structure that will hold the todo items a list
todo_items = []

# #define a function that will add a todo item to the list
# def add_todo_item(description):
#     # determine a unique ID for the task
#     # If the main tasks data structure IS empty:
#     #   set new_id to 1
#     if not todo_items:
#         new_id = 1
         
    
#     else:
#         new_id = max(item ['id'] for item in todo_items) + 1
    
#     # Create a new task item with the generated ID, provided description, and a default completion status  
#     # Create new_task_item with:
#     new_task_item = {
#             #   - id: new_id

#         'id': new_id,
#             #   - description: description

#         'description': description,
#             #   - completed: False

#         'completed': False
#     }

#     # Add the new task item to the main tasks data structure
#     # ADD new_task_item TO the main tasks data structure
#     todo_items.append(new_task_item)

#     # Inform the user user that the task was added successfully
#     # Print confirmation message with the new task ID and description
#     print(f"todo item added successfully with ID {new_id}: {description}")


# # Test calls (keep these for now to verify)
# add_todo_item("Buy groceries")
# add_todo_item("Walk the dog")   
# add_todo_item("Read a book")
# add_todo_item("Rice")

#     # NEW: Print the entire todo_items list after adding to see the structured data
# print("\nCurrent todo items list after adding")
# print(todo_items)


# Define a function to view all todo items
def view_todo_items():
   
    if not todo_items:
        print("No Task yest")
        return
    # If there are tasks, print a clear header
    # 2. Print a header for the to-do list
    # If todo_items is not empty, print "--- Your TO-DO List ---
    if todo_items:
        print("--- Your TO-DO List ----")

    

# 3. Go through each task in the list
    for task in todo_items:
        
        if task['completed']:
            status_indicator_string = "[X]"
        else:
            status_indicator_string = "[ ]"
        # Print the task with its status, ID, and description
        # Print the task in the format: "[status] ID - description"
        print(f"{status_indicator_string} {task['id']} ** {task['description']}")
#  add  a call to view_todo_items to see the current list
view_todo_items()
# Print a line like "--- End of To-Do List ---"

print("--- End of To-Do List ---")






              
# def mark_todo_item_completed(task_id):
#     task_found = False  # Assume the task is not found initially
#     for task in todo_items:  # Go through each task in the todo_items list
#         if task['id'] == task_id:  # If the task ID matches the provided ID
#             task['completed'] = True  # Mark the task as completed
#             task_found = True  # Set task_found to True
#             print(f"Task {task_id} marked as completed: {task['description']}")
#             break  # Stop searching (optional, but efficient if only one match is expected)

#     # After checking all tasks, if the task was not found
#     if task_found is False:  # If task_found IS FALSE
#         print(f"Task with ID {task_id} was not found.")

# # Example: Mark the task with ID 2 as completed
# mark_todo_item_completed(1)
# view_todo_items()

# # Define a function to delete a todo item by its ID
# def delete_todo_item(task_id):
#     task_found = False
#     deleted_description = ""
#     for task in todo_items:
#         if task['id'] == task_id:
#             deleted_description = task['description']
#             todo_items.remove(task)  # Remove the task from the list
#             task_found = True
#             print(f"Task {task_id} deleted: {deleted_description}")
#             break   # Stop searching after deleting the task

#     if not task_found:
#         print(f"Task with ID {task_id} was not found.")

# delete_todo_item(2)
# view_todo_items()

# Define a function to save the todo items to a JSON file
def save_tasks():
    global todo_items
    filename = "tasks.json"

    try:
        # Open the file in write mode('w')
        with open(filename, 'w') as file:
            json.dump(todo_items, file, indent=4)
        print(f"Tasks saved to {filename} successfully.")
    except IOError as e:
        print(f"Error saving tasks to {filename}: {e}")

    except Exception as e:
        print(f"An unexpected error occurred while saving tasks: {e}")

save_tasks()

# Define a function to load todo items from a JSON file
def load_task():
    global todo_items
    filename = "tasks.json"

    try:
        # open the file in 'read' mode ('r')
        with open(filename, 'r') as file:
            loaded_data = json.load(file)
            todo_items = loaded_data
        print(f"Tasks loaded from {filename} successfully.")

    except FileNotFoundError:
        print("No existing tasks file found. Starting with an empty list.")

    except json.JSONDecodeError:
        print("Error reading tasks file (corrupted JSON). Starting with an empty list.")
        todo_items.clear()

    except Exception as e:
        print(f"An unexpected error occured while loading tasks: {e}.starting with an empty list")
        todo_items.clear()

load_task()
print("\n--- Current tasks after loading (of empty) ---")
view_todo_items()

# add_todo_item("Learn Python")
# add_todo_item("Build a web app")

# print("\n--- Current tasks after adding new items ---")
# view_todo_items()

# mark_todo_item_completed(1)
# delete_todo_item(3)

print("\n--- Current tasks after marking and deleting ---")
view_todo_items()

# Save the current tasks to the JSON file after modifications
save_tasks()

# End of todo_app.py
print("\nScript finished. Check your 'task.json' file!")
print("Then, try running the script again with the 'add/mark/delete' lines commented out to see if tasks persist.")

