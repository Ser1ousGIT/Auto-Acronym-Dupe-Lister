# Acronym Duplicate Finder

The last script I made was too strict and ended up missing lots of important acronyms.  
So, I used a rather simple algorithm which was not so.. accurate but it had all the acronyms in the output.  
It also made duplicates.  
So, here is a Duplicate finder and lister which shows exactly how many instances of an acronym is present and what are the full forms.  
After that I can basically work manually to remove the duplicates.  

---

# Technical Features:-

- Parses '.docx' files for acronym-expansion pairs  
- Detects duplicate acronyms  
- Lists:  
  - Number of times each acronym appears  
  - All unique expansions (if applicable)  
- Outputs results in a clean table format  

---

# Packages and requirements:-

- Python (obviously)  
- 'python-docx'  
- Have a single '.docx' from which you have to find the duplicates in the same directory as the script.  
  Name it 'acryonyms.docx' or change the file path in the '.py' file.  


# Commands:-

pip install python-docx
python file_name.py
