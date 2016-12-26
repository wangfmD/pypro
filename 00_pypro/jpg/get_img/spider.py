#-*- coding:utf-8 -*-
# leaf_spider2_2014-3-6.py

import urllib


def create_dybar_str(n=100):
    '''
    @n 进度条长度
    '''
    return ['> '] * (n / 2)


def create_bar_str(n=100):
    '''
    @n 进度条长度
    '''
    pos = n // 8 - 1
    tmp = '- ' * pos
    barstr = []
    barstr.append('0%')
    barstr.append(tmp)
    barstr.append('25%')
    barstr.append(tmp)
    barstr.append('50%')
    barstr.append(tmp)
    barstr.append('75%')
    barstr.append(tmp)
    barstr.append('100%')
    return barstr


def get_and_save_url(url, savefilename):
    '''
    @url 			: 目标网址
    @savefilename	: 保存文件路径
    '''
    def callback(datanum, blocksize, filesize):
        '''
        @datanum	: 目前为止，传递的数据块数量
        @blocksize	: 每个数据块的大小，单位是byte，字节
        @filesize	: 远程文件的大小
        '''
        down_progress = 100.0 * datanum * blocksize / filesize
        if down_progress > 100:
            down_progress = 100
        tmp = barsize // 100 * (100 - int(down_progress) + 1)
        print ''.join(dybarstr[:-tmp]),
        dybarstr[:-tmp] = []

    barsize = 100
    barstr = create_bar_str(barsize)
    dybarstr = create_dybar_str(barsize)

    print '\nstart %s download' % url
    print ''.join(barstr)
    urllib.urlretrieve(url, savefilename, callback)
    print '\nfinlish download and save file to "%s"' % savefilename


if __name__ == '__main__':
    # url = 'http://www.iplaypython.com/'
    url2 = 'http://www.python.org/'
    local = 'e:\\testone.html'
    get_and_save_url(url2, local)
