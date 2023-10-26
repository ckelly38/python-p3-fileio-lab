def write_file(file_name, file_content):
    myfile = None;
    try:
        myfile = open(str(file_name) + ".txt", mode="w", encoding="utf-8");
        myfile.write(file_content);
        myfile.close();
    finally:
        if (myfile == None): pass;
        else: myfile.close();

def append_file(file_name, append_content):
    myfile = None;
    try:
        myfile = open(str(file_name) + ".txt", mode="a", encoding="utf-8");
        myfile.write(append_content);
        myfile.close();
    finally:
        if (myfile == None): pass;
        else: myfile.close();

def read_file(file_name):
    myfile = None;
    mycontent = None;
    try:
        myfile = open(str(file_name) + ".txt", mode="r", encoding="utf-8");
        mycontent = myfile.read();
        myfile.close();
    finally:
        if (myfile == None): pass;
        else: myfile.close();
    return mycontent;
