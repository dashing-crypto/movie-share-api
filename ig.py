import instaloader

#create an instance
test = instaloader.Instaloader()

#fetch the account details
acc = input('Enter the Account Username: ')

#download the data
test.download_profile(acc)   