from pypdf import PdfReader


def load_pdfs(folder_path):

    documents = []

    import os

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            reader = PdfReader(os.path.join(folder_path, file))

            for page_num, page in enumerate(reader.pages):

                text = page.extract_text()

                if text:
                    documents.append({
                        "text": text,
                        "metadata": {
                            "doc_name": file,
                            "page": page_num
                        }
                    })

    return documents