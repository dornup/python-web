let meme_click = document.querySelector('.meme_click');
let shelest_tree = new Audio('/static/sound/tree_s.mp3');
let falling_items = document.querySelector('.falling_items');
meme_click.addEventListener('click', () => {
    shelest_tree.play();

    let div = document.createElement('div');
    div.classList.add('apple');
    div.style.left = `${Math.floor(Math.random() * 98)}vw`;
    falling_items.appendChild(div)
});