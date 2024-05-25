## 遇到的问题
1. 在vscode中单独运行测试时，需要配置PYTHONPATH环境变量：
    ```json
    {
        "terminal.integrated.env.windows": {
            "PYTHONPATH": "${workspaceFolder};${env:PYTHONPATH}"
        }
    }
    ```
    为了避免不同环境python运行，路径出现问题，也增加launch.json设置当前工作目录：
    ```json
    "cwd": "${fileDirname}" // 确保工作目录设置为当前文件的目录
    ```
2. 在使图片label控件居中对齐时，发现应该在控件添加到布局时进行动态居中，即在qt designer中等效于将控件进行“布局对齐”。
3. 使用组件库的FlowLayout时，不知道如何设置背景色。FlowLayout需要寄生于QWidget上，然后对QWidget设置背景色。还发现内容过多会溢出屏幕，发现应当寄生在滚动区域上。
4. 偶尔会报QPainter的一系列冲突，发现是在父控件上定义过同名变量导致的。但是无法彻底解决，是组件库的bug[#867](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/issues/867)。
5. 在习惯界面移除旧卡片时，调用库提供的```removeAllWidgets()```方法有时不成功。通过实现手动删除组件后解决。
6. 对带动画的卡片组件设置颜色时，颜色闪现，手动调用父类中的```_updateBackgroundColor()```方法可以有效更新颜色。
7. 不知道如何将内层布局尽量挤占外层布局控件，查询文档，设置外层布局的权重，同级组件如有必要也要设置sizeConstraint。
8. 数据库删除时发现级联操作不生效，应当在数据库每次连接后手动执行```PRAGMA foreign_keys = ON;```