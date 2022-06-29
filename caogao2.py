#coding=utf-8

import requests
import re
import time

def get_one_page(url):#请求函数：获取某一网页上的所有内容
    headers = {
    'User-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Host' :'s.weibo.com',
    'Accept' : '*/*',
    'Accept-Language' :'zh-CN,zh;q=0.9',
    'Accept-Encoding' :'gzip, deflate, br',
    'Cookie' :'ALF=1626318993; SUB=_2A25NzGvBDeRhGeFL41cS8y_Kwj-IHXVvT3WJrDV8PUJbkNAKLUrFkW1NfYOeJH-XEbz-B-8GzzNBMuDdi7enNNMh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whw9UFokL8wUz.gYx83ZCV-5JpX5oz75NHD95QNSKnfe0epSo.0Ws4DqcjZHs8EdfvbqgpjM7tt; _s_tentry=weibo.cn; Apache=4541806496073.1045.1623760877113; UOR=weibo.cn,s.weibo.com,weibo.cn; SINAGLOBAL=4541806496073.1045.1623760877113; ULV=1623760877129:1:1:1:4541806496073.1045.1623760877113:; WBStorage=8daec78e6a891122|undefined',
    'DNT' :'1',
    'Connection' :'keep-alive'
     }#请求头的书写，包括User-agent,Cookie等
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url,headers = headers,verify=False)#利用requests.get命令获取网页html
    if response.status_code == 200:#状态为200即为爬取成功
        return response.text#返回值为html文档，传入到解析函数当中
    return None
    # reps = requests.get(url=url)
    # reps.content.decode("utf-8")
def parse_one_page(html):#解析html并存入到文档result.txt中
    pattern = re.compile('<span class="ctt">.*?</span>', re.S)
    items = re.findall(pattern,html)
    result = str(items)
    with open('test.txt','a',encoding='utf-8') as fp:
        fp.write(result)

for i in range(284):
    url="https://s.weibo.com/Ajax_Comment/small?act=list&mid=4643703546970359&uid=7585331693&smartFlag=false&smartCardComment=&isMain=true&suda-data=key%253Dtblog_search_weibo%2526value%253Dweibo_h_1_p_p&pageid=weibo&_t=0&__rnd=1623804901153"+str(i)
    html = get_one_page(url)
    print(html)
    print('正在爬取第 %d 页评论' % (i+1))
    parse_one_page(html)
    time.sleep(3)



