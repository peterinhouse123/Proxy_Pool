# -*- coding: UTF-8 -*-
from pyquery import PyQuery as pq
from Module import  net_fn
import json

class Google:
    def __init__(self):
        self.Net = net_fn.Net()

    def Search_Page(self,keyword,page_num):
        url = "https://www.google.com.tw/search?q={}&start={}".format(keyword,page_num*10)
        rs = self.Net.Get(url)
        data = rs.content.decode(errors='ignore')

        a_list = pq(data).find('.r a')


        end = []
        for a_item in a_list:
            rs_link = pq(a_item).attr('href')
            rs_link = self.Net.preg_get_word("\?q=(.+)&sa=",1,rs_link)
            if rs_link == "empty_data":
                continue
            end.append(rs_link)

        return end

    def Search(self,keyword,max_page_num):
        end = []

        for n in range(max_page_num):
            page_rs = self.Search_Page(keyword=keyword,page_num=n)
            for link in page_rs:
                end.append(link)

        return end



if __name__ == "__main__":
    obj = Google()
    #模擬測試
    rs = obj.Search(keyword="47.90.63.202 filetype:txt",max_page_num=10)
    print(rs)


    #proxy_list_google _result
    #['https://webanetlabs.net/freeproxylist/proxylist_at_03.01.2017.txt', 'https://webanetlabs.net/freeproxylist/proxylist_at_09.01.2017.txt', 'http://01717.ir/wp-content/uploads/2017/06/Proxy.txt', 'https://www.paighambot.com/wp-content/uploads/2016/11/proxies-15.txt', 'http://rebbis.ysmz.org/awstats/data/awstats112016.rebbis.ysmz.org.txt', 'https://github.com/yrjyrj123/MobikeAgent/blob/master/proxies.txt', 'https://sblam.com/blacklist.txt', 'http://www.simpleproxy.ru/core/1b0bf30d851b94bcd94738acdda8578e.txt', 'https://a.pomf.cat/yqbwjb.txt', 'http://stlblackmba.org/awstats/data/awstats072017.stlblackmba.org.txt', 'http://blog.chopperguy.net/awstats/data/awstats062017.blog.chopperguy.net.txt', 'http://umweltnetz.ch/awstats/data/awstats072017.umweltnetz.ch.txt', 'http://www.nptccd.health.gov.lk/uploaded/documents/tumdizin/omniapps/nptccdhealthgov/uploaded/sly.txt', 'https://www.freepublicproxylist.com/lists/6252018.txt', 'https://www.freepublicproxylist.com/lists/6242018.txt', 'https://www.freepublicproxylist.com/lists/6152018.txt', 'https://www.freepublicproxylist.com/lists/6182018.txt', 'http://h4.tgkanal.com/2018/06/28/465/5017175362606465075.txt', 'http://kishabajuku.si/awstats/data/awstats052017.kishabajuku.si.txt', 'http://kishabajuku.si/awstats/data/awstats102017.kishabajuku.si.txt', 'http://dev.bayareacasting.com/awstats/data/awstats122016.dev.bayareacasting.com.txt', 'http://williams.ie/awstats/data//awstats042018.williams.ie.txt', 'http://lafalaise-villeneuve.ch/awstats/data/awstats112016.lafalaise-villeneuve.ch.txt', 'http://www.mapwaves.org/awstats/data/awstats072017.mapwaveanalysis.com.txt', 'http://www.robinsdesk.com/awstats/data/awstats112016.shortsaleslist.com.txt', 'http://parkplaceboulder.com/awstats/data/awstats042018.parkplaceboulder.com.txt', 'http://www.amerossimplants.com/awstats/data/awstats042018.amerossimplants.com.txt', 'http://mpcreativedev.com/awstats/data/awstats042018.mpcreativedev.com.txt', 'http://technomine.ru/adept.txt', 'http://nice-hack.gid.pw/Forums/proxy.txt', 'http://www.austin-seafood.com/awstats/data/awstats112016.austin-seafood.com.txt', 'http://www.itzixue.com/%25E6%2596%25B0%25E5%25BB%25BA%25E6%2596%2587%25E6%259C%25AC%25E6%2596%2587%25E6%25A1%25A3.txt', 'http://ilaborator.ro/awstats/data/awstats052017.ilaborator.ro.txt', 'http://www.titanfighter.com/awstats/data/awstats042018.titanfighter.com.txt', 'http://www.n-souken.co.jp/cgis/awstats/stats/awstats022017.txt', 'http://montgomerymag.com/awstats/data/awstats042017.montgomerymag.com.txt', 'https://bridhaven.ie/awstats/data/awstats022017.bridhaven.ie.txt', 'http://www.auladecroly.com/awstats/data/awstats122016.auladecroly.com.txt', 'https://cdn-06.anonfile.com/laPcgff2b5/3d8ba46e-1532417546/92_899x_Elite_HQ_Mixed_Proxies_03-07-2018_._Nadal.txt', 'http://www.jagpartners.com.au/awstats/data/awstats022017.jagpartners.com.au.txt', 'http://burchellconsultinglimited.co.uk/awstats/data/awstats122016.burchellconsultinglimited.co.uk.txt', 'http://blog.casinofew.com/awstats/data/awstats012017.icelay.com.txt', 'http://hnpackages.com/awstats/data/awstats112016.hnpackages.com.txt', 'https://raw.githubusercontent.com/stamparm/aux/master/fetch-some-list.txt', 'https://alaska-travel.net/awstats/data/awstats022017.alaska-travel.net.txt', 'http://www.picom.com.au/awstats/awstats042018.dtc.txt', 'http://www.albihome-apparthotel.fr/stats/awstats122016.www.albihome-apparthotel.fr.txt', 'http://blog.redmagiccasino.com/awstats/data/awstats112016.cashcasino.biz.txt', 'http://www.engagemedia.com.mx/awstats/data/awstats072017.engagemedia.com.mx.txt', 'http://patagonia-road.com/awstats/data//awstats042018.patagonia-road.com.txt', 'http://dobrist.ch/awstats/data/awstats062018.dobrist.ch.txt', 'http://hospitalexport.com/userfiles/mahan.txt', 'http://inspekt-rgh.com.ba/awstats/data/awstats102017.inspekt-rgh.com.ba.txt', 'https://www.che.upd.edu.ph/film/awstats/awstats062018.www.filminstitute.upd.edu.ph.txt', 'http://betcasino.biz/awstats/data/awstats042017.betcasino.biz.txt', 'https://proxyscra.pe/proxies/HTTPProxies.txt', 'http://www.nightsquad.eu/proxy.txt', 'http://www.zimmob.ch/awstats/data/awstats042018.zimmob.ch.txt', 'https://www.modaizle.com/wp-content/uploads/2017-proxy-listesi.txt', 'https://malwareworld.com/textlists/suspiciousIPs.txt', 'http://chevyworldparts.com/awstats/data/awstats122016.chevyworldparts.com.txt', 'http://redbingo.org/awstats/data/awstats112016.redbingo.org.txt', 'http://teste.teclavirtual.pt/awstats/data/awstats072017.teste.teclavirtual.pt.txt', 'http://www.medinachemist.com/stats/awstats/mklettingsnottingham.com/awstats062018.txt', 'http://elektroline.ch/awstats/data/awstats012017.elektroline.ch.txt', 'http://www.ecatalogues.net/ecatalog/tmp/awstats/awstats062018.ecatalogues.net.txt', 'http://pestybest.info/z.txt', 'http://ox.users.superford.org/awstats/data/awstats112016.ox.users.superford.org.txt', 'http://www.cokme.com.ua/awstats/data/awstats012017.cokme.com.ua.txt', 'http://www.nhhillclimbchallenge.com/awstats/data/awstats062018.nhhillclimbchallenge.com.txt', 'http://www.youtubebot.org/updaterNfo/socks.txt', 'http://dhcook.net/awstats/data/awstats112016.dhcook.net.txt', 'http://www.barretts-oesophagus.co.uk/awstats/data/awstats042017.barretts-oesophagus.co.uk.txt', 'empty_data', 'http://mostreka383.website/StolenCombos/New%2520Text%2520Document.txt', 'http://forum.layposters.com/awstats/data/awstats072017.casinofit.com.txt', 'https://prodigyy.host/u/9sfk.txt', 'https://softwarenova.net/proxy.txt', 'http://www.o2ss.fr/Mauritania.txt/home/web/h0lg4.org/logs/awstats122016.h0lg4.org.txt', 'http://www.o2ss.fr/Mauritania.txt/home/web/h0lg4.org/logs/awstats042017.h0lg4.org.txt', 'http://new.acmm.ie/awstats/data/awstats012017.new.acmm.ie.txt']
