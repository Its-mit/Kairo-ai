const container = document.querySelector('.auth-container');
const LoginLink = document.querySelector('.SignInLink');
const RegisterLink = document.querySelector('.SignUpLink');

RegisterLink.addEventListener('click', ()=>{
    container.classList.add('active');
})