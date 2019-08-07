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

**Thoughts:** I didn't do the Pybite assigned by TPTM but found something similar on Exercism. I was very glad to be reminded of Processing, and to be able to inspect the Python interface and some examples now that I have been using so much Python. Processing in JS on KhanAcademy was my original introduction to programming so long ago, it is nice to pick up where I left off without too much trouble switching back into JS. I also found some alternative animation libraries in Python and started playing around with Pygame. It is also an old project but has an active community and seems more promising than returning to Processing for my stuff.

Day 10: January 15, 2019

**Today's Progress:** TPTM pytest day 1. Two text-oriented Exercism exercises. Started working through Scrapy Documentation so that i'll be able to add a new 'movie-madness' Django app component that will scrape a user collection from blu-ray.com in order to import collections.

**Thoughts:** TPTM feels like it is moving a little slow so I am glad to work on the scraping component for the movie-madness app that I had been working on a couple of months ago.

Day 11: January 16, 2019

**Today's Progress:** TPTM pytest day 2. More progress with Scrapy. Worked on an Exercism using Pytest instead of builtin unittest for Test Driven Development exercise.

**Thoughts:** Finally figured out how to setup and run simple Scrapy spider for blu-ray site. It is fun to think that I can store the pages locally to figure out my parse operations before running on all collection pages. This would be especially useful for sites like this that have restrictive data access policies. Also am getting to learn about xpath, a way to access the data in the stored request.

Day 12: January 17, 2019

**Today's Progress:** TPTM pytest day 3 working with fixtures. Exercism Bank account exercise to continue working with pytest for TDD, while reviewing class implementation.

**Thoughts:** I'm not sure what audience the Talk Python training is targeted at. Some days have been surprisingly basic while others require significant experience with all of the language, sometimes even the topic that is being covered. It is ok when I treat it as a review of basic concepts that have components that I may have missed. Today's topic covers a major component of pytest: fixtures. I don't have any experience setting up or breaking down data structures in unittest yet, so I don't really understand how it is preferable to the alternative. I'm glad that other resources have been able to fill in some gaps and supplement these exercises.

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

Day 19: January 28, 2019

**Today's Progress:** TPTM itertools day 1. Continued Scrapy project. Corey Schafer itertools tutorial.

**Thoughts:** I'm really glad to be going over iterators, iterables, and the tools in itertools. I have a vague concept of how these things function behind the scenes so it is good to supplement my understanding with the TPTM training videos and Corey Schafer's YouTube videos. Scrapy is taking some time to learn but I have gotten to a point where I was able to figure out how to scrape all movie names from the blu-ray.com collection. The collected data is heavily duplicated b/c of my poor understanding of the system. I think I can capture the parts of the page I need if I use Scrapy's "item" system.

Day 20: January 29, 2019

**Today's Progress:** TPTM itertools day 2.

**Thoughts:** Worked on parsing and tabulating Exercism using itertools and watched more Corey Schafer on the subject.

Day 21: January 30, 2019

**Today's Progress:** TPTM itertools day 3. Continued Scrapy project.

**Thoughts:** Going through spider building process again, this time using Scrapy's item interface to avoid unwanted duplicates.

Day 22: January 31, 2019

**Today's Progress:** TPTM Decorators day 1. Continued working with Scrapy. Continued investigating OOD/A/P best practices.

**Thoughts:** I came across a really good talk outlining the proper use of classes in Python. Stop Writing Classes: https://youtu.be/o9pEzgHorH0 . The Talk Python Training videos gave a good overview of decorators and when to use \*args and \*\*kwargs. For more practice I watched a video by Corey Schafer which gave an in depth view of the utility of and mechanisms behind decorators and star arguments.

Day 23: February 1, 2019

**Today's Progress:** TPTM Decorators day 2. Continued with OOP videos and started watching backlog of instructional videos collected in my 100-days Tasks list.

**Thoughts:** Today's TPTM progress involved more watching than much coding but will use the weekend to catch up and get more practice with decorators. I have some general programming topics to catch up on this weekend which will start with a list of videos I've collected in Gmail Tasks, most are by Corey Schafer. Glad to finally be back to visiting the Pythonista Cafe community after a while of not visiting.

Day 24: February 4, 2019

**Today's Progress:** TPTM Decorators day 3. More catching up on related concepts and terms.

**Thoughts:** More practice with decorators and their function in object oriented design.

Day 25: February 5, 2019

**Today's Progress:** TPTM error handiling day 1. Decorator catch-up

**Thoughts:** Hearing Michael back today talking about error handling. Also continued decorator practice as I still don't feel comfortable leaving that chapter yet.

Day 26: February 6, 2019

**Today's Progress:** TPTM errors day 2. Exercism Tournament exercise with error handling.

**Thoughts:** Need to find supplemental error content to reinforce TPTM chapter. Refactoring Exercism Tournament exercise considering error handling. Also I still need to sort output table by team with most points, then alphabetically to pass majority of tests that are left. It also needs to be able to handle a few special cases.

Day 27: February 7, 2019

**Today's Progress:** TPTM errors day 3. Exercism Matrix exercise.

Day 28: February 8, 2019

**Today's Progress:** TPTM regular expressions day 1. Exercism exercises.

**Thoughts:** I'm glad to be going over re module again. I usually avoid re but know they would be useful if I could use them easily.

Day 29: February 11, 2019

**Today's Progress:** TPTM regular expressions day 2.

**Thoughts:** More re chapter.

Day 30: February 12, 2019

**Today's Progress:** Last day for TPTM regular expressions.

**Thoughts:** Final day for re chapter. More Exercism exercises. I was able to greatly reduce code for an exercise, compared to other built in string operations, using re module to easily find all instances of a pattern with findall.

Day 31: February 13, 2019

**Today's Progress:** TPTM logging day 1.

**Thoughts:** Learning how to log with logbook. I've tried the built in way in the past but this will let me keep logs organized when making more complicated apps.

Day 32: February 14, 2019

**Today's Progress:** TPTM logging with logbook day 2. Continued planning MassCalculator.py refactor. Exercism kindergarten garden exercise with OOP.

**Thoughts:** Adding logging to chem-cli to help plan refactor.


Day 33: February 15, 2019

**Today's Progress:** TPTM logging with logbook day 3.

**Thoughts:** Had a hard time adding logbook as environments and libraries kept breaking today. I hope it is about to start working but other things are now broken so I can't tell yet.

Day 34: February 18, 2019

**Today's Progress:** TPTM Refactoring day 1. Catching up on logging with builtin logging.

**Thoughts:** Really, really frustrated trying to figure out why logbook won't work. Have uninstalled all traces and am on to refactoring chapter. Now trying to refactor notebook from Transcription repository while using builtin logging to make up for lost effort with Logbook.

