import fitz  # this is pymupdf
import re
import os

def add_tags(tag,t1,at1,at2, word1,word2):   #Generating tags like <Paper id>,<Table id>,<Abstractive summarization>,<Extractive summarization>
	return "<%s><%s><%s>%s</%s><%s>%s</%s></%s><%s>" % (tag,t1,at1, word1,at1,at2,word2,at2,t1,tag)
#C:\Python\Python392
cwd=os.getcwd()
print(cwd)
os.chdir(r"C:\Users\LENOVO\OneDrive\Desktop\PDF files") #Changing the working directory to the directory where the pdf files are present
k=''
for d in range(0,999):
    with fitz.open("doc"+str(d)+".pdf") as doc:  #Opening all the pdf files named doc1.pdf,doc2.pdf,doc3.pdf etc
        text = ""
        for page in doc:
            text += page.get_text() #Extracting the text of each pdf file in the variable text


    for i in range(1,100):
        
    
    
        RSearch1=re.findall(r"([^.]*?Table "+str(i)+":"+"[^.]*\.)",text)  #Generating the abstractive summarization using regex
        RSearch2=re.findall(r"([^.]*?Table "+str(i)+" "+"[^.]*\.)",text)  #Generating the extractive summarization using regex
        if bool(RSearch1)==False & bool(RSearch2)==False : #If there is no abstractive or extractive summarization for a specific table, break the loop 
            break
        
        if(bool(RSearch1)==False):  #If there is no abstractive summarization for a table, append NULL to the RSearch1 list 
            RSearch1.append("NULL")
        
        if(bool(RSearch2)==False):  #If there is no extractive summarization for a table, append NULL to the RSearch2 list
            RSearch2.append("NULL")
                        
        print(add_tags('paper id:'+str(d),'Table id:'+str(i),"Abstractive Summary","Extractive Summary",RSearch1,RSearch2))
        k=k+str(add_tags('paper id:'+str(d),'Table id:'+str(i),"Abstractive Summary","Extractive Summary",RSearch1,RSearch2))
        k=k+'\n'
        k+='\n'
        
        
        print('\n')
with open("SummarizedText.txt", "w", encoding="utf-8") as f:  #Generate a file containing the abstractive and extractive summarization of all 999 papers
    f.write(k) 

f.close()
