# AI Powered Study Assistant CLI

A command-line AI Study Assistant built using the **Google Gemini API** and Python.

The application generates a structured learning roadmap for any topic and supports follow-up questions through a persistent chat session.

---

## Features

* Generate beginner-to-master study roadmaps
* Maintain conversation context using a chat loop
* Ask unlimited follow-up questions
* Exit the session with `exit` or `quit`
* Display a session summary at the end
* Secure API key management using `.env`
* Clean and beginner-friendly output

---

## Tech Stack

* Python
* Google Gemini API
* python-dotenv

---

## Project Structure

```text
project/
│
├── main.py
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-link>
cd <repository-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Program

```bash
python main.py
```

---

## Example Workflow

1. Enter a topic to study.
2. The AI generates a roadmap.
3. Ask follow-up questions.
4. Type `exit` or `quit`.
5. View the session summary.

---

# Output Screenshots

### Roadmap Generation

EXAMPLE 1:-

```
==================================================
            AI POWERED STUDY ASSISTANT            
==================================================

Enter a topic to study: Java Script

==================================================
            AI POWERED STUDY ASSISTANT
==================================================

1. Basics
• Variables & Data Types: Store and manage information.
• Operators & Control Flow: Perform computations and guide program logic.
• Functions: Group reusable blocks of code for specific tasks.
• Arrays & Objects: Work with structured collections of data.
• DOM Manipulation: Dynamically interact with web page elements.
• Event Handling: Respond to user interactions on a webpage.

2. Advanced Concepts
• Asynchronous JavaScript: Handle operations that take time without blocking.
• Fetch API & REST: Communicate with external servers for data.
• ES6+ Modern Features: Leverage contemporary JavaScript syntax and patterns.
• Module Systems: Organize and reuse code efficiently across files.
• Introduction to Frameworks: Understand building scalable, complex user interfaces.

3. Practice
• Build an interactive To-Do list application.
• Fetch and display data from a public API (e.g., weather, jokes).
• Create a dynamic image gallery with user controls.

Outcome
You will be able to confidently build dynamic and interactive web applications using JavaScript.
==================================================


Ask a follow-up question (type 'exit' to quit): exit

==================================================
                 SESSION SUMMARY                  
==================================================
Topic Studied : Java Script
Questions Asked : 1
==================================================
```
---

EXAMPLE 2:-

```
==================================================
            AI POWERED STUDY ASSISTANT            
==================================================

Enter a topic to study: python

==================================================
            AI POWERED STUDY ASSISTANT
==================================================

1. Basics
• Data Types & Variables: Understand integers, strings, booleans, and how to store data.
• Operators & Expressions: Learn arithmetic, comparison, and logical operations.
• Control Flow: Master if/else statements, for loops, and while loops for program logic.
• Functions: Define reusable blocks of code for organization and efficiency.
• Basic Data Structures: Explore lists, tuples, and dictionaries for organizing collections.
• File I/O: Learn to read from and write to text files.

2. Advanced Concepts
• Object-Oriented Programming (OOP): Grasp classes, objects, inheritance, and polymorphism.
• Error Handling: Implement try/except blocks to gracefully manage program errors.
• Modules & Packages: Understand how to import and use external libraries.
• Virtual Environments: Isolate project dependencies for clean development.
• Web Development Basics: Explore frameworks like Flask or Django for building web applications.• Data Science Fundamentals: Introduce libraries like Pandas and NumPy for data manipulation.

3. Practice
• Write a function that takes a list of numbers and returns their average.
• Create a simple class for a 'Car' with make, model, and year attributes.
• Build a script to read a text file, count word frequencies, and print the top 5.

Outcome
The learner will be able to confidently develop a wide range of Python applications, from scripts to web services and data analysis tools.

==================================================


Ask a follow-up question (type 'exit' to quit): quit

==================================================
                 SESSION SUMMARY                  
==================================================
Topic Studied : python
Questions Asked : 1
==================================================
```
---

# Prompt Engineering Write-Up

## 1. What role did you assign in your system prompt, and why?

I assigned the AI the role of a **world-class mentor and Distinguished Principal Educator**. This framing encourages the model to explain topics clearly and generate structured learning paths suitable for beginners. The goal was to make complex subjects easier to understand while maintaining consistency across different topics.

---

## 2. What format did you specify for the output, and how did you enforce it?

The prompt explicitly defined the output structure and imposed several constraints. The roadmap was divided into sections such as basics, advanced concepts, practice questions, and outcome. Additional instructions limited the response length, required bullet points, and specified that each topic should occupy a single line. These constraints helped ensure consistent and predictable output.

---

## 3. What happens if the system prompt is removed?

Without the system prompt, the responses become less structured and vary significantly between topics. The model may generate long paragraphs, inconsistent formatting, and omit important sections. The system prompt improves both consistency and readability.

---

## Requirements

```txt
google-genai
python-dotenv
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your real API key to GitHub.

---

## Author

Built as part of **FORGETRACK 2026 - Week 03 Tech Track**.
