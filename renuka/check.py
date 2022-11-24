import  jpype     
import  asposecells     
jpype.startJVM() 
from asposecells.api import Workbook
workbook = Workbook("check.xlsx")
workbook.Save("Output.png")
jpype.shutdownJVM()