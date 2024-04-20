const selectElement = function (element) {
    return document.querySelector(element);
};

let imgperfil = document.querySelector('#imgperfil');
let username = document.querySelector('#username');
let count = 0;

imgperfil.addEventListener('click', function(){
    count += 1 ;
    if( count > 1 ){
        imgperfil.style.display = 'none';
    }
});

username.addEventListener('click', function() {
    imgperfil.style.display = 'initial';
    count = 0;
});