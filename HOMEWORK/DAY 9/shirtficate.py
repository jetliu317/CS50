
from fpdf import FPDF
class PDF():
    def __init__(self, name):
        self._pdf = FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        self._pdf.set_font('helvetica', 'B', 50)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.set_font("helvetica", "B", 30)
        self._pdf.set_text_color(255,255,255)
        # name = input('NAME: ')
        self._pdf.image('shirtificate.png', w=self._pdf.epw)
        self._pdf.text(x=47.5, y=140, txt = f'{name} TOOK CS50')
        self._pdf.output('shirtificate.pdf')
        
PDF('Jet')

# def main():
#     title()
#     add_name()
#     pdf.output('shirtificate.pdf')
    
# def title():
#     pdf.add_page()
#     pdf.set_font("helvetica", "B", 50)
#     pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')

# def add_name():
#     pdf.set_font("helvetica", "B", 30)
#     pdf.set_text_color(255,255,255)
#     name = input('NAME: ')
#     pdf.image('shirtificate.png', w=pdf.epw)
#     pdf.text(x=47.5, y=140, txt = f'{get_name} TOOK CS50')

# if __name__ == '__main__':
#     main()