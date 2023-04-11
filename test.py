import shop,json,os,pickle

global phoneList 
phoneList = []

def showMainMenu():
     print("\nEnter 1 to add a phone ")
     print("Enter 2 to search a phone ")
     print("Enter 3 to edit a phone ")
     print("Enter 4 to delete a phone")
     print("Enter 5 to see all phones")
     print("Enter 6 to exit \n")
     choice = int(input("Enter the choice "))
     if choice == 1:
        imei = input("Enter the imei ")
        if os.stat('sample.json').st_size> 0:  
         with open("sample.json") as outfile:
             data = json.loads(outfile.read())
             ##print(json.dumps(data))
             found = False
             for i in data:
              if str(imei) in i["imei"]:
                  found = True
             if found:
                  print("IMEI already in use")
             else:
                  brand = input("Enter the brand ")
                  model = input("Enter the model ")
                  phone = shop.shop(imei,brand,model)
                  json_object = json.dumps(phone.__dict__, indent=4)
                  with open("sample.json","a") as outfile:
                     outfile.write(json_object)
        else:
           brand = input("Enter the brand ")
           model = input("Enter the model ")
           phone = shop.shop(imei,brand,model)
           json_object = json.dumps(phone.__dict__, indent=4)
           with open("sample.json","w") as outfile:
            outfile.write(json_object)

          # with open('sample.txt', 'w') as user_file:
            #json.dump(phone.__dict__,user_file)
        showMainMenu()
     elif choice == 2:
         found = False
         if os.stat('sample.txt').st_size> 0: 
          sitem = input("Enter the imei ") 
          with open('sample.txt','r') as user_file:
             lines = user_file.readlines()
             for line in lines:
                if line.find(sitem) != -1:
                   print(line)
                   print()
                   found = True
             if found == False:
              print("Phone not available")
          showMainMenu()
         else:
           print("File empty")
           showMainMenu()
     elif choice == 3:
         found = False
         if os.stat('sample.txt').st_size> 0: 
          #sitem = input("Enter the imei ") 
          with open('sample.txt','r') as user_file:
             data = user_file.readlines()
          print(data)
          imei = "3"
          brand = "apple"
          model = " seven"
          data[1]= imei + " " + brand + " " + model + "\n"
          with open("sample.txt","w") as user_file:
             user_file.writelines(data)
          showMainMenu()
         else:
           print("File empty")
     elif choice == 4:
         pass
     elif choice == 5:
        if os.stat('sample.txt').st_size> 0:  
         with open("sample.txt") as file:
          for item in file:
           print(item)
         showMainMenu()
        else:
          print("File empty")
          showMainMenu()
     elif choice == 6:
         print("\nThank you")
     else:
         print("\nEnter a valid choice ")
         choice = int(input("Enter the choice "))
         showMainMenu()


showMainMenu()







