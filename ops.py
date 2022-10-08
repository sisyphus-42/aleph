# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:30:24 2019

@author: sisyphus42
"""

import tensorflow as tf



def InstanceNorm(inputs, name):
    with tf.variable_scope(name):
        mean, var = tf.nn.moments(inputs, axes=[1, 2], keep_dims=True)
        scale = tf.get_variable("scale", shape=mean.shape[-1], initializer=tf.constant_initializer([1.]))
        shift = tf.get_variable("shift", shape=mean.shape[-1], initializer=tf.constant_initializer([0.]))
        return (inputs - mean) * scale / tf.sqrt(var + 1e-10) + shift

def conv(name, inputs, nums_out, ksize, strides, padding="SAME", is_SN=False):
    with tf.variable_scope(name):
        W = tf.get_variable("W", shape=[ksize, ksize, int(inputs.shape[-1]), nums_out], initializer=tf.truncated_normal_initializer(stddev=0.02))
        b = tf.get_variable("b", shape=[nums_out], initializer=tf.constant_initializer(0.))
        if is_SN:
            return tf.nn.conv2d(inputs, spectral_norm(name, W), [1, strides, strides, 1], padding) + b
        else:
            return tf.nn.conv2d(inputs, W, [1, strides, strides, 1], padding) + b

def uconv(name, inputs, nums_out, ksize, strides, padding="SAME"):
    with tf.variable_scope(name):
        w = tf.get_variable("W", shape=[ksize, ksize, nums_out, int(inputs.shape[-1])], initializer=tf.truncated_normal_initializer(stddev=0.02))
        b = tf.get_variable("b", [nums_out], initializer=tf.constant_initializer(0.))
        # inputs = tf.image.resize_nearest_neighbor(inputs, [H*strides, W*strides])
        # return tf.nn.conv2d(inputs, w, [1, 1, 1, 1], padding) + b
    return tf.nn.conv2d_transpose(inputs, w, [tf.shape(inputs)[0], int(inputs.shape[1])*strides, int(inputs.shape[2])*strides, nums_out], [1, strides, strides, 1], padding=padding) + b


def fully_connected(name, inputs, nums_out):
    with tf.variable_scope(name, reuse=tf.AUTO_REUSE):
        W = tf.get_variable("W", [int(inputs.shape[-1]), nums_out], initializer=tf.truncated_normal_initializer(stddev=0.02))
        b = tf.get_variable("b", [nums_out], initializer=tf.constant_initializer(0.))
        return tf.matmul(inputs, W) + b


def spectral_norm(name, w, iteration=1):
    w_shape = w.shape.as_list()
    w = tf.reshape(w, [-1, w_shape[-1]])
    with tf.variable_scope(name, reuse=False):
        u = tf.get_variable("u", [1, w_shape[-1]], initializer=tf.truncated_normal_initializer(), trainable=False)
    u_hat = u
    v_hat = None

    def l2_norm(v, eps=1e-12):
        return v / (tf.reduce_sum(v ** 2) ** 0.5 + eps)

    for i in range(iteration):
        v_ = tf.matmul(u_hat, tf.transpose(w))
        v_hat = l2_norm(v_)
        u_ = tf.matmul(v_hat, w)
        u_hat = l2_norm(u_)
    sigma = tf.matmul(tf.matmul(v_hat, w), tf.transpose(u_hat))
    w_norm = w / sigma
    with tf.control_dependencies([u.assign(u_hat)]):
        w_norm = tf.reshape(w_norm, w_shape)
    return w_norm

def leaky_relu(x, slope=0.2):
    return tf.maximum(x, slope*x)