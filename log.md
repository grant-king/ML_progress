s# 100 Days Of Code - Log
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
 

# **Links to work:**
## Jupyter Notebooks
#### Movie JSON EDA
https://github.com/grant-king/report/blob/master/TPTM_challenges/movie_JSON_EDA.ipynb

## Exercism exercises
#### Tournament
https://exercism.io/tracks/python/exercises/tournament/solutions/16a3d12389a84d918344ec6f87ac3caa

#### High Scores
https://exercism.io/tracks/python/exercises/high-scores/solutions/1225821f040548419cf06c30954780ba

#### Bank account
https://exercism.io/tracks/python/exercises/bank-account/solutions/2ef97a17222f482cb0e30be054505e0f

<!---

Day x: May x, 2019

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
