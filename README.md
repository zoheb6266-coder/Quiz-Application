# Quiz Application

## Project Description
The Quiz Application is a simple console-based quiz developed using Python 3. It randomly selects three multiple-choice questions from a question bank, accepts the user's answers, checks them, calculates the score and percentage, and displays whether the user passed or failed.

## Features
- Contains a question bank of 10 multiple-choice questions.
- Randomly selects 3 questions for each quiz attempt.
- Displays four options (A, B, C, and D) for each question.
- Validates user input and asks again if the option is invalid.
- Shows whether each answer is correct or incorrect.
- Displays the final score, percentage, and Pass/Fail result.
- Uses a passing criterion of 50%.

## Technologies and Concepts Used
- **Language:** Python 3
- **Module:** `random`
- **Data structures:** Lists and dictionaries
- **Concepts:** Functions, loops, conditional statements, input validation, and random selection

## Requirements
- Python 3 installed on your computer.

## How to Run
1. Save the Python code in a file named `quiz.py`.
2. Open a terminal in the folder containing `quiz.py`.
3. Run the command:

   ```bash
   python quiz.py
   ```

   If your computer uses the Python launcher, you can run:

   ```bash
   py quiz.py
   ```

4. Answer each question by entering `A`, `B`, `C`, or `D`.

## How It Works
1. The program stores 10 questions, their four options, and the correct answer in a list of dictionaries.
2. The `run_quiz()` function randomly selects up to three different questions.
3. The program displays each selected question and its options.
4. The user enters an answer. Invalid options are rejected and the same question is asked again.
5. The program checks the answer and updates the score.
6. At the end, it calculates the percentage and displays `Pass` for 50% or higher; otherwise, it displays `Fail`.

## Example Result Format

```text
================================
          QUIZ RESULT
================================
Score: 2/3
Percentage: 66.67%
Result: Pass
================================
```

*The score and percentage above are an example; actual results depend on the questions selected and the answers entered.*

## Test Cases

| Test Case | Input / Scenario | Expected Result |
|---|---|---|
| Normal Input | Enter the correct answers to all 3 selected questions | Score: 3/3, Percentage: 100.00%, Result: Pass |
| Minimum / Boundary Input | Enter incorrect answers to all 3 selected questions | Score: 0/3, Percentage: 0.00%, Result: Fail |
| Invalid Input | Enter an invalid option such as `E`, then enter a valid option | Displays an invalid-option message and asks the same question again |
| Different Valid Scenario | Get 2 out of 3 answers correct | Score: 2/3, Percentage: 66.67%, Result: Pass |

**Note:** Because questions are selected randomly from the full question bank, the exact question order can vary. The fixed test answers shown in the assignment image apply only when the first three questions are asked in the specified order.

## Project Structure

```text
Quiz-Application/
├── quiz.py
└── README.md
```

## Author
Student Project — Quiz Application
