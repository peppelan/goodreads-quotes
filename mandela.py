import goodreads_quotes

quotes=[]

for page in range(1,12):
   quotes.extend(goodreads_quotes.Goodreads.get_mandela_quotes(page))

for quote in quotes:
   print(quote['quote'])
