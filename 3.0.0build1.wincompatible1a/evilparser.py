import os
import platform
print("This version of EvilParser modified by islekcaganmert")
print("Contact from:")
print("http://hereus.pythonanywhere.com/user/islekcaganmert@gmail.com")
if platform.system() == "Windows":
    class crystal:
        def __init__(self):
            config = {

                    }
            self.config = config
        def remove(self, path, vexName):
            with open(path, "r") as f:
                lines = f.readlines()
            with open(path, "w") as f:
                inVex = False
                popno = 0
                for line in lines:
                    if "vex" in line and vexName in line:
                        inVex = True
                        lines.pop(popno)
                        popno += 1
                        continue
                    if inVex and line.startswith("vex "):
                        inVex = False
                    if inVex:
                        lines.pop(popno)
                    popno += 1
        def add(self,configfile,nameOfVar,typeofVar,valueOfVar):
            with open(configfile,"a+") as f:
                f.write("vex " + typeofVar + " " + nameOfVar + ";\n")
                if type(valueOfVar) == list:
                    for x in valueOfVar:
                        f.write("spec " + str(x) + ";\n")
                else:
                    f.write("spec " + str(valueOfVar) + ";\n")
        def syntax(self):
            createVar = "vex type name;\n"
            createVal = "spec value;\n"
            return [createVar, createVal]
        def get(self, path):
            self.config = {}
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
                    elif currentvartype in ["String","char*","str"]:
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
        def getOnlyValueOf(self, path, vex):
            nowconf = self.get(self, path)
            return nowconf[vex]
else:
    import os
    class crystal:
        def __init__(self):
            config = {

                    }
            self.config = config
        def remove(self, path, vexName):
            with open(path, "r") as f:
                lines = f.readlines()
            with open(path, "w") as f:
                inVex = False
                popno = 0
                for line in lines:
                    if "vex" in line and vexName in line:
                        inVex = True
                        lines.pop(popno)
                        popno += 1
                        continue
                    if inVex and line.startswith("vex "):
                        inVex = False
                    if inVex:
                        lines.pop(popno)
                    popno += 1
        def add(self,configfile,nameOfVar,typeofVar,valueOfVar):
            with open(configfile,"a+") as f:
                f.write("vex " + typeofVar + " " + nameOfVar + ";\n")
                if type(valueOfVar) == list:
                    for x in valueOfVar:
                        f.write("spec " + str(x) + ";\n")
                else:
                    f.write("spec " + str(valueOfVar) + ";\n")
        def syntax(self):
            createVar = "vex type name;\n"
            createVal = "spec value;\n"
            return [createVar, createVal]
        def get(self, path):
            self.config = {}
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
                    elif currentvartype in ["String","char*","str"]:
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
        def getOnlyValueOf(self, path, vex):
            nowconf = self.get(path)
            return nowconf[vex]