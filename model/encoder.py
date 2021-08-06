import tensorflow as tf
def get_encoder_layer(input_data,rnn_size,num_layers,source_sequence_length,source_vocab_size,encoding_embedding_size):
    encoder_embed_input=tf.contrib.layers.embed_sequence(input_data,source_vocab_size,encoding_embedding_size)


def get_lstm_cell(rnn_size):
    lstm_cell=tf.contrib.rnn.LSTMCell(rnn_size,initializer=tf.random_uniform_initializer(-0.1,0.1,seed=2))
    return lstm_cell
cell=tf.contrib.rnn.MUltiRNNCell([get_lstm_cell(rnn_size)for - in range (mun_layers)])

encoder_output,encoder_state=tf.nn.dynamic_rnn(cell,encoder_embed_input,sequence_length=source_sequence_length,dtype=tf.float32)
return encoder_output,encoder_state