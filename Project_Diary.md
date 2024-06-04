# Group project diary
Will be updated as much as reasonably possible.

# Initial set up
We agreed to use teams to communicate

- Set up github project management
- Set up github code repository
Assign issues to the github code repository

# Monday, 18 March 2024
recieved drawing from Naman

# Tuesday, 19 March 2024
request for remaining members to join the github code repo 

Team worked on datasets and regulatory requirements for us to use in determining
relevant variables to our problem.

# Tuesday,  02 April 2024
Set up readme and project diary in github,
Currently work in progress.

# Thursday, 25 April 2024
Assigned more tasks in our group meeting, 
Julian - regulations for the observation values
Use the government regulations to create an indication on if the value means the water is safe

JacobC - scraping well data (mainly for long/latitude)
Attempting to use ECAN data to produce reports on Wells that we can use for location data in regions

JacobR - fix postgres issues, look into automation of postgesql token creation, sort out automation processes
find out why the postgres token is failing and create automated processes for configuration of each step of the data collection.

# Sunday, 28 April 2024
JacobC - Three ECAN scripts pushed into develop branch
JacobR - Wrote Docker script for getcontent.py. Also selenium scraper for groundwater is up
Julian - Out of action coming week, baby due to arrive

# Thursday, 30 April 2024
JacobR - Added jwt api file
Julian - Able to scrape Drinking Water Standards (called Scrapebook3.ipynb), but data includes HTML tags, needs to be addressed

# Monday, 6 May 2024
Short list of things to look into:
- Discuss github code layout
- Scripts to automate the process (have docker and can use that with terraform to test)
- Have JWT token so I can try and test a python script
- What state is the website in?
- Check duplicate functions
JacobC and JacobR discussed these in class

# Tuesday, 7 May 2024
JacobR - Got an AWS instance spawning using terraform, now on GitHub
Julian - Drinking Water Standards scraping script now working. Couldn't push on GitHub, script on Teams chat

# Wednesday, 8 May 2024
JacobC - Organised group meeting for when everyone is free (13 May 2024, next Monday)

# Sunday, 12 May 2024
Julian - lost all lines in wrangling.py while pushing using VS code commit and push button, to be addressed
JacobR - Resolved Julians conflict

# Monday, 13 May 2024
Group Meeting
Things to work on:
- Git structure, work on decomposing scripts
- Demo API for website (code list)
- Database design
- Determine what the dims measurements and attributes are

# Tuesday, 14 May 2024
Naman - Group needs to provide the latest test data for say 3-4 wells, and the details for all the wells(active and inactive) should be enough for the testing. Also currently the computations are done client side which is not ideal and will eventually slower down the fetch to keep the speed up we need to backend framework .
JacobC - It appears that Lawa has changed the way downloads work on their website. It appears that you have to subscribe before it will let me download the dataset. But the subscribe button doesn't even work - to be addressed. Will be opened as an issue after we are finished with the gitstructure branch and have merged it back with develop. 
       - Scripts from JacobC have all been decomposed
JacobR - Updated Docker script

# Wednesday, 15 May 2024
Julian - Updated wrangling.py and Scrapebook3 (Drinking Water Standards scraping)