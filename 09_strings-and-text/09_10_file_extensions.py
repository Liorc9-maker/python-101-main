# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"
print("file_1 is pdf: ",file_1.endswith("pdf"))
print("file_2 is pdf: ",file_2.endswith("pdf"))
if file_3.endswith("pdf"):
    print ("file_3 ends with pdf")
else:
    print("file_3 does not end with pdf")
if file_4.endswith("pdf"):
    print("file_4 ends with pdf")
else:
    print("file_4 does not end with pdf")