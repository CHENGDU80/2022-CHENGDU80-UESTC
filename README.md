# 2022 FINTECH80 UESTC比赛
*成都西财举办的金融科技比赛FINTECH80，UESTC参赛队伍所采用的私有仓库*

## 文件目录结构：
- `./Data/`：数据目录，包含原始数据以及预处理脚本
- `./Model/`：模型目录，包含模型训练入口和测试入口
- `./UI/`：结果展示目录，使用PyQT开发实现


## 数据预处理


## 模型介绍

### 环境
```
python == 3.8.13
PyTorch == 1.10.2
scikit-learn == 1.1.2
tqdm
```

### 模型训练

在`data/train`目录下运行`model.py`脚本对模型进行训练，在训练后会在验证集上对模型的各指标进行衡量：

```shelll
python model.py
```

**参数**：

+ `-reTrain`：是否重新训练，默认为True
+ `-thrs`：置信阈值
+ `-num_models`：集成学习模型数量
+ `-train_set`：训练集路径
+ `-train_label`：训练集label路径

### 模型预测

在`data/train`目录下运行`modelPredict.py`脚本对测试数据进行预测，将每条记录的标签的分输出到文件中：

```shelll
python modelPredict.py
```

**参数**：

+ `-thrs`：置信阈值
+ `-num_models`：集成学习模型数量
+ `-test_set`：测试集路径
+ `-test_label`：测试集label路径

## 前端介绍
### 环境
```
pyqt5
pyqt5-plugins
pyqt5-tools
pyecharts
```

### 文件目录结构
- `./UI/`
  	- **`Config.py`**：参数配置表文件
  	- **`Main.py`**：控制前端的页面跳转等逻辑操作，前端最主要的执行文件
	
	- **`GenerateHtml.py`**：生成pyecharts图表的html文件，生成路径位于`./Model/htmls/`与`./Model/htmls_main/`
	- `MainWindow.py`：前端的样式表等外观设计文件，由`qtDesigner`与`pyUIC`可视化工具导出代码，无需编辑
	- `resources_rc.py`：前端引用icon等图标的资源文件，无需编辑
- `./UI/`资源文件
	
  - **`MainWindow.ui`：**前端的样式表等外观设计文件，由`qtDesigner`实现设计
  	- `resources.qrc`：前端的icon组件等外观设计文件，由`qtDesigner`调用，调用`./Model/img/`下的icon组件
  	- 其余文件为UI设计或调用的测试数据，无需编辑
