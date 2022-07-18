import requests

'''
Function of getting Organization details using api
'''
def getUserName(name):
    URL = "https://api.github.com/users/"+name
    r = requests.get(url=URL)
    data = r.json()
    # print(data)

    # Show data in proper format
    type_user = data['type']    #Type of Account
    print(f"\n{type_user} Account")
    user_name = data['name']    #Name of User
    print(f"Name of user : {user_name}")
    loc = data['location']  #Location of User
    print(f"Location : {loc}")
    com_name = data['company']  #Company Name of User
    print(f"Company : {com_name}")
    pub_repo = data['public_repos'] #Number of Public Repository of User
    print(f"Public repositories : {pub_repo}")
    followers_list = data['followers']  #Number of Followers of User
    print(f"Followers : {followers_list}")
    following_list = data['following']  #Number of Following of User
    print(f"Following : {following_list}")
    acct_created = data['created_at']   #Date of Account Created
    print(f"Account created on : {acct_created}")


'''
Function of getting Organization details using api
'''
def getOrganizationName(name):
    URL = "https://api.github.com/users/"+name
    r = requests.get(url=URL)
    data = r.json()
    # print(data)

    # Show data in proper format
    type_user = data['type']    #Type of Account
    print(f"\n{type_user} Account") 
    user_name = data['name']    #Name of Organization
    print(f"Name of organization : {user_name}")
    loc = data['location']  #Location of Organization
    print(f"Location : {loc}")
    email_detail = data['email']    #Email of Organization
    print(f"Company : {email_detail}")
    pub_repo = data['public_repos'] #Number of Public Repository
    print(f"Public repositories : {pub_repo}")
    followers_list = data['followers']  #Number of Followers of Organization
    print(f"Followers : {followers_list}")
    following_list = data['following']  #Number of Following of Organization
    print(f"Following : {following_list}")
    acct_created = data['created_at']   #Date of Account Created
    print(f"Account created on : {acct_created}")


'''
Function to compare to User Account
'''
def compareUserAccount(us1, us2):
    #Details of User 1
    URL1 = "https://api.github.com/users/"+us1
    r1 = requests.get(url=URL1)
    data_us1 = r1.json()
    # print(f"\nData of 1st User {data_us1}")

    pub_repo_us1 = data_us1['public_repos'] #Number of Public Repository of User
    # print(f"Public repositories : {pub_repo_us1}")
    followers_list_us1 = data_us1['followers']  #Number of Followers of User
    # print(f"Followers : {followers_list_us1}")
    following_list_us1 = data_us1['following']  #Number of Following of User
    # print(f"Following : {following_list_us1}")
    
    # Details of User 2
    URL2 = "https://api.github.com/users/"+us2
    r2 = requests.get(url=URL2)
    data_us2 = r2.json()
    # print(f"\nData of 2nd User{data_us2}")

    pub_repo_us2 = data_us2['public_repos'] #Number of Public Repository of User
    # print(f"Public repositories : {pub_repo_us2}")
    followers_list_us2 = data_us2['followers']  #Number of Followers of User
    # print(f"Followers : {followers_list_us2}")
    following_list_us2 = data_us2['following']  #Number of Following of User
    # print(f"Following : {following_list_us2}")

    #Compare the details
    # print(f"Public Repository of of {us1} is greater than {us2} and count is {pub_repo_us1}" if pub_repo_us1 > pub_repo_us2 else f"Public Repository of of {us2} is greater than {us1} and count is {pub_repo_us2}")
    #Compare Public Repository
    if (pub_repo_us1 > pub_repo_us2):
        print(f"Most Public Repository : {us1} with {pub_repo_us1} repositories")
    elif (pub_repo_us1 == pub_repo_us2):
        print(f"Public Repository of {us1} and {us2} are same and count is {pub_repo_us1}")
    else:
        print(f"Most Public Repository : {us2} with {pub_repo_us2} repositories")
    
    #Compare Followers
    if (followers_list_us1 > followers_list_us2):
        print(f"Most Followers : {us1} with {followers_list_us1} followers")
    elif(followers_list_us1 == followers_list_us2):
        print(f"Followers of {us1} and {us2} are same and count is {pub_repo_us1}")
    else:
        print(f"Most Followers : {us2} with {followers_list_us2} followers")
    
    #Compare Following
    if (following_list_us1 > following_list_us2):
        print(f"Most Following : {us1} with {following_list_us1} following")
    elif (following_list_us1 == following_list_us2):
        print(f"Following of {us1} and {us2} are same and count is {pub_repo_us1}")
    else:
        print(f"Most Following : {us2} with {following_list_us2} following")



# Menu
print("WELCOME TO GitHub PROJECT")
while True:
    print("\nMAIN MENU")
    print("1. Get User GitHub details")
    print("2. Get organization GitHub details")
    print("3. Compare two user GitHub details")
    print("4. Exit")
    choice1 = int(input("Enter your choice: "))
    if choice1 == 1:
        getUserName(input("Enter your GitHub username: "))
    elif choice1 == 2:
        getOrganizationName(input("Enter your Organization GitHub username: "))
    elif choice1 == 3:
        compareUserAccount(input("Enter 1st User GitHub username: "), input("Enter 2nd User GitHub username: "))
    elif choice1 == 4:
        exit()
    else:
        print("Incorrect Choice")