Day 35: February 19, 2019

**Today's Progress:** TPTM refactor chapter day 2. Refactoring Transcription notebook for readability and with object orientated design. Gathering resources for next phase of learning.

**Thoughts:** It is funny to see how awful my code was less than a year ago. I'm sure I will think the same in some months if I look back at my present output. I'm glad to be going back through the Transcription repository to clarify the unfinished mess. I still haven't deployed anything that a non-developer could run, but I am much closer to being able to produce a usable app than when I started this project last year. Once this is working, I could immediately figure out the best way to get it to someone who will use it. Today I finally deciphered and rewrote the most wasteful portion of the notebook, so that client objects hold all source info rather than a convoluted and mostly unnecessary iteration over the source before calculating and storing the needed info per client.

Day 36: February 20, 2019

**Today's Progress:** TPTM refactor day 3. Exercism exercise.

**Thoughts:** Continuing to refactor Transcription and an Exercism exercise.

Day 37: February 21, 2019

**Today's Progress:** TPTM CSV data day 1. Exercism.  

**Thoughts:** I like watching the CSV data tutorial get a reminder of what is happening behind the scenes in Pandas, but will probably stick to using Pandas for things as involved as what's in the example.

Day 38: February 22, 2019

**Today's Progress:** TPTM CSV chapter day 2.  

**Thoughts:** Need to get back to Scrapy and then Movie database project before I forget what I've done. Also anxious to get as many Exercism done as possible, although finishing it shouldn't be priority.

Day 39: February 25, 2019

**Today's Progress:** TPTM CSV chapter day 3. Continued refactoring Transcription notebook. Started EDX OOP/algorithms course.

**Thoughts:** Final day reviewing CSV operations. Transcription is slowly getting less confusing and is a good place to try new structure practices. I would like to learn more about OOP and improve my general knowledge of algorithms, so I found a course on EDX that goes through both with Python.

Day 40: February 26, 2019

**Today's Progress:** TPTM JSON chapter day 1. Continued Scrapy movie scraping project.

**Thoughts:** Trying to be better about documenting project tasks. I hope that when I come back to projects after a while I won't have to go through everything again to pick it up again.

Day 41: February 27, 2019

**Today's Progress:** TPTM JSON day 2. Continued Scrapy project. Started scraping course at DataCamp.

**Thoughts:** Successfully generated some JSON data to practice with for TPTM chapter. My Scrapy spider is barely functional, but at least to the point that it can scrape all movie titles from the 27 pages of movies from S's collection on bluray site. I made a notebook to do some basic EDA on the titles.  

I need to learn Scrapy basics more formally than I am with YouTube. Luckily DataCamp just came out with a course for exactly what I have been trying to do. The first quarter is review from trying to get up to speed with the revived scraping project yesterday, but also covered key xpath details that are immediately useful. Last year while doing other  courses at DataCamp, I felt like I wasn't able to retain the content of many exercises without a real-world, personal problem to practice on. I think this is how I should use DataCamp going forward; I think things are most likely to stick if I have a project to immediately apply new tools to.  

Day 42: February 28, 2019

**Today's Progress:** TPTM JSON day 3. Continued Scrapy course.

**Thoughts:** Xpath and CSS selectors make sense now. Finished first half of course and half of the third-quarter chapter.

Day 43: March 1, 2019

**Today's Progress:** TPTM HTTP services day 1. Continued Scrapy course on DataCamp.

**Thoughts:** This module on consuming http services also goes well with Scrapy course and movies project.

Day 44: March 4, 2019

**Today's Progress:** TPTM HTTP services day 2. Finished Scrapy course on DataCamp.

**Thoughts:** Even though DataCamp can get through a topic quickly, it comes at the cost of deeper understanding. As long as I use it as an intermediate learning step I think it is still worth using.

Day 45: March 5, 2019

**Today's Progress:** TPTM HTTP services day 3. Continued working on Scrapy project.

**Thoughts:** I'm having a hard time categorizing the scraped titles as the associated elements aren't directly related. Trying to figure out what to do in this situation.

Day 46: March 6, 2019

**Today's Progress:** TPTM BeautifulSoup4 module day 1. Working on email notification script.

**Thoughts:** Attempting to set up an automated process to check for a movie on a particular page and send an email if it finds a match. Scraping is simple but I don't remember how to set it up as a job to check automatically and email. For these things I'm following a recent Corey Schafer tutorial that covers these tasks.

Day 47: March 7, 2019

**Today's Progress:** TPTM bs4 chapter day 2. Continued notification script.

**Thoughts:** Still working on notification notebook. Saving gmail credentials in environment variables to send notification email.

Day 48: March 15, 2019

**Today's Progress:** TPTM bs4 day 3. Continued movie notification script.

**Thoughts:** Notification script now scrapes, checks and sends and email under the right conditions. The script is inefficient in that it checks two pages to make sure the movie has moved to another location before sending the confirmation email. The script is running from a shell script to launch it every hour that my comp is in use. I need to save something to file in order to keep the script from continuing to send emails every hour after the movie moves to the right page. I will use JSON library to save the state of a class that will indicate if an email has already been sent as well as prevent redundant checking of both movie pages each time.

Day 49: March 18, 2019

**Today's Progress:** TPTM performance profiling day 1. TDD tutorial at Real Python.

**Thoughts:** I'm not a fan of this TPTM module but will try to find areas of another tutorial on TDD to apply related lessons to. I'm very happy that Real Python suddenly has hundreds of new tutorials. It seems like a better supplementary resource than some I've been using, especially while going through certain sections of TPTM training course.

Day 50: March 19, 2019

**Today's Progress:** Performance monitoring. Continued TDD tutorial.

**Thoughts:** I'm glad to be reviewing TDD again. I hope to apply some of these techniques to the chemistry cli app soon.

Day 51: March 20, 2019

**Today's Progress:** Applying performance monitoring and TDD to new version of Opera movie scraping script.

**Thoughts:** Having a hard time with environments acting as they shouldn't. There is an error somewhere but too many things are malfunctioning to be able to figure out what is happening. Traceback doesn't really make sense. Can't import any non-built-in packages or run the script. Something is being thrown out of whack by the testing setup.

Day 52: March 21, 2019

**Today's Progress:** Movie scraping script is functional again. TPTM RSS feed parser module day 1.

**Thoughts:** Implementing better code organization with class approach in this new version of the Opera movie scraping script. It is difficult to get the Testing structure and functionality down... it is still having side effect issues but at least my main environment is able to run a script again. Also getting started in a new notebook for feed_parser library to parse RSS feeds.


Day 53: March 22, 2019

**Today's Progress:** TPTM feed parser day 2. Continued working on Opera movie notification project. Working with JSON and encoding custom objects.

