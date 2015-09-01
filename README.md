# Ping it

Tiny project to do ping test for multiple website, and find out which one has stable & faster connection.

“ping它”是个有助于你选择VPS或其他服务器的微型项目，它的主要逻辑就是定时对一个服务器地址列表做ping测试。再分析测试结果，以选取出最稳定、最快速的服务器。至于做这个的目的，你懂的~

**Ping it result table**:

```
                            host   loss      avg  stddev  graph
                   www.baidu.com,  1.3%,    9.75,   8.77, .........11]
      speedtest.tokyo.linode.com,  0.5%,  111.95,  17.37, ..........12]
            wa-us-ping.vultr.com,  0.4%,  183.79,  38.19, ..................20]
        sjo-ca-us-ping.vultr.com,  0.7%,  200.32,  32.20, ...................21]
        lax-ca-us-ping.vultr.com,  0.5%,  196.68,  39.36, ....................22]
                    www.bing.com,  2.2%,  101.86,  23.76, .......................25]
           fra-de-ping.vultr.com,  0.3%,  302.49,  46.00, .........................27]
           par-fr-ping.vultr.com,  0.4%,  300.88,  43.94, .........................27]
           hnd-jp-ping.vultr.com,  2.8%,  113.55,  23.62, ...........................29]
            il-us-ping.vultr.com,  0.8%,  259.62,  50.83, ............................30]
            fl-us-ping.vultr.com,  0.9%,  314.02,  43.82, ............................30]
 speedtest-ams1.digitalocean.com,  0.7%,  380.15,  45.29, ..............................32]
            ga-us-ping.vultr.com,  1.3%,  254.32,  50.66, ...............................33]
           ams-nl-ping.vultr.com,  0.9%,  352.69,  47.50, ...............................33]
            tx-us-ping.vultr.com,  1.4%,  320.91,  48.17, ..................................36]
           syd-au-ping.vultr.com,  1.8%,  267.23,  49.46, ..................................36]
 speedtest-ams3.digitalocean.com,  1.0%,  404.54,  49.01, ...................................37]
 speedtest-ams2.digitalocean.com,  1.3%,  394.39,  46.45, ...................................37]
 speedtest-sgp1.digitalocean.com,  3.2%,  189.75,  33.13, ....................................38]
    speedtest.fremont.linode.com,  2.2%,  268.84,  51.42, .....................................39]
    speedtest.atlanta.linode.com,  2.2%,  330.81,  49.75, ........................................42]
     speedtest.dallas.linode.com,  3.9%,  279.52,  47.68, ................................................50]
           lon-gb-ping.vultr.com,  5.0%,  387.17,  49.08, .............................................................63]
 speedtest-nyc2.digitalocean.com,  6.1%,  326.61,  46.17, .................................................................67]
 speedtest-sfo1.digitalocean.com,  7.0%,  281.11,  40.97, ...................................................................69]
     speedtest.newark.linode.com,  6.5%,  334.33,  47.29, ...................................................................69]
 speedtest-nyc1.digitalocean.com,  7.4%,  346.15,  47.42, ..........................................................................76]
 speedtest-nyc3.digitalocean.com,  7.5%,  333.10,  57.91, ..............................................................................80]
     speedtest.london.linode.com,  9.0%,  458.54,  46.11, .........................................................................................91]
 speedtest-lon1.digitalocean.com, 19.9%,  382.57,  47.13, ..............................................................................................................................................................161]
            nj-us-ping.vultr.com, 20.9%,  281.61,  55.03, ...................................................................................................................................................................166]
```

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
1. UNIX base OS (Max & Linux) with python support
2. Apache with CGI support.

## Usage
1. clone the repository.
2. config the "sites.txt" file.
3. schedule the "multi-ping.sh" periodically.
4. copy the Python files to a directory can access by CGI.
5. create a soft link point to the ping test result folder.
5. Access "table" & "site" from web.

