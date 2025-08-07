# 🔑Hangman Game Project | Day 7- 100 Days of Python

## A fun(& frustrating) game of Hangman where user tries to guess the correct word...and tries to prevent a tragic end from hanging

### **What It Teaches**
 - How to import specific components(list,string,etc.) from a module using `from module import component`
 - How to find length of a string using `len()`
 - How to use logical operators such as `and`
 - How to use membership operators such as `not in` and `in`
 - How to convert a `list` into `string`

### ❓**How Is It Run**

1. Open a terminal  
2. Navigate to the project folder:
   ```bash
   cd 100DaysOfPython_Kaustubh/Hangman_Game
   python Hangman_Game.py
   ```
3. You can also run the code in an IDLE such as Visual Studio Code or PyCharm

### 💻 **Sample Output**
```
 Guess a letter: k
__________
You guessed k, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
      |
      |
      |
=========

****************************<???>/5 LIVES LEFT****************************
Guess a letter: a
__________
You guessed a, that's not in the word. You lose a life.

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************<???>/4 LIVES LEFT****************************
Guess a letter: b
____b_____

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

****************************<???>/4 LIVES LEFT****************************
Guess a letter:

```

### 🙏 **Credits**
This project is part of my journey through the 
[100 Days of Code: Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.  

The project idea comes from the course, but the code and documentation here are my own work.  
At times I referenced the course material when stuck, and in some cases my solution may look very similar to the course’s — simply because there are only a few straightforward ways to solve certain beginner problems.  
Either way, the implementation reflects my own understanding and learning process.
