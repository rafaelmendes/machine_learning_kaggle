clc; clear all; close all; 

train_data_path = '/home/rafael/Documents/aula_mestrado/aprend_maquinas/trabalho_eric/kaggle/data/new_train.csv';
teste = '/home/rafael/Documents/aula_mestrado/aprend_maquinas/trabalho_eric/kaggle/data/train_simpler.csv';

% trainData = csvread(train_data_path,1);

% trainData = importdata(train_data_path,1);

trainData = readtable(teste,'Delimiter',',');
