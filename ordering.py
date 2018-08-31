print(" Press 1 for Pizza")
print(" Press 2 for Soft Drinks")
print(" Press 3 for Sides")

ch=int(raw_input())
if(ch==1):
  print("You have selected the pizza")
  print("Press 1 for Veg")
  print("Press 2 for Non Veg")
  chp=int(raw_input())
  if(chp==1):
    print("You have selected the Veg")
    print("Press 1 for corn")
    print("Press 2 for onion")
    chv=int(raw_input())
    if(chv==1):
      print("You have selected the corn Pizza")
      print("Cost for corn Pizza=165")
    elif(chp==2):
      print("You have selected the onion Pizza")
      print("Cost for onion Pizza=190")
    else:
      print("no choice")
    
  elif(chp==2):
    print("You have selected the non Veg")
    print("Press 1 for cheese")
    print("Press 2 for chicken")
    chnv=int(raw_input())
    if(chnv==1):
      print("You have selected the Cheese Pizza")
      print("Cost for cheese Pizza=165")
    elif(chnv==2):
      print("You have selected the Cheese Pizza")
      print("Cost for chicken Pizza=200")
    else:
      print("no choice")
  else:
      print("no choice")
  
    









elif(ch==2):
  print("You have selected the drink")
  print("Press 1 for hot drink")
  print("Press 2 for softdrink")
  chd=int(raw_input())
  if(chd==1):
    print("You have selected the hot drink")
    print("Press 1 for tea")
    print("Press 2 for coffee")
    chd=int(raw_input())
    if(chd==1):
      print("You have selected the tea")
      print("Cost for tea=65")
    elif(chd==2):
      print("You have selected the coffee")
      print("Cost for coffee=90")
    else:
      print("no choice")
  
  elif(chd==2):
      print("You have selected the soft drink")
      print("Press 1 for coke")
      print("Press 2 for fanta")
      chds=int(raw_input())
      if(chds==1):
        print("You have selected the Coke")
        print("Cost for coke=160")
      elif(chds==2):
        print("You have selected the fanta")
        print("Cost for fanta=220")
      else:
        print("no choice")
  
  else:
      print("no choice")
    







elif(ch==3):
  print("You have selected the sides")
  print("Press 1 for fries")
  print("Press 2 for tikka")
  chs=int(raw_input())
  if(chs==1):
    print("You have selected the fries")
    print("Press 1 for frenchfries")
    print("Press 2 for smiley")
    chs=int(raw_input())
    if(chs==1):
      print("You have selected the frenchfries")
      print("Cost for fries=165")
    elif(chs==2):
      print("You have selected the smiley")
      print("Cost for smiley=190")
    else:
      print("no choice")
  
  elif(chs==2):
      print("You have selected the tikka")
      print("Press 1 for chicken tikka")
      print("Press 2 for mutton tikka")
      chnv=int(raw_input())
      if(cht==1):
        print("You have selected the Chicken tikka")
        print("Cost for chicken=260")
      elif(cht==2):
        print("You have selected the mutton tikka")
        print("Cost for mutton tikka=320")
      else:
        print("no choice")
  





else:
  print("no choice")
