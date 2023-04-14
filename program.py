import shop,json,os

def showMainMenu():
    try:
     print("\nEnter 1 to add a phone ")
     print("Enter 2 to search a phone ")
     print("Enter 3 to edit a phone ")
     print("Enter 4 to delete a phone")
     print("Enter 5 to see all phones")
     print("Enter 6 to exit \n")
     choice = int(input("Enter the choice "))
     if choice == 1:
        try:
         data = []
         imei = int(input("Enter the imei "))
         if os.stat('sample.json').st_size> 0:  
           with open("sample.json") as outfile:
               data = json.loads(outfile.read())
               found = False
               for i in data:
                if str(imei) in i["imei"]:
                    found = True
               if found:
                    print("\nIMEI already in use")
               else:
                    with open("sample.json") as outfile:
                     data = json.loads(outfile.read())
                    brand = input("Enter the brand ")
                    model = input("Enter the model ")
                    imei = str(imei)
                    phone = shop.shop(imei,brand,model)
                    data.append(phone.__dict__)
                    json_object = json.dumps(data, indent=4)
                    with open("sample.json","w") as outfile:
                       outfile.write(json_object)
                       print("Successfully added")
         else:
             brand = input("Enter the brand ")
             model = input("Enter the model ")
             imei = str(imei)
             phone = shop.shop(imei,brand,model)
             data.append(phone.__dict__)
             json_object = json.dumps(data, indent=4)
             with open("sample.json","w") as outfile:
              outfile.write(json_object)
              print("Successfully added")
        except:
           print("Enter a valid IMEI")
           showMainMenu()
        showMainMenu()
     elif choice == 2:
        try:
         TChoice = int(input("Enter 1 to choose by IMEI or 2 to choose by Brand "))
         found = False
         if os.stat('sample.json').st_size> 0: 
            if TChoice == 1:
             try:
              sitem = int(input("Enter the imei "))
              with open("sample.json") as outfile:
                data = json.loads(outfile.read())
                for i in data:
                 if str(sitem) in i["imei"]:
                    found = True
                    print("\nIMEI : ",end="")
                    print(i["imei"],end="")
                    print("\nBrand : ",end="")
                    print(i["brand"],end="")
                    print("\nModel : ",end="")
                    print(i["model"],end="")
                    print("\n")
              if found == False:
                 print("\nPhone not available")
             except:
                print("Enter a valid IMEI")
            elif TChoice == 2:
             sitem = input("Enter the brand ") 
             with open("sample.json") as outfile:
              data = json.loads(outfile.read())
              for i in data:
               if str(sitem) in i["brand"]:
                  found = True
                  print("\nIMEI : ",end="")
                  print(i["imei"],end="")
                  print("\nBrand : ",end="")
                  print(i["brand"],end="")
                  print("\nModel : ",end="")
                  print(i["model"],end="")
                  print("\n")
             if found == False:
                print("\nPhone not available")
            else:
               print("Enter a valid choice")
         else:
             print("File empty")
             showMainMenu()
        except:
            print("Enter a valid number")
        showMainMenu()
     elif choice == 3:
        try:
         found = False
         if os.stat('sample.json').st_size> 0: 
          sitem = int(input("Enter the imei ")) 
          with open("sample.json") as outfile:
             data = json.loads(outfile.read())
             for i in data:
              if str(sitem) in i["imei"]:
                  print("Current IMEI : ")
                  print(i["imei"])
                  print("\nCurrent Brand : ")
                  print(i["brand"])
                  print("\nCurrent Model : ")
                  print(i["model"])
                  found = True
                  brand = input("Enter new brand : ")
                  i["brand"] = brand
                  model = input("Enter new model : ")
                  i["model"] = model
                  json_object = json.dumps(data, indent=4)
                  with open("sample.json","w") as outfile:
                     outfile.write(json_object)
                     print("\nEditing success")
          if found == False:
              print("\nPhone not available")
         else:
           print("File empty")
           showMainMenu()
        except:
           print("Enter a valid IMEI")
        showMainMenu()
     elif choice == 4:
        try:
         found = False
         if os.stat('sample.json').st_size> 0: 
          sitem = int(input("Enter the imei ")) 
          with open("sample.json") as outfile:
             data = json.loads(outfile.read())
             for i in data:
              if str(sitem) in i["imei"]:
                  data.remove(i)
                  found = True
                  json_object = json.dumps(data, indent=4)
                  with open("sample.json","w") as outfile:
                     outfile.write(json_object)
                     print("\nDeleting success")
          if found == False:
              print("\nPhone not available")
         else:
           print("File empty")
           showMainMenu()
        except:
           print("Enter a valid IMEI")
        showMainMenu()
     elif choice == 5:
        if os.stat('sample.json').st_size> 0:  
         with open("sample.json") as file:
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
    except:
      print("Enter a valid choice")
      showMainMenu()


showMainMenu()







