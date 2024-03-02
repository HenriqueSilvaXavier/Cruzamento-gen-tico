filhos=[]
a1=input("Digite o primeiro genótipo: ")
a2=input("Digite o segundo genótipo: ")
if "aA" in a1:
	a1=a1.replace("aA", "Aa")
if "aA" in a2:
	a2=a2.replace("aA", "Aa")
print("Cruzamento: {} x {}".format(a1, a2))
filhos.append("{}{}".format(a1[0], a2[0]))
filhos.append("{}{}".format(a1[0], a2[1]))
filhos.append("{}{}".format(a1[1], a2[0]))
filhos.append("{}{}".format(a1[1], a2[1]))
if filhos.count("AA")>0:
	c=filhos.count("AA")
	p=(c/len(filhos))*100
	if (filhos.count("Aa")+filhos.count("aA"))>0 or filhos.count("aa")>0:
		print("{:.0f}% de AA".format(p), end=", ")
	else:
		print("{:.0f}% de AA".format(p), end=". ")
if filhos.count("Aa")>0 or filhos.count("aA")>0:
	c=filhos.count("Aa")+filhos.count("aA")
	p=(c/len(filhos))*100
	if filhos.count("aa")>0:
		print("{:.0f}% de Aa".format(p), end=", ")
	else:
		print("{:.0f}% de Aa".format(p), end=".")
if filhos.count("aa")>0:
	c=filhos.count("aa")
	p=(c/len(filhos))*100
	print("{:.0f}% de aa".format(p), end=".")