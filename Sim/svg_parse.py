import xml.etree.ElementTree as ET
from svglib import svglib
from reportlab.graphics import renderPDF
import fitz  # PyMuPDF
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def highlight_organs(svg_file, organs_to_highlight, output_svg, output_png):
    # Parse the SVG file
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Define the namespace
    ns = {'svg': 'http://www.w3.org/2000/svg', 'inkscape': 'http://www.inkscape.org/namespaces/inkscape'}

    # Print available organ IDs for debugging
    print("Available organ IDs in the SVG:")
    for group in root.findall(".//{*}g", ns):
        id_attr = group.attrib.get('id', 'No ID')
        label_attr = group.attrib.get('inkscape:label', 'No Label')
        print(f"ID: {id_attr}, Label: {label_attr}")

    # Keep track of found organs
    found_organs = []

    # Iterate through each organ ID to highlight
    for organ_id in organs_to_highlight:
        organ_group = root.find(f".//{{*}}g[@id='{organ_id}']", ns)
        if organ_group is not None:
            organ_group.set('style', 'fill:red;stroke:none')  # Highlight color
            found_organs.append(organ_id)
        else:
            print(f"Organ ID '{organ_id}' not found.")

    # If no organs were found, print a warning
    if not found_organs:
        print("No organs were highlighted. Check the organ IDs.")

    # Write the modified SVG to a new file
    tree.write(output_svg)

    # Convert the SVG to PNG using svglib and fitz
    convert_svg_to_png(output_svg, output_png)

def convert_svg_to_png(svg_file, output_png):
    # Convert SVG to PDF in memory
    drawing = svglib.svg2rlg(svg_file)
    pdf = renderPDF.drawToString(drawing)

    # Open PDF with fitz (PyMuPDF) to convert to PNG
    doc = fitz.open(stream=pdf, filetype='pdf')
    pix = doc.load_page(0).get_pixmap(alpha=True, dpi=300)
    pix.save(output_png)

if __name__ == "__main__":
    # Specify your SVG file, organs to highlight, and the output file names
    svg_file = '/Users/vspendyala/Downloads/homo_sapiens.male.svg'
    organs_to_highlight = ["UBERON_0000955", "UBERON_0000948", "UBERON_0002048"]  # Add more organ IDs as needed
    output_svg = 'highlighted_human_body.svg'
    output_png = 'highlighted_human_body.png'

    highlight_organs(svg_file, organs_to_highlight, output_svg, output_png)
    plt.imshow(mpimg.imread(output_png))
    plt.show()
    print(f"Highlighted organs saved to {output_svg} and {output_png}")
