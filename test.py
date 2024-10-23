import flask


app=flask.Flask("test")


def get_html(page_name):
    html_file=open(page_name+ ".html")
    content=html_file.read()
    html_file.close()
    return content


def get_notes():
   notepaddb=open("notepad.txt")
   content=notepaddb.read()
   notepaddb.close()
   notes=content.split("\n")
   notes.pop(len(notes)-1)
   return notes


##ROUTES###

@app.route("/")
def homepage():
    return get_html("index")

#main route

@app.route("/main")
def main():
   html_page=get_html("main")
   return html_page
   
#view all notes

@app.route("/viewallnotes")
def viewallnotes():
   html_page=get_html("viewallnotes")
   notes=get_notes()
   actual_values=""

   for note in notes:
        actual_values += "<p>" + note + "</p>"

    
   html_page=get_html("viewallnotes")
   return html_page.replace("$$notes$$" , actual_values)  
 


##add note route

@app.route("/addnote")
def addnote():
   html_page=get_html("addnote" )
   return html_page


#write notes and save them in the text file

@app.route("/insertnote")
def write():
    note=flask.request.args.get("note")
    file=open("notepad.txt","a")
    file.write(note + "\n")
    file.close()
    notes=get_notes()
    actual_values=""

    for note in notes:
        actual_values += "<p>" + note + "</p>"

    html_page=get_html("viewallnotes")
    return html_page.replace("$$notes$$" , actual_values)  
    
   



##searching for a note


@app.route("/search")
def searching():
   html_page=get_html("search" )
   return html_page



@app.route("/filternote")
def search():
   
    query=flask.request.args.get("note")
    notes=get_notes()
    result=""
    for note in notes:
        if note.lower().find(query.lower())!=-1:
            result+= "<p>" + note + "</p>"
 
    if result == "":
     result = "<p> No Result found </p>"

    html_page=get_html("search")
    return html_page.replace("$$notes$$" , result)  


