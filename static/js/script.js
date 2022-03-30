const hideBtn = document.getElementById("updateBtn");
const pannel = document.getElementById("change_profile");

hideBtn.addEventListener('click', () => {
    pannel.classList.toggle('hide')
})