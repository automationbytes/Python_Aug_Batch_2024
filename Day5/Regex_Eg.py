import  re

text = "Abc123xyz"

#a = re.findall("[0-9]",text) #extracting numbers
a = re.findall("\d",text)  #extracting numbers

print(a)
b = "".join(a)
print(b)

a = re.findall("[a-zA-Z]",text) #extracting chars
#a = re.findall("\D",text)  #extracting chars

print(a)
b = "".join(a)
print(b)

myphone = "Hello my phone number is 1234-456-7890"
match = re.search(r'(\d+-?){3}',myphone)
print(match)
print(match.group())

myphone = "Hello my phone number is 123-456-7890-7977"
match = re.search(r'(\d+-?){3}',myphone)
print(match)
print(match.group())

text = 'visit https://www.google.com/ or http://www.facebook.com/. And for more information https://www.amazon.com/'
urls = re.findall(r'https?://\S+',text)
print(urls)

urls = re.findall(r'https://\S+',text)
print(urls)

text = "Python is more user friendly. python is very easy to learn. python is used as General purpose language"
pattern = r'[Pp]ython'
updatedtext = re.sub(pattern,'Java',text)
print(updatedtext)

print(text.replace("Python", "Java"))

