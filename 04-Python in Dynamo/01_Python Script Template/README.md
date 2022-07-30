Python Script Template (Dynamo Node)

<br>
</br>

-	[1] Load the Python Standard Libraries
	- import sys

<br>
</br>

-	[2] Import Design Script
-	[x] Converts other languages into Python Syntax
-	[x] clr = Common Language Runtime
-	[x] ProtoGeometry
	- import clr
	- clr.AddReference('ProtoGeometry')
	- from Autodesk.DesignScript.Geometry import *

<br>
</br>

-	[3] This library contains Dynamo to Revit Elements
-	[x] RevitNodes
	- clr.AddReference("RevitNodes")
	- import Revit
	- clr.ImportExtensions(Revit.Elements)

<br>
</br>

-	[4] This library translates Dynamo Objects into Revit Objects
-	[x] Geometry Conversion
	- clr.ImportExtensions(Revit.GeometryConversion)

<br>
</br>

-	[5] Import RevitServices Transactions
-	[x] This library tells Dynamo to "stop-running" once the operation is completed
-	[x] e.g. "History"
	- clr.AddReference("RevitServices")
	- import RevitServices
	- from RevitServices.Persistence import DocumentManager
	- from RevitServices.Transactions import TransactionManager

<br>
</br>

-	[6] Import RevitAPI
-	[x] Autodesk Revit
	- import Autodesk
	- from Autodesk.Revit.DB import *
	- from Autodesk.Revit.DB.Architecture import *

<br>
</br>

-  	[ ]CONSTANTS VARIABLE
-	[A] Suggest to run the program only to the live (current) document
   - doc = DocumentManager.Instance.CurrentDBDocument

<br>
</br>

-	[ ]CONSTANT NODES
-	[A1] The inputs to this node will be stored as a list in the IN variables
   - dataEnteringNode = IN

<br>
</br>
<br>
</br>
<br>
</br>

-	[ ]VARIABLES-SAMPLE
-	[x] VARIABLE-SAMPLE = UnwrapElement(IN[0]) 
-	This translates dynamo Object into Revit object
   - line = UnwrapElement(IN[0]) 
   - geoCurve = line.GeometryCurve
   - level = UnwrapElement(IN[1])
   - levelId = level.Id

<br>
</br>

<br>
</br>

-	[ ]	PROGRAM-SAMPLE (RUNNER)
-	[x] "newWall" is an object
-	[x] Wall.Create(var1, var2, var3, var4) are defined on RevitAPI docs
   - with Transaction(doc, "insert transaction name") as transaction:
     - transaction.Start()
     - newWall = Wall.Create(doc, geoCurve, levelId, False)
     - transaction.Commit()

<br>
</br>
<br>
</br>

-	[ ] CONSTANT NODES
-	[A2] Assign your output to the OUT variable
   - OUT = newWall

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

