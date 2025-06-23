# Choose Your Own Adventure: Plane Crash Island Quest (Less Info Text)

def adventure_game():
 while True:
  print("\n--- ISLAND QUEST: THE LOST TREASURE ---")
  print("You wake up on a beach after a plane crash. The wreckage is nearby. You remember rumors of pirate treasure on this island.")
  print("To your left is jungle, to your right is beach cliffs, behind you is the wreckage.")

  choice1 = input("\nWhere do you go? (jungle/beach/wreckage): ").strip().lower()

  if choice1 == "wreckage":
   print("\nYou search the wreckage and find a flare gun, a burned map, and water.")
   print("The map shows a skull in the jungle and an 'X' near the cliffs.")
   choice2 = input("Go to the jungle or the cliffs? (jungle/cliffs): ").strip().lower()
   if choice2 == "jungle":
    print("\nYou follow the map into the jungle and reach a fork: cave or waterfall.")
    choice3 = input("Which way? (cave/waterfall): ").strip().lower()
    if choice3 == "cave":
     print("\nYou find a locked chest with a puzzle: What has keys but can't open locks?")
     answer = input("Your answer: ").strip().lower()
     if "piano" in answer:
      print("\nThe chest opens! Inside is a compass and a note: 'Follow the compass.' You find a lagoon and signal a rescue boat. You win!")
      break
     else:
      print("\nWrong answer. Bats chase you out. Try again!")
    elif choice3 == "waterfall":
     print("\nAt the waterfall, a clue says: 'Treasure where the sun sets behind twin peaks.'")
     choice4 = input("Hike to the peaks or return to wreckage? (peaks/wreckage): ").strip().lower()
     if choice4 == "peaks":
      print("\nAt sunset, you find a hidden cave with treasure and a radio. You call for help and win!")
      break
     else:
      print("\nYou return to the wreckage. Try again!")
    else:
     print("\nYou get lost and end up back at the crash site.")
   elif choice2 == "cliffs":
    print("\nYou climb the cliffs and find a fire pit and an old journal.")
    choice3 = input("Wait for low tide to find a secret passage or explore the cliff top? (wait/explore): ").strip().lower()
    if choice3 == "wait":
     print("\nAt low tide, you find a cove with treasure. You signal a ship and win!")
     break
    else:
     print("\nYou slip and return to the beach. Try again!")
   else:
    print("\nYou wander and end up back at the crash site.")
  elif choice1 == "jungle":
   print("\nYou find a stone altar with a rusty key and a riddle: 'Where water falls, secrets call.'")
   choice2 = input("Go to the waterfall or keep moving? (waterfall/move): ").strip().lower()
   if choice2 == "waterfall":
    print("\nYou unlock a stone door behind the falls. Inside is treasure and a radio. You win!")
    break
   else:
    print("\nYou get lost as night falls. Try again!")
  elif choice1 == "beach":
   print("\nYou find a lifeboat and a message: 'Beware the cave of shadows.'")
   choice2 = input("Check the lifeboat or search for the cave? (lifeboat/cave): ").strip().lower()
   if choice2 == "lifeboat":
    print("\nThe lifeboat has a flare and a map to a cave.")
    choice3 = input("Repair the lifeboat or go to the cave? (repair/cave): ").strip().lower()
    if choice3 == "repair":
     print("\nYou repair the lifeboat, use the flare, and are rescued! You win!")
     break
    else:
     print("\nYou solve cave riddles, find treasure, and signal for help. You win!")
     break
   else:
    print("\nA storm catches you. Try again!")
  else:
   print("\nYou lose daylight. Try again!")

  retry = input("\nTry again? (yes/quit): ").strip().lower()
  if retry == "quit":
   print("Thanks for playing! Goodbye.")
   break

adventure_game()