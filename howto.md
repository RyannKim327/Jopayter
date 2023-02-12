### Jopayter
#### MPOP Reverse II (Ryann Kim Sesgundo)

---
### Download
Just run this code to your terminal (with installed git)
```Bash
git clone https://github.com/RyannKim327/Jopayter.git
```
---
### Usage
> Always run the program thru main.py as main of the program, you may also modify it [main.py](main.py). Here's the sample code in terminal where you need to execute to run the program.
```Bash
python main.py
```
Take a note that you've must have python3 installed program in your device, but you may use pydroid3 here.

---
### How to start
> First thing is you need to create a file named index.json, or in any file name, but must be in json file type. And then, initiate the class **Jopayter** to your program.
```Python
from jopayter import Jopayter

# index.json is the file where you can store the codes.
jopay = Jopayter("index.json")
```
---
### How to execute .execCode(array)
> This is to execute a code, this must be in an array form, so every key you stored in the index.json is already an array or set of strings.
```Python
from jopayter import Jopayter

# index.json is the file where you can store the codes.
jopay = Jopayter("index.json")
key = input("Enter your keycode: ")
jopay.execCode(jopay.key(key))

```
**OR**
```Python
jopay = Jopayter("index.json")
code = [
	"print(\"Hello World\")"
]
jopay.execCode(code)
```
---
### How to add a code .write()
> You just need to call the write function write in Jopayter
```
from jopayter import Jopayter

# index.json is the file where you can store the codes.
jopay = Jopayter("index.json")
jopay.write()
```
---
### How to update the code .editCode(key)
> This is to update the code, if ever that you type something or any error, just type cls to clear the entire line.
```Python
jopay = Jopayter("index.json")
print(jopay.getJSON().keys())
key = input("Enter the key to use: ")
jopay.editCode(key)
```
---
### How to check a code .check(key)
> This is just same as the write, but the function for this is to check the code, or to scan a code. This code returns in array string
```Python
jopay = Jopayter("index.json")
print(jopay.getJSON().keys())
key = input("Enter key: ")
for i in range(len(jopay.checkCode(key))):
	print(f"{i + 1}: {jopay.checkCode(key)[i]}")
```
---
### How to delete a code .deleteCode(key)
> This function is simply deleting a code thru it's key
```Python
jopay = Jopayter("index.json")
print(jopay.getJSON().keys())
key = input("Enter the key to use: ")
jopay.deleteCode(key)
```
---
### Note
> This project is just to enhance my knowledge and skills in programming, I didn't own the code, also the logic of the program. You may still use this, but don't sell the project as giving credits. I created this tutorial if ever that you want to study my code too.