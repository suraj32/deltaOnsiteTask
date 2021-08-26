const allKeys = document.querySelectorAll('.key')

//allKeys.forEach( key =>{
//    console.log(key);
//    key.addEventListener('click', function(key){ playSound(key);});
//})
for (var i = 0 ; i < allKeys.length; i++) {
    allKeys[i].addEventListener('click' , playSound(allKeys[i]) ) ;
}

function playSound(key) {
    const audio = document.getElementById(key.dataset.sound);
    audio.currentTime = 0;
    audio.play();
    key.classList.add('shade');
    audio.addEventListener('ended', () => {
    key.classList.remove('shade')
    })
}
