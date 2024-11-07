# Python3 program to convert docx to pdf
# using docx2pdf module
 
# Import the convert method from the
# docx2pdf module
from docx2pdf import convert
 
# Converting docx specifying both the input 
# and output paths
convert("input\project_proposal_template.docx", "output\project_proposal_template.pdf")