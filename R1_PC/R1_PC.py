# @author: Oscar Hong, Duke University

# helper functions

def chooseStall(stallState):
    for i in xrange(1,len(stallState)-1):
        if stallState[i] == 'O':
            # calculate left distance (LS)
            LS = 0
            counter = 0
            for j in xrange(i, 0, -1):
                if stallState[i] == 'X':
                    LS = counter
                    break
                else:
                    counter += 1

            # calculate right distance (RS)
            RS = 0
            counter = 0
            for j in xrange(i,len(stallState)-1):
                if stallState[i] == 'X':
                    RS = counter
                    break
                else:
                    counter += 1


# main program
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
input = open("R1_PC_Input.txt", "r")
output = open("R1_PC_Output.txt","w")

t = int(input.readline())

for i in range(1, t + 1):
  n, k = [int(s) for s in input.readline().split(" ")] # N stalls; K ppl

  # init stall state
  stallState = []
  for i in xrange(n+2):
      if i == 0 or i == n+1:
          stallState.append('X')
      else:
          stallState.append('O')

  for i in xrange(k):
      chooseStall(stallState)

  # output.write("Case #{}: {} {}".format(i, lastMax, lastMin))

output.close()