from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

str1 = 'NLTK is a leading platform for building Python programs to work with human language data.'

stop_words = set(stopwords.words('english'))

tokens = word_tokenize(str1)
result = [i for i in tokens if not i in stop_words]
