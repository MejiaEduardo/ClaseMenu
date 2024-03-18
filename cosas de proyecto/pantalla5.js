 // Add a click event listener for the 'Acceder' submit button
 document.querySelector('form > button[type=submit]').addEventListener('click', (e) => {
    // Prevent the form from being submitted
    e.preventDefault();

    // Get input values
    const dni = document.getElementById('dni').value;
    const password = document.getElementById('password').value;

    // Perform form validation
    if (dni.length === 0 || password.length === 0) {
        alert('Please enter both DNI and password');
    } else {
        // If the inputs are valid, you can submit the form or perform further actions
        alert('DNI: ' + dni + '\nPassword: ' + password);
    }
});

// Add a click event listener for the 'Registrarme' button
document.querySelector('form > button[type=button]').addEventListener('click', () => {
    // Show a simple registration form
    const name = prompt('Enter your name');
    const age = prompt('Enter your age');
    const weight = prompt('Enter your weight');
    const height = prompt('Enter your height');

    // Display the user's input data
    alert('Name: ' + name + '\nAge: ' + age + '\nWeight: ' + weight + '\nHeight: ' + height);
});