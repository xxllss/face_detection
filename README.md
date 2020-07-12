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

    http://localhost:8080/face_detection?image=https://pic3.zhimg.com/v2-35306ff8000cc2ad945bb8c04b3a5e0e_1440w.jpg?source=172ae18b

#### 成功返回参数：

    {
      "status": 0,
      "data": [
        [
          53,
          51,
          403,
          403
        ]
      ]
    }

#### 失败返回参数

    //请求：
    http://localhost:8080/face_detection?image=http://localhost:8080/image/not_found.jpg
    
    //返回：
    {"status":-1,"data":"HTTP Error 404: Not Found"}


-----------------

#### 原始图像:

![image](https://github.com/xxllss/face_detection/blob/master/src/image/test.jpeg)

#### 识别到的人脸:

![image](https://github.com/xxllss/face_detection/blob/master/src/image/test_result.jpeg)

# 参考
- [A Python REST Server](https://sites.google.com/view/programtuto/web-programming/a-python-rest-server)
- [opencv-data](https://github.com/opencv/opencv/tree/master/data)
