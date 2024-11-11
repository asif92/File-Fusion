# Import the convert method from the docx2pdf module
from docx2pdf import convert
 
# Converting docx present in the same folder
convert("project_proposal_template.docx")
 
# Converting docx specifying both the input and output paths
convert("input\project_proposal_template.docx", "output\project_proposal_template.pdf")

# Bulk Conversion (By specifying the input folder)
convert("input\")