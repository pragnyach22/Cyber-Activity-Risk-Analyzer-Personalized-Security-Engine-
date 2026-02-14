Cyber Activity Risk Analyze
Project Description

This Python program analyzes student login activity intensity scores to detect suspicious behavior.
It categorizes activity scores into different risk levels and applies a personalized security filter based on the last digit of the student's register number.

Features

The program performs the following tasks:
Accepts multiple activity scores from the user.
Cleans invalid data (negative scores).
Categorizes valid scores into:
Low Risk
Medium Risk
High Risk
Critical Risk
Applies a personalized filtering rule based on register number digit.
Generates a final security report.

Risk Categorization Rules
Score Range	Risk Level
Score < 0	Ignored
0 – 30	Low Risk
31 – 60	Medium Risk
61 – 100	High Risk
> 100	Critical Risk

Personalized Security Filter
Let:
D = Last digit of Register Number
(Currently set as D = 2 in the program)
If D is EVEN:
Remove all Low Risk scores
Keep Medium, High, and Critical
If D is ODD:
Remove all Critical Risk scores
Keep Low, Medium, and High

Variables Used
scores → Stores activity scores
low_risk, medium_risk, high_risk, critical_risk → Risk category lists
validcount → Total valid scores
icount → Ignored (invalid) scores
rcount → Scores removed due to personalization

How to Run
Run the Python program.
Enter number of scores.
Enter each score one by one.
View:
Risk categorization
Personalized filtering result
Final summary report

Example

Input:
8,10,45,78,120,-5,30,99,150

If D = 2 (Even):
Low Risk scores will be removed.

Constraints Followed

✔ Used Lists
✔ Used For Loops
✔ Used Conditional Statements
✔ No List Comprehension
✔ No Dictionaries
✔ No filter()
✔ No sum(), max(), min()
✔ No Hardcoded categorization values# Cyber-Activity-Risk-Analyzer-Personalized-Security-Engine-
