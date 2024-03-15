// сердечки в welcome зону
let htmlbg_logo = document.querySelector('section#welcome .bg_logo');
let heart_x = 0; let heart_y = 0;
for (let row = 0; row < 2; row++) {
    for (let column=0; column < 5; column++) {
        let img_tag = document.createElement('img');
        img_tag.src = '{{ url_for("static", filename="img/logo1.png") }}'
        htmlbg_logo.append(img_tag)
        heart_x += 50;
    }
    heart_y += 50;
}