
import numpy as np

def read_minibatch(data, batch_size, max_length, shuffle = True):
    """
    Args:
        data: the list of raw data, in the form [[author_index, [word1, word2, ...]]
                                                 [author_index, [word1, word2, ...]]
                                                 [author_index, [word1, word2, ...]]
                                                 ...
                                                                                   ]
        max_length: the fixed length of a sentence

        batch_size: the number of rows in each batch

        shuffle: determine whether shuffle the input data or not

    Returns:
        a list of minibatches, in the form [batch1, batch2, ...]
        each batch is made of three lists:
        batch[0]: feature list
        batch[1]: mask list
        batch[2]: label list(only one number in each row)
    """
    data_size = len(data)
    indices = np.arange(len(data))
    batch_list = []
    if shuffle is True:
        np.random.shuffle(indices)
    for minibatch_start in np.arange(0, data_size, batch_size):
        minibatch_indices = indices[minibatch_start : minibatch_start + batch_size]
        selected_data = [data[i] for i in minibatch_indices]
        batch = process_to_minibatch(selected_data, max_length)
        batch_list.append(batch)
    return batch_list

def process_to_minibatch(data, max_length):

    batch = []

    feat_list = []
    mask_list = []
    label_list = []
    for i in range(len(data)):
        minifeat_list = []
        minimask_list = []
        for j in range(max_length):
            if(j >= len(data[i][1])):
                minimask_list.append(False)
                #minifeat_list.append(match_word_to_vector(" "))
                minifeat_list.append([0])
            else:
                minimask_list.append(True)
                #minifeat_list.append(match_word_to_vector(data[j][1][i]))
                minifeat_list.append([data[i][1][j]])
        feat_list.append(minifeat_list)
        mask_list.append(minifeat_list)
        label_list.append(data[i][0])

    batch.append(feat_list)
    batch.append(mask_list)
    batch.append(label_list)

    return batch


def match_word_to_vector(word, word_dict, glove_mat):
    # this function is to map a word to its Glove vector
    if(word_dict.has_key(word) is True):
        ind = word_dict[word]
        return glove_mat[ind, :] # return the corresponding vector
    else:
        return None

data = [ [1, [1, 2, 3, 4, 5, 6]],
         [0, [1, 2, 3, 4, 5, 6]],
         [1, [1, 2, 3, 4, 5, 6]],
         [3, [1, 2, 3, 4, 5, 6]],
         [1, [1, 2, 3, 4, 5, 6]],
         [1, [1, 2, 3, 4, 5, 6]],
         [7, [1, 2, 3, 4, 5, 6]],
         [1, [1, 2, 3, 4, 5, 6, 7, 8]],
         [19, [1, 2, 3, 4]],
         [1, [1, 2, 3, 4, 5, 6]],
         [1, [1, 2, 3, 4, 5, 6]],
         [1, [1, 2, 3, 4, 5, 6]],
         [1, [1, 2, 3, 4, 5, 6]]]

batch_list = read_minibatch(data, 3, 6)
print batch_list
