class CupParser:

    import os
    import unicodedata

    title = ''
    groups = dict()

    def present(self,fileName:str):
        if(len(fileName)) == 0:
            print("no file name in CupParser")
            return
        with open(fileName, 'r',encoding='utf-8') as cupSource:
            # separate description from matchs detail
            content = cupSource.read().split(sep='\n\n\n\n')
            # print(len(content))
            # print(content[0])
            description = content[0].split(sep='\n\n\n')
            # print(len(description))
            # print(description[1])
            self.title = description[0].split('#')[0].strip()[2:]
            self.groups  = dict(
                map(lambda x : list(
                    map(lambda y : y.strip(),
                        x.split('|'))),
                            description[1].splitlines()))
# TODO Clean groups composition
            # print(self.groups )
            # self.groups 