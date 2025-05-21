# Technical Interviews

### Why?

> Imagine you are a recruiter
> You have a large number of candidates who, on paper, sound like fantastic workers
> However, how do you know that they know what they say they know?
>
> Technical interviews allow hiring managers to check that they can know
> that what we say we know that we actually know

## Types of technical interviews

1. Technical coding interviews
2. Take home exams
3. Technical questioning interviews

Alternatively, some interviewers will just look at your 'portfolio' (read: GitHub)

### Coding interviews

These are live coding sessions with a technical person. They will give a prompt, or a series of tasks
then watch as you work through them. This is similar to your Stage 3 interview.

Key points:
- We care more about communication, breaking down the problem and planning than code that is O(1)
- Think about 'good' solutions (please don't do double for loops if you don't need it). Best practice is more important than speed
- TESTING ALWAYS
- Run pytest frequently and early
- You should not have to run your scripts if you write good tests

### Take home exams

These are the same as the above, but you get to do it by yourself. Usually you are given a time frame: Work for no longer than x hours and submit before Monday.

Key points:
- Think about code quality - this is what the markers will be looking at
- Think about documentation - you don't need a million in line comments, just docstrings as you would normally
- In most cases, your code will speak for itself

### Technical Questioning

This is about knowledge. A person with a lot of technical knowledge will ask the following:
- Tell me about a project you recently worked on
  - Followup questions: what problems did you face?
  - If cloud - how much did it cost to run?
  - What interesting insights did you find out?
- They will then ask specific questions about technology. Usually these are related to the project you spoke about
  - If you mention EC2, they will ask about that

Key points:
- Most interviewers will only ask about technologies that you mention, so don't show off
- When talking about a project, always think about the business value
  - What metrics do you have to show that your project was successful?
- The interviewer wants to know how you communicate effectively (to technical and non-technical people)


## Coding interview

1. **Understand** the problem (2 mins): Again. Make sure you understand the problem and the requirements. Most people fail because they don't read the question properly.
2. **Ask Questions** (1 min): If you don't understand something, ask the interviewer. They are there to help you.
    - "My understanding of the problem is ... is that correct?"
    - IMPORTANT: you are NOT asking permission to do things, you are asserting that you have a plan
3. **Inputs and Outputs** (1 min): Make sure you understand the base and edge cases. This means understanding the minimum and maximum inputs and outputs as well as outside values (e.g. empty input, null input, etc.)
4. Have a small **plan** (2 mins): Spend a little time thinking about how you will solve the problem. This will help you to solve the problem faster and more accurately.
5. Write your **function outlines** (2 mins): Write your function outlines (i.e. definitions and type hints and docstrings)
   - DO NOT WRITE CODE: I WILL STOP THE INTERVIEW IF YOU DO
6. Write **tests** for all functions (3 mins): Write your unit tests and test your code. Make sure it works as expected.
   - Enough tests to cover the base and edge cases (~3 on average for each function, ideally more)
7. **Solve the problem**: Write your code to solve the problem. Make sure you are writing clean, well-documented, and well-tested code.
8. **Iterate**: If you have time, iterate on your solution. Make it better.

