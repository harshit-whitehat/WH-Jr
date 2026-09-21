let words = [
  {
    word: "Piano",
    hint: "A musical instrument",
    numOfLetters: 5,
    letters: ["A", "I", "N", "O", "P"],
  },
  {
    word: "Carrom",
    hint: "An indoor game",
    numOfLetters: 6,
    letters: ["A", "C", "M", "O", "R"],
  },
  {
    word: "Zucchini",
    hint: "A vegetable",
    numOfLetters: 8,
    letters: ["C", "H", "I", "N", "U", "Z"],
  },
  {
    word: "Fridge",
    hint: "A home appliance",
    numOfLetters: 6,
    letters: ["D", "E", "F", "G", "I", "R"],
  },
  {
    word: "Mongolia",
    hint: "A country in East Asia",
    numOfLetters: 8,
    letters: ["A", "G", "I", "L", "M", "N", "O"],
  },
  {
    word: "Santiago",
    hint: "Capital of Chile",
    numOfLetters: 8,
    letters: ["A", "G", "I", "N", "O", "S", "T"],
  },
  {
    word: "Topaz",
    hint: "A rare gemstone",
    numOfLetters: 5,
    letters: ["A", "O", "P", "T", "Z"],
  },
];

$(function () {
  let word = words[Math.floor(Math.random() * words.length)];

  let livesSpan = document.createElement("span");
  livesSpan.innerHTML = `Lives: 5`;
  $("#header").append(livesSpan);

  let hintSpan = document.createElement("span");
  hintSpan.innerHTML = `Hint: ${word.hint}`;
  $("#header").append(hintSpan);

  let lettersSpan = document.createElement("span");
  lettersSpan.innerHTML = `${word.numOfLetters} Letters`;
  $("#header").append(lettersSpan);

  for (let i = 0; i < word.numOfLetters; i++) {
    let spanEl = document.createElement("span");
    spanEl.classList = `letter ${word.word.split("")[i].toLowerCase()}`;
    spanEl.innerHTML = " __ ";
    $("#word").append(spanEl);
    console.log(spanEl);
  }

  let rightGuesses = 0;
  $(".btn").click(function () {
    let letter = $(this).attr("id").split("-")[1];
    let lives = livesSpan.innerHTML.split(" ")[1];
    console.log("letter", letter);
    if (word.letters.includes(letter.toUpperCase())) {
      rightGuesses++;
      $(`.${letter}`).html(` ${letter.toUpperCase()} `);
    } else {
      lives--;
      livesSpan.innerHTML = `Lives: ${lives}`;
    }

    if (rightGuesses == word.letters.length) {
      $("#header").html(
        `<span style="margin: auto; font-size: 30px; font-weight: bold">You win!!</span>`
      );
      $(".btn").attr("diabled", "true");
    }
    if (lives <= 0 ) {
      $("#header").html(
        `<span style="margin: auto; font-size: 30px; font-weight: bold">The word was ${word.word}.</span>`
      );
      
      $(".btn").attr("diabled", "true");
    }

    $(this).attr("disabled", "true");
  });
});
