import os.path as op

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup


with open('matematica_notas_ordinaria.html', 'rt') as fobj:
    html_doc = fobj.read()
soup = BeautifulSoup(html_doc, 'html.parser')

pages = [c for c in soup.body.children if c.name == 'div']
# From looking at the PDF
assert len(pages) == 307


def process_page(page):
    divs = [c for c in page.children if c.name == 'div']
    entries = [e.text for e in divs if 'cls_007' in e.attrs.get('class', [])]
    school, via = entries[0:2]
    s_entries = entries[2:]
    assert len(s_entries) % 3 == 0
    assert len(s_entries) >= 3
    students = []
    for i in range(0, len(s_entries), 3):
        id_no, name, mark = s_entries[i:i+3]
        mark = np.nan if mark == 'Aus' else float(mark.replace(',', '.'))
        students.append([school, via, id_no, name, mark])
    return students


students = sum([process_page(p) for p in pages], [])
df = pd.DataFrame(students, columns=['school', 'school_type', 'id', 'name', 'mark'])

# From: https://proyectoinventario.org/resultados-examen-ingreso-matematica-habana
#
# De los 7 735 estudiantes que debían tomar el examen, no se presentaron 775,
# para un total de 6 960 examinados que sí recibieron una nota.
assert len(df) == 7735
assert np.sum(df['mark'].isna()) == 775

# Later - this list of Vía de ingreso:
VIAS = ('Academias Deportivas de Alto Rendimiento',
        'Cadetes MININT',
        'Concurso',
        'Escuelas de Iniciación Deportiva',
        'Institutos Preuniversitarios',
        'ORDEN 18',
        'Servicio Militar Voluntario Femenino examina')

assert set(df['school_type'].unique()) == set(VIAS)

# Save to CSV without row labels
df.to_csv(op.join('processed', 'havana_math.csv'), index=False)
