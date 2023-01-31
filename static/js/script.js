// Add star rating
const rating = document.querySelector('form[name=rating]');
    alert('Сосаать', rating);
rating.addEventListener("change", function (e) {
    console.log('Сосу', this.action)
    // Получаем данные из формы
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
        .then(response => alert("Рейтинг установлен"))
        .catch(error => alert("Ошибка"));
});