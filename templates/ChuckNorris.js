window.addEventListener('load', function(){
    let btnGetJoke = document.getElementById('getJoke')

    btnGetJoke.addEventListener('click', async function(){
        let response = await fetch('https://api.chucknorris.io/jokes/random')
        let data_json = await response.json()
        
        let pJoke = document.getElementById('joke')

        pJoke.innerHTML = data_json.value

    })
})