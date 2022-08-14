const question = document.getElementById("question");
const choices = Array.from(document.getElementsByClassName("choice-text"));
const progressText = document.getElementById("progressText");
const scoreText = document.getElementById("score");
const progressBarFull = document.getElementById("progressBarFull");
let currentQuestion = {};
let acceptingAnswers = true;
let score = [0,0,0,0];
let questionCounter = 0;
let availableQuesions = [];

let questions = [
  {
    question: "How much is comedy your favourite Genre?",
    choice1: "I don't like comedy",
    choice2: "I like comedy just a bit",
    choice3: "I like comedy so much",
    choice4: "I love comedy",

  },
  {
    question: "How much exitment do you want the movie to have?",
    choice1: "I'm just Chilling",
    choice2: "Maybe just a bit",
    choice3: "I want to get so exited",
    choice4: "I want to have a dopanie BLAST",

  },
  {
    question: "How romantic do you want to feel after watching the movie?",
    choice1: "I'm not in a romantic mood RN (I'm Single)",
    choice2: "Maybe a bit romantic",
    choice3: "Show me the beaty of romance",
    choice4: "Show me the most romantic movie ever!",

  },
  {
    question: "How scared do you want to get when you're watching the movie?",
    choice1: "I never liked Scary movies",
    choice2: "Maybe show me a scary movie",
    choice3: "i actually would appreciate a scary movie",
    choice4: "Freak me out so i can't sleep tonight!",
  }
];

//CONSTANTS
const MAX_QUESTIONS = 4;
startGame = () => {
  questionCounter = 0;
  score = [0,0,0,0];
  availableQuesions = [...questions];
  getNewQuestion();
};

getNewQuestion = () => {
  if (availableQuesions.length === 0 || questionCounter >= MAX_QUESTIONS) {
    localStorage.setItem("mostRecentScore", score);
    //go to the end page
    return 1;
  }
  questionCounter++;
  progressText.innerText = `Question ${questionCounter}/${MAX_QUESTIONS}`;
  //Update the progress bar
  progressBarFull.style.width = `${(questionCounter / MAX_QUESTIONS) * 100}%`;

  const questionIndex = 0
  currentQuestion = availableQuesions[questionIndex];
  question.innerText = currentQuestion.question;

  choices.forEach(choice => {
    const number = choice.dataset["number"];
    choice.innerText = currentQuestion["choice" + number];
  });

  availableQuesions.splice(questionIndex, 1);
  acceptingAnswers = true;
  questionIndex+=1;
};

choices.forEach(choice => {
  choice.addEventListener("click", e => {
    if (!acceptingAnswers) return;
    
    acceptingAnswers = true;
    const selectedChoice = e.target;
    const selectedAnswer = selectedChoice.dataset["number"];
    point=0.0;
    if(selectedAnswer=="2"){
      point+=1;
    }
    else if(selectedAnswer=="3"){
      point+=2;
    }
    else if(selectedAnswer=="4"){
      point+=3;
    }

    const classToApply =
      selectedAnswer == currentQuestion.answer ? "correct" : "incorrect";

    incrementScore(questionCounter-1,point);

    selectedChoice.parentElement.classList.add(classToApply);

    setTimeout(() => {
      selectedChoice.parentElement.classList.remove(classToApply);
      getNewQuestion();
    }, 0);
  });
});

function incrementScore(index, num) {
  score[index]+=num
  scoreText.innerText = score;
};

startGame();
