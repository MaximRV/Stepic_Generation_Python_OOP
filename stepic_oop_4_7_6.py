import re


class CaseHelper:
    @staticmethod
    def is_snake(line: str):
        if len(line.split()) > 1:
            return False
        elif len(line.split('_')) >= 1 and line.islower():
            return True
        else:
            return False

    @staticmethod
    def is_upper_camel(line:str)->bool:
        pattern = r'^([A-Z][a-z0-9]+)+$'
        return bool(re.match(pattern, line))

    @staticmethod
    def to_snake(UpperCamelLine: str)->str:
        result = re.sub(r'([А-ЯA-Z])', r' \1', UpperCamelLine).lower().split()
        return '_'.join(result)

    @staticmethod
    def to_upper_camel(SnakeCaseLine: str)->str:
        return "".join(word.capitalize() for word in SnakeCaseLine.split("_"))


test_number = 9

with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print()

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)
