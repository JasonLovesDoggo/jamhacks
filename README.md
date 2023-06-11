# PhysioQuest
> Gamifiyng physiotherapy to encourage consistency and accuracy 

## How to run
#### Website
1. Install python
2. clone the repo using `git clone` https://github.com/JasonLovesDoggo/jamhacks.git and `cd` into the directory 
3. run `pip install -r requirements.txt`
4. run `cd jamhacks`
5. run the following 
  - `python ./manage.py migrate --run-syncdb`
  - `python ./manage.py loaddata fixtures/users.json`
  - `python ./manage.py loaddata fixtures/exercises.json`
  - `python ./manage.py loaddata fixtures/quests.json`
 6. start the server using `python ./manage.py runserver`

#### AI model (openCV)
1. Change the directory to `jamhacks\camera`
2. Enter the command `python -m streamlit run ArmRaise_Webcam.py`


## Inspiration
This project came about because of our group's personal experience with how difficult it is to actually stay on top and keep track of exercises that physiotherapists assign. About a week ago, I went to the physiotherapist to check up on my jaw (it was misaligned), and the physiotherapist gave me a list of exercises for me to do every evening until our next appointment. I told myself I would do the exercises, but when the next day came, I forgot, and the day after that, I was too lazy to do it. Physioquest is meant to be an answer to this problem of being unable to complete daily exercises, a problem that I'm sure is experienced by more than just me. 

### What it does
Physioquest turns the mundane physiotherapist-assigned exercises into a game, encouraging you to complete your exercises every day by creating streaks and providing points for accuracy. It also contains other features such as a ranking system, badges, an admin interface for physiotherapists to assign exercises to their clients, and much, much more.

The OpenCV Camera Demo can be found [here](https://youtu.be/K0PG3x9Bbh4).

### How we built it
Physioquest utilizes the Mediapipe Pose Landmarks library to detect and track human poses from a live camera feed. It then measures the angle of each shoulder to ensure the user is correctly completing the given quest and rewards them based on accuracy.

### Challenges we ran into
One challenge we encountered is integration. Although we were able to get each aspect working individually, we struggled with integrating them all together. Another challenge we ran into was time management. Given a 36 hour time frame, we struggled with keeping on task to complete the project on time.

### Accomplishments that we're proud of
We are proud of our use of AI considering the fact that none of us had knowledge on how to create an AI model going into this project. We are also proud of our effective communication and teamwork, utilizing each other's strengths and recognizing weaknesses to effectively create an AI based project.

### What we have learned
Going into this project, we had little to no knowledge on the use of OpenCV. Throughout the course of this project, we were able to learn how to use facial detection and body movements to complete complex tasks.

### What's next for PhysioQuest
The first thing to do would be to fully integrate openCV with our program to get full functionality. Then, we would implement some of the following:
- a better admin panel for physiotherapists that is more intuitive. Currently, we are just using basic django admin models. 
- fleshing out the socialization feature, allowing users with similar issues to connect and work together to get better
- make the program into a mobile application, as it would probably be more applicable/practical there. Currently, our product is a pwa. 
- incorporate more game aspects like sprites and other graphics to make it a better user experience




<br/>


##### DB setup (dev)


Dump fixtures: `python manage.py dumpdata backend.model_name --indent 4 > fixtures/model_name.json`

Load fixtures:
`python manage.py loaddata fixtures/exercises.json`
`python manage.py loaddata fixtures/quests.json`
`python manage.py loaddata fixtures/users.json`
