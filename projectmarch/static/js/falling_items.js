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

        let falling_object = document.createElement('div');
        falling_object.classList.add('apple');
        falling_object.style.left = `${Math.floor(Math.random() * 98)}vw`;
        falling_items.appendChild(falling_object);
        
        // само падение
        function getHeight() {
            return Math.max(
                document.body.scrollHeight, // высота содержимого body, включая прокрутку
                document.documentElement.scrollHeight, // высота финальной странички
                document.body.offsetHeight, // высота body, включая border и padding
                document.documentElement.offsetHeight, // высота document, включая border и padding
                document.body.clientHeight, // высота видимой части border, включая padding, исключая border
                document.documentElement.clientHeight, // высот
            )
        }

        let currentTop = 0;
        let speed = 5; // скорость падения в px
       
        function fall() {
                const pageHeight = getHeight(); //получаем высоту страницы
                const appleHeight = falling_object.offsetHeight; // высота падающего элемента
                const targetTop = pageHeight - appleHeight; // сколько падать (чтобы не выпасть)

                if (currentTop < targetTop) {
                    currentTop += speed;
                    if (currentTop > targetTop) currentTop = targetTop;
                    falling_object.style.top = currentTop + 'px';
                    requestAnimationFrame(fall);
                };  
        }
        requestAnimationFrame(fall); // запускаем анимацию
        /*
        1. Планирование перерисовки на следующих циклах перериисовки -> браузер пытается синхронизировать смену кадров и анимацию
        2. Более простая остановка анимации -> просто прекратили вызовы request 
         */
    });
    
});