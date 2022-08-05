import os

class crystal:
    def __init__(self):
        config = {

                }
        self.config = config
    def syntax(self);
        createVar = "vex type name;"
        createVal = "spec value;"
        return [createVar, createVal]
    def get(self, path):
        if not os.path.exists(path):
            raise Exception("Path does not exist")
        with open(path, "r") as f:
            lines = f.readlines()
        currentname = "NOTKNOWNYET"
        currentsituation = "NOTKNOWNYET"
        for line in lines:
            line = line.strip()
            if line.startswith("//") or line == "":
                continue
            if line.startswith("vex "):
                if not line.endswith(";"):
                    print("at " + path)
                    print("at " + line,end=" ")
                    print(lines.index(line + "\n"))
                    print("; excepted but not found")
                    raise Exception("; expected but not found")
                currentname = line.split(" ")[2].replace(";","")
                currentvartype = line.split(" ")[1]
                if currentvartype in ["int","integer"]:
                    currentsituation = "int"
                elif currentvartype in ["float","double"]:
                    currentsituation = "float"
                elif currentvartype in ["String","char*"]:
                    currentsituation = "string"
                elif currentvartype in ["bool","boolean"]:
                    currentsituation = "bool"
                elif currentvartype in ["char[]","char[]*","char*[]"]:
                    self.config[currentname] = []
                    currentsituation = "chararray"
                elif currentvartype in ["int[]","int[]*","int*[]"]:
                    self.config[currentname] = []
                    currentsituation = "intarray"
                elif currentvartype in ["float[]","float[]*","float*[]"]:
                    self.config[currentname] = []
                    currentsituation = "floatarray"
                elif currentvartype in ["bool[]","bool[]*","bool*[]"]:
                    self.config[currentname] = []
                    currentsituation = "boolarray"
                elif currentvartype in ["void","void(*)"]:
                    currentsituation = "void"
                else:
                    print("at " + path)
                    print("at " + line,end=" ")
                    print(lines.index(line + "\n"))
                    print("unknown type")
                    raise Exception("unknown type")
                continue
            if currentsituation == "NOTKNOWNYET":
                continue
            if not line.startswith("spec"):
                print("at " + path)
                print("at " + line,end=" ")
                print(lines.index(line + "\n"))
                print("type expected but not given")
            if currentsituation == "int":
                self.config[currentname] = int(line[5:].replace(";",""))
            elif currentsituation == "float":
                self.config[currentname] = float(line[5:].replace(";",""))
            elif currentsituation == "string":
                self.config[currentname] = line[5:].replace(";","")
            elif currentsituation == "bool":
                self.config[currentname] = bool(line[5:].replace(";",""))
            elif currentsituation == "chararray":
                self.config[currentname].append(line[5:].replace(";",""))
            elif currentsituation == "intarray":
                self.config[currentname].append(int(line[5:].replace(";","")))
            elif currentsituation == "floatarray":
                self.config[currentname].append(float(line[5:].replace(";","")))
            elif currentsituation == "boolarray":
                self.config[currentname].append(bool(line[5:].replace(";","")))
            elif currentsituation == "void":
                self.config[currentname] = None
            else:
                print("at " + path)
                print("at " + line,end=" ")
                print(lines.index(line + "\n"))
                print("unknown situation")
                raise Exception("unknown situation")
        return self.config
