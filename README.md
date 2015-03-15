bcrobot
 
bcrobot是一个连接微信公众号和BearyChat的消息机器人，主要实现了以下功能：
1.微信和BearyChat消息的互相通信（仅限微信公众平台）,当微信公众号被关注时，微信后台发布内容或者用户发消息时，BearyChat能够即时得到通知
2.订阅推送服务
（使用OutComing机器人发送Incoming机器人的地址）
3.天气预报
   
使用方法：
下面以pydata公众号为例，介绍相关使用方法：
1.微信扫码 ![pydata](media/image/qrcode.jpg)
2.新建OutComing机器人，并填入justpic 和 服务器地址http://robot.justpic.org/outcome
3.新建InComing机器人，并复制订阅地址:http://hook.bearychat.com/your_webhook_url，
4.在聊天对话框中输入justpic sub http://hook.bearychat.com/your_webhook_url,(注意空格),即可完成订阅推送服务。
5.在聊天对话框中输入justpic wx 完成微信公众号状态监听，当没有订阅推送服务时，只能查询历史消息通知。
6.在聊天对话框中输入justpic tianqi查询天气状态（不需要订阅功能的支持）。
7.在聊天对话框中输入justpic cancel http://hook.bearychat.com/your_webhook_url,取消订阅推送服务。


