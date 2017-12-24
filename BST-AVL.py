class theBinarySearchThree:

	def __init__(self,value):
		self.setValue(value)
		self.setParent(None) 
		self.setLeft(None)
		self.setRight(None)
		self.setBalance(0)
		self.setLevel(0)

	def getLeft(self):
		return self._left

	def setLeft(self,value):
		self._left = value		

	def getRight(self):
		return self._right
			
	def setRight(self,value):
		self._right = value
	
	def getParent(self):
		return self._parent

	def setParent(self,value):
		 self._parent = value	

	def setValue(self,value):
		self._v = int(value)	

	def getValue(self):
		return self._v

	def setLevel(self,level):
		self._level = int(level)	

	def getLevel(self):
		return self._level		

	def setBalance(self,value):
		self._balance = int(value)

	def getBalance(self):
		return self._balance

class operationsWithBST:

	def __init__(self):
		self._root = None

	def insert(self,value):
		if self._root != None:
			cur = theBinarySearchThree(value)
			new = self._root
			while 1:
				if cur.getValue() > new.getValue() and new.getRight() == None:
					new.setRight(cur)
					cur.setParent(new)
					break
				elif cur.getValue() > new.getValue() and new.getRight() != None:
					new = new.getRight()	

				if cur.getValue() < new.getValue() and new.getLeft() == None: 
					new.setLeft(cur)
					cur.setParent(new)		
					break
				elif cur.getValue() < new.getValue() and new.getLeft() != None:
					new = new.getLeft()		
		else:
			self._root = theBinarySearchThree(value)	
		
	def search(self,element):
			new = self._root
			element = int(element)
			while new != None:
				if element > new.getValue():
					new = new.getRight()
				elif element < new.getValue():
					new = new.getLeft()	 
				else:
					return new
					break		

	def delete(self,element):
			new = self._root
			new = self.search(element)
			tmp = new.getParent().getValue()
			if element == new.getValue() and element <= self._root.getValue():	
				self.DNFLS(new)
					
			elif element == new.getValue() and element >= self._root.getValue():
				self.DNFRS(new)
			return int(tmp)
				

	#Delete the node from the left subtree or root

	def DNFLS(self,new):		
		new = self._root
		while 1:
			if new.getRight() != None and new.getLeft() == None:
				new.setValue(new.getRight().getValue())
				if new.getRight().getLeft() != None:
					new.getRight().getLeft().setParent(new)
					new.setLeft(new.getRight().getLeft())

				if new.getRight().getRight() != None:	
					new.getRight().getRight().setParent(new)
					new.setRight(new.getRight().getRight())	
				else:
					new.setRight(None)	
				break

			elif new.getLeft() != None and new.getRight() == None:
				new.setValue(new.getLeft().getValue())	
				if new.getLeft().getRight() != None:	
					new.getLeft().getRight().setParent(new)
					new.setRight(new.getLeft().getRight())	

				if new.getLeft().getLeft() != None:
					new.getLeft().getLeft().setParent(new)
					new.setLeft(new.getLeft().getLeft())
				else:
					new.setLeft(None)	
				break

			elif new.getLeft() != None and new.getRight() != None:
				if new.getRight().getLeft() == None:
					new.setValue(new.getRight().getValue())
					if new.getRight().getRight() == None:
						new.setRight(None)
						break
					else:
						new.getRight().getRight().setParent(new)
						new.setRight(new.getRight().getRight())	
						break

				elif new.getRight().getLeft() != None:	
					cur = new.getRight().getLeft()
					while 1:
						if cur.getLeft() != None:
							cur = cur.getLeft()
						elif cur.getLeft() == None and cur.getRight() == None:
							new.setValue(cur.getValue())
							cur.getParent().setLeft(None)
							break	
						elif cur.getLeft() == None and cur.getRight() != None:	
							new.setValue(cur.getValue())
							cur.getRight().setParent(cur.getParent())
							cur.getParent().setLeft(cur.getRight())
							break	
							
			elif new.getLeft() == None and new.getRight() == None and new.getParent().getLeft() == new:
				new.getParent().setLeft(None)
				break

			elif new.getLeft() == None and new.getRight() == None and new.getParent().getRight() == new:	
				new.getParent().setRight(None)
				break

	#Delete the node from the right subthree or root
	def DNFRS(self,new):
		while 1:			
			if new.getRight() != None and new.getLeft() == None:
				new.setValue(new.getRight().getValue())
				if new.getRight().getLeft() != None:
					new.getRight().getLeft().setParent(new)
					new.setLeft(new.getRight().getLeft())	

				if new.getRight().getRight() != None:	
					new.getRight().getRight().setParent(new)
					new.setRight(new.getRight().getRight())	
				else:
					new.setRight(None)
				break

			elif new.getLeft() != None and new.getRight() == None:
				new.setValue(new.getLeft().getValue())	
				if new.getLeft().getRight() != None:	
					new.getLeft().getRight().setParent(new)
					new.setRight(new.getLeft().getRight())
						
				if new.getLeft().getLeft() != None:
					new.getLeft().getLeft().setParent(new)
					new.setLeft(new.getLeft().getLeft())
				else:
					new.setLeft(None)	
				break

			elif new.getLeft() != None and new.getRight() != None:
				if new.getRight().getLeft() == None:
					new.setValue(new.getRight().getValue())
					if new.getRight().getRight() == None:
						new.setRight(None)
						break
					else:
						new.getRight().getRight().setParent(new)
						new.setRight(new.getRight().getRight())	
						break

				elif new.getRight().getLeft() != None:	
					cur = new.getRight().getLeft()
					while 1:
						if cur.getLeft() != None:
							cur = cur.getLeft()
						elif cur.getLeft() == None and cur.getRight() == None:
							new.setValue(cur.getValue())
							cur.getParent().setLeft(None)
							break	
						elif cur.getLeft() == None and cur.getRight() != None:	
							new.setValue(cur.getValue())
							cur.getRight().setParent(cur.getParent())
							cur.getParent().setLeft(cur.getRight())
							break

			if new.getLeft() == None and new.getRight() == None and new.getParent().getLeft() == new:
				new.getParent().setLeft(None)
				break

			elif new.getLeft() == None and new.getRight() == None and new.getParent().getRight() == new:	
				new.getParent().setRight(None)
				break		

	def printInorder(self):	
		self.inorder(self._root)			

	def inorder(self,root):
		if root != None:
			self.inorder(root.getLeft())
			print("Value:",root.getValue())
			print("Level:",root.getLevel())
			print("Balance:",root.getBalance())
			self.inorder(root.getRight())

	def printPostorder(self):
		self.postorder(self._root)

	def postorder(self,root):
		if root != None:
			self.postorder(root.getLeft())
			self.postorder(root.getRight())	
			print(root.getValue())	

	def printPreorder(self):
		self.preorder(self._root)

	def preorder(self,root):
		if root != None:
			print(root.getValue())
			self.preorder(root.getLeft())
			self.preorder(root.getRight())	

	def balanceTheTreeAfterInsertion(self,value):
		cur = self.search(value)
		while cur != None:	
			if cur.getLeft() != None and cur.getRight() != None:
				cur.setBalance(cur.getRight().getLevel() - cur.getLeft().getLevel())
				cur.setLevel(max(cur.getRight().getLevel(),cur.getLeft().getLevel()) + 1)
			elif cur.getLeft() == None and cur.getRight() != None:	
				cur.setBalance(cur.getRight().getLevel() + 1)
				cur.setLevel(cur.getRight().getLevel() + 1)
			elif cur.getLeft() != None and cur.getRight() == None:	
				cur.setBalance((-1) - cur.getLeft().getLevel())
				cur.setLevel(cur.getLeft().getLevel() + 1)
			elif cur.getLeft() == None and cur.getRight() == None:	
				cur.setBalance(0)
				cur.setLevel(0)			

			if cur.getBalance() < -1:
				if cur.getLeft().getLeft() != None or cur.getLeft().getLeft() != None and cur.getLeft().getRight() != None:
					self.leftLeftRotation(cur)
				elif cur.getLeft().getLeft() == None and cur.getLeft().getRight() != None:
					self.leftRightRotation(cur)

			if cur.getBalance() > 1:
				if cur.getRight().getRight() != None or cur.getRight().getRight() != None and cur.getRight().getLeft() != None:
					self.rightRightRotation(cur)
				elif cur.getRight().getRight() == None and cur.getRight().getLeft() != None:
					self.rightLeftRotation(cur)	

			cur = cur.getParent()		

	def leftLeftRotation(self,node):
		cur = node
		if cur != self._root:
			cur.getLeft().setParent(cur.getParent())
			cur.setParent(cur.getLeft())
		else:
			cur.setParent(cur.getLeft())
			cur.getLeft().setParent(None)
			self._root = cur.getLeft()	
		if cur.getLeft().getRight() == None:	
			cur.getLeft().setRight(cur)
			cur.setLeft(None)
			cur.setLevel(0)
			cur.setBalance(0)	
		else:
			cur.getLeft().getRight().setParent(cur)	
			tmp = cur.getLeft().getRight()
			cur.getLeft().setRight(cur)
			cur.setLeft(tmp)
			cur.setLevel(1)
			cur.setBalance(1)
		if cur.getParent().getParent() != None:
			cur.getParent().getParent().setLeft(cur.getParent())		

	def leftRightRotation(self,node):
		cur = node
		cur.getLeft().setLevel(0)
		cur.getLeft().setBalance(0)
		cur.getLeft().getRight().setParent(cur)
		cur.getLeft().setParent(cur.getLeft().getRight())
		cur.getLeft().getRight().setLeft(cur.getLeft())
		cur.setLeft(cur.getLeft().getRight())
		self.leftLeftRotation(cur)

	def rightRightRotation(self,node):
		cur = node
		if cur != self._root:
			cur.getRight().setParent(cur.getParent())
			cur.setParent(cur.getRight())
		else:
			cur.setParent(cur.getRight())
			cur.getRight().setParent(None)
			self._root = cur.getRight()	
		if cur.getRight().getLeft() == None:	
			cur.getRight().setLeft(cur)
			cur.setRight(None)
			cur.setLevel(0)
			cur.setBalance(0)	
		else:
			cur.getRight().getLeft().setParent(cur)	
			tmp = cur.getRight().getLeft()
			cur.getRight().setLeft(cur)
			cur.setRight(tmp)
			cur.setLevel(1)
			cur.setBalance(1)		
		if cur.getParent().getParent() != None:
			cur.getParent().getParent().setRight(cur.getParent())
			
	def rightLeftRotation(self,node):
		cur = node
		cur.getRight().setLevel(0)
		cur.getRight().setBalance(0)
		cur.getRight().getLeft().setParent(cur)
		cur.getRight().setParent(cur.getRight().getLeft())
		cur.getRight().getLeft().setRight(cur.getRight())
		cur.setRight(cur.getRight().getLeft())
		self.rightRightRotation(cur)	
		
	def chechIfBalanced(self,node):
		if node != None:
			if node.getBalance() > 1 or node.getBalance() < -1:
				return "Epic fail"
			self.chechIfBalanced(node.getLeft())
			self.chechIfBalanced(node.getRight())	