![Project VSAP](https://media.discordapp.net/attachments/777942258569576468/845900648356118579/Banner_2.png?width=1014&height=676)

# Welcome to VSAP (Vaccine Seeker And Pasport)

## Inspiration & Explanation:
After realizing the massive increase of vaccines being distrubuted in canada, as well as vaccines now being distributed to children, we saw that there is no proper system to log and identify people with the vaccine. 
As more and more places are being openned up, there is an increasing need for an open and easy to use system for consumers and owners to show and read vaccination data. 

***Project VSAP is made to solve all issues related to COVID19 Vaccination identification***

**Doccumentation + Hourly Log:** [Project VSAP Doccumentation - JustPaste.it](https://justpaste.it/project-vsap)

**Demonstration Video: ** [Youtube - JamHacks V: Project VSAP](https://www.youtube.com/watch?v=cn72vaj4BQk)

## Preview:
![enter image description here](https://media.discordapp.net/attachments/844733789011836948/845987840571605062/thumnail1.png?width=1080&height=539)
![enter image description here](https://media.discordapp.net/attachments/844733789011836948/845987840835715112/thumnail2.png?width=1078&height=559)![enter image description here](https://media.discordapp.net/attachments/844733789011836948/845987844476633108/thumnail4.png?width=1080&height=544)
![enter image description here](https://media.discordapp.net/attachments/844733789011836948/845987849602203658/thumnail5.png?width=1080&height=507)![enter image description here](https://media.discordapp.net/attachments/844733789011836948/845988330046881854/thumnail6.png?width=1080&height=537)

## How we built it:
We used the [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/) as a base for our website as we were all experienced with python and were eager to learn more about this framework. Here is all the list of modules we used:

>flask == 1.1.2

>flask_login == 0.5.0

>flask_migrate == 2.7.0

>flask_mysqldb == 1.2.9

>flask_wtf == 0.14.3

>flask_sqlalchemy == 2.4.4

>sqlalchemy == 1.3.23

>psycopg2

>email_validator == 1.1.2

>python-decouple == 3.4

>gunicorn == 20.0.4

>jinja2 == 2.11.3

As well as making it perform good, we also wanted for it to look good, so we added in along with the Flask basework lots of design with CSS and JS. The website in the end is a sleek and good looking admin pannel as well as hyper-responsive with interactive widgets, and scalable assets. It also is mobile-friendly.

We were all working on the project in parts, with Yair creating the overall base and the spotter, Michael working on the QR code and pasporting, David working on the toolbox/utilities and Katelyn providing info for the statistics page.

Our website is also updatable, where all of its data is connected through seperate govermnent/open-source API's and is neatly visualised through graphs and whatnot. 

We also used [CockroachDB](https://www.cockroachlabs.com/) for our data sets as it's simple to use, versatile, and works like any other PostgreSQL databases.

## Challenges/Difficulties:
Our main challenge was creating a valid method to convert data into a QR code. We went through many ideas as well as prototypes and settled on the info being automatically created as a new page, and instead of the QR code reading the info it generates a unique link which then directs to the info page: 
![enter image description here](https://cdn.discordapp.com/attachments/844733789011836948/845993423889760326/unknown.png)

Another challenge we ran into is how to create a working and (somewhat) secure login page. After a bit of research, we ended up creating a local SQLite file, and then hashing the logins in [SHA512](https://en.wikipedia.org/wiki/SHA-2) , a very secure encryption format. The following is a snippet from our login code:
![enter image description here](https://media.discordapp.net/attachments/844733789011836948/845726741405892678/unknown.png)

And finally the biggest problem so far was just thinking of a way to create an informative but also good looking UI. After what felt like an infinite ammount of revisions, we tuned the website to not only look good but also be changabale, there is a little widget that lets you change the appearance and color of the website
![enter image description here](https://cdn.discordapp.com/attachments/844733789011836948/845994708168605716/unknown.png)

## What we learned & What's next
We learned a lot of usefull formatting tips as well as identifying personell through logins and information in python as well as a general use of Flask and its fraimwork. We already knew a good ammount of styling and UI development prehand but I personally learned a lot about CSS Scripting and morphing assets together to create a truly compelling website.

We plan on adding in more features as listed in our to-do list, and overall make the app ready for production (we want to make this a real thing!!).

We believe Project VSAP was not only a fun development, but also has massive potential for the future of vaccination, if you're reading this and interested in planning something up, feel free to get in contact with our team :)



*If you made it to all the way here, thank you for reading about our development and we hope you have a great day!*

![enter image description here](https://i2.wp.com/wowlookawebsite.com/wp-content/uploads/2018/07/that_s_all_folks__by_surrimugge-d6rfav1.png?fit=1024,576&ssl=1)
