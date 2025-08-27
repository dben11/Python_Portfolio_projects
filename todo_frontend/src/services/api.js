// Define the base URL for your Flask API.
const API_BASE_URL = "http://127.0.0.1:5000";

// Helper function to handle common API response errors
const handleResponse = async (response) => {
  if (!response.ok) {
    let errorMessage = `HTTP error! Status: ${response.status}`;
    try {
      if (response.status !== 204) {
        const errorData = await response.json();
        errorMessage = errorData.error || errorMessage;
      }
    } catch (parseError) {
      console.error("Failed to parse error response:", parseError);
    }
    throw new Error(errorMessage);
  }
  // For Delete (204 No Content), there's no body to parse
  if (response.status === 204) {
    return null;
  }
  return response.json();
};

// -------------------------------------------------------------------------
// API Functions for Tasks (CRUD Operations)
// Each function exports an `async` function that performs a specific API call
// -------------------------------------------------------------------------

/**
 * Fetch all tasks from the API
 */

export const fetchTasks = async () => {
  const response = await fetch(`${API_BASE_URL}/tasks`);
  return handleResponse(response);
};

/**
 * Crate a new task in the API
 * @param {string} description - The description of the new task
 */
export const createTask = async (description) => {
  const response = await fetch(`${API_BASE_URL}/tasks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ description, completed: false }),
  });
  return handleResponse(response);
};

/**
 * Update an existing task in the API.
 * @param {number} id - The ID of the task to update
 * @param {boolean} completed - The new completion status
 */
export const updateTask = async (id, completed) => {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ completed }),
  });
  return handleResponse(response);
};

// updateTaskDescription
/**
 *  Update an existing task's description in the API.
 *  @param {number} id - The ID of the task to update
 *  @param {string} description - The new description
 */

export const updateTaskDescription = async (id, description) => {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ description }),
  });
  return handleResponse(response);
};

/**
 * Delete a task from the API.
 * @param {number} id - The ID of the task to delete
 */
export const deleteTask = async (taskId) => {
  const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
    method: "DELETE",
  });
  return handleResponse(response);
};
