import tree_sitter_python as tspython
from tree_sitter import Language, Parser


parser = Parser(Language(tspython.language()))
samples = {
    "function": b"def sapa(nama):\n    return nama\n",
    "if_else": b"if siap:\n    mulai()\nelse:\n    tunggu()\n",
    "class": b"class Greeter:\n    def halo(self):\n        return 'hai'\n",
    "missing_colon": b"def sapa(nama)\n    return nama\n",
}

for label, source in samples.items():
    tree = parser.parse(source)
    print(f"== {label} ==")
    print(tree.root_node)
    print(f"has_error: {tree.root_node.has_error}")

    if label == "function":
        print("children langsung function_definition:")
        for child in tree.root_node.named_children[0].children:
            status = "bernama" if child.is_named else "anonim"
            print(f"  {child.type}: {status}")
        parameters = tree.root_node.named_children[0].child_by_field_name("parameters")
        print("children parameters:")
        for child in parameters.children:
            status = "bernama" if child.is_named else "anonim"
            print(f"  {child.type}: {status}")
