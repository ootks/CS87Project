# Using `textualtoy.py`
Note: This file needs tweaking to prevent total punctuation loss, which causes words such as "well" and "we'll" to be interpreted as the same word.


### The `get_poem()` function
`get_poem(user_corpus, minimum_length=20, maximum_rank=3)`

This is the main function in the file, for which every other function is a helper. All information in this README is a duplicate of comments in the file, edited for clarity.

* Input: A text made out of sentences, in the form of a list of strings.
* Output: A 3-line short story / poem.
* Techniques: Cosine Similarity, TF-IDF.

### Note on constants:

* `minimum_length`: This constant indicates the minimum number of sentences as input. If input is below this minimum, we pad with random Simon & Garfunkel lyrics in `simon_and_garfunkel.txt`

* `maximum_rank`: We cannot randomly select a sentence ranked below this constant in importance. This number is used in *all* sentence selections, and so functions as a general "entropy" constant. This number should NEVER be greater than 'minimum_length' variable. Ex: If this constant is 5, we cannot select the 6th most important sentence.

### `simon_and_garfunkel.txt`
Just a list of lyrics pulled from three Simon & Garfunkel. Duplicate lyrics were removed, and some lines were concatenated for sufficient length, but otherwise the lyrics are untouched. This is used to pad user input if the user input length is below `minimum_length`.

### `dickinson.txt`
This is a list of first lines sourced from 444 of her published poems. These lines are used as the source for the second of the three poem lines.

### `cosine_similarity_claire.py` and `tf_idf_claire.py`
These files are very similar to `tf_idf.py` and `cosine_similarity.py`, but are included due to the `textualtoy` having different functional needs than the `chatbot`.

