import pandas as pd


def postprocess(out):
    # out - huggingface pipeline object output
    curr_b = []
    curr_g = []
    for x in out:
        if x["entity_group"] == "BRAND":
            curr_b.append(x["word"])
        else:
            curr_g.append(x["word"])
    curr_b = list(map(lambda x: ','.join(x), curr_b))
    curr_g = list(map(lambda x: ','.join(x), curr_g))
    return {
        "brands:": curr_b,
        "goods:": curr_g
    }
    