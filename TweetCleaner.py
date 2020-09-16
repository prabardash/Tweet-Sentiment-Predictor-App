class TweetCleaner():
    def __init__(self):
        self.input = None
        self.stopwords = stopwords = [ "a", "about", "above", "after", "again",
        "against", "all", "am", "an", "and", "any", "are", "as", "at", "be",
        "because", "been", "before", "being", "below", "between", "both", "but",
        "by", "could", "did", "do", "does", "doing", "down", "during", "each",
        "few", "for", "from", "further", "had", "has", "have", "having", "he",
        "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him",
        "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've",
        "if", "in", "into", "is", "it", "it's", "its", "itself", "let's",
        "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only",
        "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own",
        "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than",
        "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there",
        "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
        "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've",
        "were", "what", "what's", "when", "when's", "where", "where's", "which",
        "while", "who", "who's", "whom", "why", "why's", "with", "would", "you",
        "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]


    def removeSpaces(self):
        stringval = str(self.input)
        while stringval[0] == " ":
            stringval = stringval[1:]
        while stringval[-1] == " ":
            stringval = stringval[:-1]
        return stringval

    def to_lowercase(self):
        text= (self.input).lower()
        return text

    def remove_url(self):
        words = self.input.split()
        for idx, val in enumerate(words):
            if (('https://' in val) | ('http://' in val)):
                words.remove(val)
        self.input = ' '.join(words)
        clean_text = self.removeSpaces()
        return clean_text

    def replace_ap(self):
        words = self.input.split()
        for idx, val in enumerate(words):
            if len(val)>1:
                val = val.replace('`','\'')
                words[idx] = val
        clean_text = ' '.join(words)
        return clean_text


    def remove_sw(self):
        line = self.input
        for word in self.stopwords:
            token = " "+word+" "
            line.replace('token', " ")
            line.replace("  "," ")
        return line


    def inference_clean(self, raw_tweet):
        self.input = raw_tweet
        self.input = self.removeSpaces()
        self.input = self.to_lowercase()
        self.input = self.remove_url()
        self.input = self.replace_ap()
        clean_text = self.remove_sw()

        return clean_text
