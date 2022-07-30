Python Script Template (Dynamo Node)

---

# --------------------------------------------
#Load the Python Standard Libraries
<br>
</br>
import sys
<br>
</br>
# --------------------------------------------
# Import Design Script
# Converts other languages into Python Syntax
# clr = Common Language Runtime
<br>
</br>
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
<br>
</br>
# --------------------------------------------
# This library containts Dynamo to Revit Elements
<br>
</br>
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
<br>
</br>
# --------------------------------------------
# This library translates Dynamo Objects into Revit Object
<br>
</br>
clr.ImportExtensions(Revit.GeometryConversion)
<br>
</br>
# --------------------------------------------
# Import RevitServices Transactions
# This library tells Dynamo to "stop-running" once the operation is completed
# e.g. "History"
<br>
</br>
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
<br>
</br>
# --------------------------------------------
# Import RevitAPI Library
<br>
</br>
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
<br>
</br>
# --------------------------------------------
<br>
</br>
# Constants
# Below suggest that to run the program only to the live (current) document 
<br>
</br>
doc = DocumentManager.Instance.CurrentDBDocument
<br>
</br>

# ----------------------------

# The inputs to this node will be stored as a list in the IN variables.
<br>
</br>
dataEnteringNode = IN
<br>
</br>
# # Variables here

# ## = UnwrapElement(IN[0]) This translates dynamo Object into Revit object
# line = UnwrapElement(IN[0]) e.g.
<br>
</br>
line = UnwrapElement(IN[0]) 

geoCurve = line.GeometryCurve

level = UnwrapElement(IN[1])
levelId = level.Id

<br>
</br>

# This is the runner (sample)
<br>
</br>
with Transaction(doc, "insert transaction name") as transaction:
	transaction.Start()
	# --------------------------------------------------
	# Function
	# Wall.Create(var1, var2, var3, var4) are defined on RevitAPI docs
	newWall = Wall.Create(doc, geoCurve, levelId, False)
	# --------------------------------------------------
	transaction.Commit()
<br>
</br>

# ----------------------------
# Assign your output to the OUT variable.
# Call the Function
# OUT = newWall (sample)
<br>
</br>
OUT = newWall
<br>
</br>
# ----------------------------
<br>
</br>


<br>
</br>
<br>
</br>
<p>
  <a href="https://www.linkedin.com/in/binoootuliao/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
  </a> &nbsp; 
  <a href="https://github.com/melbinoooo" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
  </a>
</p>