**Thoughts:** Working through the final parts of JSON tutorial at RealPython, in order to save custom objects to disk for later retrieval and processing. Implementing in both Opera scraping notebook and new RSS notebook. RSS notebook will save movie objects for later processing.

Day 54: March 26, 2019

**Today's Progress:** Continued RSS feed parsing and JSON custom object transcoding notebook for TPTM feed parser day 3. Exercism twelve-days exercise.

Day 55: March 27, 2019

**Today's Progress:** Exercism grade-school exercise. TPTM working with APIs in Python with Uplink library day 1. Dunder method tutorial at Real Python.

**Thoughts:** Started a new Exercism for creating a class roster; using a simple school model involving a Student class holding name and grade. This is mostly practice but am having to work out how to set up the Student class so that elements within School class roster attribute order themselves according to grade and then their name when a list of instances is passed to sorted.

I needed to learn more about Dunder methods \_\_str\_\_ and \_\_repr\_\_ to start to figure this out. Real Python was a big help. Now I need to learn about the other dunders that can be manipulated to determine default ordering and comparison between instances of a class.

Uplink library looks very useful. I may want to check out Blink cameras API again to see if this is something I could use for that. Otherwise I will find another API that requires a lot of structure within the request but doesn't have an official Python implementation.

Day 56: March 28, 2019

**Today's Progress:** Continued Exercism. More practice with dunder methods for custom object comparison, iteration, and selection. More API stuff with Uplink.

Day 57: March 29, 2019

**Today's Progress:** More Exercism. Last day of Uplink.

**Thoughts:** Mostly exercisms today. Working on robot-simulator exercise to help with exploring graph theory. Need to plan to cover more of these missed or not-yet-reached aspects of cs.


Day 58: April 1, 2019

**Today's Progress:** Working through two new involved courses. TPTM Twitter data analysis day 1. Exercism run-length-encoding exercise.

**Thoughts:** I have started following my revised plan for the next phase of learning. I need more CS theory background before I feel comfortable moving forward with the projects I have in mind. One new course is to learn to maximize the time I have to learn this stuff, called mindshift: https://www.coursera.org/learn/mindshift/home/welcome

The other course is more of an interactive textbook that I will use to guide me through learning this next level of CS concepts in an ideal order. I've already covered a lot of the concepts but in piecemeal to get through projects. I need to properly learn these concepts for a better overall comprehension. Although it uses modern python in the examples, the textbook has some major navigation, style, and clarity drawbacks so I hope to mostly use it to track my overall progress through these topics: https://runestone.academy/runestone/static/pythonds/index.html

Today is the first day of twitter data analysis in the TPTM training course. So far mostly setup. I finally realized a better way to install packages in Anaconda. I don't know why it has taken me this long to realize what was happening. I will remember to add conda-forge to the sources of new environments for easy community package installations. I think using pip when conda comes up blank may have caused all of those frustrating package errors previously.

Day 59: April 2, 2019

**Today's Progress:**  Continued courses at coursera and runestone. Learned more about itertools to work runestone examples. Very little with TPTM twitter day 2.

**Thoughts:** I really like the mindshift course. It has a lot of good reminders about how people learn, and I'm excited to get into all the stuff I have no idea about, like working with a mentor.

I am getting a little frustrated with how convoluted the coding examples are in the runestone book. Although if I don't try to untangle and understand the flow of the default code, is good practice to rewrite the examples from the functional description in a way that makes sense.

I am similarly frustrated with the current TPTM module, in that the author seems to be showing something for the sake of recording it, without regard for how unnecessary many of the stumbling points would be for the less-informed.

In rewriting the four approaches to determining if two words are anagrams, I had to look into itertools. I am glad to get more experiene with this library and learn about the iterator algebra that combine the tools to construct more capable functions.


Day 60: April 3, 2019

**Today's Progress:** Worked on a new project for Transcription repository. Continued runestone and mindshift courses.

**Thoughts:** It made things a lot easier to try and plan the program logic out before jumping into things that I still need to read code documentation to set up. I'm really glad I've been improving auxiliary programming skills to keep the code more organized and logical. I can see that combining OOP structures with what I do with data science tools will help me write things that have a simple, easy-to-follow program flow.

Day 61: April 4, 2019

**Today's Progress:** Continued new Transcription project. "Intermediate Data Science" practice at DataCamp. "Reading and Writing CSV Files in Python" at Real Python for review. Runestone course supplemented by Khan Academy computer science course.

**Thoughts:** It has been too many months since I've tried anything in Pandas, so I needed some reminders from DataCamp and Real Python. Luckily it is still in my head, just hard to recall onto an empty editor line. I made good progress with notebook today. Harvest CSV can be loaded into custom objects, now just need to order and reassemble the table, and then format excel output to specifications.

Finished analysis chapter on Runestone site.

Day 62: April 9, 2019

**Today's Progress:** Continued Harvest transcription project. VS Code tutorials. Packaging article and CLI app tutorial both at Real Python.

**Thoughts:**


Day 63: April 11, 2019

**Today's Progress:** Freezing python apps using pyinstaller. TPTM smtp mailer day 1. Continued work on Harvest script.

**Thoughts:** account setup for mailer... setup app passwords and multifactor authentication for smtplib practice.


Day 63: April 11, 2019

**Today's Progress:** More Harvest invoice generator script. DataCamp practice. Seaborn review.  TPTM mailer day 2.

**Thoughts:** Trying to figure out some visualizations for Harvest app. Reviewed Seaborn basics and added some examples to think about. SMTPlib is fun to play around with. I'm glad I recently did some of this or I'd maybe have a harder time. I'm hoping to try and set up the Harvest output to be sent by email until I can figure out a secure way to deliver a usable app.


Day 64: April 15, 2019

**Today's Progress:** TPTM mailer day 3. Supplement with Corey Schafer Python mailing review. DataCamp practice. Continued coursera Mindshift week 2. UI automation library with Pywinauto, very brief intro to MS UIA accessibility API. 

**Thoughts:** I need to automate some things, and would like to have some custom accessibility tools at some point. I completely missed staying on top of some things last week so trying to catch up on various items. I am preparing to plan steering my cirriculum to get back into some computer vision projects after I finish some of these current items.


April 17, 2019

**Today's Progress:** More smtplib practice supplemented by CoreyMS videos. TPTM pyperclip module day 1. Continued Coursera Mindshift week 2. Continued data structures/algorithm book.

**Thoughts:** I am switching to one 3-day TPTM training module per week, so will just stop counting days here. Doing one per day is fine but breaking a module over a weekend isn't efficent. It will also be nice to be able to dive deeper into modules that I need to. I will have extra time on two days each week to work on other things.

