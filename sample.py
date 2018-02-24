from argparse import ArgumentParser
from generate import sample_text
from tensorflow import keras
import pickle
import os


def load_alphabet(model_dir, alphabet_name):
    with open(os.path.join(model_dir, alphabet_name)) as file:
        chars_indices, indices_chars = pickle.load(file)
    return chars_indices, indices_chars


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--length',
                        help='length of generated text',
                        type=int)
    parser.add_argument('--start_text',
                        help='first sequence to predict next',
                        type=str)
    parser.add_argument('--model_dir',
                        help='directory of model to load',
                        type=str,
                        default='checkpoints')
    parser.add_argument('--model_name',
                        help='name of model to load',
                        type=str)
    parser.add_argument('--seq_len',
                        help='length of sequence and start text',
                        type=int,
                        default=64)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    error = 'sequence length and lenght of start text are not matching'
    assert args.seq_len == len(args.start_text), error
    model = keras.models.load_model(args.model_name)
    chars_indices, indices_chars = load_alphabet(args.model_dir,
                                                 args.alphabet_name)
    sample_text(model, args.length, chars_indices, indices_chars,
                args.start_text)
