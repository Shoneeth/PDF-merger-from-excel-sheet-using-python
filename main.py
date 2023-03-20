import pandas as pd
from links import merge_pdf_from_drive_links

filedata= pd.read_excel("test.xlsx","Sheet1")
drive_links = filedata['links'].values.tolist()

#drive_links = ['https://drive.google.com/file/d/1lbHKNgLAMUoEtBgpZO94UPqVfDmJLmJP/view?usp=share_link',
#    'https://drive.google.com/file/d/1qvVhsEIVHGq0Jmqoilzzsm7zSEQn7xlj/view?usp=share_link',
#               'https://drive.google.com/file/d/1qvVhsEIVHGq0Jmqoilzzsm7zSEQn7xlj/view?usp=share_link']

merge_pdf_from_drive_links(drive_links, 'merged.pdf')
