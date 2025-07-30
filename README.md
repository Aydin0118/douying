# 抖音新反爬虫解决
之前的m3u8方法已被服务器阻止
<img width="1325" height="595" alt="Snipaste_2025-07-30_11-17-11" src="https://github.com/user-attachments/assets/17286bc4-01a8-4631-a145-8eecbc73efbe" />
打开抖音网页，从博主的主页入手，新一代douyin.com刷视频的内在包无法再次通过抓包获取，点开你要下载的视频按f12开始抓包
<img width="1366" height="626" alt="抓包" src="https://github.com/user-attachments/assets/a997df4e-61ab-4ace-88b2-9059f72474aa" />
按缓存从大到小排序，选择最大的fetch文件

<img width="1283" height="547" alt="Snipaste_2025-07-30_13-26-40" src="https://github.com/user-attachments/assets/5d046ffd-0e3f-49e2-bceb-07839d02950d" />

206也不用管，在request中会持续请求到最后就完全成功才到200
找到标头的URL在新窗口打开
<img width="1323" height="545" alt="Snipaste_2025-07-30_13-26-30" src="https://github.com/user-attachments/assets/1bba3613-9bee-46a4-a0bf-04541f5bcc7e" />


打开后可以看到视频的就可以作为URL去爬取了
也可以在元素中获取后台的地址去作为URL
##重要的一点，要有headers##







