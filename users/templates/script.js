// Reference of elements of login form
const loginForm = document.getElementById('loginForm');
const loginUsername = document.getElementById('loginUsername');
const loginPassword = document.getElementById('loginPassword');
const loginButton = document.getElementById('loginButton');

// Reference of elements of signup form
const signUpForm = document.getElementById('signUpForm');
const signUpUsername = document.getElementById('signUpUsername');
const signUpemail = document.getElementById('signUpemail')
const fname = document.getElementById('fname');
const lname = document.getElementById('lname');
const signUpPassword = document.getElementById('signUpPassword');
const signUpButton = document.getElementById('signUpButton');

// Reference of elements of reset form
const resetPassForm = document.getElementById('resetPassForm');
const resetUsername = document.getElementById('resetUsername');
const resetButton = document.getElementById('resetButton');

const loginContainer = document.getElementById('loginContainer');
const signupContainer = document.getElementById('signupContainer');
const resetPassContainer = document.getElementById('resetPassContainer');
const showSignUp = document.getElementById('showSignUp');
const showLogin = document.getElementById('showLogin');
const showReset = document.getElementById('showReset');
const showSignUpFromReset = document.getElementById('showSignUpFromReset');
const showLoginFromReset = document.getElementById('showLoginFromReset');

// Function to check if the fields are empty or not
function validateLoginFields() {
    if (loginUsername.value.trim() !== '' && loginPassword.value.trim() !== '') {
        loginButton.disabled = false;
    } else {
        loginButton.disabled = true;
    }
}

// Function to check if the fields are empty or not for sign-up form
function validateSignUpFields() {
    if (signUpUsername.value.trim() !== '' && fname.value.trim() !== '' && lname.value.trim() !== '' && signUpPassword.value.trim() !== '') {
        signUpButton.disabled = false;
    } else {
        signUpButton.disabled = true;
    }
}

// Function to check if the fields are empty or not for reset form
function validateResetFields() {
    if (resetUsername.value.trim() !== '') {
        resetButton.disabled = false;
    } else {
        resetButton.disabled = true;
    }
}

// Event listeners for login form
loginUsername.addEventListener('input', validateLoginFields);
loginPassword.addEventListener('input', validateLoginFields);

// Event listeners for sign-up form
signUpUsername.addEventListener('input', validateSignUpFields);
fname.addEventListener('input', validateSignUpFields);
lname.addEventListener('input', validateSignUpFields);
signUpPassword.addEventListener('input', validateSignUpFields);

// Event listeners for reset form
resetUsername.addEventListener('input', validateResetFields);

// Initial validation call for login form
validateLoginFields();

// Initial validation call for sign-up form
validateSignUpFields();

// Initial validation call for reset form
validateResetFields();

// To show sign-up form
showSignUp.addEventListener('click', function(event) {
    event.preventDefault();
    loginContainer.style.display = 'none';
    signupContainer.style.display = 'block';
    resetPassContainer.style.display = 'none';
});

// To show login form
showLogin.addEventListener('click', function(event) {
    event.preventDefault();
    signupContainer.style.display = 'none';
    loginContainer.style.display = 'block';
    resetPassContainer.style.display = 'none';
});

// To show reset form
showReset.addEventListener('click', function(event) {
    event.preventDefault();
    loginContainer.style.display = 'none';
    signupContainer.style.display = 'none';
    resetPassContainer.style.display = 'block';
});

// To show sign-up form from reset form
showSignUpFromReset.addEventListener('click', function(event) {
    event.preventDefault();
    resetPassContainer.style.display = 'none';
    signupContainer.style.display = 'block';
});

// To show login form from reset form
showLoginFromReset.addEventListener('click', function(event) {
    event.preventDefault();
    resetPassContainer.style.display = 'none';
    loginContainer.style.display = 'block';
});

// main page
loginForm.addEventListener('submit', function(event){
    event.preventDefault();
    window.location.href = 'search.html';
})
