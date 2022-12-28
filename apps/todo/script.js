// Get references to the form and to-do items container
const todoForm = document.getElementById('todo-form');
const todoItems = document.getElementById('todo-items');

// Add a submit event listener to the form
todoForm.addEventListener('submit', (event) => {
  // Prevent the form from submitting
  event.preventDefault();

  // Get the value of the input field
  const todoText = document.querySelector('.todo-input').value;

  // Create a new to-do item element
  const todoItem = document.createElement('div');
  todoItem.classList.add('todo-item');

  // Add a checkbox to the to-do item
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.addEventListener('change', (event) => {
    // Toggle the "completed" class when the checkbox is checked or unchecked
    if (event.target.checked) {
      todoItem.classList.add('completed');
    } else {
      todoItem.classList.remove('completed');
    }
  });
  todoItem.appendChild(checkbox);

  // Add the to-do text to the to-do item
  const text = document.createElement('span');
  text.textContent = todoText;
  todoItem.appendChild(text);

  // Add a delete button to the to-do item
  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Delete';
  deleteButton.addEventListener('click', () => {
    // Remove the to-do item when the delete button is clicked
    todoItems.removeChild(todoItem);
  });
  todoItem.appendChild(deleteButton);

  // Add the to-do item to the to-do items container
  todoItems.appendChild(todoItem);

  // Reset the form
  event.target.reset();
});
