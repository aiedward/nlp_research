# nlp_research


## 介绍
  
    本项目支持的NLP任务包括 分类、匹配、序列标注、文本生成等.
    - 对于分类任务，目前支持多分类、多标签分类，通过选择不同的loss即可。
    - 对于匹配任务，目前已支持交互模型和表示模型。

## 数据

    训练数据:
    （1）对于分类任务的数据使用csv格式，csv头部包括列名‘target’和‘text’;
    （2）对于匹配任务的数据使用csv格式，csv头部包括列名‘target’,‘text’ 或者 ‘target’,‘text_a’,‘text_b’
    （3）对于NER任务的数据，参考"data/ner/train_data",或者使用其它格式的数据的话，修改task/ner.py中的read_data方法即可。
    预训练数据(目前在分类和匹配任务上已支持):
    如果使用到bert作为预训练，请提前运行"sh scripts/prepare.sh"

## 快速开始
    [依赖]
         环境：python3+tensorflow 1.10(python2.7已支持)
         pip3 install --user -r requirements.txt
         
    各类任务的参数定义在conf/model/内的以任务名命名的yml文件中"conf/model/{task}.yml"
    目前已支持的常见任务如下：       
    [分类]
         1.生成tfrecords数据，训练:
            python3 run.py classify mode=train
           或者直接使用脚本:
            sh scripts/restart.sh classify
         
         2.测试：
           单个测试：python3 run.py classify model=test_one
    [匹配]
         1.生成tfrecords数据，训练:
             python3 run.py match mode=train
           或者直接使用脚本:
             sh scripts/restart.sh match
         2.测试：
            单个测试：python3 run.py match model=test_one
    [序列标注]
        ...
        sh scripts/restart.sh ner
    [翻译]    
        ...
        sh scripts/restart.sh translation
## 任务



## 模块

    1. encoder
        cnn
        fasttext
        text_cnn
        dcnn
        dpcnn
        vdcnn
        rnn        
        rcnn
        attention_rnn
        capsule
        esim
        han
        matchpyramid
        abcnn
        transformer
  
    2. common 
        loss
        attention
        lr
        ...
    
    3. utils
        data process
## 联系

    如果有任何问题，欢迎发邮件到zfz1015@outlook.com
    如果觉得我的工作对您有所帮助，请不要吝啬右上角的小星星哦！
    欢迎Fork、Star！也欢迎一起建设这个项目！
    
  
