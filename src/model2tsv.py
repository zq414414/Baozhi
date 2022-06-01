#将训练好的model.wv文件转化成画图用tsv

#如果第一行是word总数信息，需要手动删除第一行
vecfile = "vector.wikia1.w2v" #文件名,后缀.txt

out1 = open("./"+vecfile+".vocab.tsv", 'w')
out2 = open("./"+vecfile+".vec.tsv", 'w')
file = open("./"+vecfile+".txt", 'r')
lines = file.readlines()
print(len(lines))
cntline = 0
for line in lines:
	vocab, vector = line.split(' ',1) #在第一个空格处分割
	out1.write(vocab+"\n")
	out2.write(vector.replace(' ', '\t'))
	cntline+=1
print(cntline,'\n')
file.close()
out1.close()
out2.close() 
