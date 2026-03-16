# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
 The purpose of the game is to guess the secret number with the help of hints available after each attempts. It provides three levels with different number of attempts and ranges. 
- [ ] Detail which bugs you found.
I found that the hints were wrong, The secret number alone got updated upon clicking new game and not the attempts, The difficulty levels were reasoned wrongly and the player has the opportunity to input numbers that were not in the range. 
- [ ] Explain what fixes you applied.
I moved the core logic to logic_utils, fixed the difficulty ranges, attempt limits, wrong hints problem, out of range inputs and hard coded range in UI. Fixed all these.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

![alt text](<Screenshot 2026-03-15 at 7.50.44 PM.png>)

## 🚀 Stretch Features
- [ ]  Advanced edge case testing: 

![alt text](<Screenshot 2026-03-15 at 7.43.03 PM.png>)

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

