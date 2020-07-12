# 人脸检测

##### 使用cgi 提供人脸检测服务

### 安装相关模块
    pip install numpy opencv-python
> 注意：代码是基于python3开发

URL: `localhost:8080`
URI：`/face_detection`
method: `GET`
## 请求参数
参数             | 解释
-----           | ---
image           | 图片地址

## 返回参数
参数             | 解释
-----           | ---
status          | 0`成功，`-1`失败
data            | 人脸在原始图片上的坐标位置~~~~

#### 请求样例：

    GET:  http://localhost:8080/face_detection?image=

#### 成功返回参数：

    {"status": 0, "data": [[530, 1837, 53, 53], [80, 760, 598, 598]]}

#### 失败返回参数

    //请求：
    http://localhost:8080/face_detection?image=http://localhost:8080/image/not_found.jpg
    
    //返回：
    {"status":-1,"data":"HTTP Error 404: Not Found"}


-----------------

#### 原始图像:

![image](http://localhost:8080/image/test.jpg)


#### 识别到的人脸:

![image](http://localhost:8080/image/test_result.jpg)


# 参考
- [A Python REST Server](https://sites.google.com/view/programtuto/web-programming/a-python-rest-server)
- [opencv-data](https://github.com/opencv/opencv/tree/master/data)
