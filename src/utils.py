
def get_item_title(item: dict):
    return item["name"] if "name" in item else "No Title"

def parse_description_md(description: str):
    return "{}\n\n".format(description.replace("\.", ".").replace("  ", " "))

def print_postman_title(postman: dict):
    return "# {}\n\n".format(get_item_title(postman["info"]))

def print_test_detail(item: dict, level: list[str]):
    result = ""
    if "description" in item["request"]:
        result += "## {}\n\n".format(get_item_title(item))
        result += "> {}\n\n".format(" > ".join(level))
        result += "`{} {}`\n\n".format(item["request"]["method"], item["request"]["url"]["raw"])
        result += parse_description_md(item["request"]["description"])

        result += "***\n\n"
    
    return result

def read_item_to_md(items: list[dict], level: list[str] = [], result_md = ""):
    for item in items:
        if "item" in item:
            level_dup = level.copy()
            level_dup.append(get_item_title(item))
            result_md += read_item_to_md(item["item"], level_dup)
        elif "request" in item:
            result_md += print_test_detail(item, level)
    
    return result_md