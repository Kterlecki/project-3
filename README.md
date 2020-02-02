# Exercise manager!

In this project I focused on trying to create a simple gym exercise tracker. Currently this gym tracker can be used to take data about a users gym experience on a particular day. It can be used as a reminder what a user has to do in the gym on a particular day.

This is a more conveniant way of keeping on top of your exercise schedule than a paper notepad or plan. It only needs your phone to run which makes it more conveniant than carrying around  extra plans and notepads in the gym. 


Please find a live Demo of the website below:



# UX
This Application is primarly aimed at people who want to make their gym experience less of a hassle. Healthy living is becoming very popular and sustaining it can be a problem. This website is for all age groups and genders. Each page provides the necessary information and/or inter activeness to try and make it enjoyable to go through each page. 

A user can go to the main page and see all the tasks they hav created. The user can delete each taks by pressing 'done' and edit each task by pressing 'edit'. By pressing on each task a user can expand each task to see an exercise description which is available for each task present.

When a user presses the edit button of a task they are brought to an edit window which shows data that has been already entered into each field. The user can then proceed with any changes that may be required. Upon completion the user can click on the edit task button to complete the editing of that task.

A user can also click on the 'new task' button located in the navbar which brings them to a page which allows them to add a task. A user can select from a category of different body parts, add task name, add a description of what they want to do and select the date which this will be done.

A user can also select the 'manage categories' button from the navbar which leads them to a category window. In this window a user can add or delete different categories which will then appear in the category select dropdown in add task/edit task windows.


The UI colors that were chosen for this project emphasise each section and make it easily legible.

# Features

## Exercise manager (homepage)

The homepage allows the user to view, edit and delete tasks which are then stored in mongo.

## New Task

New task allows for a user to add new tasks to the database. These then appear on the homepage which the user is redirect once a new task has been added.

## Manage categories 

This page provides a user the ability to view, add and delete different categories that a user might use in the category name dropdown that is present on each task or add task window



## Plans for improvement

In the future this application could get more functionality. For example it would be beneficial to add in whole workout plans for beginners for different bodyparts or style of training. It would also be beneficial to have a link for each exercise to show how its performed correctly by either providing a video, images or a description on correct technique.

It would also be beneficial to make a calory intake calculator. This would allow people to calculate their healthy calory in take for the day.

I would also like to implement pop-ups  that appear after exercises are completed in order to motivate more people.

The application would switch from using materialize to Bootstrap. Bootstrap has been a lot more convenient to use and provides easier building options.

## Technologies Used

### HTML5 
- HTML 5 was used as it uses semantic markups to effectively design webages.

### CSS3

- was used for styling and layout options of the HTML pages.

### Materialize

- Was used to style and help with certain aspects of the layout of the HTML page

### JS
- this was used for some of the functionality of the page

### Jquery
- this was used for some of the functionality of the page

### Python
- used to build the application

### MongoDB
- this was used for storing user data

### Flask
- has been used with python to build and connect this application

### w3schools
- was used to optimise both CSS and HTML code. Helped me to adjust and insert different features.

 ### [Stackoverflow](https://stackoverflow.com)

- Used this webiste for troubleshooting issues to common problems

# Testing

Testing was carried out on each navigation button on each site to ensure the links are working correctly. Other testing that was performed was the responsiveness of the website on mobile, tablet and desktop. Both portrait and landscape was tested.

googole developer tools was used to test the website on all different screen resolutions available and switching from landscape to portrait modes.

The functionality of each command was tested. For example the 'done' button located on the home page has been tested to delete a task. the edit button has been tested to edit a particular and any updated that were made, once saved appeared on the home page.
The add task button has been tested for addition of new tasks with correct values that were put in.
The manage category page has been tested to ensure delete and addition functionality is working correctly

The code was also tested on html and css validator

The entire website was tested on responsinator just in case anything was missed on googole developer tools

Application was tested on Google chrome, firefox and Opera

One bug which i havent been able to figure out was when editing the data, the date selected would not appear on the updated task. It would appear as none. This had to have been something with my task update code

Was also tested on real life devices like :

- Samsung S8 and S9 Plus

- Iphone X

## Responsive testing

The website has been designed to be responsive to different screen sizes. This was achieved by using Materialize.

# Deployment

I decided to use github/Heroku to host my application. I found a guide on how to do this on the following page: https://www.codecademy.com/articles/f1-u3-github-pages

Github Pages Guide
One of the main reasons why I decided to use github for version control is that we have used it through the course and I feel relatively familiar with it. It also helps that its free. Version control was particularly important in this project as I ran into bugs constantly.

For good practise a variable has been added into the password field for mongo db

Heroku has been used to deploy the application

Please find a live Demo of the website below:


# Credits

https://materializecss.com/
https://courses.codeinstitute.net/
## Content

The contact form was taken from Materialize and adjusted to fit my needs
Code from the mini-project for data centric development has been used for this project.
Some of the code has been adjusted to fit my requirements




## Acknowledgements
https://www.mongodb.com/
https://materializecss.com/
https://courses.codeinstitute.net/
https://stackoverflow.com/
