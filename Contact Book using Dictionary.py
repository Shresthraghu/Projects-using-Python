# Write a program to create a Contact book in which you can add phone number and name , can easily view all contacts , , search by name and can delete a contact .


# Contact Book using Dictionary :-


# In this project users can :-

# 1.Add new contacts(name,phone)
# 2.View all contacts.
# 3.Search by name.
# 4.Delete a contact.



contacts={}

print("Contact Book")

while(True):
    print("\n1.Add Contact\n2.View All\n3.Search\n4.Delete\n5.Exit")
    
    choice=input("Enter your choice : ")
    if(choice=='1'):
        name=input("Name : ")
        phone=input("Phone : ")
        contacts[name]=phone
        print("Contact Saved")

    elif(choice=='2'):
        for name,phone in contacts.items():
            print(name,":",phone)

    elif(choice=='3'):
        name=input("Enter name you want to search : ")
        if name in contacts:
            print(name,"'s :",contacts[name])
        else:
            print("Contact not found.")

    elif(choice=='4'):
        name=input("Enter name you want to delete : ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not deleted successfully.")

    elif(choice=='5'):
        print("Thankyou for using contact book.")
        break

    else:
        print("Invalid Choice")
    

    
