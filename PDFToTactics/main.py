from pdf2image import convert_from_path
import os,sys
pages = convert_from_path('D:/ChessProject/Flasking/test_docs/Mikhail_Tal_-_Life__Games_of_Mikhail_Tal_1997.pdf')
i=0
for page in pages:
    page.save(f'Tactics_0{i}.png', 'PNG')
    i+=1