import requests
import random


class Generator:

    # returns a random word from a online dictionary
    def get_from_dictionary(self):
        response = requests.get("http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain")
        words = response.content.splitlines()
        word = random.choice(words)
        return word.decode("utf-8")  # decodes to utf-8 because word was a byte-type value
