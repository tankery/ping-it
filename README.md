# Ping it
Tiny project to do ping test for multiple website, and find out which one has stable & faster connection.

“ping它”是个有助于你选择VPS或其他服务器的微型项目，它的主要逻辑就是定时对一个服务器地址列表做ping测试。再分析测试结果，以选取出最稳定、最快速的服务器。至于做这个的目的，你懂的~

## About
Ping it use shell script to do the ping test, output the test result to files. Use Python to analyze the result, and with CGI support in apache, the result can be access through web.

The project is not that complete, it contains only the core logic code, you should distribute and schedule it by your self. Hope it can inspire you at least~

Ping它 使用shell脚本做ping测试，输出结果到文件中；使用Python来分析测试结果；再利用Apache的CGI支持，使得分析结果能通过网页访问。

这个工程并不是那么完备，它只包含一些核心代码，你必须自己去部署这些代码，定时调用部分，也需要你自行解决。但我希望这个工程至少能激发你的一些想法就很好了~

## About Python analyzing code
For Python code, I use a Functional Programming paradigm, I'm a beginner for that, so I think its also a good example to demo it.

对于Python代码，我还想多说一些。我尝试使用了函数式编程范式来实现这个分析过程。因为我对于函数式编程也才刚刚入门，所以我想这个工程也是一个很好的示例代码。

## Directory structure

```
multi-ping.sh     # The script to do the ping test through a host list.
sites.txt         # Sample text file to list the dest hosts.
ping/             # The python scripts hosting directory,
  |               # put contents in this folder to CGI-Excutable folder.
  |
  |- utils.py     # util functions, like pipeline helper.
  |
  |- analyzer.py  # core logic to do the analyzer, each function is a step,
  |               # then use pipeline to chain it.
  |
  |- table*       # The CGI script in Python, collecting result for all sites,
  |               # and sort by a score of site.
  |
  |- site*        # The detais for one site, display the history of ping result.
  |
  `- collection@ -> /path/of/ping/test/result/folder
```

## Prerequisit
Apache with CGI support.

## Usage
1. clone the repository.
2. config the "sites.txt" file.
3. schedule the "multi-ping.sh" periodically.
4. copy the Python files to a directory can access by CGI.
5. create a soft link point to the ping test result folder.
5. Access "table" & "site" from web.

