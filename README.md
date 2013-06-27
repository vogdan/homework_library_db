homework_library_db
===================


Challenge:

Small school library has many borrowers and students are not very keen on keeping books in
correct order. This makes teachers’ job more difficult, hence they would want to keep library in
good order with printed lists. One main problem is adding new books to this list since school is
participating in national reading digest program and get couple new books per week. The school
has touchscreen that can read simple text file.

TASK:

The task is to create program that takes a file as the first command line argument.
E.g.
python my_library_db.py library.txt
The file contains rows, which each keep information of name of book, name of the writer and
ISBN
E.g.
Hobit
J.R.R.Tolkien
9788072037223
The Richard Burton Diaries Richard Burton 9780300180107

After reading the file, program shows user interface, where is option to 1) Add new book, 2)
Print current database content in ascending order by writer’s name or Q) Exit the program
With first option program should ask user the book’s name, writer’s name and book’s ISBN.
Then show the results to user and ask, does user want to update the database. If user selects
to update the database program should add the new book’s information into file given as
command line input argument. And otherwise return to main menu.
The Input file should be kept in alphabetical order based on writer’s name in all time. Also if user
choose to print current database content, program should print out to screen all information from
database, old and new information.

The visual content of file, user interface or printing out the database can be freely chosen,
but should be human readable format ( new line feeds and some kind of separators are
recommended.) :)
