# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- hints are wrong
- secret keeps changing when new game button is clicked but not the history 
- doesn't understand how the score is calculated
- difficulty logic isnt correct
- attempts counter didnt count the first one
- can input numbers that aren't in the range
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot and Calude Code for this project. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
For the bug which was allowing the players to input numbers in the range outside the particular range, Claude code suggested that a range check would help which wasn't being done. After implementing the range check, I verified by running the pytest written for this case as well as running the app and by giving a number outside the range manually. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
For the number of attempts fix, AI suggested something irrelevant and I felt it was misleading. I tried to ask it about what it suggested and it quickly changed its answer. After implementation, I tested the application to confirm the bug is fixed. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tried to write pytest for cases I could think of as well as manually ran the application using streamlit and verified a particular scenario to make sure it is fixed. 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
After implementing the range check, bug fix, I verified by running the pytest written for this case as well as running the app and by giving a number outside the range manually. It showed that the code was initially faulty ( or had the bug) but is now fixed. It also showed the importance of testing it manually even though I had a pytest test case for it. 
- Did AI help you design or understand any tests? How?
Yes, AI helped in understanding the test cases. It gave me idea about what each test case should cover and what is the particular scenario that is being tested in the test case. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because whenever we press any button, it would run the entire code which also included the random.randint() used to initialize the secret number and hence, it kept changing in the original app. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Imagine you are writing in a document from templete. Without saving it, if you close it and try to open the template, it just shows the original template without whatever changes you made. Session state is like saving whatever things that need to be saved( like changing a heading).
- What change did you make that finally gave the game a stable secret number?
Adding a if condition which checks whether the secret is already fixed or not. If yes, then it does not refresh the secret number but just maintains it. If no, then a random.randint() is selected as the secret number. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Writing pytest cases alongside every bug fix was the most valuable habit from this project. Each time a bug was identified, writing a test first made it clear exactly what correct behavior should look like, and confirmed the fix actually worked rather than just appearing to work from manual testing.
- What is one thing you would do differently next time you work with AI on a coding task?
I would verify AI suggestions more critically before applying them, especially for anything involving framework-specific behavior like Streamlit reruns. When the AI gave misleading advice on the attempts counter, it cost time that could have been saved by reading the Streamlit docs directly first.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI-generated code can look clean and complete at first glance but still contain subtle logical bugs that only surface during real use. This project showed that treating AI output as a starting point to be tested and debugged, not a finished product, is the right mindset.