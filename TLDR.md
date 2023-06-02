![Baner](./assets/logo/Banner.png "Banner")
# 卡通农场
该仪表盘用于可视化游戏里面各种物品之间的依赖关系。

# 目标

帮助玩家更好的制定游戏策略。

## 运行示意图

![screenshot1](./screenshots/screenshot1.png "opt title")
![screenshot1](./screenshots/screenshot2.png "opt title")
![screenshot1](./screenshots/screenshot3.png "opt title")

# 怎么运行

- `python3.9+`.

- 安装需求文件 `requirements.txt` 里面需要的模块。

  > python3 -m pip install -r requirements.txt 参考链接：https://muzing.top/posts/594ac4a6/

- 运行 `python3 visualization.py`。没有报错的情况下，在浏览器中打开 http://127.0.0.1:8050 即可查看仪表盘。

  


# 数据来源

所有图片和数据均来自https://hayday.fandom.com/wiki/Hay_Day_Wiki


# 可能的报错解决

<img width="535" alt="截屏2023-06-02 14 26 35" src="https://github.com/fancyfsz/HayDayDashboard/assets/16755699/a2751aa9-f935-4ab4-9d98-55798577b8d7">


原因是没有安装pygraghviz库。如果在Mac arm芯片的机器上直接用`pip3 install pygraphviz`会安装失败，解决方法可以参见：https://github.com/pygraphviz/pygraphviz/issues/398

```
brew install graphviz
python3 -m pip install \
    --global-option=build_ext \
    --global-option="-I$(brew --prefix graphviz)/include/" \
    --global-option="-L$(brew --prefix graphviz)/lib/" \
    pygraphviz
```

