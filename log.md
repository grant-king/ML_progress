# 100 Days Of Code - Log
Day 1: January 2, 2019

**Today's Progress:** Watched introduction videos again. Watched videos for first chapter, on datetimes. Wrote detailed notes and example code in a Jupyter notebook.

**Thoughts:** It seems like there isn't a very distinct day 2, so I will start writing the coding challenge tomorrow and finish it on the third day.

Day 2: January 3, 2019

**Today's Progress:** Completed Python practice challenge, calculating datetimes within a server log on Python Bytes site. Fiddled with datetimes, os, and logging libraries in the notebook.

**Thoughts:** It turns out there is a very distinct day 2. Today's TPTM plan involved completing a coding practice challenge on Python Bytes website. After first use, I am already not a fan of the Python Bytes experience. If it continues to be terrible to work with I can search exercism, codewars, or other alternative for relevant exercises.

Day 3: January 4, 2019

**Today's Progress:** Made small logging script using datetimes, logging, and os.

**Thoughts:** Found Corey Schafer YouTube video to help understand basics of logging and os modules. Used datetimes to add readable datetime log entries instead of unreadable timestamp.

Day 4: January 7, 2019

**Today's Progress:** Started investigating beginning steps and potential project paths for working with Python in Blender. Learned about collections module.

**Thoughts:** I am happy to be getting started with the scripting process in Blender. I have 3d data in the Gradient Descent notebook I am working on, it might be fun to use Python to try and map objects to that data in Blender. As for the collections module, I will certainly start using the namedtuple where it makes sense in my code.

Day 5: January 8, 2019

**Today's Progress:** Reviewed file operations. Day two of learning about collections module.

**Thoughts:** The code challenge for this module is more involved. Because of frustration last time I am working from a notebook rather than the PyBites environment. I couldn't remember the best way to open files but reviewed with a Corey Schafer video. It is important to know how to open most files using a context manager but since this challenge is working with CSV data I think it is best for me to use the familiar Pandas functionality.

Day 6: January 9, 2019

**Today's Progress:** Started an app to render a small picture in Blender.

**Thoughts:** I'm using namedtuple to store pixel color data in app that takes small jpg and writes blender script that will be able to translate pixel data from the picture into a flat plane within the 3d environment of appropriately colored solid cubes.

Day 7: January 10, 2019

**Today's Progress:** TPTM course reviewed basic data structures. Continued learning Blender API.

**Thoughts:** Glad to review basics of lists, dictionaries, and tuples. The Blender script is difficult to get to work consistently.

Day 8: January 11, 2019

**Today's Progress:** TPTM data structures day 2 featured a PyBite on lists and dictionaries. Also found a related Exercism exercise. Continued learning Blender API. Restarting unfinished Coursera project planning course.

**Thoughts:** I liked the Pybite but am having trouble finding a good reason to want to submit it to their system. The embedded interpreter is not helpful to work in and only validates that I was able to submit passable code using their awkward system. In contrast, Exercism's command line interface, exhaustive prewritten tests, and clean website makes for much more fruitful exercises. I appreciate that I can easily search, browse, and immediately recognize the content of different exercises. Working on a file locally and then submitting through the CLI app is really nice. It is especially nice that there aren't any preloaded environment variables to worry about. I think PyBites would be better for learning if it had more distinction between the information, testing environment, and submittal interfaces.

Day 9: January 14, 2019

**Today's Progress:** TPTM data structures day 3. Reviwed/continued Natural simulaitons course on KhanAcademy using JS, started playing with Python mode on Processing IDE. Started exploring Pygame as a more powerful animation alternative. Reviewed simple OOP structure and list operations with high_scores exercise on Exercism.

**Thoughts:** I didn't do the Pybite assigned by TPTM but found something similar on Exercism. I was very glad to be reminded of Processing, and to be able to inspect the Python interface and some examples now that I have been using so much Python. Processing in JS on KhanAcademy was my original introduction to programming so long ago, it is interesting to pick up where I left off without too much trouble switching back into JS. I also found some alternative animation libraries in Python and started playing around with Pygame. It is also an old project but has an active community and seems more promising than returning to Processing for my stuff.

Day 10: January 15, 2019

**Today's Progress:** TPTM pytest day 1. Two text-oriented Exercism exercises. Started working through Scrapy Documentation so that i'll be able to add a new 'movie-madness' Django app component that will scrape a user collection from blu-ray.com in order to import collections.

**Thoughts:** TPTM feels like it is moving a little slow so I am glad to work on the scraping component for the movie-madness app that I had been working on a couple of months ago.

Day 11: January 16, 2019

**Today's Progress:** TPTM pytest day 2. More progress with Scrapy. Worked on an Exercism using Pytest instead of builtin unittest for Test Driven Development exercise.

**Thoughts:** Finally figured out how to setup and run simple Scrapy spider for blu-ray site. It is fun to think that I can store the pages locally to figure out my parse operations before running on all collection pages. This would be especially useful for sites like this that have restrictive data access policies. Also am getting to learn about xpath, a way to access the data in the stored request.

Day 12: January 17, 2019

