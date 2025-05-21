import logging

def is_valid_string(string):
    if not isinstance(string,str):
        logging.info("Not a string")
        return False
    if any((not c.isalnum() for c in string)):
        logging.info("Not letters or numbers")
        return False
    return True

def is_valid_size(string: str):
    if len(string) < 5:
        return False
    if string.count(" ") > 10:
        return False
    return True


def main_function(string):
    if is_valid_string(string) and is_valid_size(string):
        return "Its good mate"
    
    

if __name__ == "__main__":
    valid_input = "this is a valid string"