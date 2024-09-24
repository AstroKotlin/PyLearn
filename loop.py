import color
import os

SYSTEM = color.LIGHT_CYAN

text = str(input(SYSTEM + "Text for loop: "));
loop = int(input(SYSTEM + "Number of repetitions: "));
# ---
os.system("clear")
output = ""

for num in range(loop):
	output += text

text2 = text.replace("\n","").replace("/","_").replace("\\n","").replace("\\","")

path = "output/loop_"+text2+".txt"
file = open(path, "w")
file.write(output)
file.close()

print("Repeated text \""+text+"\" with the number of times: "+str(loop))