**Today's Progress:** TPTM pytest day 3 working with fixtures. Exercism Bank account exercise to continue working with pytest for TDD, while reviewing class implementation.

**Thoughts:** I'm not sure who this Talk Python training is trying to teach. Some days have been surprisingly basic while others require significant experience with all of the language, including the very topics that are being covered. It is ok when I treat it as a review of basic concepts that have components that I may have missed, but is otherwise disjointed and pretty drudgerous. Today's topic rushes to cover a major component of pytest: fixtures. I have no experience setting up or breaking down data structures in unittest, so I have no idea what this man is talking about. I'm glad that other resources have been able to fill in the gaps and give work that keeps me motivated to continue logging this 100 days.


Day 13: January 18, 2019

**Today's Progress:** TPTM classes day 1.


Day 14: January 21, 2019

**Today's Progress:** TPTM classes day 2 exercise. Rewatching Corey Schafer OOP series as supplement. Continued learning about pygame while following OOP examples.

**Thoughts:** I liked the exercise planned by Talk Python today. I followed instructions to build a textual rock, paper, scissors game. I found areas where I could use both class methods and static methods. I am using a class method as an alternative constructor to handle the interactive creation of a player, while normal initialization will allow for objects to be created without assigning a name. The static method is like a normal method that has some logical tie to a class, so it can be included with that class without passing default self or cls values.
I have started setting up test classes in a pygame script. I am modeling these classes around real-life elements as that seems like a simple, familiar object with distinct attributes and behavior that I could edutainingly incorporate into this project.

Day 15: January 22, 2019

**Today's Progress:** TPTM classes day 3. Researching TDD and other software development frameworks.

**Thoughts:** I really liked the day 3 challenge planned by TPTM training. Today's exercise makes it easy to see the benefit of using an object oriented paradigm. Michael asks for us to extend yesterday's work into a version with 15 plays/categories instead of just the 3. I'm glad that the structure of the code makes this as simple as adding a new Roll class method that can be called on to construct the roll types of the new game according to the rules of a local csv file. The file contains roll type names and distinguishes between the outcome of that roll winning when pit against each of the other roll types. I got really confused by the wording for some reason and ended up having to just code it one way and read what the output was to determine if my code was logically sound.  

Day 16: January 23, 2019

**Today's Progress:** TPTM lists and generators day 1. Started looking at some old code that would be good for OOP rewrite.

**Thoughts:** I like the videos for today, I didn't know how generators could be created with yield.

Day 17: January 24, 2019

**Today's Progress:** TPTM lists and generators day 2. Continued planning refactor. Worked through a simple Exercism exercise.

**Thoughts:** The TPTM topic for this chapter isn't very new or exciting, although I understand generator objects better now.

Day 18: January 25, 2019

**Today's Progress:** TPTM lists and generators day 3. Dictionary comprehensions. Exercism 'tournament' exercise. Resuming Scrapy basics

**Thoughts:** I remember learning about dictionary comprehensions in some DataCamp course last year but I couldn't find the same activity. I found a helpful tutorial article at https://www.datacamp.com/community/tutorials/python-dictionary-comprehension. Returning to working through Scrapy tutorial but for scraping blu-ray collections for movie-madness Django site project.

Day 19: January 26, 2019

**Today's Progress:** TPTM itertools day 1. Continued Scrapy project. Corey Schafer itertools tutorial.

**Thoughts:** I'm really glad to be going over iterators, iterables, and the tools in itertools. I have a vague concept of how these things function behind the scenes so it is good to supplement my understanding with the TPTM training videos and Corey Schafer's YouTube videos. Scrapy is taking some time to learn but I have gotten to a point where I was able to figure out how to scrape all movie names from the blu-ray.com collection. The collected data is heavily duplicated b/c of my poor understanding of the system. I think I can capture the parts of the page I need if I use Scrapy's "item" system.

**Link to work:**


<!---

Day x: January x, 2019

**Today's Progress:**

**Thoughts:**

**Link to work:**

### Day 0: February 30, 2016 (Example 1)
##### (delete me or comment me out)

**Today's Progress**: Fixed CSS, worked on canvas functionality for the app.

**Thoughts:** I really struggled with CSS, but, overall, I feel like I am slowly getting better at it. Canvas is still new for me, but I managed to figure out some basic functionality.

**Link to work:** [Calculator App](http://www.example.com)

### Day 0: February 30, 2016 (Example 2)
##### (delete me or comment me out)

**Today's Progress**: Fixed CSS, worked on canvas functionality for the app.

**Thoughts**: I really struggled with CSS, but, overall, I feel like I am slowly getting better at it. Canvas is still new for me, but I managed to figure out some basic functionality.

**Link(s) to work**: [Calculator App](http://www.example.com)


### Day 1: June 27, Monday

**Today's Progress**: I've gone through many exercises on FreeCodeCamp.

**Thoughts** I've recently started coding, and it's a great feeling when I finally solve an algorithm challenge after a lot of attempts and hours spent.

**Link(s) to work**
1. [Find the Longest Word in a String](https://www.freecodecamp.com/challenges/find-the-longest-word-in-a-string)
2. [Title Case a Sentence](https://www.freecodecamp.com/challenges/title-case-a-sentence)
--->
