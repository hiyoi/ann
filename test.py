# coding: utf-8
import network
from PIL import Image
import numpy as np
import struct
import file_tools
import json


def main():
    input_num = 28 * 28
    hidden_num = 70
    output_num = 10
    alpha = 0.3
    count = 0
    nw = network.NetWork(input_num, hidden_num, output_num, alpha)

    with open('data.json', 'r') as f:
        data = json.load(f)

    input_num = data['input_num']
    hidden_num = data['hidden_num']
    output_num = data['output_num']
    nw.hidden_weight = np.asarray(data['hidden'])
    nw.output_weight = np.asarray(data['output'])
    nw.hidden_theta = np.asarray(data['hidden_theta'])
    nw.output_theta = np.asarray(data['output_theta'])
    test_num = 100  # 测试样本数
    for i in xrange(test_num):
        # index = int(np.random.random()*9999)
        img_list = file_tools.read_image('t10k-images.idx3-ubyte', i)
        expect_list = file_tools.read_label('t10k-labels.idx1-ubyte', i)
        result = nw.get_output_result(img_list)

        print expect_list, '\t', np.argmax(result), i
        if (np.equal(np.argmax(expect_list),np.argmax(result))):
            print 'success'
            count += 1
        else:
            print 'fail'
    print 'success count=' + str(count)

if __name__ == '__main__':
    main()
