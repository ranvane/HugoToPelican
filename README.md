# HugoToPelican
将静态网站内容从 Hugo 转换为 Pelican

Convert content from o Hugo to Pelican

## 使用方法：
安装required packages：

```bash
pip install -r requirements.txt
```

修改代码中源路径和目标路径：
```python
source_folder = ".../hugo_blog/content/post" #Hugo conentent folder
destination_folder = ".../pelican_blog/content" #Pelican content folder
```
执行脚本：
```python
python hugo_to_pelican.py
```

转换完成后将`images` 文件夹拷贝到pelican_blog的output文件夹中。

至于Hugo的其他metadata转换，可以直接修改函数`write_peclican`的代码，添加实现。

## Usage:
Install required packages:
```bash
pip install -r requirements.txt
```
Modify the source and destination folder in the code:
```python
source_folder = ".../hugo_blog/content/post" #Hugo conentent folder
destination_folder = ".../pelican_blog/content" #Pelican content folder
```
Execute the script:
```python
python hugo_to_pelican.py
```
After the conversion, copy the `images` folder to the output folder of pelican_blog.
For the Hugo metadata conversion, you can modify the code in the function `write_peclican` to add the implementation.
