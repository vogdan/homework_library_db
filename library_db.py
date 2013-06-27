import sys

def add_book_interact(db_file):
  print "Enter book... details"
  writer = raw_input("Writer name: ")
  title = raw_input("Book title: ")
  isbn = raw_input("ISBN code: ")
  
  print """You entered: 
	Writer name: {0}
	Book title: {1}
	ISBN code: {2}""".format(writer, title, isbn)
  is_valid = 0 
  while not is_valid:
    response = raw_input("Add book[Y/N]:")
    is_valid = 1
    if response == 'Y':
      print "Adding book..."
      add_book(db_file, writer, title, isbn)
      break
    if response == 'N':
      print "Adding canceled."
      break
    else:
      print "Option not valid."
      is_valid = 0

def add_book(db_file, writer, title, isbn):
  with open(db_file, 'r') as f:
    lines = f.readlines()
    with open(db_file, 'w') as f:	
      lines.append("{}\t{}\t{}\n".format(writer, title, isbn))
      for line in sorted(lines):
        f.write(line)	
	
def print_database(db_file):
  print "\nDatabase contents are:\n"
  with open(db_file, 'r') as f:
    for line in f:
      print "\t{}".format(line.strip())

      
def  main_menu_interact():
  print """
Available Options:
	1.Add book
	2.Print books
	Q.Quit"""
  return raw_input('Your Option: ')


try:
  db_file = sys.argv[1]
except:
  print "ERROR: No database file specified."
  exit(1) 
  
try:
  f = open(db_file, 'r')
  f.close()
except IOError:
  print "ERROR: Database file '{}' does not exist.".format(db_file)
  exit(1)
  
print "Data base file is '{}'\n.".format(db_file)

response = "obrrc"
while ( response != "Q"):
  response = main_menu_interact()
  if response == "1":
    add_book_interact(db_file)
  elif response == "2":
    print_database(db_file)
  else:
    print "Invalid option '{}'. Please try again.".format(response)
    
    
