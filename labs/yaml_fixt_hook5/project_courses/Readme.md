# Sign Up Page Algorithm
This describes testing the sign-up page for users on the courses site.<br>

Users: students, teachers<br>
Users register and confirm by email. <br>

**Students, teachers:**<br>
from 16 age to 100 age, from datetime.now()<br>

**Teacher**:<br>
teacher enters a code after verification by the administration on the popup<br>

## **Elements of the Sign-up page:**<br>
1. Title - Sign Up
2. Fields:
- firstname, required
- lastname, required
- password, required
- confirm password, required
- age, required
  - select in the calendar
  - or enter manually
3. Dropdown Select: student or teacher
   - if teacher:
     - display a popup, 
     - enter a code into the field, required
     - Send button
     - close popup
4. Sign up button

## Algorithm:<br>
1. Open the site main page<br>
2. Click the Sign Up button at the top<br>
3. Display the Sign Up page
4. Check the title 'Sign Up'<br>
5. Fill the fields:<br>
   - Enter firstname:<br>
       - only letters<br>
       - 20 characters<br>
       - if not letters:<br>
           - display error<br>
   - Enter lastname:<br>
       - only letters<br>
       - 20 characters<br>
       - if not letters:<br>
           - display error<br>
   - Enter password<br>
     - letters, numbers, symbols
     - 20 characters
6. Apply agreements checkbox
7. Click the "Sign Up" button below the form
8. Confirm by email
9. Open the main page on the site as a registered user
   - success popup about confirmation email
   - display at the top
     - user number
     - user firstname
     - user lastname
   - if a student:
      - display student page
   - if a teacher
      - display teacher page

**Selenium, Pytest**:
1. fixtures, hooks
2. skip - 
   - sending empty fields, 
   - selecting age 
3. fail - 
   - verification code


    