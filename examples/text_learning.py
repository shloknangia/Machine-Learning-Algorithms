from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
string1 = "Hi this machine learning class is great great great class"
string2 = "Hello the class will start late"
string3 = "Hi this class will me most excellent"

email_list = [string1, string2,string3]

bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)

print bag_of_words
print vectorizer.vocabulary_.get("great")
# print vectorizer.vocabulary_.get_feature_names()


# using nltk package

# finding stop words
from nltk.corpus import stopwords
sw = stopwords.words("english")
print sw, len(sw)

# finding the root or stem of a word
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print stemmer.stem("responsiveness")
print stemmer.stem("looking")
print stemmer.stem("unresponsive")
print stemmer.stem("learning")
