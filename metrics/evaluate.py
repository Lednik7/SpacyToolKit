from SpacyToolKit import spans_to_words

def IoU(model, data):
    """
    Intersection by union is a scoring metric
    used to measure the accuracy of an object detector on a particular dataset,
    but let's use it for nlp!
    """
    scores = []
    for text, annotations in data:
        y_pred = set([(ent.text) for ent in model(text).ents])
        y_true = set(spans_to_words((text, annotations)))
        intersection = len(y_pred.intersection(y_true))
        union = len(y_pred.union(y_true))
        try:
          scores.append(intersection / union)
        except ZeroDivisionError:
           scores.append(0)
    return scores

def evaluate(model, examples):
    """
    Spacy standard metric
    """
    assert len(examples) != 1, "Length of test data must be more than 1"
    return model.evaluate(examples).scores['ents_per_type']