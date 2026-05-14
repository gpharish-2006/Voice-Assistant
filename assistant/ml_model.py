from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from assistant.intents import intents

x = []
y = []

for intent, patterns in intents.items():
    for pattern in patterns:
        x.append(pattern)
        y.append(intent)

vectorizer = CountVectorizer()

x_vec = vectorizer.fit_transform(x)

model = MultinomialNB()

model.fit(x_vec, y)


def predict_intent(text):

    vec = vectorizer.transform([text])

    prob = max(model.predict_proba(vec)[0])

    if prob < 0.40:
        return ""

    return model.predict(vec)[0]