# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "herself", "her" ]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
# Function definitions

def redact(document):               #Master redaction function, scrubs proprietary_terms automatically, then checks if negative_words also needs scrubbed
    document = scrub(document, proprietary_terms)
    neg_count =0
    for word in negative_words:
        neg_count += document.count(word)
    if neg_count > 2:
        document = scrub(document, negative_words)
    return document


def scrub(document, list):            #Goes through list and splits document into words, eliminates words on naughty list and nearby words as well.
    for term in list:
        document_split = document.split("\n")   #
        for i in range(len(document_split)):
            document_split[i] = document_split[i].split(" ")
            for w in range(len(document_split[i])):
                if " " in term:                             #checks if term being filtered has multiple words and handles them.
                    term_split = term.split()
                    term_split_word_count = len(term_split)
                    if term_split == document_split[i][w:w+term_split_word_count]:
                        for m in range(term_split_word_count):
                            document_split[i][w-1+m] = blackout(document_split[i][w-1+m])
                            document_split[i][w+m] = blackout(document_split[i][w+m])
                            document_split[i][w+1+m] = blackout(document_split[i][w+1+m])
                elif document_split[i][w].lower() == term.lower():
                    document_split[i][w-1] = blackout(document_split[i][w-1])
                    document_split[i][w] = blackout(document_split[i][w])
                    document_split[i][w+1] = blackout(document_split[i][w+1])
            document_split[i] = " ".join(document_split[i])
        document = "\n".join(document_split)
    #print(document_split)
    return document

def blackout(word):
    blackout = "X"*len(word)
    return blackout

#Execution secion - remove commenting to run
#email_one_scrubbed = redact(email_one)
#print(email_one_scrubbed)

#email_two_scrubbed = redact(email_two)
#print(email_two_scrubbed)

#email_three_scrubbed = redact(email_three)
#print(email_three_scrubbed)

email_four_scrubbed = redact(email_four)
print(email_four_scrubbed)
