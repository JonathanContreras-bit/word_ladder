#!/bin/python3
from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny',
    'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey',
    'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]

    else:
        stack = []
        stack.append(start_word)
        q = deque([])
        q.append(stack)

        with open(dictionary_file) as df:
            dfl = [word.strip() for word in df.readlines()]

            while q:
                s = q.popleft()
                dflc = dfl.copy()

                for word in dflc:
                    if _adjacent(word, s[-1]):
                        if word == end_word:
                            s.append(word)
                            return s

                        t = s.copy()
                        t.append(word)
                        q.append(t)
                        dfl.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder:
        if len(ladder) > 1:
            for i in range(1, len(ladder)):
                if not (_adjacent(ladder[i - 1], ladder[i])):
                    return False
            return True

        elif len(ladder) == 1:
            return True

    else:
        return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) == len(word2):
        differ = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differ += 1

        return differ == 1

    else:
        return False
