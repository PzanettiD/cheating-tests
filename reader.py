from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, resolve1
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from io import BytesIO
import glob

testes = []
for i in range(1, 31):
    for j in ['a', 'b', 'c', 'd', 'e']:
        temp = f'{i}. {j}'
        temp2 = f'0{i}. {j} '
        temp3 = f'0{i}. {j}'
        temp4 = f'0{i}. Alternativa {j}.'
        testes.append(temp4)
        testes.append(temp3)
        testes.append(temp2)
        testes.append(temp)
def pdf_to_text(path):
    codec = 'utf-8'
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams()
    device = TextConverter(manager, retstr, codec=codec, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    
    for page in PDFPage.get_pages(filepath, 0, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue().decode()
    all_text = text.splitlines()
    
    anth = set()
    for l in testes:
        if l in all_text:
            anth.add(l)

    raw = list(anth)
    raw_list = []
    for b in raw:
        a = b.split(' ')
        for n in a:
            c = n.split('.')
            for x in c:
                d = x.split('Alternativa')
                for v in d:
                    raw_list.append(v)
    result = list(filter(None, raw_list))
    del result[::2]
    filepath.close()
    device.close()
    retstr.close()

    return result

    

a = 0
b = 0
c = 0
d = 0
e = 0
paths = glob.glob('pdf/**/**/*.pdf')
for path in paths:    
    text = pdf_to_text(path)
    for t in text:
        if t == 'a':
            a += 1
        if t == 'b':
            b += 1
        if t == 'c':
            c += 1
        if t == 'd':
            d += 1
        if t == 'e':
            e += 1
    print(f"Loading: {path}")
    print(f"A: {a}", end=' ')
    print(f"B: {b}", end=' ')
    print(f"C: {c}", end=' ')
    print(f"D: {d}", end=' ')
    print(f"E: {e}")
    print()