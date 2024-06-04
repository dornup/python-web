// сердечки в welcome зону
let htmlbg_logo = document.querySelector('section#welcome .bg_logo');
let heart_x = 0; let heart_y = 0;
for (let row = 0; row < 2; row++) {
    for (let column=0; column < 5; column++) {
        let img_tag = document.createElement('img');
        img_tag.src = '../static/img/bg-filler.png'
        // img_tag.style.left = `${heart_x}px`
        htmlbg_logo.append(img_tag)
        // heart_x += 100;
    }
    // heart_y += 100;
}