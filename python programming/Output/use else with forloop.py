f1=open("does.txt")
try:
    f = open("does2.txt")
except EOFError as e:
    print("print eof error aa  jay ga ", e)

except IOError as e:
    print("print  io error aa jay ga ", e)
else:
    print("it is not running")
finally:
    print("run this    any day....")
    f1.close()
print("important stuff")