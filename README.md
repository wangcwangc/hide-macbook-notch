# hide-macbook-notch

使用黑色壁纸隐藏新MBP刘海屏。

使用Python实现了一个简单的脚本，向壁纸中添加一行黑色像素，由于MacOS菜单栏透明会使得菜单栏与刘海融为一体。

Hide new MacBook Pro notch with black wallpaper. 

A simple script was implemented using Python to add a line of black pixels to the wallpaper. The MacOS menu bar is transparent so that it blends in with the notch.

## Install

```python
pip install -r requirement.txt
```

## Use

```shell
cd hide-macbook-notch/
python hide-macbook-notch -i <infile-image> -o <output-path>
```

Optional

```shell
-p <menu-high-pixel> //default pixel = high * 0.023
```
in my external screen 1920*1080, menu pixel is 25, 25/1080≈0.023

## Example
  
<img width="1214" alt="example" src="https://user-images.githubusercontent.com/19590572/139057103-bd7d5d36-30f5-4d68-bdd4-0c58c03cd570.png">



## Last
看了网上很多大神的解决方案，先写了个脚本，等有了新MBP试一试（/手动狗头
