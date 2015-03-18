bcrobot
 
###bcrobot是一个建立在BearyChat的消息机器人，主要实现了以下功能：
1.微信和BearyChat消息的互相通信（仅限微信公众平台），主要实现了以下子功能：
  当微信公众号被关注时，微信后台发布内容或者用户发消息时，BearyChat能够即时得到通知  
  在BearyChat中得到hacknews新闻后，可以转发给微信公众新闻消息。
2.订阅推送服务  
（使用OutComing机器人发送Incoming机器人的地址）  
  在BearyChat中可以实时的接收服务器发出的消息，能够实时监控服务器的运行情况。
3.天气预报  (支持每日推送
 输入城市，可以查看今天和明天的天气预报
4.hackernews信息浏览，订阅推送后会每日得到hackernews更新，也可以输入命令即时查看hackernews。
5.BearyChat AI聊天
6.团队与团队之间的管理和交流，团队关系管理。(Todo)


###使用方法：  
下面以pydata微信公众号为例，介绍相关使用方法：   
1.微信扫码 ![pydata](media/image/qrcode.jpg)  
2.在BearyChat内新建OutComing机器人，并填入触发词bcrobot 和 服务器地址http://bearychat.justpic.org/outcome  
3.新建InComing机器人，并复制订阅地址:http://hook.bearychat.com/<your_webhook_url>，  
4.在聊天对话框中输入justpic sub http://hook.bearychat.com/your_webhook_url subtype,(注意空格,其中subtype可以为weixin,weather,server,hackernews),即可完成订阅推送服务。 
 在完成了订阅推送服务后，即可实时监听服务器运行状态和其他推送内容
 发送justpic server可以即时得到当前服务器运行状态信息
5.在聊天对话框中输入bcrobot wx 可进行微信管理功能，完成微信公众号状态监听，当没有订阅推送服务时，只能查询历史消息通知。  
6.在聊天对话框中输入bcrobot weather <city>查询天气状态（支持推送)。  
7.在聊天对话框中输入bcrobot hn显示hacknews列表(提供hot，latest选项）  
8.在聊天对话框中输入bcrobot ai <message>可以进行AI机器人聊天。
9.在聊天对话框中输入bcrobot cancel subtype/all,取消订阅推送服务/所有。  
10.在聊天对话框中输入bcrobot status 查看订阅推送服务状态。
11.在聊天对话框中输入bcrobot chat <message>可以与BearyChat外部用户进行聊天。

###部署指南
（部署于外部服务器）  
1.git clone https://gitcafe.com/matrixorz/bcrobot.git  
2.cd bcrobot && pip install -r requirements.txt  
3.python manage.py validate && python manage.py syncdb  
4.python manage.py runserver 8000  
5.编辑nginx配置文件，并重新启动nginx
6.启动redis-server，启动celery任务  
7.点击[微信公众平台](https://mp.weixin.qq.com)进入开发者中心设置服务器地址  

###说明
由于outgoing机器人在接收响应请求后，对响应文本处理的长度有限制和attachments没有处理，hacknews在outgoing机器人下面不能正常使用，天气服务由于服务器在国外，获取数据网络不稳定，后期会做优化
大家可以通过订阅推送每小时接收最新的HackerNews消息。





