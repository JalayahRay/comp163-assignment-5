# COMP 163 - Assignment 5: Loop Mastery

This project demonstrates three different loop structures in Python: `while`, `for`, and nested `for` loops. Each challenge was chosen to match the loop type that fits best with the problem.

---

## Challenge 1: Collatz Conjecture — *Why a while loop?*
- The number of steps is **unknown** ahead of time.  
- A `while` loop continues **until** the number reaches 1, making it the natural choice.  
- The loop repeatedly updates the number:  
  - If even → divide by 2  
  - If odd → multiply by 3 and add 1  
- The program prints the sequence and counts how many steps were required.

---

## Challenge 2: Prime Number Checker — *Why a for loop?*
- Possible divisors are in a **known fixed range**: from `2` up to `n - 1`.  
- A `for` loop is best because it runs over a definite set of numbers.  
- The program tests each divisor:  
  - If one divides evenly → stop early and report it.  
  - If no divisors are found → the number is prime.

---

## Challenge 3: Multiplication Table — *Why nested loops?*
- A multiplication table is **2D data** (rows × columns).  
- The **outer loop** controls the rows (1–10).  
- The **inner loop** controls the columns (1–10).  
- Each product is printed with fixed spacing so the grid lines up neatly.

---

## AI Assistance Disclosure
- AI was used only for clarification, debugging tips, and formatting suggestions.
- All algorithms were studied, written, and understood by me before submission.

---

## Git Workflow
1. Created repo `comp163-assignment-5` (public).  
2. Added `.py` file and README.  
3. Commit after each challenge:  
   - `Challenge 1: Collatz sequence - while loop for unknown iterations`  
   - `Challenge 2: Prime checker - for loop for known range`  
   - `Challenge 3: Multiplication grid - nested loops for 2D data`  
   - `Add loop design documentation`  
4. Pushed repo to GitHub and submitted link.

---

## How to Run
```bash
python3 JalayahRay_assignment_5.py
