import builtins
TAB="   "



def pprint(data):
    """
    Pretty-print data
    """
    builtins.print(prettify(data))

def prettify(data):
    """
    Prettify data
    """

    def prettifylist():
        return ",\n".join((TAB+prettify(i).replace("\n","\n"+TAB) for i in data))

    if isinstance(data,builtins.list):
        return "[\n"+prettifylist()+"\n]"

    if isinstance(data,builtins.tuple):
        return "(\n"+prettifylist()+"\n)"
    if isinstance(data,builtins.set):
        return "{\n"+prettifylist()+"\n}"
    if isinstance(data,builtins.dict):
        return "{\n"+",\n".join(
            TAB+prettify(key).replace("\n","\n"+TAB)\
                +": "+prettify(value).replace("\n","\n"+TAB)
                for key,value in data.items())+"\n}"
    data=repr(data)
    if "\n" in data:
        return "(\n"+TAB+(data.replace("\n","\n"+TAB))+"\n)"
    return data
def tofile(data,file="rrprettier_data.py"):
    """
    Prettify data and then save it
    """
    with open(file,"w") as f:
        f.write("d="+prettify(data))

#print([1,2,3,4,5,[1,2]])

#print(printer({1:2,3:4,50:[1,2]}))
#saveinfile({1:2,3:4,5:6,"abbbbccccc":[1,2,3]})
#dprint({1:2,3:4,5:6})q
#print(".".join((str(a) for a in range(6)))