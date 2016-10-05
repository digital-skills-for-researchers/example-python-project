from nldl_parser import *


source_file = 'data/TEK0000.CSV'

parser = NLDLParser()
data = parser.parse_file(source_file)
