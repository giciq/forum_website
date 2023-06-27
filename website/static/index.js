const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', ()=>{
   wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=>{
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=>{
    wrapper.classList.remove('active-popup');
});

function myMap(){
    var opcjeMapy = {
        zoom: 15,
        center: new google.maps.LatLng(51.2356705,22.5466661),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var mapa = new google.maps.Map(document.getElementById("mapka"), opcjeMapy);
};
function deleteNote(noteId){
    fetch('/delete-note',{
        method: 'POST',
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) =>{
        window.location.href = "/mynotes"
    })
}