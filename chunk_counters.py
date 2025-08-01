from collections import Counter

def np_chunk_counter(chunked_sentences):
    """
    Pulls noun phrase chunks out of chunked sentences and finds the most common chunks.
    
    Args:
        chunked_sentences (list): List of chunked sentences from NLTK parser
        
    Returns:
        list: List of tuples with the 30 most frequent NP chunks and their counts
    """
    
    # create a list to hold chunks
    chunks = list()

    # for-loop through each chunked sentence to extract noun phrase chunks
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
            chunks.append(tuple(subtree))

    # create a Counter object
    chunk_counter = Counter()

    # for-loop through the list of chunks
    for chunk in chunks:
        # increase counter of specific chunk by 1
        chunk_counter[chunk] += 1

    # return 30 most frequent chunks
    return chunk_counter.most_common(30)


def vp_chunk_counter(chunked_sentences):
    """
    Pulls verb phrase chunks out of chunked sentences and finds the most common chunks.
    
    Args:
        chunked_sentences (list): List of chunked sentences from NLTK parser
        
    Returns:
        list: List of tuples with the 30 most frequent VP chunks and their counts
    """
    
    # create a list to hold chunks
    chunks = list()

    # for-loop through each chunked sentence to extract verb phrase chunks
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'VP'):
            chunks.append(tuple(subtree))

    # create a Counter object
    chunk_counter = Counter()

    # for-loop through the list of chunks
    for chunk in chunks:
        # increase counter of specific chunk by 1
        chunk_counter[chunk] += 1

    # return 30 most frequent chunks
    return chunk_counter.most_common(30) 