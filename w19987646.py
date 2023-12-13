# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1985710 
# Date: 7 April 2023

validInputs = [0,20,40,60,80,100,120] #list with valid inputs to validate the user input
no_of_progress = 0  #variable to store the number of progress
no_of_module_trailer = 0 #variable to store the number of module trailer
no_of_retriever = 0 #variable to store the number of module retriever
no_of_exclude = 0 #variable to store the number of excludes

Progressions = [] #list to store the progressions of students

#function to validate the user input
def validation(input_credit):
    while True:
        # try-except to check whether the input is integer or not
        try:
            credit = int(input(input_credit)) #getting user input for credits
            if(credit not in validInputs): #checks is the user input credit is within the allowed range
                print("Out of range") #error message for not in the range of credits
                continue #should continuously ask for the user input if the input is not valid
            break #To break the while loop if the input is integer and within the range
        except:
            #action to perform if the input is not an integer
            print("Integer required") #error message
    
    return credit #returns the value from the function


while True: #to repeatly asking the credits if the user selects "y"
    while True: #to repeatly asking the credits while the input credits are not valid
        passCredit = validation("\nPlease enter your credits at pass: ") #vaiable for pass credits
        deferCredit =  validation("Please enter your credit at defer: ") #vaiable for defer credit
        failCredit = validation("Please enter your credit at fail: ") #vaiable for fail credit
        
        #checks whether the total number of credits are valid or not
        if (passCredit + deferCredit + failCredit != 120): #the total of pass, defer, and fail credits should be 120
            print("Total incorrect") #error message
            continue
        else:
            break #if the total is correct this should break the while loop        

    if(passCredit == 120) : #conditions for progress in academic year
        status = "Progress"
        no_of_progress += 1 #increment
    elif ((deferCredit == 20 or failCredit == 20) and passCredit == 100): #conditions for module trailer in academic year
        status = "Progress (module trailer)"
        no_of_module_trailer += 1 #increment
    elif (failCredit >= 80): #conditions for exclude in academic year
        status = "Exclude"
        no_of_exclude += 1 #increment
    else: #for module retriever
        status = "Do not progress - module retriever"
        no_of_retriever += 1 #increment

    print(status) #prints the progression outcome for given credits
    Progressions.append([status, passCredit, deferCredit, failCredit]) #append all of the entered credits to a list with students credits and progressions


    continue_quit = "" #initial assigment to run the while loop to run

    while(not (continue_quit.upper() == "Y" or continue_quit.upper() == "Q")): #validate the user input to continue or quit
        print("\nWould you like to enter another set of data?")
        continue_quit = input("Enter 'y' for yes or 'q' to quit and view results: ")

    # To break the while loop if the user selected to quit 
    if(continue_quit.upper() == "Q"): 
        break

#code to print the histogram
print("_"*100)
print("Histogram")
print(f"Progress {no_of_progress}\t: " + "*"*no_of_progress)
print(f"Trailer {no_of_module_trailer}\t: " + "*"*no_of_module_trailer)
print(f"Retriever {no_of_retriever}\t: " + "*"*no_of_retriever)
print(f"Excluded {no_of_exclude}\t: " + "*"*no_of_exclude)

print(f"\n{no_of_progress+no_of_module_trailer+no_of_retriever+no_of_exclude} outcomes in total.")
print("_"*100)


print("\n")

print("Part 2:")

#to print the student's progression details from the list
for i in range(len(Progressions)):
    print(f"{Progressions[i][0]} - {Progressions[i][1]}, {Progressions[i][2]}, {Progressions[i][3]}")

print("\n")
print("Part 3:")
# to store the student's progression details in a text file
file = open("Progressions.txt", "w") # open or create the file in write mode

#write the details in the file from stored list
for i in range(len(Progressions)):
    file.write(f"{Progressions[i][0]} - {Progressions[i][1]}, {Progressions[i][2]}, {Progressions[i][3]} \n")

file.close() #closes the file

file = open("Progressions.txt", "r") # open the file in read mode

print(file.read()) #read and prints the content of the file

file.close() #closes the file

