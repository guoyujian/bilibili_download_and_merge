# bilibili_download_and_merge

我在B站上发现很多视频课专辑，这些专辑很有意思，对我的学习很有帮助。  
但是由于版权问题，这些专辑很容易失效。
又由于手机存储空间有限，因此我想将其保存到PC。
在Google的过程中，找到了几个思路：  
1. 用硕鼠下载器下载。缺点：硕鼠下载器只支持批量解析20个视频连接，而很多专辑分P多达上百个。  
2. 用安卓手机APP：Bilibili缓存视频，在用缓存合并工具.apk将视频合并到一个文件夹中，最后导出到电脑。  
&nbsp;&nbsp;缺点：太麻烦了。在手机上本来就不好了操作，还要将几个G的文件导出到电脑。  
3. 用安卓模拟器，其他步骤同上。缺点：模拟器中的缓存合并工具并不好用，无法识别。而且下载的文件很琐碎*。  
&nbsp;&nbsp;*. 目录结构见文件夹《B站手机app保存到本地的文件目录结构》

---

因此本项目目标是：
1. 将用安卓模拟器下载的视频片段合并，输出到目标文件夹*。  
&nbsp;&nbsp;*生成得文件目录见：输出的文件目录结构.png
2. 将弹幕xml文件转换成普通视频播放器能识别的ass文件。  
&nbsp;&nbsp;a. 估计得研究JS文件
3. 直接根据av号，下载整个专辑，包括：  
&nbsp;&nbsp;a. 根据av号，读取专辑下的分P数。  
&nbsp;&nbsp;b. 用you-get下载每一P。  
&nbsp;&nbsp;c. 处理弹幕文件xml。


2019/4/5  
完成目标1。如何使用：调用merge模块下的exec_merge(input_path, isAlbum, to_path)方法，该方法有三个参数:  
&nbsp;&nbsp;input_path：保存到本地的视频目录，例如“C:\Users\guoyujian_lc\Desktop\18896337”  
&nbsp;&nbsp;isAlbum：暂时没用，默认值为True  
&nbsp;&nbsp;to_path：输出的完整视频的文件夹。例如：“C:\Users\guoyujian_lc\Desktop\aim”  
已知缺陷：速度略慢，待改进。