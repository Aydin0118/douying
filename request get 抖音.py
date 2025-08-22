import requests
import tkinter as tk    


def download_video():
    video_url=entry_1.get().strip()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.douyin.com/',
        # 'Accept': 'video/webm,video/ogg,video/*;q=0.9,application/octet-stream;q=0.8,*/*;q=0.7',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Connection': 'keep-alive',
        # 'Sec-Fetch-Dest': 'video',
        # 'Sec-Fetch-Mode': 'no-cors',
        # 'Sec-Fetch-Site': 'cross-site'
    }
    e = requests.get(video_url, headers=headers, stream=True)
    if e.status_code == 200:
        with open('douyin_video.mp4', 'wb') as f:
            for chunk in e.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("视频下载完成！")
    else:
        print(f"下载失败，状态码：{e.status_code}")
        
    print(e.status_code)
    
root = tk.Tk()

tk.Label(root, text="注意：请确保输入的 URL 正确无误！").grid(row=6, columnspan=2, pady=10)
root.title("抖音视频下载器")
root.geometry("400x300")  # 设置窗口大小
# 设置窗口图标
try:   
    root.iconbitmap(r"D:\党培祥\进阶\抖音\android-download_icon-icons.com_50526.ico") 
except:
    pass
# 视频的URL输入框
tk.Label(root, text="视频v3链接:").grid(row=0, column=0)
entry_1 = tk.Entry(root)
entry_1.grid(row=0, column=1, pady=5, padx=5)
tk.Button(root, text="开始爬取", command=download_video).grid(row=4, columnspan=2, pady=10)
var= tk.StringVar()
var.set("请填写所有字段")
while entry_1.get() == "":
    var.set("请填写所有字段")
    root.update()  # 更新窗口
    tk.Label(root, textvariable=var).grid(row=5, columnspan=8, pady=10)
   
else:
    var.set("所有字段已填写，请点击开始爬取按钮")
    root.update()
tk.Label(root, textvariable=var).grid(row=5, columnspan=2, pady=10)

root.mainloop()
