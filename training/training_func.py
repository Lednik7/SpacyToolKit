import spacy
import random
from tqdm import tqdm
from SpacyToolKit.metrics import evaluate
import os

def create_blank(TRAIN_DATA, lang="en"):
    """
    The function creates an empty Spacy model
    """
    nlp = spacy.blank(lang)
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner, last=True)

    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])
    return nlp, ner

def begin_training(nlp, TRAIN_DATA, VAL_DATA=False, n_iter=1, save_iter=False, output_dir="./iterations/", drop_out=0.5, progressbar=True, seed=42):
    random.seed(seed)

    if save_iter:
        print(f"\n\033[32mSave models to {output_dir}\033[0m")

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            print(f"\033[31m\nIterations: {itn + 1}\033[0m")
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in tqdm(TRAIN_DATA, disable=not progressbar):
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=drop_out,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)

            if VAL_DATA:
                scores = evaluate(nlp, VAL_DATA)
                print(f"\n{scores}")

            if save_iter:
                if "iterations" not in os.listdir():
                    os.mkdir(output_dir)
                nlp.to_disk(os.path.join(output_dir, f"model_{itn + 1}"))

            print(f"Losses: {losses}")
    print("\033[32mDone\033[0m")
    return nlp