from sklearn.feature_extraction.text import CountVectorizer

#to open txt file
document = open(r"C:\Users\Asus\Desktop\hi.txt","r")

#convert text file to string
def conv_to_string(x):
    list1=list(document)
    listofdoc=[]
    for x in list1:
        listofdoc.append(str(x))
    return listofdoc

document=conv_to_string(document)

#instantiate a vectoriser
element = CountVectorizer()

#fit to given document
element.fit(document)

#print(element.vocabulary_)

element = element.transform(document)

print(element.toarray())