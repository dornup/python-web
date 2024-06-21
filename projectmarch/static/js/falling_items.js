document.addEventListener('DOMContentLoaded', () => { // когда страница прогружена
    let meme_click = document.querySelector('.meme_click');
    let shelest_tree = new Audio('/static/sound/tree_s.mp3');
    let falling_items = document.querySelector('.falling_items');
    let documentH = document.documentElement.scrollHeight; // высота страницы
    let viewportH = window.innerHeight; // высота viewport
    let totalH = documentH - viewportH;// полная высота без окна просмотра
    // обработка нажатия
    meme_click.addEventListener('click', () => {
        shelest_tree.play();

        let div = document.createElement('div');
        div.classList.add('apple');
        div.style.left = `${Math.floor(Math.random() * 98)}vw`;
        falling_items.appendChild(div);

        // падение
        startTime = null;
        function fall(timestamp) {
            if (!startTime) startTime = timestamp // инициализация времен начала анимации
            
            let progress = timestamp - startTime; // прошедшее время с начала анимации
            let position = Math.min(progress / 10, totalH); // текущая позиция

            div.style.top = `${position}px`

            if (position < totalH) {

                requestAnimationFrame(fall)
            }
        };

        requestAnimationFrame(fall);
    });
    
});