Yesterday and today I worked through CoreyMS video on smtplib. I much prefer the content I find outside of the TPTM course, but I feel like it is good to get exposure to both approaches to instruction. I just have to be sure not to let myself get stuck trying to work out problems that arise from the TPTM content, as the problems generally don't occur when following more careful sources of instruction. Sometimes just following the documentation associated with a library can be more informative and less frustrating than the paid course's catered instruction.

No problems yet in this section though. Pyperclip seems like it may come in handy for improving productivity in some things I work on, but it doesn't seem like a module I'd include in anything meant for someone else to use. 

Continued the interactive runestone book called Problem Solving with Algorithms and Data Structures. This chapter is still mostly review, 27 sections covering different basic data structures like stack, queue, and lists and several others. The chapter will cover where these can best be used and how they are implemented.

April 18, 2019

**Today's Progress:** Continued cousera Mindshift course 2nd week. Continued ALgorithms/Data Structures chapter 3. Continued with smtplib. Reviewing scrapy for small project. 

**Thoughts:** I am preparing to work on a small project that will involve using scrapy to scrape each section from the hard-to-navigate runestone interactive Problem Solving with Algorithms and Data Structures site and then email them to myself with smtplib. This will be an easier way to track my progress with the course and not have to lament the site's navigation and tracking difficulties. 

Also need to return to the transcription project to see if using an email interface is a good option for quickly getting it to people who can use it. There are also easy hosted notebook/script options I need to investigate. At some point soon I hope I can wrap it up in a Django app or something else cross platform, functional, and pretty.

April 19, 2019

**Today's Progress:** Continued Mindshift, finished week 2. Continued Algorithm study. TPTM pyperclip day 3. Hackerrank practice. 


April 22, 2019

**Today's Progress:** Mindshift week 3. Continued Algorithm study. TPTM openpyxl Excel automation library. 

**Thoughts:** Reviewing recursion and applicable problems, like recursive art and Towers of Hanoi.

April 23, 2019

**Today's Progress:** TPTM openpyxl day 2/3. Exercism exercise. Continued mindshift course. Continued researching CLI options for Harvest app.

**Thoughts:** I'm still trying to figure out the easiest way to set up the Harvest invoice generating app for others to use. 

April 24, 2019

**Today's Progress:** Continued mindshift course. Investigating hosted notebook options. Colab introduction. Published Harvest notebook to Colab. Continued algorithm study.

**Thoughts:** Colab looks like it is the quickest option to getting the script somewhere accessible to others. It actually has a lot of great features, and I can connect it to a local kernel if I use it for more computationally intense things.

April 25, 2019

**Today's Progress:**Finished mindshift week 3. Continued polishing colab script. Started scrapy review. Pygame review.

April 26, 2019

**Today's Progress:** Started runestone site scraping project. 

April 29, 2019

**Today's Progress:** TPTM Selenium automation day 1. Started final week of mindshift course. Continued scrapy Problem Solvinng book project. Datacamp practice.

**Thoughts:**  I should continue doing Scrapy scraping projects right after this one. It takes a lot of time to reintroduce a topic, although I know I have to sometimes. I'm glad that I'm already familiar enough with the components of Scrapy that it doesn't take long. Still, I think I'm to a certain point of familiarity with it that it wouldn't be difficult to get lots of practice in order to commit the operating specifics to memory.

April 30, 2019

**Today's Progress:** Continued Scrapy project. Reviewing DataCamp Scrapy course. Continued Mindshift week 4. TPTM Selenium day II. 

**Thoughts:** It looks like Scrapy has a way to interact with Javascript pages using something called Splash. This is an alternative to what TPTM course talks about with Selenium. I think my time will be better spent sticking to Scrapy methods for now.

May 1, 2019

**Today's Progress:** Continued book scraping project. Started new scrapy project for plants.

**Thoughts:** The book worked out. Trying again to build a database of plants.

May 2, 2019

**Today's Progress:** Continued working with plant Scrapy project. DataCamp practice sessions. Continued Mindshift course. Continued algorithm study.

**Thoughts:** I'm finally using Postman a little to find proper class names to use in the selector method on a response object in Scrapy.

May 3, 2019

**Today's Progress:** Continued plant spider. Finished Mindshift course. Continued algorithm study. RealPython stuff.

**Thoughts:** I am enjoying doing this other scrapy project right after the last one. It is nice to have to use different approaches to scraping the information from this plant website. I am now trying to build a database of plants that I can have a scheduled smtp script access to generate and send dialy plant emails. 

I'm working on running scraped item dictionaries through the Scrapy pipeline to format or parse certain values before storing using the feed exports. I had been saving scraped items to a json file, which is ok for a few pages of scraped details. If I want to scrape all 500 pages * 10 items/page * 10 attributes/item, those 50k attributes could cause memory problems if stored in a JSON file. JSON Lines, .jl files will just store each of the 5,000 item dictionaries as seperately loaded objects, each with only 10 attributes.

May 6, 2019

**Today's Progress:** Continued plant spider. Getting started with MongoDB.

**Thoughts:** The spider is now able to save items to jl file. I added a pipeline function to follow and download the image link associated with each plant. The filenames are set to use the unique titles, but devoid of punctuation. I got the string method translate() to remove punctuation, i'm glad to see how to use this "fastest" punctuation removal method.

I've set up MongoDB so that soon I can try and feed these items into it. 
 
May 7, 2019

**Today's Progress:** Continued plant spider. Started plant mailer. Started UCI project planning course on Coursera. Datacamp practice.

**Thoughts:** The plant spider is ready to save all plants to a jl file and all plant images to the appropriate pictures directory. I'll keep tinkering with it for  a few days to make sure I like how it is set up before scraping everything. I think it will take a long time. I should figure out how long it will take and plan to do it during off hours.

I have the last three pages of plants and their images saved as a test for planning the daily plant mailer script. I've started planning in a notebook. I am considering using the imaging library to add the text over a darkened image. Alternatively I might rebuild the text into html and insert the image. I will send the result with smtp.

UCI project planning course is first of four in a specialization on Coursera. This first course is six weeks. It is not geared for any kind of software development. It sounds like it will be helpful, but I'm not sure yet. I think it will be good to have this industry agnostic version before I get back to learning more about development paradigms.

May 8, 2019

**Today's Progress:** Continued plant mailer. Finished 2nd week UCI PM course. Started Coursera Agile course. 

**Thoughts:** I've started a new Agile specialization to determine if the UCI course is the right thing to take or if I can get by with just the Agile. I will do both until it is clear what should come first or if UCI is unneeded.

I have the feeling it'll be helpful to get both the big picture from the UCI course and the specific software product development workflow and guiding principals from the Agile course.

May 9, 2019

**Today's Progress:** Continued plant mailer. Continued Agile course. 

