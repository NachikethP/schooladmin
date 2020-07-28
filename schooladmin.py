import csv
def write_into_csv(csv_list):
    with open("schooladmin.csv","w",newline='') as file:
        writer = csv.writer(file)
        if file.tell()==0:
            writer.writerow(["name","age","DOB","class","house_color"])

        writer.writerow(csv_list)

if __name__=='__main__':
    cond=True
    stu_num=1
    while(cond):
                student_info=input("Enter the student info for student no. #{} in the following format (name age dob class house_color):".format(stu_num))
                student_info_list=student_info.split(' ')
                print("\nThe entered info is:-\nName:{}\nage:{}\nDOB:{}\nclass:{}\nhouse_color:{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
                choice_check=input("Is the entered info correct(yes/no):")
                if choice_check=="yes":
                    write_into_csv(student_info_list)

                    cond_check=input("enter yes/n0 if u want to continue:")
                    if cond_check=='yes':
                        cond=True
                        stu_num=stu_num+1
                    elif cond_check=='no':
                        cond=False

                elif choice_check=="no":
                    print("\nplease re-enter the information:")
