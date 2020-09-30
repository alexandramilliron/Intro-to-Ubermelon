log_file = open("um-server-01.txt")
#opening a file so that the contents can be read by Python

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

#creating a function called sales_report that takes an open file as an argument
#the "for" loop loops over each line in the file (each line is a string)
#rstrip (string method) removes trailing characters at the end of a string
#day slices the string from the first character to the third character 
#the "if" statement evaluates the day of the week - if it evaluates to True, it prints the line

sales_reports(log_file)