**Thoughts:** I've been trying to use Pillow to add the scraped details to a unique composite image including the plant image. I also want to use a CV library to extract colors for the palette for background and fonts. Alternatively colormind.io has a service I can use. Generating a gradient or unique design for the background might also be something to add. I'm running into basic problems with alignment and positioning, it may be better to just follow a standard layout template with varying elements.

May 10, 2019

**Today's Progress:** Continued plant mailer. Continued agile course. 

**Thoughts:** I have a working class that solves the text layout issue I was having. Text boxes can be generated, and later scaled and positioned onto the final composition.

May 13, 2019

**Today's Progress:** Continued agile course. Started new movie scraping Scrapy project. Datacamp practice. TPTM Flask day 1.

**Thoughts:** I'm still having a hard time trying to figure out how to reorganize the titles into their categories after they are scraped. Knowing more about Scrapy hasn't relieved this obstacle; I'll start by just scraping title details and possibly titled images. Maybe after working through it this way the steps to reorganization will become clear.

The agile course is great. The specilization will help me understand the best systematic approach to designing software and will also give me a lot of good general business insight into tech operations. It is definately the right course for me to take right now. I will also continue with the general PM specialization for a more complete understanding of the projet process, from a generic perspective.

May 14, 2019

**Today's Progress:** Continued Agile course. TPTM Flask day 2 and supplement videos from Corey Schafer. 

**Thoughts:** I really like the simplicity of Flask so far. Following TPTM Julian's videos and Corey's more in-depth equivalents to get a primer on the basics and make a simple web app. I can see the situations where I'd prefer it over Django. I won't delve too deep with learning it for now, but it will be a good thing to experiment with more when I get back to doing stuff in Django.

May 15, 2019

**Today's Progress:** Continued Agile week 2. TPTM Flask day 3. Continued Scrapy movie project.  

**Thoughts:** It is getting easier to build attractive output using Scrapy's feed exports. I'm using JSON lines again for this, and it is currently able to build a complete collection list consisting of each title, blu-ray url, and release year across ~25 pages of categorized titles. 

There's still no clear way to keep them categorized. Each movie is its own table element, only sibling to other movies and the h2's that mark each category. I might be able to record the category of each movie by finding a system that can determine if subsequent sibling elements are going to be a movie or the heading for a new category. I hope there is a simpler way.

I'm considering how to extend this from here. One thought is to get a bunch of user collection url's and scrape similar lists from each. I could then do some potentially interesting analysis across all lists.

The Agile course is demonstrating the basic use of the Venture Design Framework. The document is a cumbersome, unfriendly gdoc that needs to be filled with filler text that is very distracting. It might be something to consider turning into an app if I end up using it a lot.

May 16, 2019

**Today's Progress:** Finished week 2 of Agile course. Made small Flask app using movie data from yesterday. Finished week 2 of UCI Project Management course. Continued algorithm study.

**Thoughts:** I will keep taking the UCI course for now as it is the best option for this broader perspective. If nothing else, I'm glad to be easily learning about general project management vocabulary and resources.

May 17, 2019

**Today's Progress:** Datacamp importing practice. Khan statistics practice. Continued Algorithm study. Preparing plant scraper for full scrape.  

May 20, 2019

**Today's Progress:** Started week 3 of Agile course. Started week 3 of UCI PM course. TPTM SQLite3 day 1. Continued Algorithm tutorial on KhanAcademy.  JavaScript animation challenges from tutorial on Khan Academy.

**Thoughts:** I'm going back through the JavaScript animation tutorials on KhanAcademy so I can start with their advanced JS animation tutorials soon. I haven't looked at JavaScript much in the last 4 years. So far it is easy to skip through and just complete the unit challenges to get a refresher on the basics of Processing JS and JS in general. I hope the advanced animation course will help as I get ready to do more with Pillow, OpenCV, and Pygame.

May 21, 2019

**Today's Progress:** TPTM SQLite3 day 2. Started flower price multi-site Scrapy project. 

**Thoughts:** I started work on the next Scrapy project. This will be the first to have multiple spiders for scraping different domains. I think flower strain names and prices among local dispensaries would be a good multi-site thing to scrape. 

I feel like I'd really benefit from knowing how to use Chrome developer tools better.

May 22, 2019

**Today's Progress:** Continued Agile course. TPTM SQLite day 3.

**Thoughts:** I'm glad to get this refresher on using SQL and how to use SQLite3 with Python. It was pretty simple to write something to create a database using the plant items in a JSON file. The data is fine to transfer as it was scraped from the mygardenlife site. The data is certianly not at all structured according to best practices but it is good to see how to quickly build a database from this existing data.

May 23, 2019

**Today's Progress:** Continued Agile course. Finished plant site Scrapy project. Continued Algorithm study. 

**Thoughts:** Almost done with algorithms course. This current module covers graph representation.

May 24, 2019

**Today's Progress:** Finished week 3 Agile course. Finished week 3 UCI PM course. Made a short walkthrough video for Harvest Transcription Colab notebook. Finished graph representation module. Continued JS animation basics review. Continued multisite spider. Dev tool walkthrough.

**Thoughts:** I think I need to find a simpler product for multisite scraping, or to replan my approach. The site uses obfuscated classes that are making it really hard to scrape in an organized way. I think there may be another way to encounter the data at a lower level using Chrome dev tools, but I need more practice. I'll put that project on hold for now and plan another Scrapy multisite thing for next week.

May 28, 2019

**Today's Progress:**Continued Agile course, started week 4. Started Rice interactive Python specialization on Coursera. Started U. Michigan Web Data Access Python course on Coursera. TPTM Plotly day 1. 

**Thoughts:** I started the Rice interactive Python specialization. It will help to reinforce language fundamentals that I missed or have forgotten, and to eventually continue with more advanced concepts that I'm getting as piecemeal from other resources. The content from the first two weeks seems overly familiar; I'll just complete the exercises until I get to the units that have new concepts. I am going through the entire specialization because each course covers a lot of ground and the later content seemes to build on the particular foundation of the early courses. I think it will be good to reinforce basic best practices until it gets to the courses that I'm really interested in. The entire specialization has 6 courses, 4 weeks each. I think I can get through the first two courses fairly quickly so that the interesting work picks up when I have more free capacity.

I am taking the U. Michigan Web Data Access course to help me with scraping and data transfer projects. The first week gives an excellent overview of regex.

May 29, 2019

**Today's Progress:**Continued Agile course. Finished week 1 Rice Python course 1. TPTM Plotly day 2. Started modern robotics specilization on coursera. Finished week 4 UCI PM course.

**Thoughts:** The general PM course isn't offering what I expected. The odd presentation hasn't faded with the introductory material, and it is hard to imagine gaining much from several courses worth of material presented this way. I now think the course might just be incredibly drawn out due to poor course planning, rather than to allow for a deeper exploration of the subject. I will stop this course now and find more concise sources for insight into traditional project management techniques.

