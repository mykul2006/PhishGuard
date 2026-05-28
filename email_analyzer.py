danger_words=[
"urgent",
"verify now",
"click immediately",
"suspended",
"login now",
"action required"
]

def analyze_email(text):

    found=[]

    text=text.lower()

    for word in danger_words:

        if word in text:
            found.append(word)

    return found