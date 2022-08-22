
import os


class Search:
    def __init__(self, file, search_keyword, search_path):
        self.file = file
        self.keyword = search_keyword
        self.path = search_path

    def searching(self):
        count = ''
        with open(os.path.join(self.path, self.file), 'r', encoding="utf-8", errors='ignore') as read_file:
            for index, item in enumerate(read_file, 1):
                if self.keyword in item:
                    print('\n\t\t', self.keyword, 'Exist! in the file', self.file, 'in line no. :', index)
                    count += ' True '
                else:
                    count += ' False '
            with open(os.path.join(os.getcwd(), 'result.txt'), 'a+') as result_file:
                result_file.write(count)
                result_file.write('\n')


flag = True
result = ''
extension = ('.txt', '.py', '.xml', '.js', '.xls', '.xlsx', '.docx')
while flag:
    with open(os.path.join(os.getcwd(), 'result.txt'), 'w+') as res:
        res.truncate(0)
    keyword = input('\nKeyword to Search* : ')
    path = input('\nEnter file name or Folder path if any else leave blank for current: ')
    path = path if path else os.getcwd()
    try:
        list_of_file = (file for file in os.listdir(path))
        for file in list_of_file:
            if file.endswith(extension):
                if file and keyword:
                    s = Search(file, keyword, path)
                    try:
                        os.path.isfile(file)
                        s.searching()
                    except Exception as e:
                        print(e)
                        print(file, 'Do not Exists!!')
                else:
                    print('\n\t\tKeyword is missing!!')
                    break
        with open(os.path.join(os.getcwd(), 'result.txt'), 'r') as file:
            result = file.read()
            if 'True' not in result:
                print('\n\t\tOPps!! No MatCh fOuND!!')

    except Exception as e:
        print(e)
        print('\nDirectory Does not Exist!!')
    finally:
        os.remove('result.txt')
        flag = input('\n\nContinue y/n :')
        if flag is 'n':
            flag = False
