
# Open all emails
with open('email_one.txt') as email:
    email_one = email.read()
with open('email_two.txt') as email:
    email_two = email.read()
with open('email_three.txt') as email:
    email_three = email.read()
with open('email_four.txt') as email:
    email_four = email.read()


def censor_one(email, specificword='learning algorithms'):
    """censor a specific word or phrase"""
    censor = "#" * len(specificword)
    result = email.replace(specificword, censor)
    return result

# Email One


def censor_two(email, wordlist):
    """Censoring text as per the wordlist, supplied in a list"""
    wordlist = add_variations(wordlist)
    for term in wordlist:
        email = email.lower().replace(term, '▓'*len(term))
    return email

# Email Two


def censor_three(email, wordlist):
    """Censoring second and further occurence froom the banned list"""
    email_split = email.split()
    # print(email_split)
    banned_words = []
    i = 0
    clean_word = ''
    for words in email_split:
        clean_word = word_cleaning(words)
        if clean_word in wordlist:
            banned_words.append(clean_word)
            if banned_words.count(clean_word) > 1:
                censored_word = '▓'*len(words)
                email_split[i] = censored_word
        i += 1
    return ' '.join(email_split)

# Email Three


def censor_four(email, wordlist):
    print(wordlist)
    """Censoring all banned and near words"""
    eliminate_spaced_words(email, wordlist)
    email_split = email.split()
    email_censored = email_split
    # clean_word = ''
    email_lenght = len(email_split)
    for i in range(email_lenght):
        if word_cleaning(email_split[i]) in wordlist:
            email_censored[i] = censor_this(email_split[i])
            email_censored[i-1] = censor_this(email_split[i-1])
            email_censored[i+1] = censor_this(email_split[i+1])
    print(' '.join(email_censored))


def censor_four_2(email, wordlist):
    """A better implementation of the previous one"""
    eliminate_spaced_words(email, wordlist)
    email_split = email.split()
    new_banned_words_set = set()
    new_banned_words_set.update(wordlist)
    email_lenght = len(email_split)
    for i in range(email_lenght):
        if word_cleaning(email_split[i]) in wordlist:
            new_banned_words_set.add(word_cleaning(email_split[i-1]))
            new_banned_words_set.add(word_cleaning(email_split[i+1]))
    return censor_two(email, new_banned_words_set)


# ====== SERVICE FUNCTIONS ======

def censor_this(word):
    """Censorship implementation -- lenght of the word, concatinate punctuation. Requires word_cleaning"""
    clean_word, pre_punctuation, post_punctuation = word_cleaning(word, full=True)
    # return the censorship word as a lenght based
    return pre_punctuation + '▓'*len(clean_word) + post_punctuation


def word_cleaning(word, full=False):
    """Ridicolously ineffiecient way to get rid of punctuation """
    clean_word = word.lower()
    post_punctuation = ''
    pre_punctuation = ''
    if clean_word[0] == '(':
        clean_word = clean_word[1:]
        pre_punctuation = '('
    if clean_word[-1] in '!"#$%&()*+, -.:; <=  > ?@[]^_`{|}~':
        post_punctuation = clean_word[-1]
        clean_word = clean_word[:-1]
    if not full:
        return clean_word
    return clean_word, pre_punctuation, post_punctuation


def eliminate_spaced_words(email, wordlist):
    """Replaces space in to an underscore within the word"""
    for word in wordlist:
        word_no_space = word.replace(' ', '_')
        email.replace(word, word_no_space)
    return email


def add_variations(wordlist):
    """Add lower  to the list"""
    new_wordlist = []
    for word in wordlist:
        new_wordlist.append(word.lower())
    return new_wordlist


# censored_words = proprietary_terms + negative_words


proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her",
                     "herself"]
negative_words = ["she", "concerned", "behind", "danger", "dangerous",
                  "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage",
                  "damaging", "dismal", "distressed", "distressed",
                  "concerning", "horrible", "horribly", "questionable"]
total_linguistic_ban = negative_words + proprietary_terms

print(' === email ONE === \n\n')
print(censor_one(email_one, 'learning algorithms'))
print('\n === email TWO === \n\n')
print(censor_two(email_two, proprietary_terms))
print('\n === email THREE === \n\n')
print(censor_three(email_three, negative_words))
print('\n === email FOUR === \n\n')
print(censor_four(email_four, total_linguistic_ban))
print('\n === email FOUR v 2 === \n\n')
print(censor_four_2(email_four, total_linguistic_ban))
