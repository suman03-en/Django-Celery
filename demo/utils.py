from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_report_card(data):
    """
    Generates a PDF report card.
    data = {"name": "John Doe", "address": "123 Main St", "education": "B.Sc Computer Science"}
    """
    filename = f"{data['name']}_report_card.pdf"
    
    # Create the canvas
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # --- Header ---
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 50, "STUDENT REPORT CARD")
    
    # Draw a line under the header
    c.setStrokeColor(colors.black)
    c.line(50, height - 60, width - 50, height - 60)

    # --- Content ---
    c.setFont("Helvetica", 12)
    
    # Define vertical starting point
    y_position = height - 100
    
    # Writing the dictionary data
    c.drawString(70, y_position, f"Name: {data.get('name')}")
    y_position -= 30
    
    c.drawString(70, y_position, f"Address: {data.get('address')}")
    y_position -= 30
    
    c.drawString(70, y_position, f"Education: {data.get('education')}")

    # --- Footer ---
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(70, 50, "This is a computer-generated document.")

    # Save the PDF
    c.showPage()
    c.save()
    
    return filename