May 30, 2019

**Today's Progress:** Continued modern robotics course. Continued Agile course. 

**Thoughts:** The robotics courses are going to take significant commitment. I didn't expect to find something with this much depth, but I think it would be good to go through it all to see how that field feels. The specialization covers some programming, but mostly has a lot of theory based in engineering and physics. I haven't thought about robots since I started getting into CS, but it seems like the perfect multidisciplinary outlet to apply many adjacent intrests to.

May 31, 2019

**Today's Progress:** Continued modern robotics course. Finished week 2 of Web Data Access course. Finished first Agile course. Exercism Phone Number exercise. 

June 3, 2019

**Today's Progress:** Continued modern robotics course week 1. Continued related Queensland Uni Tech "Masterclass" video resources on 2D geometry. Started week 2 of Rice Interactive Computing course.

**Thoughts:** The Rice interactive computing course is now introducing the event-driven paradigm and how it is used in GUI programming. The course uses a custom GUI library that works within their perscribed browser environment. I'll translate the exercises to use the wxPython GUI toolkit so that I can get practice with the real tools.

I am using the video lectures on the Queensland University of Technology Robot Academy site to help remind me of basic physics and help me move through the Modern Robotics course. The course seems to assume that I know a lot more than I do about physics and mechanical engineering. I think the combination of resources will give me the information I need to understand the more mechanical aspects of the Modern Robotics course.

June 4, 2019

**Today's Progress:** Continued Rice IPP course. Reproducing event-driven exercises with wxpython.

**Thoughts:** Even though is taking some time to get up to speed with wxpython, it looks like it is a good choice over using the course's custom library. I should be able to reproduce all of the course's practice exercises with wx's tools.

June 5, 2019

**Today's Progress:** Continued Rice IPP course. Continued Modern Robotics course.

June 6, 2019

**Today's Progress:** Finished U. Michigan Web Data Access week 3. Continued Rice IPP course. 

**Thoughts:** The Pythohn Web Data Access course covered web sockets and how to access them by manually sending requests or using python libraries to retrieve and parse data. This week's content is partially review, but includes some new stuff on lower-level workings of the web. The same instructor has another Coursera course that dives deep into web history and technologies, I will start it next.

June 7, 2019

**Today's Progress:**  Finished week 1 Modern Robotics and 2D geometry QUT lecture series. Started Linear Algebra on Khan Academy. Finished week 3 Rice interactive programming course. 

**Thoughts:** The math for these robotics courses isn't easy to follow. So far it involves some trig but a lot from linear algebra. I had a bit of linear algebra in the last weeks of college trig, but that was a few years ago. I will pause the robotics courses until I can get a better handle on the math. I am going to take khan academy's linear algebra course to catch up.

I was able to reproduce this week's programming challenge with wxpython for the Rice IPP course. There were some speedbumps trying to figure out some concepts that the Rice course hasn't reached yet, but that are required for a very basic wxpython app. I think the course will get to these, so I figured out what I could to just get it working.

June 10, 2019

**Today's Progress:** Started first week of course 2 of Agile specialization. Started Khan linear algebra course.


**Thoughts:** This second Agile course focuses on planning and managing design sprints. I still like the instructor. 

June 11, 2019

**Today's Progress:** Continued Agile II course. Continued Linear Algebra course. Continued week 4 Rice Interactive Programming course. 

**Thoughts:** The Rice interactive programming course is still covering familiar Python topics, but all of the GUI and event-driven concepts are new to me. This week's unfamiliar concept involves drawing graphics within the gui window. The simplified exercises make sense and involve drawing text and simple shapes to a canvas widget within the codeskulptor environment. 

It is more challenging to translate this outcome to wxpython. I found a helpful tutorial on someone's website but I still haven't quite figured it out. I think translating these exercises to wxpython will get easier as the concepts get more difficult, so hopefully I will not be overwhelmed with both difficulties simultaneously.

June 12, 2019

**Today's Progress:** Continued first section of Linear Algebra course. Continued week 4 Rice Interactive Programming course. 

**Thoughts:** I am switching from wxpython to QT for Python after doing some more research. I am having a hard time tyring to find recent or helpful resources for wxpython. I considered pyqt4 for its better documentation, but it sounds like that is also out of date at this point. The successor is pyqt5. I'm not using that because there's a twin framework with even more support, and that is QT for Python. I am trying to reproduce the stuff what I've done in wxpython, and QT already seems much more friendly.

June 13, 2019

**Today's Progress:** Continued catching up with QT for Python. Continued Rice course. Continued Agile II course. 

June 14, 2019

**Today's Progress:** Finished Agile II week 1. Continued Rice course.

**Thoughts:** I had too much to get through this week. I'm moving Rice interactive computing course, U. Michigan web data course, and linear algebra course deadlines to next week. I think it would be a better approach to save Rice course activities for later in the week once I'm done with less sticky things.

June 17, 2019

**Today's Progress:** Continued U. Michigan Access Web Data course week 4. Started Agile II week 2. 

June 18, 2019

**Today's Progress:** Finished U. Michigan Access Web Data course week 4. Finished Agile II week 2.

**Thoughts:** I am getting a lot out of this Agile course, but it does refer to many unfamiliar aspects of business operations that I've never encountered before. I think it will be a good plan to achieve a broad overviw of this topic and retake all Agile courses again after I've had more experience in the industry. I think I will be able to absorb more useful subtleties when I can use specific experience to anchor the theory of Agile venture design to something that I've personally worked through.

The Web Data course is a good demonstration of this return-after-experience idea. I learned a lot of this from other sources before I had any experience with it. Now it is much easier to relate these methods to things I've done before in order to absorb a deeper understanding of these fundamental mechanisms for accessing web data. This week explores the urllib library and parsing html with bs4.

June 19, 2019

**Today's Progress:** Continued Rice Interactive Programming course week 4. 

**Thoughts:** I'm still catching up some with QT for Python.

June 20, 2019

**Today's Progress:** Continued Rice course. Catching up with Pygame.

**Thoughts:** It is too much to try and get up to speed with QT with its current available resources. A lot of the documentation is very recent; I think tere will be more helpful resources in the near future. I'm putting it aside for now. I'm going to try to use Pygame for the remainder of the course.

June 21, 2019

**Today's Progress:** Finished Rice IPP course week 4.

**Thoughts:** I feel adequately caught up in the Rice course with Pygame. It looks like it has the functionality and documentation that I need to reproduce the challenges outside of the course's CodeSkulptor environment. I didn't get to linear algebra this week but I think I will have much more time next week now that I'm up to speed with Pygame.

June 24, 2019

**Today's Progress:** Started Agile II week 3. Started Rice IPP course week 5.

