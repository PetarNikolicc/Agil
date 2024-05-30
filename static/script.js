function openPopup(title, text) {
    document.getElementById('popupTitle').innerText = title;
    document.getElementById('popupText').innerText = text;
    document.getElementById('recipePopup').style.display = 'flex';
}

function closePopup() {
    document.getElementById('recipePopup').style.display = 'none';
}
