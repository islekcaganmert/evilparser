import os
class crystal:
    def __init__(self):
        self.config = {

                }
    def get(self, path):
        if not os.path.exists(path):
            raise Exception("Path does not exist")
        with open(path, "r") as f:
            lines = f.readlines()
        processingListObject = False
        cconfname = "NOTKNOWNYET0096"
        currentsituation = "NOTKNOWNYET0096"
        for line in lines:
            if line.startswith("|"):
                continue
            if line.startswith("::"):
                cconfname = line.split("::")[1].split(";")[0].strip()
                cconfvalue = line.split("::")[1].split(";")[1].strip()
                if cconfvalue == "int" or cconfvalue == "integer" or cconfvalue == "numobject":
                    currentsituation = "int"
                elif cconfvalue == "str" or cconfvalue == "char*" or cconfvalue == "string" or cconfvalue == "texobject":
                    currentsituation = "str"
                elif cconfvalue == "list" or cconfvalue == "array" or cconfvalue == "arraylist" or cconfvalue == "lisobject":
                    currentsituation = "list"
                    self.config[cconfname] = []
                elif cconfvalue == "integlist" or cconfvalue == "intlist" or cconfvalue == "numlist":
                    currentsituation = "intlist"
                    self.config[cconfname] = []
                elif cconfvalue == "bool" or cconfvalue == "boolean" or cconfvalue == "boolobject":
                    currentsituation = "bool"
                elif cconfvalue == "float" or cconfvalue == "double" or cconfvalue == "floatobject":
                    currentsituation = "float"
                else:
                    print("ERROR AT PARSING: UNKNOWN VAR TYPE: " + cconfvalue)
                    exit(1)
                continue
            if cconfname == "NOTKNOWNYET0096":
                continue
            if currentsituation == "int":
                self.config[cconfname] = int(line.strip())
            elif currentsituation == "str":
                self.config[cconfname] = line.strip()
            elif currentsituation == "list":
                self.config[cconfname].append(line.strip())
            elif currentsituation == "intlist":
                self.config[cconfname].append(int(line.strip()))
            elif currentsituation == "bool":
                self.config[cconfname] = bool(line.strip())
            elif currentsituation == "float":
                self.config[cconfname] = float(line.strip())
            else:
                print("ERROR AT PARSING: UNKNOWN VAR TYPE: " + currentsituation)
                exit(1)
        return self.config
