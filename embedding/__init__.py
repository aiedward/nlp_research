#-*- coding:utf-8 -*-
import sys,os
ROOT_PATH = '/'.join(os.path.abspath(__file__).split('/')[:-1])
sys.path.append(ROOT_PATH)
from word_embedding import WordEmbedding
from char_embedding import CharEmbedding
from subword_embedding import SubwordEmbedding
from region_embedding import RegionEmbedding

embedding = {}
embedding['word_embedding'] = WordEmbedding
embedding['char_embedding'] = CharEmbedding
embedding['subword_embedding'] = SubwordEmbedding
embedding['region_embedding'] = RegionEmbedding

