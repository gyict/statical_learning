#!/usr/bin/python 
# -*- coding: utf-8 -*-  
from numpy import *
import operator
import os


def CreateDataSet():
	alldata = array([[3,3],[4,3],[1,1]])
	labels = [1,1,-1]
	return alldata, labels


def perceptronClassify(trainData, trainLabel):
	global w,b
	Found = False
	numSamples = trainData.shape[0]
	mLength = trainData.shape[1]
	w = [0]*mLength
	b = 0
	while(not Found):
		for i in xrange(numSamples):
			if cal(trainData[i],trainLabel[i]) <= 0:
				print w,b
				update(trainData[i], trainLabel[i])
				break
			elif i== numSamples-1:
				print w,b
				Found = True



def cal(row, trainLabel):
	global w,b
	res = 0
	for i in xrange(len(row)):
		res += row[i]*w[i]
	res += b
	res *= trainLabel
	return res

def update(row, trainLabel):
	global w,b
	for i in xrange(len(row)):
		w[i] += trainLabel*row[i]
	b += trainLabel
	
	
if __name__ == '__main__':
	g,l = CreateDataSet()
	perceptronClassify(g,l)	
