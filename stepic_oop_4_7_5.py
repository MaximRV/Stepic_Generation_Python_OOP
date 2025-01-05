from string import ascii_lowercase


class StrExtension:
    @classmethod
    def remove_vowels(cls, row):
        vowels = 'aeiouyAEIOUY'
        row = ''.join(elem for elem in row if elem not in vowels)
        return row

    @classmethod
    def leave_alpha(cls, row):
        return ''.join(char for char in row if char.isalpha())

    @classmethod
    def replace_all(cls, string: str, chars, char):
        for elem in chars:
            string = string.replace(elem, char)
        return string


text = '''I live in a house near the mountains. I have two brothers and one sister, and I was born last. My father teaches mathematics, and my mother is a nurse at a big hospital. My brothers are very smart and work hard in school. My sister is a nervous girl, but she is very kind. My grandmother also lives with us. She came from Italy when I was two years old. She has grown old, but she is still very strong. She cooks the best food!
My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains. My sister likes to cook with my grandmother. On the weekends we all play board games together. We laugh and always have a good time. I love my family very much.'''

print(StrExtension.remove_vowels(text))
print(StrExtension.leave_alpha(text))
print(StrExtension.replace_all(text, ascii_lowercase, ''))