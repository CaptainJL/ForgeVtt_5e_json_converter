# Open a file dialog to select a JSON file
import json
import pdfrw


from actor_template import pdf_to_json_mapping, pdf_decode_value









def load_dnd_character_template_pdf(json_data):
    # Open the PDF file
    pdf_file = pdfrw.PdfReader('DND_charactersheet_template.pdf')

    # Get the first page of the PDF
    page = pdf_file.pages[0]

    # Get the form fields on the page
    fields = page['/Annots']

    # Iterate over the fields and print their names and values
    for field in fields:
        print(field['/T'], field['/V'])

        value = pdf_decode_value(json_data, field['/T'])
        if value:
            field.update(pdfrw.PdfDict(V=pdfrw.PdfName(str(value))))
    # To edit a field, you can modify its value like this:
    # field['/V'] = 'New value'

    # To save the changes, you can write the updated PDF to a new file
    pdfrw.PdfWriter().write('updated_DND_charactersheet_template.pdf', pdf_file)


def load_dnd_character_json():
    # Open the JSON file
    with open('test_actor.json', 'r', encoding='utf-8') as file:
        # Load the JSON data
        json_data = json.load(file)

    # Print the data
    # print(json_data)
    return json_data



if __name__ == '__main__':
    json_data = load_dnd_character_json()
    load_dnd_character_template_pdf(json_data)




