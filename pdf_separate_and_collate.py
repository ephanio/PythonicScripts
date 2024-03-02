import pikepdf

def split_and_collate_pdf(input_file, output_folder):
    with pikepdf.open(input_file) as pdf:
        for i, page in enumerate(pdf.pages):
            if i % 2 == 0:
                new_pdf = pikepdf.new()
                new_pdf.pages.append(page)
                next_page = pdf.pages[i + 1] if i + 1 < len(pdf.pages) else None
                if next_page:
                    new_pdf.pages.append(next_page)
                    output_file = f"{output_folder}/Set_{i//2 + 1}.pdf"
                    new_pdf.save(output_file)

input_file = "input.pdf"  # Replace with the path to your input PDF
output_folder = "output"  # Replace with the path to your output folder
split_and_collate_pdf(input_file, output_folder)