**Thoughts:** I'm really glad I switched to Pygame. This week covers motion control and navigation. It is a good time to be taking linear algebra.

June 25, 2019

**Today's Progress:** Continued Agile II week 3. Continued Rice IPP week 5. Continued Linear Algebra Vectors unit. 

**Thoughts:** The more I use Pygame, the happier I am that I'm using it instead of the alternatives that I tried. I'm not sure why I tried the alternatives before trying Pygame.

The Agile course has a lot of helpful ideas, even without much familiarity with traditional project managment. This chapter is delves into principals from Lean Startup and how they can be used to help make the right design decisions.

June 26, 2019

**Today's Progress:** Continued Rice IPP week 5. Continued Linear Algebra Vectors unit.

**Thoughts:** I am all through this week's exercises and am working on the coding challenge to build a pong clone.

June 27, 2019

**Today's Progress:** Continued Rice IPP week 5. Continued Agile II week 3.

**Thoughts:** I like this Rice course a lot, but I'm really glad to be avoiding the perscribed Python 2 CodeSkulptor environment. The general coding lessons are still very basic while all of the event driven programming concepts are new to me. This class feels like it would be a bad choice for someone just learning how to program. I can imagine starting here and immediately drowning in the lopsided skill requirements. I'm glad the course can be efficiently adapted to my needs. Recreating things in Pygame certainly feels like the most productive use of the course content.

June 28, 2019

**Today's Progress:** Finished Rice IPP week 5 and coding challenge Pong project. Finished Agile II week 3. Continued Khan Linear Algebra, Vectors unit. Finished U. Michigan Web Data Access week 5.

**Thoughts:** The Web Data course is reviewing how to use Python send data across the network to any application while independently validating that data on each side according to a protocol schema. XML/XSD is used to illustrate this point. The material is getting less familiar but is still easy to follow. I'm glad this course exists.

July 1, 2019

**Today's Progress:** Started Rice IPP II week 1 and coding challenge Memory project.

**Thoughts:** I'm having a lot of fun with Pygame.

July 2, 2019

**Today's Progress:** Started UMich Web Data Access course week 6. Started Agile II week 4. Continued Rice IPP II week 1 coding project.

**Thoughts:** This week the UMich course reviews web services. It makes it easier for sevices to communicate when they have a service layer that can use a standard serialization format like XML or JSON. This course delves into the topic more thouroughly than other stuff I've seen related to this topic.

July 3, 2019

**Today's Progress:** Continued UMich Web Data Access week 6. Continued IPP II week 1 coding project. Continued Agile II week 4.

**Thoughts:** I'm almost finished with this week's Memory game coding project. It has come together well but still has a bug. The game is like memory with moving cards. It is comically difficult to play but the code was fun to figure out. The board generates a set number of matched cards that bounce around the screen and off of eachother. Clicking a card reveals its color, clicking another assesses the match, and another to return unmatched to the default card back or keep the match revealed and start another reveal loop.

At this point it feels like this course is just providing starting points for Pygame project ideas. The videos are uneven and it has been a little irritating to listen to long-winded descriptions of things I've heard other people describe efficiently. Reviewing fundamentals doesn't usually feel wasteful. It is hard to want to get through each and every video considering what I'm trying to get out of it. I'm finding more appropriate event-driven instructions from other resources and can glean theory keywords from other course materials. I will try watching every video again when some of the instructors and skill requirements change in courses III to VII of this specialization.

July 4, 2019

**Today's Progress:** Completed Linear Combinations unit of Linear Algebra course on Khan academy. Continued UMich Web Data Access week 6. Finished Agile II week 4.

July 5, 2019

**Today's Progress:** Finished final week of UMich Web Data Access course.

**Thoughts** Memory is all finished and the unrealistic movement of the cards makes me want to learn more about how to model particle systems.

July 8, 2019

**Today's Progress:** Started U Mich Databases in Python course. Started U Geneva Natural Models and Simulations course. Started week 2 of Rice IPP II course. 

**Thoughts:** The new U Mich course is on SQL and Databases through Python. It seems like all of the content planned for the next 5 weeks will be review. I havent learned about SQL since before I knew anything about programming. It should be relatively easy to reabsorb the in-depth fundamentals of relational databases this way. The course after this in the specialization will focus on building a robust scraping application. I need to be able to design a relational database for this capstone project, so I'm happy to get the review.

Both this new course and this week's main topic in the Rice course are covering OOP theory fundamentals. It is good, repetitious review that I can just skim through. This week's project for the Rice course is to make a blackjack game that looks like 1995. Their starting code is something I want to try to follow and expand on top of now that they are using a completely object-oriented approach.

To make up for easy SQL course, I started a natural models and simulations course. I think it is a good candidate for a course that would help me get a handle on the various computational science processes that I've been learning piecemeal through other resources. I think the Khan JS animation courses gave me a great foundation for animation and some modeling but didn't provide much theory for being able to simulate anything complicated. This course feels like a good fit for many things i'm trying to learn about now.

July 9, 2019

**Today's Progress:** Finished UMich Databases with Python week 1. Started Agile II week 5. Continued project for Rice IPP II week 2.

July 10, 2019

**Today's Progress:** Finished UG Natural Models and Simulations week 1. 

July 11, 2019

**Today's Progress:** Finished final week of Agile II course. Continued blackjack project for Rice IPP II week 2.

**Thoughts:** The cards for the blackjack game are in a sprite sheet. This is the first time I've had to write a spritesheet class to return a specified rect of the spritesheet, for drawing each card individually when given a sprite cell index. 


July 12, 2019

**Today's Progress:** Finished blackjack project for week 2 of Rice IPP II course.

**Thoughts:** I've learned a lot of new things while programming this Blackjack game. I think it is the best organized and longest thing I've written. I wrote this into multiple files; it's the first time I've had to modularize, outside of a framework. It meets my minimum goals but there is a lot more I could add to make it more enjoyable. I'd like to work on it more in the future as I have time. 

July 15, 2019

**Today's Progress:** Completed lectures for second week in U. Geneva Natural models and simulations course. Started first week of Agile III course. Started Rice IPP II week 3. 

**Thoughts:** This week in UG NMS course is devoted to introducing Python, and is all review. I was interested to see how they would present it, and I'm glad I watched most of the videos. The new lecturer presented the most basic conceipts of working with Python and introduced the Numpy library. It is very apparent that this guy doesn't appreciate consistency or clarity in his code examples, and may have very little experience with Python. I hope that I can remember how Python was presented in case I get frustrated with any other difficult explanations about other stuff, stuff that I don't have experience with.

I started the third of five courses from the Agile Development specialization. I still really like this instructor. This couse focuses on "managing an aglie team" and this week is exploring scrum and xp development approaches. The materials for this week included a great video from Spotify about its development culture and how it continues to evolve. I really like what they had to talk about.

