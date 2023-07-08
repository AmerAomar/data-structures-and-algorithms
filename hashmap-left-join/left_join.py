def left_join(synonyms, antonyms):
    result = []
    for key in synonyms:
        if key in antonyms:
            result.append([key, synonyms[key], antonyms[key]])
        else:
            result.append([key, synonyms[key], None])
    return result


