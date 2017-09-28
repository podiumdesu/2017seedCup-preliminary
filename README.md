### 2017 "贝贝网 · 种子杯"初赛
数据处理相关

#### 目录结构：

    Src
     ├── 2017“贝贝网·种子杯”编程PK赛-初赛题.pdf
     ├── README.md
     ├── data
         ├── teamData.csv
         ├── getTeamData.py
         ├── result.csv
         ├── check.py
         ├── matchDataTrain.csv
         ├── computeScore.py
         ├── computeResult.csv
         ├── removeBadData.py
         ├── finalData.py
         ├── predictPro_template.csv
         └── matchDataTest.csv

#### 文件介绍

__teamData.csv__

主办方给的数据

__getTeamData.py__

读取_teamData.py_的内容，将每组的球员信息合并成向量，并使所有的队伍补齐队员人数，存入_result.csv_中

__result.csv__


__check.py__

检查result.py中每行是否是同样长度

__computeScore.py__

读取result.csv，读取matchDataTrain.csv中的对局数据，将队伍名使用result.csv中的数据替代，将"0胜1负"使用'0','1'代替，最后的比分，若客场获胜即积1分，否则为0分。将最后的数据写入computeResult.csv中。

__computeResult.csv__

存放数据

__finalData.py__

最终的数据，每行1069个数据元

__predictPro_template.csv__

主办方给的数据，未使用

__matchDataTest.csv__

主办方给的数据，未使用
