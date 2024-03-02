import pikepdf

def split_and_separate_pdf(input_file, output_folder):
    with pikepdf.open(input_file) as pdf:
        for i, page in enumerate(pdf.pages):
            new_pdf = pikepdf.new()
            new_pdf.pages.append(page)
            if i % 2 == 0:
                set_number = i // 2 + 1
                output_file = f"{output_folder}/Set_{set_number}.pdf"
            else:
                output_file = f"{output_folder}/Set_{set_number}.pdf"
            new_pdf.save(output_file)

input_file = "input.pdf"  # Replace with the path to your input PDF
output_folder = "output"  # Replace with the path to your output folder
split_and_separate_pdf(input_file, output_folder)
