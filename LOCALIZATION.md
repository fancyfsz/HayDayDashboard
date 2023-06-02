原仓库 https://github.com/castroavila/hayday.git 没有对物品名称等显示作本地化的处理。

笔者为中国玩家，因此打算对它进行本地化以方便中文玩家进行查看。

参考链接：https://cloud.tencent.com/developer/article/1567188

具体做法：

1. 引入python的gettext库，调用gettext.gettext即可查找对应key的value。因此需要对item.py进行修改，具体而言就是

   ```python
   import gettext
   _ = gettext.gettext
   
   使用 sed -i ''  "s/name='\([^']*\)'/name=_('\1')/g" item.py 即可全局替换格式。
   ```

   

2. 准备翻译文件

   使用xgettext可以提取需要翻译的字符串的模版

   ```shell
   xgettext -k_ -o item.pot --from-code=UTF-8 item.py
   ```

   注意这里应该是UTF-8而不是UTF8，原博有拼写错误。

   使用msginit生成不同翻译的文件.po

   ```shell
   msginit -l zh_CN -i item.pot
   ```

   执行完会生成zh_CN.po

   如果item.pot有变化，需要更新zh_CN.po里面的key值的话用更新命令

   ```shell
   msgmerge -U zh_CN.po item.pot
   ```

   生成二进制文件.mo用于应用程序读取

   首先，创建存放mo文件的locale目录，目录结构要和系统的locale目录结构一样

   ```shell
   mkdir -p locale/zh_CN/LC_MESSAGES
   ```

   然后在对应目录生成不同的.mo文件

   ```shell
   msgfmt -o locale/zh_CN/LC_MESSAGES/item.mo zh_CN.po
   ```



3. 在python代码中添加国际化支持

   ```python
   APP_NAME = "item"
   LOCALE_DIR = os.path.abspath("locale")
   # 将域APP_NAME与LOCALE_DIR目录绑定，
   # 这样gettext函数会在LOCALE_DIR目录下搜索对应语言的二进制APP_NAME.mo文件
   gettext.bindtextdomain(APP_NAME, LOCALE_DIR)
   # 声明使用现在的域，可以使用多个域，便可以为同一种语言提供多套翻译，
   # 本程序只使用了一个域
   gettext.textdomain(APP_NAME)
   ```

   

具体修改可以参考：4c1db94346fafab9fa27f6de6c63f12f4b647695
