CS50 Final Project:

This project is a to-do-list and pomodoro combined website, with the target user being myself. I have ADHD and make extensive use of to-do-lists and pomodoro timers, and I wanted to combine them in one app.

To-Do list features:

On the "ToDo" page you can create a new task with a category of today, tomorrow, or long-term, and a priority of 1, 2, or 3.The tasks are automatically sorted by category 1st, then by priority 2nd, and finally by date/time inputted (newer tasks lower down). Tasks that are priority one are marked with a red square, tasks that are priority two are marked with an orange square, and tasks that are priority three are marked with a purple square. Categories only appear if there are tasks in that category. Additionally, you can delete a task by clicking on the priority square, which will turn into a checkmark before reloading the page and deleting the task. On the "Completed" page you can see a list of all of the tasks you completed starting with the most recent ones.

Pomodoro features;

On the "ToDO" page you can start a timer, which will count up the minutes and seconds that you have been working on a task. You can also stop the timer, which will reset the seconds to zero so that you can begin a new interval once you take a break. Additionally, you can run multiple timers simultaneously which is useful if you have one task that has subtasks.

Structure:

I used SQL, python, flask, javascript, CSS, and HTML. The database that stores all of the tasks is todo.db. I have the files organized in the way flasks needs them to be with templates and static files, as well as the requirements.txt and app.py documents. Helpers.py contains the apology function, which I decided to borrow from finance.

How to run the project:

Run the project by: 1.) cd into the ToDo folder 2.) type Flask Run into the command line 3.) Click on the link (note that sometimes the first time you click on the link the CSS doesn't render right away, if this happens just refresh the page)

The video link for my final project is here: https://www.youtube.com/watch?v=-fv1QwvMGGw
