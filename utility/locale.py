class Locale(object):
    __locales: {} = {}

    def __getitem__(self, item: str) -> str:
        return self.__locales[item.lower()]

    def __setitem__(self, key: str, value: any):
        self.__locales[key.lower()] = value


class EnglishLocale(Locale):
    def __init__(self):
        self['title'] = 'COMP102 Subject Materials'
        self['loading'] = 'Loading resources'
        self['home_header'] = 'Choose from these topics'
