# *Nine Lives*

"Nine Lives" is a classic word-guessing game that puts players' vocabulary and deduction skills to the test. Much like its counterpart, Hangman, players attempt to guess a hidden word by suggesting letters one at a time. However, in "Nine Lives," the stakes are higher as players are granted a limited number of incorrect guesses, represented by the titular nine lives. With each incorrect guess, a life is lost, bringing them one step closer to failure. The challenge lies in strategically selecting letters to unveil the mystery word before all nine lives are depleted. "Nine Lives" offers a thrilling and engaging experience, combining elements of wordplay and suspense to keep players on the edge of their seats until the very end.


[Nine Lives](https://nine-lives-68c816aea862.herokuapp.com/).


---


## User Experience

   ### How to Play

    1. Describe the basic premise of the game. Link to Wikipedia with more detail.
    2. Distinguish any differences in this game and others.
    3. Give a clear organised list of instructions. This may be separate from the previous two points.

   ### User Story (OPTIONAL)

   #### External user’s goal:(OPTIONAL)

    - Goal 1
    - Goal 2
    - Goal None: You may have 1 or none.

   #### Site owner's goal:(OPTIONAL)

    - Goal 1
    - Goal 2
    - Goal None: You may have 1 or none.


---


## Design

   ### Flow Chart

    DELETE ANYTHING NOT APPLICABLE TO THIS PROJECT.
    There are some nice schema applications you can use for planning your project:
    - [Miro](https://miro.com/app/board/uXjVNiugb1U=/)
    - [Lucidchart](https://www.lucidchart.com/pages)

    I used _____ to illustrate some of the main logical points before I began to code.
    ![Flowchart](link_to_flowchart_documentation_here)
    I used _____ to plan the logic of my applicaiton.
    ![Flowchart](link_to_flowchart_documentation_here)


---


## Features


| Feature | Existing Features | Future Implementations | Screenshots |
| --- | --- | --- | --- |

### Gameplay
---


## Technologies Used


   ### Language

   - [Python](https://www.python.org/) was the core language used.


   ### Libraries

   - [Python Library](https://docs.python.org/3/):
      - [join method](https://docs.python.org/3/search.html?q=join%28%29) was used to turn an iterable into a string.
      - [random.choices](https://docs.python.org/3/library/random.html#random.choice) was used to randomly choose a word from a list.
      - [set class](https://docs.python.org/3/library/stdtypes.html#set) was used to ensure a selection of unique words.
      - [string](https://docs.python.org/3/library/string.html#module-string) was used to concatenate input letters.



   ### Frameworks & Tools

    DELETE ANYTHING NOT APPLICABLE TO THIS PROJECT.
   - [ChatGPT](https://chat.openai.com/)
   - [Ezgif.com](https://ezgif.com/maker)
   - [GitHub](https://github.com/) was used to create & store my repository.
   - [Gitpod](https://www.gitpod.io/) was used as my IDE workspace.
   - [Heroku](https://www.heroku.com/) was used to deploy the application.
   - [Lucid Chart](https://www.lucidchart.com/pages/)
   - [Miro](https://miro.com/app/board/uXjVNiugb1U=/)
   - [Replit](https://replit.com/) was used to experiment with variations of code.


---


## Deployment & Local Development


  ### Deployment

  The site was deployed using Heroku. The is how the live site was deployed:

  1. Log in (or sign up) to Heroku.
  2. Go to the user dashboard & click "Create new app". Keep in mind that each app name on Heroku has to be unique.
  3. Select the region & click "Create app".
  4. Go to the settings tab & scroll to the "Config vars" section.
  5. Click "Reveal Config Vars".
  6. Create a Config Var, set the key field to "PORT" & the value key to "8000".
  7. If you have credentials, insert "CREDS" for the key field. Copy & paste the entire JSON file to the value field.
  8. Scroll to the "Buildpacks" section.
  9. Click "Add buildpacks". Select "Python" and "nodejs", and in that order.
  10. Go to the “Deploy” tab.
  11. Scroll to the “Deployment Method” section.
  12. Click on “Connect to Github”. Search for the repository name & click "Connect".
  13. Scroll to the "Manual Deploys" section.
  14. Click "Deploy Branch". A message will show up to say "Your app was usccessfully deployed. The "View" button will take you to your deployed link.


  ### Local Development

  #### How to Fork

  To fork the Nine Lives repository:

  1. Log in (or sign up) to Github.
  2. Go to the repository for this project, [Kate McGuane / nine-lives](https://github.com/KateMcGuane/nine-lives).
  3. Click the Fork button in the top right corner. This action will create a copy of the repository under your GitHub account.


  #### How to Clone

  To clone the Nine Lives repository:

  1. Log in (or sign up) to GitHub.
  2. Go to the repository for this project, [Kate McGuane / nine-lives](https://github.com/KateMcGuane/nine-lives).
  3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
  4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
  5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.


---


## Testing

Please see [TESTING.md](TESTING.md) for a comprehensive list of tests performed.


---


## Credits

  ### Markup

    The markup outline for this project was taken from the following README files:
    - [Kate McGuane / hobby](https://github.com/KateMcGuane/hobby).
    - [PedroCristo / portfolio_project_3](https://github.com/PedroCristo/portfolio_project_3/blob/main/README.md).


  ### Content

  - The terminal function & template for the deployable application was created by Code Instutute for their [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template).
  - The introduction for the README file was generated by Chat GPT.


  ### Code

  - [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg&t=5795s&ab_channel=freeCodeCamp.org) established the main logic for this project. I adapted the code to suit the needs of this project.
  - [Hangman](https://github.com/kying18/hangman) the code was adapted from this source. The words.py file was copied & pasted directly.


  ###  Media

  - [12 Beginner Python Projects - Coding Course](https://www.youtube.com/watch?v=8ext9G7xspg&t=5795s&ab_channel=freeCodeCamp.org) by freeCodeCamp.org was used as an educational aid, assited in laying out the logic, and coding process.


  ###  Acknowledgments

  - Thank you to my mentor, cohort leader & CI team for your support and understanding during this project.
  - To Sarah, thank you for all the 1:1 zoom calls.
  - To Mikhail, thank you for your continued support.