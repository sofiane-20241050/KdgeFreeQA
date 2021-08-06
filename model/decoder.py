import tensorflow as tf
def decoding_layer(target_letter_to_int,decoding_embedding_size,num_layers,rnn_size,target_sequence_length,
                   max_target_sequence_length,encoder_state,decoder_input):
    target_vocab_size=len(target_letter_to_int)
    decoder_embeddings=tf.Varible(tf.random_uniform([target_vocab_size,decoding_embedding_size]))
    decoder_embed_input=tf.nn.embedding_lookup(edcoder_embeddings,decoder_input)
    def get_decoder_cell(rnn_size):decoder_cell=tf.contrib.rnn.LSTMCell(rnn_size,initializer=tf.random_uniform_initializer(-0.1,0.1,seed=2))
        return get_decoder_cell
    cell=tf.contrib.rnn.MultiRNNCell([get_decoder_cell(rnn_size) for _  in range(num_layers)])
output_layer=Dense(target_vocab_size,kernel_initializer=tf.truncated_normal_initializer(mean=0.0,atddev=0.1))
