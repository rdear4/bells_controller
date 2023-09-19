let tempo = 1.00
let isPlaying = false
let buttonsDisabled = false;

let pauseSymbol = "⏸"
let playSymbol = "⏵"

$(document).ready(() => {

    //Disable all control buttons
    $('.control-button span').addClass(buttonsDisabled ? 'disabled' : '')

    //Get list of songs from server
    let songTitles = songs.reduce( (acc, curr) => [...acc, curr.title], [])



    //Add actions to the elements
    $("#song-list").on('change', (e) => {
        console.log($(e.target).val())
    })

    $("#inc-tempo-btn").on('click', () => {
        tempo += 0.05
       
        updateTempoDisplay()
        //make req to update tempo

    })
    
    $("#dec-tempo-btn").on('click', () => {
        tempo -= 0.05
      
        updateTempoDisplay()

        //make req to update tempo

    })

    $("#stop-btn").on("click", () => {
        isPlaying = false;

        $("#stop-btn").addClass("disabled")
        $("#play-pause-btn").text( playSymbol)
    })

    $("#play-pause-btn").on("click", () => {

        isPlaying = !isPlaying

        $("#play-pause-btn").text(isPlaying ? pauseSymbol : playSymbol)

        if (isPlaying) {
            $("#stop-btn").removeClass("disabled")
        } else {
            $("#stop-btn").addClass("disabled")
        }
        ///make fetch request to upate play pause state
    })



    for (let songIndex in songs) {
        // console.log(songIndex)
        // console.log(songs[songIndex])
        $("#song-list").append($(`<option value=${songIndex}>${songs[songIndex].title}</option>`))

    }
    

})

const updateTempoDisplay = () => {

    $("#tempo").text(`${tempo.toFixed(2)} x`)
}