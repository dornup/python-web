// закругление через input:range
document.getElementById('ava_round').addEventListener('input', function() {
    console.log(this.value)
    document.querySelector('main .avatar .mask').style.borderRadius = this.value + '%';
})