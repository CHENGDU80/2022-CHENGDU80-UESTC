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
```

### 文件目录结构（未定）
- `./Model/`
	- `fit.py`：模型训练入口
	- `train.py`：模型训练流程定义
	- `model.py`：模型定义
	- `validation.py`：验证流程定义
	- `dataop.py`：为模型整理输入数据集
	- `predict.py`：预测入口


### 模型训练（未定）

**参数**：



### 模型预测（未定）

**参数**：







## 前端介绍
### 环境
```
pyqt5
pyqt5-plugins
pyqt5-tools
pyecharts
```

### 文件目录结构（未定）
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
