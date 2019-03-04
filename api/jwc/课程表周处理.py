import re
c='<input id="jsids" name="jsids" type="checkbox" value="31E24556DF70492AB22A553586832C39"/>'

t=re.search('ue=.\w+',c).group()
print(t)