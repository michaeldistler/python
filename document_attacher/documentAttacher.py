import os
from path_locations import path_list
from settings import SCANNED_DOCUMENTS_PATH
### Unnecessary when using scanner ###
documents = {}




class DocumentPath(object):
    def __init__(self, company, path):
        self.company = company
        self.path = path

    def path_list(self):
        print "Document Type:"
        for path in path_list:
            print path[1]

    # Only needed for extra company additions to location list in the future
    def path_add(self):
        path_addition = self.company, self.path
        path_list.append(path_addition)



class Document(object):
    def __init__(self, name, path=SCANNED_DOCUMENTS_PATH):
        # Name Format = month number-month-year
        self.name = name
        # SCANNED_DOCUMENTS_PATH
        self.path = path

    # Dest needs to be queried before
    def move(self, dest):
        #if os.path.exists(dest):
        os.rename(self.path, dest)
        self.path = dest
        return self.path
        #else:
            #return "The destination path does not exist."

    ### Unnecessary when using scanner ###
    def save(self):
        documents["name"] = self.name
        documents["path"] = self.path


docName = "test"
docLoc = DocumentPath("Invoice","bin/local")
docLoc2 = DocumentPath("Post Offer", "user/bin/lib")
docLoc.path_add()
docLoc2.path_add()
print docLoc.path_list()
testPath = docLoc.path

doc = Document(name, testLocation)
doc_save = doc.save()

print "Document Information:"
for key, var in documents.iteritems():
    print key, var

doc2.move("5-january-2015")
doc2_save = doc2.save()

print doc2.name
