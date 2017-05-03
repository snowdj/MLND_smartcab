from IPython.core.display import *
 
global MathJax 
MathJax = True
def MDPL(string): display(Math(string)) if MathJax else display(Latex(string))
 
def add(x,y): return x+y
 
def comp_str(listofstrings): return reduce(add,listofstrings)
 
class math_expr(object):
   '''''Math Expression object'''''
 
   def __init__(self,arg1):
      '''''init takes arg: list of atoms, each atom being a compilable chunck of LaTeX expression'''''
      self.listofatoms = arg1
 
   def show(self):
      '''''Displays the content of the expression in mathmode'''''
      MDPL(comp_str(self.listofatoms))
 
   def replace(self,pos,newstr):
      '''''Replaces an atom with another atom'''''
      MDPL(comp_str(self.colouratoms([pos])))
      self.listofatoms[pos] = newstr
      MDPL(comp_str(self.colouratoms([pos],True)))
 
   def merge(self,positions):
      '''''Merges atoms: the input is a list of positions. The new atom is placed at the position of the foremost of the positions'''''
      MDPL(comp_str(self.colouratoms(positions)))
      temp = [ self.listofatoms[i] for i in positions ]
      positions.sort()
      positions.reverse()
      for i in positions: del self.listofatoms[i]
      self.listofatoms.insert(positions[-1],comp_str(temp))
      MDPL(comp_str(self.colouratoms([positions[-1]],True)))
 
#    def split(self,pos,newatoms):
#       '''''Splits atoms: replaces an atom in place with multiple sub atoms'''''
#       MDPL(comp_str(self.colouratoms([pos])))
#       del self.listofatoms[pos]
#       templen = len(newatoms)
#       while len(newatoms) &gt; 0:
#          self.listofatoms.insert(pos,newatoms.pop())
#       MDPL(comp_str(self.colouratoms(range(pos, pos+templen),True)))
 
#    def cancel(self,positions):
#       '''''Cancels a bunch of terms: input a list of positions'''''
#       MDPL(comp_str(self.colouratoms(positions)))
#       positions.sort()
#       positions.reverse()
#       for i in positions: del self.listofatoms[i]
#       self.fullshow()
 
#    def move(self,posini,posfin):
#       '''''Move atom at posini to posfin, pushing all others back'''''
#       MDPL(comp_str(self.colouratoms([posini])))
#       temp = self.listofatoms.pop(posini)
#       self.listofatoms.insert(posfin if posfin &lt; posini else posfin-1, temp)
#       MDPL(comp_str(self.colouratoms([posfin if posfin &lt; posini else posfin-1],True)))
 
   # def colouratoms(self,positions,labelled=False):
   #    '''''Returns the list of atoms, but with selected terms coloured'''''
   #    temp = list(self.listofatoms)
   #    if labelled:
   #       self.labelatoms()
   #       temp = list(self.labeledatoms)
   #    for i in positions: temp[i] = &quot;\color{red}{&quot;+temp[i]+&quot;}&quot;
   #    return temp
 
#    def labelatoms(self):
#       '''''Label atoms by adding underbraces'''''
#       self.labeledatoms = [ &quot;\underbrace{&quot; + self.listofatoms[i] + &quot;}_{&quot; + str(i) + &quot;}&quot; for i in range(len(self.listofatoms)) ]
 
#    def fullshow(self):
#       '''''Shows the content whilst labeling positions'''''
#       self.labelatoms()
#       MDPL(comp_str(self.labeledatoms))