#!/usr/bin/env python
# -*- coding: utf-8 -*-


import jieba

"""
# API
# jieba.cut(, cut_all, HMM)
# jieba.lcut(, cut_all, HMM)
# jieba.cut_for_search(, HMM)
# jieba.lcut_for_search(, HMM)
# jieba.Tokenizer(dictionary = DEFAULT_DICT)
# jieba.load_userdict(file_name)
"""


# =================================
# 分词
# =================================

# 精确模式
seg_acc_HMM = jieba.cut("我来到北京清华大学", cut_all = False, HMM = False)
seg_acc_list_HMM = jieba.lcut("我来到北京清华大学", cut_all = False, HMM = False)
seg_acc_noHMM = jieba.cut("我来到北京清华大学", cut_all = False, HMM = True)
seg_acc_list_noHMM = jieba.lcut("我来到北京清华大学", cut_all = False, HMM = True)
print("【Default Mode with HMM】: " + "/ ".join(seg_acc_HMM))
print("【Default Mode list with HMM】: " + "/ ".join(seg_acc_list_HMM))
print("【Default Mode without HMM】: " + "/ ".join(seg_acc_HMM))
print("【Default Mode list without HMM】: " + "/ ".join(seg_acc_list_HMM))


# 全模式
seg_all_noHMM = jieba.cut("我来到北京清华大学", cut_all = True, HMM = False)
seg_all_list_noHMM = jieba.lcut("我来到北京清华大学", cut_all = True, HMM = False)
seg_all_HMM = jieba.cut("我来到北京清华大学", cut_all = True, HMM = True)
seg_all_list_HMM = jieba.lcut("我来到北京清华大学", cut_all = True, HMM = True)
print("【Full Mode with HMM】: " + "/ ".join(seg_all_noHMM))
print("【Full Mode list with HMM】: " + "/ ".join(seg_all_list_noHMM))
print("【Full Mode without HMM】: " + "/ ".join(seg_all_HMM))
print("【Full Mode list without HMM】: " + "/ ".join(seg_all_list_HMM))


# 搜索引擎模式
seg_search_noHMM = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM = False)
seg_search_list_noHMM = jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM = False)
seg_search_HMM = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM = True)
seg_search_list_HMM = jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", HMM = True)
print("【Search Mode with HMM】: " + "/ ".join(seg_search_noHMM))
print("【Search Mode list with HMM】: " + "/ ".join(seg_search_list_noHMM))
print("【Search Mode without HMM】: " + "/ ".join(seg_search_HMM))
print("【Search Mode list without HMM】: " + "/ ".join(seg_search_list_HMM))


# =================================
# 添加自定义词典
# =================================
# 载入词典




# 调整词典
