from datetime import datetime

def main():
    
    task = []

    while True:
        try:
            print("1.Add Task\n2.Showtask\n3.Exit")
            choose_task = int(input("Choose one option: "))

        except ValueError:
            print("You have to type 1, 2 or 3.")
            continue

        try:
            if choose_task == 1:
                i = 1
                n_task = int(input("How many task(s) did you want today: "))
                

                while i <= n_task:
                    add_task = input(f"{i}. ").capitalize()
                    date_added = datetime.now().strftime("%Y_%m-%d")

                    task.append((add_task, date_added))
                    i+=1
                    
                    
                
                print("Your task(s) added successfully.")
                

            elif choose_task == 2:
                if not task:
                    print("There is no task.")
                
                else:
                    for index, (added_task, date_added) in enumerate(task, start =1):
                        print(f"{index}. {added_task} (Added task on: {date_added})")

                
                

            elif choose_task == 3:
                print("Have a good one! See you again...")
            
                break

            else:
                print("please choose the available options.")

        except ValueError:
            print("Please input how many task(s) did you want to add?")


main()
        

        