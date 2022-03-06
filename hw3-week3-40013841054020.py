#Short answer questions
print("\nMohammad Javad Esmkhani\t40013841054020\tHomeWork3-Week3\n")
#1 :
print("1 :\n")
#a :
i=3
j=5
k=7
if i<j :
	if j < k :
		i = j
	else :
		j = k
else :
	if j > k:
		j=i
	else :
		j = k 
print("\t#a :\n\t\t i = ", i, "j = " ,j , "k = ", k , "\n")

#b :
i=3
j=7
k=5
if i<j :
	if j < k :
		i = j
	else :
		j = k
else :
	if j > k:
		j=i
	else :
		j = k 
print("\t#b :\n\t\t i = ", i, "j = " ,j , "k = ", k , "\n")

#c :
i=5
j=3
k=7
if i<j :
	if j < k :
		i = j
	else :
		j = k
else :
	if j > k:
		j=i
	else :
		j = k 
print("\t#c :\n\t\t i = ", i, "j = " ,j , "k = ", k , "\n")
#d :
i=5
j=7
k=3
if i<j :
	if j < k :
		i = j
	else :
		j = k
else :
	if j > k:
		j=i
	else :
		j = k 
print("\t#d :\n\t\t i = ", i, "j = " ,j , "k = ", k , "\n")
#e :
i=7
j=3
k=5
if i<j :
	if j < k :
		i = j
	else :
		j = k
else :
	if j > k:
		j=i
	else :
		j = k 
print("\t#e :\n\t\t i = ", i, "j = " ,j , "k = ", k , "\n")
#f :
i=7
j=5
k=3
if i<j :
	if j < k :
		i = j
	else :
		j = k
else :
	if j > k:
		j=i
	else :
		j = k 
print("\t#f :\n\t\t i = ", i, "j = " ,j , "k = ", k , "\n")

#2:
print("2 :\n\t???\n")

#Programing Question
print("Programing Question\n")
#1 :
print("1 :\n")
x = int (input ("\tPlease Enter Your income : "))
if (x<=1000):
	tax = 0
elif (x>1000 and x<=2500):
	tax = x*10/100
elif (x>2500 and x<=4000):
	tax = x*15/100
elif (x>4000 and x<=6000):
	tax = x*20/100
else :
	tax = x*30/100
print("\tYour net income = " , x-tax , "\n" )

#2 :
print("2 :\n")
a = int(input("\tPlease Enter a : "))
b = int(input("\tPlease Enter b : "))
c = int(input("\tPlease Enter c : "))
if ( a+b>c and a+c>b and b+c>a) :
	print("\tRight triangle\n")
else :
	print("\tNot right\n")

#3 :
print("3 :\n\t????")
