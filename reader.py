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
        temp5 = f'{i}. {j} '
        temp6 = f'{i}. Alternativa {j}.'
        temp7 = f'Alternativa {j}.'
        testes.append(temp7)
        testes.append(temp6)
        testes.append(temp5)
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

    return all_text

    
a, b, c, d, e = 0, 0, 0, 0, 0
paths = glob.glob('pdf/2018/**/*.pdf')
total = 0
for path in paths:    
    text = pdf_to_text(path)
    #print(text)
    count = 0
    loc_a, loc_b, loc_c, loc_d, loc_e = 0, 0, 0, 0, 0
    for t in text:
        if t == 'a':
            a += 1
            loc_a += 1
        if t == 'b':
            b += 1
            loc_b += 1
        if t == 'c':
            c += 1
            loc_c += 1
        if t == 'd':
            d += 1
            loc_d += 1
        if t == 'e':
            e += 1
            loc_e += 1
        count += 1
    
    total += count
    print(f"Carregando: {path}")
    print(f"A: {loc_a} B: {loc_b} C: {loc_c} D: {loc_d} E: {loc_e}")
    print(f"Total de testes: {count}")
    print()

print(f"Resultado: A: {a}, B: {b}, C: {c}, D: {d}, E: {e}")
print(f"Total de Testes testados: {total}")