July 16, 2019

**Today's Progress:** Continued Rice IPP II week 3 and started weekly project.  

**Thoughts:** I'm very rusty on the simple physics and trig required for reproducing this week's coding project. I am starting to need to reference the videos more, and I'm trying to get through basic physics course on Khan for general helpful reminding while I'm doing this stuff.

I'm looking ahead in the U Geneva natural models and simulations course, and I'm excited for getting exposure to the theory and methods for lifelike simulations. I'm particularly excited to see their coverage of cellular automata in the next couple of weeks. I'm hoping to be able to implement a configurable, 2d cellular automata in Pygame.

July 17, 2019

**Today's Progress:** Continued Rice IPP II week 3 project. Continued Agile III week 3. Started U Mich Databases with Python week 2.

July 18, 2019

**Today's Progress:** Continued Rice IPP II week 3 project. Continued Agile III week 3.

**Thoughts:** The main Ship class is fully implemented and was working. It is temporarily disabled as I am  attempting to optimize some of the controls code. I'm using a dictionary with button handler values so that I can just iterate through the list of controllable keys rather than having nested if elifs to catch button down events. I am also trying to alter the left/right rotational control to be a continuous instruction when pressed, like how the up arrow toggles the main thrust to accelerate when held down. There is some unexpected behaviour as I am attempting to set the thrust and rotation attributes with a generalized, configurable handler.

July 19, 2019

**Today's Progress:** Finished U Mich Databases with python week 2. Finished Agile III week 3. Finished first part of Rice IPP II final project, week 3 project. 

**Thoughts:** I have written to a good place to end this week's project. The player controlled ship is working with continuous control capabilities. The main window spawns animated enemies with random acceleration. I've reimplemented the Spritesheet class from the Blackjack game to help animate the enemies. I would like to refactor the player Ship and enemy Rock classes to be more DRY by making them inherit from a more general, custom sprite class. The collision detection and projectiles will be implemented in the next stage, for week 4's project.

July 22, 2019

**Today's Progress:** Started UG Natural Models and Simulations week 3. Started Agile III week 4.

July 23, 2019

**Today's Progress:** Started Rice IPP II week 4. Continued UG NMS week 3. Wrote random walk simulation in Pygame. Continued Agile III week 4. 

**Thoughts:** I used an approach outlined in the NMS course to make a random walk simulation animation in Pygame. 

July 24, 2019

**Today's Progress:** Continued Rice IPP II week 4. Continued UG NMS week 3. Finished U Mich Databases with python week 3. Continued Agile III week 4. Made intro demo notebook with simpleaudio library. Forked and continued random walk simulation in new animations folder of pygame repo.

**Thoughts:** I really enjoyed working on the random walk simulation. I'm continuing the project in a new animations folder of my pygame repository. I have made it prettier, and am experimenting with tweaking different parameters to affect the end result. It could benefit from threading. It is very calming to watch, and it makes me want to do something similar with sound at the same time to enhance that effect. 

July 25, 2019

**Today's Progress:** Finished UG Natural Models and Simulations week 3. Continued Agile III week 4. 

**Thoughts:** The math presented with this week's lectures of the simulations course is mostly over my head. It involves some recongnizible calculus and vaguely familiar operations, but for the most part is very dense. Much of this week was exploring specific applications of highly generalized equations all while assuming that the audience must have the same experience as the lecturer. The language barrier certainly doesn't help with the difficult communication. It is helpful to assume that the bulk of this is incomprehensible for the same reasons that this lecturer's introduction to Python programming was mostly just confusing and unhelpful. I watched the exhausting series in hopes that some of this is valid and will somehow seep into my head to help me understand difficult programming obstacles later. 

I am very, very excited for next week's topic on cellular automata. Glancing ahead it already seems infinitely more understandable than this pure, pure math has been.

July 26, 2019

**Today's Progress:** Continued Agile III week 4. 

**Thoughts:** I am still trying to get through the rest of this week's Agile lectures. There are a lot of sections this week, all with very helpful workflow productivity information. I will have to stretch this week's content over two weeks.

July 29, 2019

**Today's Progress:** Continued Agile III week 4. Started UG Natural Models and Simulations week 4.

**Thoughts:** I haven't gotten very far with the lectures, but everything seems clear so far. I can already see a way to implement a simple 2d automaton with the Pygame tools. I've started working on the first script to visiualize this simple version; I was able to reuse a lot of the code structure from the random walk simulation visualization from last week. I am really excited to continue working with CA and hear about all of their useful applications. 

July 30, 2019

**Today's Progress:** Continued Agile III week 4. Continued UG NMS week 4.

**Thoughts:** I've made a working version of Conway's game of life automaton. It seems really slow. I'm trying to find and come up with some ways to make it able to run faster.

July 31, 2019

**Today's Progress:** Finished Agile III week 4. Continued UG NMS week 4. 

**Thoughts:** The UG course has talked about several automata I'd like to try to make. One is a competition/inhibition process, another is a traffic model, and the third is a Langton Ant. I'm interested to see if multiple ants could be used to make a larger pattern, possibly a noded web of highways. The automata demonstration videos are really short and the lecturer doesn't mention anything about recreating them. I am curious about how they will incorportate Python in this course.                                                  

August 1, 2019

**Today's Progress:** Continued UG NMS week 4. Started traffic automaton project. Started UMich Databases with Python week 4.

August 2, 2019

**Today's Progress:** Continued UG NMS week 4. Continued traffic automaton project. 

**Thoughts:** I am really enjoying the content in NMS this week, and would like to make more projects inspired by CA theory. I think I will stretch this week over one to three more weeks in order to dive deeper into this content.

August 5, 2019

**Today's Progress:** Started Rice Principals of Computing I Coursera course. Continued UG NMS week 4 and other resources on CAs. Continued traffic automaton project.

**Thoughts:** I'm starting the next course in the Fundamentals of Computing Specialization. This course still isn't the anticipated algorithmic thinking course, but a prerequisite step. It looks like the content and assignments will be mostly review, but it is time for a refresher on many of the topics. This first week was introductory and light so I hope to get through the second week's content, later this week.

I'm continuing the UG NMS course and closely inspecting the unit on LGAs to try and plan out a Pygame implementation.

August 6, 2019

**Today's Progress:** Continued investigating topics mentioned in UG NMS week 4. Started HPP model Lattice Gas Automaton project. Started Agile III week 3.

**Thoughts:** I am trying to write an optimized implementiation of the HPP model LGA and visualize it in Pygame. I haven't found much accesible information about implementing it, so it may end up unoptimized if I can't translate the description properly. The HPP model is the simplest to start with and I hope it gives me a better grasp on the concepts so that I can try implementing some of the more advanced LGA models.

<!---

Day x: August x, 2019

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
