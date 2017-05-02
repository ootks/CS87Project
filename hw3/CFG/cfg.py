import re, random

#The pattern for a line of the CFG.
lhs_pattern = re.compile('(<.+>):(.*)')
rhs_prefix_pattern = re.compile('(.*?)(\||$)')
non_terminal_pattern = re.compile('<.*?>')

def get_rule(line):
    #Get the first match on the given line
    (lhs, rhs) = (re.findall(lhs_pattern, line))[0]
    rhs= [x[0] for x in re.findall(rhs_prefix_pattern, rhs) if x[0] != '']
    return (lhs, rhs)

def text_to_cfg(text):
    cfg = dict()
    for line in re.split("\n", text):
        try:
            (lhs, rhs) = get_rule(line)
            cfg[lhs] = rhs
        except IndexError:
            continue
    return cfg

def get_random_rhs(cfg, non_terminal):
    x = random.choice(cfg[non_terminal])
    return x#random.choice(cfg[non_terminal])

def cfg_to_string(cfg):
    string = "<start>"
    #Generate regex for anything on the rhs of a rule
    non_terminal_pattern = re.compile("|".join(["("+x+")" for x in cfg.keys()]))
    #Iteratively replace all of the non terminals with random entries from their 
    #rhs
    while bool(re.match(non_terminal_pattern, string)):
        string = re.sub(non_terminal_pattern,
                lambda x: get_random_rhs(cfg, x.group(0)), string)
    return string
