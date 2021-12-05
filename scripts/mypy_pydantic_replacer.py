import os
import re


def replace(file_path):
    """
    Function that looks for a certain regex pattern and replaces it
    to have a valid mypy
    """
    found_expressions = []
    new_file = ''
    with open(file_path, "r+") as file:
        file_contents = file.read()
        # new_contents = re.sub(r "(\b\d+\.\d+)[a-z]", r "\1 seconds", file_contents) #substitutes 8.13 s
        new_contents = re.findall(r'Optional(.*?){', file_contents)
        # print(new_contents)
        for matchword in new_contents:
            if not 'Dict' in matchword:
                object_name = re.match(r'\[(.*?)\]', matchword)
                start = object_name.pos
                raw = object_name.group(0)[start+1:-1]
                x = {"key_name": raw, "match": object_name.group(0), "matchword": matchword}
                found_expressions.append(x)
        # find and replace
        for entry in found_expressions:
            raw = entry["key_name"]
            matchword = entry["matchword"]
            # found = re.findall(re.escape(matchword), file_contents)
            # print(found)
            if raw == "DependsOn":
                replace_with = f"{matchword}{raw}(**"
                print(replace_with)
                m = re.findall(re.escape(matchword), file_contents)
                print(len(m))
                generate = re.sub(re.escape(matchword), replace_with, file_contents)
                new_file += generate
        
        file.seek(0)
        file.truncate()
        file.write(generate)

#Optional[DependsOn] = {
#r'Optional(.*?){'

if __name__ == "__main__":
    base_path = os.path.join(os.path.dirname( __file__ ), '..', 'dagserializer', 'dbtschematas')
    target_file = os.path.join(base_path, 'testv1.py')
    replace(target_file)



# grep -o -P '(?<=Optional).*(?={)'