import os
from fpdf import FPDF
from PIL import Image

# Function to convert PNG images with specific index1 and index2 values to a PDF file
def images_to_pdf_filtered(image_folder, output_pdf, index1_values, index2_values):
    pdf = FPDF()
    #pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Add the first page from "Potential_Energy_Surfaces_page1.pdf"
    pdf.add_page()
    pdf.image("Potential_Energy_Surfaces_page1.png", x=10, y=10, w=190)

    for index1_value in index1_values:
        for index2_value in index2_values:
            # Construct the filename pattern based on index1 and index2
            image_file_pattern = f"{index1_value}_{index2_value}_"

            # Find PNG files matching the pattern in the image folder
            matching_files = [f for f in os.listdir(image_folder) if f.startswith(image_file_pattern)]

            # Process matching PNG files
            for image_file in matching_files:
                print(image_file)
                image_path = os.path.join(image_folder, image_file)
                if os.path.exists(image_path):
                    img = Image.open(image_path)

                    # Convert the image to RGB mode to ensure transparency is handled correctly
                    img = img.convert('RGB')

                    # Scale the image to fit the page, you can adjust the scale as needed
                    pdf.add_page()
                    img_width, img_height = img.size
                    max_width, max_height = pdf.w - 2 * pdf.l_margin, pdf.h - 2 * pdf.b_margin
                    scale = min(max_width / img_width, max_height / img_height)
                    img_width *= scale
                    img_height *= scale

                    pdf.image(image_path, x=pdf.l_margin, y=pdf.t_margin, w=img_width, h=img_height)

    pdf.output(output_pdf)

# Folder containing the PNG images
image_folder = './'

# Output PDF file name
output_pdf = '../../PES_Nan_et_al_QM_MM.pdf'

# Specify the index1 and index2 values you want to include in the PDF
index1_values = ['acet', 'aceh', 'acem', 'benz', 'dmds', 'dmpl', 'dms', 'imid', 'indo', 'mam1', 'mas', 'meet', 'meoh', 'mes', 'mesh', 'nma','phen', 'phet', 'adeb', 'guab', 'cytb', 'thyb', 'urab', 'imim', 'mguan','nc1']
index2_values = ["lit", "sod", "pot", "rub", "ces", "cla"]

# Convert PNG images with the specified index1 and index2 values to a PDF
images_to_pdf_filtered(image_folder, output_pdf, index1_values, index2_values)

