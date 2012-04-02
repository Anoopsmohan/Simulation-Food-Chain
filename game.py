import random
import time
class Animals:
	def jump1(self):
		if self.dtn=="N" and self.lis[1]<9:
			self.lis[1]+=1
		elif self.dtn == 'S' and self.lis[1]>0:
			self.lis[1]-=1
		elif self.dtn == 'E' and self.lis[0]<9:
			self.lis[0]+=1
		elif self.dtn == 'W' and self.lis[0]>0:
			self.lis[0]-=1
		else:
			self.dtn=self.turn()
		print "%s%s%s"%(self.name,self.lis,self.dtn)

	def turn(self):
		if(self.dtn=='N'):
			dtn_list=['S','E','W']
		elif(self.dtn=='S'):
			dtn_list=['N','E','W']
		elif(self.dtn=='E'):
			dtn_list=['N','S','W']
		else:
			dtn_list=['N','S','E']
		return random.choice(dtn_list)
	def jump2(self):
		if self.dtn == 'N' and self.lis[1]<8:
			self.lis[1]+=2
		elif self.dtn == 'S' and self.lis[1]>1:
			self.lis[1]-=2
		elif self.dtn == 'E' and self.lis[0]<8:
			self.lis[0]+=2
		elif self.dtn=='W' and self.lis[0]>1:
			self.lis[0]-=2
		else:
			self.dtn=self.turn()
		print "%s%s%s"%(self.name,self.lis,self.dtn)

class Worm(Animals):
	def __init__(self,name,lis,dtn):
		self.name=name
		self.lis=lis
		self.dtn=dtn
		print "Worm Created:%s%s%s"%(self.name,self.lis,self.dtn)
	def jump(self):
		Animals.jump1(self)
		
class Ghopper(Animals):
	def __init__(self,name,lis,dtn):
		self.name=name
		self.lis=lis
		self.dtn=dtn
		print "Grass hopper created:%s%s%s"%(self.name,self.lis,self.dtn)
	def jump(self):
		Animals.jump2(self)
class Frog(Animals):
	def __init__(self,name,lis,dtn):
		self.name=name
		self.lis=lis
		self.dtn=dtn
		print "Frog created:%s%s%s"%(self.name,self.lis,self.dtn)
	def jump(self):
		Animals.jump2(self)
	
class Snake(Animals):
	def __init__(self,name,lis,dtn):
		self.name=name
		self.lis=lis
		self.dtn=dtn
		print "Snake created:%s%s%s"%(self.name,self.lis,self.dtn)
	def jump(self):
		Animals.jump1(self)
		
class Bfrog(Animals):
	def __init__(self,name,lis,dtn):
		self.name=name
		self.lis=lis
		self.dtn=dtn
		print "Bigfrog created:%s%s%s"%(self.name,self.lis,self.dtn)
	def jump(self):
		Animals.jump2(self)
def main():
	W1=Worm('W1',[1,1],'N')
	W2=Worm('W2',[4,5],'S')
	G1=Ghopper('G1',[2,1],'N')
	G2=Ghopper('G2',[3,5],'S')
	F1=Frog('F1',[2,3],'W')
	S1=Snake('S1',[5,2],'S')
	B1=Bfrog('B1',[5,3],'W')
	objlist=[W1,W2,G1,G2,F1,S1,B1]
	while(len(objlist)>0):
		fchain=[]
		time.sleep(1)
		print"------------------------------"
		for obj in objlist:
			obj.jump()
			fchain.extend([obj,obj.lis])
			for i in range(1,len(fchain)-2,2):
				if fchain[i] == obj.lis:
					class_name1=obj.__class__.__name__
					class_name2=fchain[i-1].__class__.__name__
					if class_name1=="Ghopper" and class_name2=="Worm":
						objlist.remove(fchain[i-1])
						print "Ghopper eats Worm"
						fchain.remove(fchain[i])
						fchain.remove(fchain[i])
					elif class_name1 == "Worm" and class_name2 == "Ghopper":
						objlist.remove(obj)
						print "Ghopper eats worm" 
						fchain.remove(obj.lis)
						fchain.remove(obj)
					elif class_name1 == "Frog" and class_name2 == "Ghopper":
						objlist.remove(fchain[i-1])
						print "Frog eats Ghopper"
						fchain.remove(fchain[i])
						fchain.remove(fchain[i])
					elif class_name1 == "Ghopper" and class_name2 == "Frog":
						objlist.remove(obj)
						print "Frog eats Ghopper"
						fchain.remove(obj.lis)
						fchain.remove(obj)
					elif class_name1 == "Snake" and (class_name2 == "Frog" or class_name2== "Ghopper"):
						objlist.remove(fchain[i-1])
						print "Snake eats %s"%(fchain[i-1].__class__.__name__)
						fchain.remove(fchain[i])
						fchain.remove(fchain[i])
					elif (class_name1 == "Frog" or class_name1== "Ghopper") and class_name2 == "Snake":
						objlist.remove(obj)
						print "Snake eats %s"%(obj.__class__.__name__)
						fchain.remove(obj.lis)
						fchain.remove(obj)
					elif class_name1 == "Bfrog" and (class_name2=="Snake" or class_name2 =="Frog"):
						objlist.remove(fchain[i-1])
						print "Bigfrog eats %s"%(fchain[i-1].__class__.__name__)
						fchain.remove(fchain[i])
						fchain.remove(fchain[i])
					elif (class_name1 == "Snake" or class_name1 == "Frog") and class_name2 == "Bfrog":
						objlist.remove(obj)
						print "Bigfrog eats %s"%(obj.__class__.__name__)
						fchain.remove(obj.lis)
						fchain.remove(obj)
	print "Game over"
main()
