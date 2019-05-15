      Gallary
===================
## Description
This is a personal gallery application that enables you to display various photos of ```Diet,Fashion and Exercise.```

------------------------------------------------------------------------

## User Requirements

1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
3. Search for different categories of photos.
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

## Features

+ [x] Create and display photos based on categories
+ [x] Django admin dashboard for adding & managing images, categories and location
+ [x] Bootstrap image model and copy link button.
+ [x] Filter images based on category and location.
+ [x] search functionality based on image description.




## Models

### Location and Category models
* Location and category that link to the Image model.
* `save`, `update` and `delete` methods in both models

## Admin Dashboard
Use django admin to post photos to the database and manage the photos

## Setup

### Requirements
This project should be able to work on different kind of platforms
* Tested on Debian Linux
* Python3.6

### Cloning the repository
```bash
git clone git@github.com:probantan/gallary.git&& cd personal-gallery
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```
pip3 install -r requirements
```




### Database migrations

``
python manage.py migrate
```


```

### Running the server 
```
python manage.py runserver
```



## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11]
* [Heroku](https://heroku.com)




### License
Copyright (c) {year} **{Morings School}**