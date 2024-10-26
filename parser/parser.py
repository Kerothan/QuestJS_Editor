from pyjsparser import parse

class Jsparser:
    def __init__(self):
        self.text = ""
    
    def jsparse(self, file):
        print(file)
        with open(file) as input:
            print(file)
            raw = input.read()
            print("Read success")
            self.text = parse(raw)
        try:
            with open(file) as input:
                print(file)
                raw = input.read()
                print("Read success")
                self.text = parse(raw)
        except:
            return "error"
        return self.text
