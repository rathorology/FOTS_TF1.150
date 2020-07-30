# Fast Oriented Text Spotting with a Unified Networks
### Introduction
This is an use of [FOTS: Fast Oriented Text Spotting with a Unified Network](https://arxiv.org/pdf/1801.01671.pdf)
### Install
+ Python3.5
+ tensorflow 1.12.0
+ OpenCV
```
pip install -r requirements.txt
git clone -b dev https://github.com/Pay20Y/FOTS_TF.git
```
### Extract images to one location
```
python3 uniform_images.py
```
### Make annotation for training in FOTS format
```
python3 make_annotation.py
```

### Used pretrained model to train 
SynthText 6-epochs pretrained model can be found [here](https://github.com/Pay20Y/FOTS_TF/releases/download/v2/SynthText_6_epochs.tar)
### Train
```
python3 main_train.py --gpu_list='-1' --learning_rate=0.0001 --train_stage=2 --training_data_dir=data --training_gt_data_dir=annotation
```
![train_shots/10.png](train_shots/10.png)
![train_shots/20.png](train_shots/20.png)
![train_shots/40.png](train_shots/40.png)
![train_shots/60.png](train_shots/60.png)
![train_shots/80.png](train_shots/80.png)
![train_shots/100.png](train_shots/100.png)


### Test
```
python3 main_test.py --gpu_list='-1' --test_data_path=/path/to/testset/ --checkpoint_path=checkpoints/
```

### Align results with ground truth for train and test data

```
python3 final_output.py
```

### Evaluate model on test
```
python3 evaluation.py
```

### Test Accuray
```
72.21%
```
### Metric for evaluation

Percentage match of strings