# 预处理
content = '''
[][][]['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">好自私的回答，小孩出生就是要为你养老和干活。</span>', '<span class="ctt">你倒是去采访年轻的育龄女性啊</span>', '<span class="ctt">一个小时的反对声音里剪出来一分钟的同意，辛苦了<img alt="[作揖]" src="//h5.sinaimg.cn/m/emoticon/icon/others/h_zuoyi-519f80d31c.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">回复<a href="/n/%E9%9F%AD%E8%8F%9C%E4%BD%95%E5%AD%905271">@韭菜何子5271</a>:他要是敢出个结婚冷静期，估计都没多少人结婚了</span>', '<span class="ctt">没有人管狗生几只，人就要</span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">好自私的回答，小孩出生就是要为你养老和干活。</span>', '<span class="ctt">你倒是去采访年轻的育龄女性啊</span>', '<span class="ctt">一个小时的反对声音里剪出来一分钟的同意，辛苦了<img alt="[作揖]" src="//h5.sinaimg.cn/m/emoticon/icon/others/h_zuoyi-519f80d31c.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">回复<a href="/n/%E9%9F%AD%E8%8F%9C%E4%BD%95%E5%AD%905271">@韭菜何子5271</a>:他要是敢出个结婚冷静期，估计都没多少人结婚了</span>', '<span class="ctt">没有人管狗生几只，人就要</span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">好自私的回答，小孩出生就是要为你养老和干活。</span>', '<span class="ctt">你倒是去采访年轻的育龄女性啊</span>', '<span class="ctt">一个小时的反对声音里剪出来一分钟的同意，辛苦了<img alt="[作揖]" src="//h5.sinaimg.cn/m/emoticon/icon/others/h_zuoyi-519f80d31c.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">回复<a href="/n/%E9%9F%AD%E8%8F%9C%E4%BD%95%E5%AD%905271">@韭菜何子5271</a>:他要是敢出个结婚冷静期，估计都没多少人结婚了</span>', '<span class="ctt">没有人管狗生几只，人就要</span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">好自私的回答，小孩出生就是要为你养老和干活。</span>', '<span class="ctt">你倒是去采访年轻的育龄女性啊</span>', '<span class="ctt">一个小时的反对声音里剪出来一分钟的同意，辛苦了<img alt="[作揖]" src="//h5.sinaimg.cn/m/emoticon/icon/others/h_zuoyi-519f80d31c.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">回复<a href="/n/%E9%9F%AD%E8%8F%9C%E4%BD%95%E5%AD%905271">@韭菜何子5271</a>:他要是敢出个结婚冷静期，估计都没多少人结婚了</span>', '<span class="ctt">没有人管狗生几只，人就要</span>', '<span class="ctt">贷款生娃，支持祖国！</span>', '<span class="ctt">未看到是一个政策,只看到是一个可选项.只是生了不罚你钱而已, 没有务实地去支持...(当笑话看看就算了)</span>', '<span class="ctt">回复<a href="/n/%E6%88%91%E7%9A%84%E5%90%8D%E5%AD%97%E5%8F%AB%E5%A4%A7%E8%80%B3%E6%9C%B5">@我的名字叫大耳朵</a>:你果然是个男的</span>', '<span class="ctt">河南确实是生育大省，其实还不如取消计划生育，只是从政策和资金上鼓励生育就完事儿了，什么三孩不三孩的，有能力 有意愿的就多生，没能力 没意愿的就少生，生育本来就是顺其自然的事儿，非要计划，违背人伦和自然规律，最后达不到目的，得不偿失。</span>', '<span class="ctt">说点实话 不能说实话的时候尽量别说话</span>', '<span class="ctt">当初计生只生一个好的时候他们也是支持的<img alt="[费解]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_feijie-c1df37ef03.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">好自私的回答，小孩出生就是要为你养老和干活。</span>', '<span class="ctt">你倒是去采访年轻的育龄女性啊</span>', '<span class="ctt">一个小时的反对声音里剪出来一分钟的同意，辛苦了<img alt="[作揖]" src="//h5.sinaimg.cn/m/emoticon/icon/others/h_zuoyi-519f80d31c.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">回复<a href="/n/%E9%9F%AD%E8%8F%9C%E4%BD%95%E5%AD%905271">@韭菜何子5271</a>:他要是敢出个结婚冷静期，估计都没多少人结婚了</span>', '<span class="ctt">没有人管狗生几只，人就要</span>', '<span class="ctt">贷款生娃，支持祖国！</span>', '<span class="ctt">未看到是一个政策,只看到是一个可选项.只是生了不罚你钱而已, 没有务实地去支持...(当笑话看看就算了)</span>', '<span class="ctt">回复<a href="/n/%E6%88%91%E7%9A%84%E5%90%8D%E5%AD%97%E5%8F%AB%E5%A4%A7%E8%80%B3%E6%9C%B5">@我的名字叫大耳朵</a>:你果然是个男的</span>', '<span class="ctt">河南确实是生育大省，其实还不如取消计划生育，只是从政策和资金上鼓励生育就完事儿了，什么三孩不三孩的，有能力 有意愿的就多生，没能力 没意愿的就少生，生育本来就是顺其自然的事儿，非要计划，违背人伦和自然规律，最后达不到目的，得不偿失。</span>', '<span class="ctt">说点实话 不能说实话的时候尽量别说话</span>', '<span class="ctt">当初计生只生一个好的时候他们也是支持的<img alt="[费解]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_feijie-c1df37ef03.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">好自私的回答，小孩出生就是要为你养老和干活。</span>', '<span class="ctt">你倒是去采访年轻的育龄女性啊</span>', '<span class="ctt">一个小时的反对声音里剪出来一分钟的同意，辛苦了<img alt="[作揖]" src="//h5.sinaimg.cn/m/emoticon/icon/others/h_zuoyi-519f80d31c.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">回复<a href="/n/%E9%9F%AD%E8%8F%9C%E4%BD%95%E5%AD%905271">@韭菜何子5271</a>:他要是敢出个结婚冷静期，估计都没多少人结婚了</span>', '<span class="ctt">没有人管狗生几只，人就要</span>', '<span class="ctt">贷款生娃，支持祖国！</span>', '<span class="ctt">未看到是一个政策,只看到是一个可选项.只是生了不罚你钱而已, 没有务实地去支持...(当笑话看看就算了)</span>', '<span class="ctt">回复<a href="/n/%E6%88%91%E7%9A%84%E5%90%8D%E5%AD%97%E5%8F%AB%E5%A4%A7%E8%80%B3%E6%9C%B5">@我的名字叫大耳朵</a>:你果然是个男的</span>', '<span class="ctt">河南确实是生育大省，其实还不如取消计划生育，只是从政策和资金上鼓励生育就完事儿了，什么三孩不三孩的，有能力 有意愿的就多生，没能力 没意愿的就少生，生育本来就是顺其自然的事儿，非要计划，违背人伦和自然规律，最后达不到目的，得不偿失。</span>', '<span class="ctt">说点实话 不能说实话的时候尽量别说话</span>', '<span class="ctt">当初计生只生一个好的时候他们也是支持的<img alt="[费解]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_feijie-c1df37ef03.png" style="width:1em; height:1em;" /></span>'][][][][][][][][][][][][][][][][][][]['<span class="ctt">以前的人就是为了多生孩子防老，就算孩子都饿着也要生，还有为了跳出局限的生活，每多生个孩子就多一分希望。当时消息不发达，能吃苦就能成功。</span>', '<span class="ctt">采访老年人？？？？生个足球队要不要呀？主持人生三孩嘛<img alt="[二哈]" src="//h5.sinaimg.cn/m/emoticon/icon/others/d_erha-139d0e07bd.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">前两个都是男人，男人又不管带孩子，有本事让他们自己生自己带。生孩子又不是为了给自己生养个老来照顾你，伺候你的保姆。真是可笑！</span>', '<span class="ctt">笑了</span>', '<span class="ctt">...采访的都是不能生的，那不管人家事儿没牵扯到人家的利益肯定无所谓啊</span>', '<span class="ctt">生下来在河南等着上各种师范和职业学校吗，真是逗</span>', '<span class="ctt">当人都是傻子了 你播啥我信啥</span>', '<span class="ctt">少生优生幸福一生</span>']['<span class="ctt">回复<a href="/n/%E5%96%80%E6%8B%89%E6%8B%89110">@喀拉拉110</a>:养老不会买社保？人是不可控的，他以后想对你好是他的事，不想理你想破头都没用。</span>', '<span class="ctt">你采访的是育龄女性吗？你的新闻也太没意义了吧</span>', '<span class="ctt">不支持的都不播</span>', '<span class="ctt">你让那些人生，看看能生出来多少，你采访的是育龄期的女性吗？调查具有实际意义吗？</span>', '<span class="ctt">受访者都身价千万吧呵呵哒</span>', '<span class="ctt">回复<a href="/n/%E8%BF%9F%E9%92%9D%E7%9A%84%E9%A5%BA%E5%AD%90">@迟钝的饺子</a>:不然呢？本质就是养老</span>', '<span class="ctt">不生不生 即要日常带孩子 还要上班工作 又有家务缠身 说破天 我也不会要三胎</span>']['<span class="ctt">我真的有头牛啊</span>', '<span class="ctt">回复<a href="/n/%E5%B0%A4%E6%A9%98%E5%AD%90">@尤橘子</a>:没钱 男的带也不行呀<img alt="[允悲]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_yunbei-a14a649db8.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">都离婚冷静期了，为什么不出个生育冷静期呢？？？</span>', '<span class="ctt">能养得起吗？</span>', '<span class="ctt">这是演员？</span>', '<span class="ctt">小编，小编，你真能！给你几个鸡腿子</span>', '<span class="ctt">你能，你说的都对</span>', '<span class="ctt">生孩子就是为了自己老有所养？估计这么想的人老了肯定也不会太好</span>', '<span class="ctt">应该去民企采访适龄的人</span>', '<span class="ctt">溜须</span>']['<span class="ctt">一个小时的反对声音里剪出来一分钟的同意，辛苦了<img alt="[作揖]" src="//h5.sinaimg.cn/m/emoticon/icon/others/h_zuoyi-519f80d31c.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">都是为了响应政府号召，电视台的本职工作而已</span>', '<span class="ctt">谁爱生谁生。生出来被割韭菜？</span>', '<span class="ctt">又来黑我大河南</span>', '<span class="ctt">这是什么阴间话题……</span>', '<span class="ctt">好自私的回答，小孩出生就是要为你养老和干活。</span>', '<span class="ctt">你倒是去采访年轻的育龄女性啊</span>', '<span class="ctt">呃呃 觉悟真高</span>', '<span class="ctt">采访男士是？男的生男的带，我也觉得生三个没问题</span>']['<span class="ctt">如果人的出生可以选择，看看还有没有人愿意为了干活为了伺候老人选择降生。如果还能选择家庭，估计有这种自私想法的人连孩子都莫得</span>', '<span class="ctt">这采访 一个育龄妇女都不访？ 是这俩帅哥生呢？还是这大妈生？</span>', '<span class="ctt">对着镜头说好话谁不会呢<img alt="[doge]" src="//h5.sinaimg.cn/m/emoticon/icon/others/d_doge-be7f768d78.png" style="width:1em; height:1em;" /></span>', '<span class="ctt">啥d</span>', '<span class="ctt">让他们生五个试试，电视说好听的谁都会说。</span>', '<span class="ctt">？</span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>']['<span class="ctt">:【<a href="https://weibo.cn/pages/100808topic?extparam=%E9%83%91%E5%B7%9E%E8%A1%97%E5%A4%B4%E5%B8%82%E6%B0%91%E6%94%AF%E6%8C%81%E4%B8%89%E5%AD%A9%E7%94%9F%E8%82%B2%E6%94%BF%E7%AD%96&amp;from=feed">#郑州街头市民支持三孩生育政策#</a>：人多好干活，好养老！<img alt="[思考]" src="//h5.sinaimg.cn/m/emoticon/icon/default/d_sikao-ff9602dd08.png" style="width:1em; height:1em;" /></span>'][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
'''
rawResults = re.findall(">.*?<",content,re.S)
firstStepResults  = []
for result in rawResults:
    #print(result)
    if ">\'][\'<"  in result:
        continue
    if ">:<"  in result:
        continue
    if ">回复<"  in result:
        continue
    if "><"  in result:
        continue
    if ">\', \'<"  in result:
        continue
    if "@"  in result:
        continue
    if "> <"  in result:
        continue
    if "#郑州街头市民支持三孩生育政策#" in result:
        continue
    if  "【" in result:
        continue
    if ":" in result:
        continue
    if "[]"  in result:
        continue
    else:
        firstStepResults.append(result)
subTextHead = re.compile(">")
subTextFoot = re.compile("<")
i = 6593
f=open("C:/Users/86132/.PyCharmCE2019.3/config/scratches/rgresult.txt",'a',encoding='gbk')
for lastResult in firstStepResults:
    resultExcel1 = re.sub(subTextHead, '', lastResult)
    resultExcel = re.sub(subTextFoot, '', resultExcel1)
    print(i,resultExcel)
    # wf = f.write(resultExcel)
    i+=1
# 词云图绘制
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
excludes=["什么","一个","我们","那","你们","如今","说道","知道","起来","这","他","你","我","是",
          "众人","只见","怎么","的","两个","没有","不是","不知","这个","和","了"]
txtfilepath="C:/Users/86132/.PyCharmCE2019.3/config/scratches/rgresult.txt"
# mask1=np.array(open("D:/24/可/杂/1.jpg"))
with open(txtfilepath,encoding='gbk') as f:
    txt= f.read()
    words = jieba.cut(txt)
newtxt = ' '.join(words)
wc = WordCloud(background_color="white",width=800,height=600,font_path="msyh.ttc",max_words=100,
               max_font_size=80,stopwords = excludes,)#mask=mask1
wc.generate(newtxt)
plt.imshow(wc)
plt.show()
