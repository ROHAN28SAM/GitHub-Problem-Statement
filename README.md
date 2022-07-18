# GitHub Profile display 
Functionality 1

User GitHub Profile
   - Taking User input for <username> and then used in GET api
   - Function will fetch from https://api.github.com/users/<username> GET Request's Response. 
   - Where <username> is input taken from the User
   
Organization GitHub Profile
   - Taking User input for <username> and then used in GET api
   - Function will fetch from https://api.github.com/users/<username> GET Request's Response. 
   - Where <orgs> input taken from the user
   
Compare Two User GitHub Profile
   - Function will take two <username> from user and will call the https://api.github.com/users/<username>
   - Will collect detailes from response body and will compare the details
   - It will display
      - User with More Follower
      - User with More Following
      - User with More Public Repository
