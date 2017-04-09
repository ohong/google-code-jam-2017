# @author: Oscar Hong, Duke University

# main program
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
input = open("R1_PB_Input.txt", "r")
output = open("R1_PB_Output.txt","w")

t = int(input.readline())

for i in range(1, t + 1):
  n = int(input.readline())
  lastTidyNum = getLastTidyNum(n)
  output.write("Case #{}: {}\n".format(i, lastTidyNum))

output.close()