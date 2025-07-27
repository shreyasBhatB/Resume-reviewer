from pypdf import PdfReader
import re


class Resume:
    def __init__(self,resume):
        reader = PdfReader(resume)
        self.text = ""
        urls = []
        # Extract text and look for annotations (links)
        for page in reader.pages:
            # Extract text
            self.text += page.extract_text() or ""

            # Extract annotations (if any)
            if "/Annots" in page:
                for annot in page["/Annots"]:
                    obj = annot.get_object()
                    if "/A" in obj and "/URI" in obj["/A"]:
                        urls.append(obj["/A"]["/URI"])

        # Also find URLs in plain text
        text_urls = re.findall(r'https?://\S+', self.text)
        # Combine both sets of URLs
        self.all_urls = list(set(urls + text_urls))

    def get_text(self):
        return self.text
    def get_urls(self):
        return  "\n".join(self.all_urls)

