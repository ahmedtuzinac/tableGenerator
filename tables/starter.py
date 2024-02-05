import asyncio
from table import *

if __name__ == '__main__':
    import docx
    import time

    start_time = time.time()

    doc = docx.Document()
    table = doc.add_table(rows=3, cols=3)
    asyncio.run(apply_styles(document['styles'], table.rows[0]))
    doc.save(f'{file_path}/outputs/output.docx')

    end_time = time.time()
    print(f'Duration of executing script: {end_time - start_time} seconds.')
