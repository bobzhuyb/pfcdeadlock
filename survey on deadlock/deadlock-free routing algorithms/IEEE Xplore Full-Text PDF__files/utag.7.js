//tealium universal tag - utag.7 ut4.0.201612191506, Copyright 2016 Tealium.com Inc. All Rights Reserved.
try{(function(id,loader){var u={};utag.o[loader].sender[id]=u;if(utag.ut===undefined){utag.ut={};}if(utag.ut.loader===undefined){u.loader=function(o){var a,b,c,l;a=document;if(o.type==="iframe"){b=a.createElement("iframe");b.setAttribute("height","1");b.setAttribute("width","1");b.setAttribute("style","display:none");b.setAttribute("src",o.src);}else if(o.type==="img"){utag.DB("Attach img: "+o.src);b=new Image();b.src=o.src;return;}else{b=a.createElement("script");b.language="javascript";b.type="text/javascript";b.async=1;b.src=o.src;}if(o.id){b.id=o.id;}if(typeof o.cb==="function"){b.hFlag=0;b.onreadystatechange=function(){if((this.readyState==='complete'||this.readyState==='loaded')&&!b.hFlag){b.hFlag=1;o.cb();}};b.onload=function(){if(!b.hFlag){b.hFlag=1;o.cb();}};}l=o.loc||"head";c=a.getElementsByTagName(l)[0];if(c){utag.DB("Attach to "+l+": "+o.src);if(l==="script"){c.parentNode.insertBefore(b,c);}else{c.appendChild(b);}}};}else{u.loader=utag.ut.loader;}
u.ev={'view':1,'link':1};u.initialized=false;u.scriptrequested=false;u.queue=[];u.event_lookup={"pageview":"1","registration":"2","order":"3","purchase":"3","shopaction9":"3","cart":"4","shopaction5":"4","productview":"5","prodview":"5","conversionevent":"14","conversion":"14","element":"15"};u.concat_attr=function(a,e,c,d,f,g){g="";for(f=1;f<=c;f++){if(typeof d!="undefined"&&u.data[e+a+f+""]instanceof Array){g+=((typeof u.data[e+a+f+""][d]!="undefined")?u.data[e+a+f+""][d]:"")+"-_-"}else{g+=((typeof u.data[e+a+f+""]!="undefined")?u.data[e+a+f+""]:"")+"-_-"}}
return g};u.map={"ibm_client_id":"ClientID","sheet_name":"PageviewTag_pi","sheet_type":"PageviewTag_cg","search_keyword":"PageviewTag_se","search_results_count":"PageviewTag_sr","user_id":"PageviewTag_pv_a1","user_institution_id":"PageviewTag_pv_a2","user_type":"PageviewTag_pv_a3","user_product":"PageviewTag_pv_a4","user_third_party":"PageviewTag_pv_a5","document_id":"PageviewTag_pv_a6","document_pub_id":"PageviewTag_pv_a7","browse_content_type":"PageviewTag_pv_a8","browse_topic":"PageviewTag_pv_a9","course_category_name":"PageviewTag_pv_a10","course_sub_category":"PageviewTag_pv_a11","publisher":"PageviewTag_pv_a12","search_search_within":"PageviewTag_pv_a13","search_type":"PageviewTag_pv_a14","link_name":"ConversionEventTag_cid","user_grantingID":"PageviewTag_pv_a15","content_type":"PageviewTag_pv_a16","book_chapter":"PageviewTag_pv_a17","book_number":"PageviewTag_pv_a18","course_number":"PageviewTag_pv_a19","denial":"PageviewTag_pv_a21","link_category":"ConversionEventTag_ccid","conversion_event":"ConversionEventTag_cid","registerID":"RegistrationTag_cd","unique_registerID":"RegistrationTag_rg1","link_action":"ConversionEventTag_cat","ibm_event:registration":"Registration","ibm_event:video":"Element","ibm_event:concurrency":"Element,Element","html_usage":"PageviewTag_pv_a41","video_name":"ElementTag_eid","video_category":"ElementTag_ecat","video_position":"ElementTag_e_a14","video_duration":"ElementTag_e_a15","video_status":"ElementTag_e_a13","ibm_cookie_domain":"CookieDomain","element_id":"ElementTag_eid","element_category":"ElementTag_ecat"};u.extend=[function(a,b){if(utag_data.document_isAbstract){b.html_usage='AB'}},function(a,b){if(utag_data.document_isDHTML==true){if(getCookie('HTML_DocIDs')==null){utag_data.HTMLUsage=[];utag_data.HTMLUsage.push(utag_data.document_id);utag_data.HTMLUsage=JSON.stringify(utag_data.HTMLUsage);document.cookie="HTML_DocIDs="+utag_data.HTMLUsage+";path=/;domain="+window.location.hostname+";expires=";b.html_usage='HTML-AB';}
else if(JSON.parse(getCookie('HTML_DocIDs')).indexOf(utag_data.document_id)<0){var tempHTMLUsage=JSON.parse(getCookie('HTML_DocIDs')).replace(/\]|\[|"| /g,'').split(',');tempHTMLUsage.push(utag_data.document_id);tempHTMLUsage=JSON.stringify(tempHTMLUsage);document.cookie="HTML_DocIDs="+tempHTMLUsage+";path=/;domain="+window.location.hostname+";expires=";b.html_usage='HTML-AB';}}},function(a,b){if(utag_data.document_isHTML==true){if(getCookie('HTML_DocIDs')==null){utag_data.HTMLUsage=[];utag_data.HTMLUsage.push(utag_data.document_id);utag_data.HTMLUsage=JSON.stringify(utag_data.HTMLUsage);document.cookie="HTML_DocIDs="+utag_data.HTMLUsage+";path=/;domain="+window.location.hostname+";expires=";b.html_usage='HTML';}
else if(JSON.parse(getCookie('HTML_DocIDs')).indexOf(utag_data.document_id)<0){var tempHTMLUsage=JSON.parse(getCookie('HTML_DocIDs')).replace(/\]|\[|"| /g,'').split(',');tempHTMLUsage.push(utag_data.document_id);tempHTMLUsage=JSON.stringify(tempHTMLUsage);document.cookie="HTML_DocIDs="+tempHTMLUsage+";path=/;domain="+window.location.hostname+";expires=";b.html_usage='HTML';}}}];u.send=function(a,b){if(u.ev[a]||u.ev.all!==undefined){var c,d,e,f,g;u.data={"qsp_delim":"&","kvp_delim":"=","a":a,"base_url":"//libs.coremetrics.com/eluminate.js"||"//libs.coremetrics.com/eluminate.js","ClientID":"","TestClientID":"","DataCollectionMethod":true,"DataCollectionDomain":"data.coremetrics.com","CookieDomain":"ieeexplore.ieee.org","test_domains":",,","tid":{},"test":false,"pv_a":"","pv":"","s_a":"","sx":"","o_a":"","or":"","rg":"","pr_a":"","c_a":"","cx":"","e_a":"","product_id":[],"product_name":[],"product_category":[],"product_quantity":[],"product_unit_price":[]};for(c=0;c<u.extend.length;c++){try{d=u.extend[c](a,b);if(d==false)return}catch(e){}};c=[];for(d in utag.loader.GV(u.map)){if(b[d]!==undefined&&b[d]!==""){e=u.map[d].split(",");for(f=0;f<e.length;f++){if(e[f]==="tid"){g=u.event_lookup[(""+b[d]).toLowerCase().replace("_","")]+"";if(g!==""){u.data.tid[g]=true;}else{u.data.tid[b[d]]=true;}}else{u.data[e[f]]=b[d];}}}else{c=d.split(":");if(c.length===2&&b[c[0]]===c[1]){g=""+u.event_lookup[u.map[d].toLowerCase().replace("_","")];if(g!==""){u.data.tid[g]=true}}}}
u.data.order_id=u.data.order_id||b._corder||"";u.data.order_subtotal=u.data.order_subtotal||b._csubtotal||"";u.data.order_shipping=u.data.order_shipping||b._cship||"";u.data.order_currency=u.data.order_currency||b._ccurrency||"";u.data.customer_id=u.data.customer_id||b._ccustid||"";u.data.customer_city=u.data.customer_city||b._ccity||"";u.data.customer_state=u.data.customer_state||b._cstate||"";u.data.customer_zip=u.data.customer_zip||b._czip||"";u.data.customer_country=u.data.customer_country||b._ccountry||"";if(u.data.product_id.length===0&&b._cprod!==undefined){u.data.product_id=b._cprod.slice(0);}
if(u.data.product_name.length===0&&b._cprodname!==undefined){u.data.product_name=b._cprodname.slice(0);}
if(u.data.product_category.length===0&&b._ccat!==undefined){u.data.product_category=b._ccat.slice(0);}
if(u.data.product_quantity.length===0&&b._cquan!==undefined){u.data.product_quantity=b._cquan.slice(0);}
if(u.data.product_unit_price.length===0&&b._cprice!==undefined){u.data.product_unit_price=b._cprice.slice(0);}
u.loader_cb=function(b){u.initialized=true;if(u.data.test_domains.indexOf(","+location.hostname+',')>-1){u.data.test=true;}
if(u.data.test){u.data.ClientID=u.data.TestClientID;u.data.DataCollectionMethod=u.data.TestDataCollectionMethod||false;u.data.DataCollectionDomain=u.data.TestDataCollectionDomain||"testdata.coremetrics.com";}
if(u.data.ClientID){cmSetClientID(u.data.ClientID,u.data.DataCollectionMethod,u.data.DataCollectionDomain,u.data.CookieDomain);}
if(u.data.cmSetupOther&&window.cmSetupOther){window.cmSetupOther(u.data.cmSetupOther);}else if(u.data.cmSetupOther&&!window.cmSetupOther){utag.DB("cmSetupOther is not defined. This probably means the coreMetrics library has not initialized correctly.");}
if(u.data.a==="view"){e="PageviewTag_";u.data.pv_a=u.concat_attr("pv_a",e,50);u.data.pv=u.concat_attr("pv",e,15);if(u.data["ManualPageviewTag_ul"]){f="ManualPageviewTag_";cmCreateManualPageviewTag(u.data[e+"pi"],u.data[e+"cg"],u.data[f+"ul"],u.data[f+"rf"],u.data.pv_a,u.data[e+"se"],u.data[e+"sr"],u.data.pv);}else{cmCreatePageviewTag(u.data[e+"pi"],u.data[e+"cg"],u.data[e+"se"],u.data[e+"sr"],u.data.pv_a,u.data.pv);}}else if(u.data.a=="link"&&u.data["ManualLinkClickTag_hr"]){e="ManualLinkClickTag_";cmCreateManualLinkClickTag(u.data[e+"hr"],u.data[e+"nm"],u.data[e+"pi"]);u.data[e+"hr"]="";return;}
if(u.data["ManualImpressionTag_pi"]&&(u.data["ManualImpressionTag_cm_sp"]||u.data["ManualImpressionTag_cm_re"])){e="ManualImpressionTag_";cmStartTagSet();if(typeof u.data[e+"cm_re"]==="string"){u.data[e+"cm_re"]=u.data[e+"cm_re"].split(',');}
if(typeof u.data[e+"cm_sp"]==="string"){u.data[e+"cm_sp"]=u.data[e+"cm_sp"].split(',');}
if(u.data[e+"cm_re"]instanceof Array&&u.data[e+"cm_re"].length>0){for(f=0;f<u.data[e+"cm_re"].length;f++){var cm=new _cm("tid","9");cm.cm_re=u.data[e+"cm_re"][f];cm.pi=u.data[e+"pi"]||c1(cm.ci);cm.st=cm_ClientTS;cm.write(1);}}
if(u.data[e+"cm_sp"]instanceof Array&&u.data[e+"cm_sp"].length>0){for(f=0;f<u.data[e+"cm_sp"].length;f++){var cm=new _cm("tid","9");cm.cm_sp=u.data[e+"cm_sp"][f];cm.pi=u.data[e+"pi"]||c1(cm.ci);cm.st=cm_ClientTS;cm.write(1);}}
cmSendTagSet();u.data[e+"pi"]="";}
if(u.data.order_id||u.data["ShopAction9Tag_on"]){b._cevent="purchase";}
if(b._cevent==="purchase"){if(u.data.order_currency)cmSetupOther({"cm_currencyCode":u.data.order_currency});e="ShopAction9Tag_";u.data[e+"on"]=u.data[e+"on"]||u.data.order_id;u.data[e+"tr"]=u.data[e+"tr"]||u.data.order_subtotal;u.data[e+"cd"]=u.data[e+"cd"]||u.data.customer_id||utag.data["cp.utag_main_ses_id"];u.data[e+"pr"]=u.data[e+"pr"]||u.data.product_id;u.data[e+"pm"]=u.data[e+"pm"]||u.data.product_name;u.data[e+"qt"]=u.data[e+"qt"]||u.data.product_quantity;u.data[e+"bp"]=u.data[e+"bp"]||u.data.product_unit_price;u.data[e+"cg"]=u.data[e+"cg"]||u.data.product_category;for(f=0;f<u.data[e+"pr"].length;f++){u.data.s_a=u.concat_attr("s_a",e,50,f);u.data.sx=u.concat_attr("sx",e,15,f);cmCreateShopAction9Tag(u.data[e+"pr"][f],u.data[e+"pm"][f],u.data[e+"qt"][f],u.data[e+"bp"][f],u.data[e+"cd"],u.data[e+"on"],u.data[e+"tr"],u.data[e+"cg"][f],u.data.s_a,u.data.sx);}
cmDisplayShops();}
if(u.data.tid["3"]||b._cevent==="purchase"){e="OrderTag_";u.data[e+"on"]=u.data["ShopAction9Tag_on"]||u.data[e+"on"];u.data[e+"tr"]=u.data["ShopAction9Tag_tr"]||u.data[e+"tr"];u.data[e+"cd"]=u.data["ShopAction9Tag_cd"]||u.data[e+"cd"];u.data[e+"sg"]=u.data[e+"sg"]||u.data.order_shipping;u.data[e+"ct"]=u.data[e+"ct"]||u.data.customer_city;u.data[e+"sa"]=u.data[e+"sa"]||u.data.customer_state;u.data[e+"zp"]=u.data[e+"zp"]||u.data.customer_zip;u.data.o_a=u.concat_attr("o_a",e,50);u.data.or=u.concat_attr("or",e,15);cmCreateOrderTag(u.data[e+"on"],u.data[e+"tr"],u.data[e+"sg"],u.data[e+"cd"],u.data[e+"ct"],u.data[e+"sa"],u.data[e+"zp"],u.data.o_a,u.data.or);}
if(u.data.tid["2"]||b._cevent==="register"||(u.data["RegistrationTag_em"]&&b._cevent==="purchase")){e="RegistrationTag_";u.data[e+"cd"]=u.data["ShopAction9Tag_cd"]||u.data[e+"cd"]||u.data.customer_id||utag.data["cp.utag_main_ses_id"];u.data[e+"ct"]=u.data[e+"ct"]||u.data.customer_city;u.data[e+"sa"]=u.data[e+"sa"]||u.data.customer_state;u.data[e+"zp"]=u.data[e+"zp"]||u.data.customer_zip;u.data[e+"cy"]=u.data[e+"cy"]||u.data.customer_country;u.data.rg=u.concat_attr("rg",e,50);cmCreateRegistrationTag(u.data[e+"cd"],u.data[e+"em"],u.data[e+"ct"],u.data[e+"sa"],u.data[e+"zp"],u.data[e+"cy"],u.data.rg);}
if((u.data.tid["4"]&&b._cevent!="purchase")||b._cevent==="cartview"){if(u.data.order_currency)cmSetupOther({"cm_currencyCode":u.data.order_currency});e="ShopAction5Tag_";u.data[e+"pr"]=u.data[e+"pr"]||u.data.product_id;u.data[e+"pm"]=u.data[e+"pm"]||u.data.product_name;u.data[e+"qt"]=u.data[e+"qt"]||u.data.product_quantity;u.data[e+"bp"]=u.data[e+"bp"]||u.data.product_unit_price;u.data[e+"cg"]=u.data[e+"cg"]||u.data.product_category;for(f=0;f<u.data[e+"pr"].length;f++){u.data.s_a=u.concat_attr("s_a",e,50,f);u.data.sx=u.concat_attr("sx",e,15,f);cmCreateShopAction5Tag(u.data[e+"pr"][f],u.data[e+"pm"][f],u.data[e+"qt"][f],u.data[e+"bp"][f],u.data[e+"cg"][f],u.data.s_a,u.data.sx);}
cmDisplayShops();}
if((u.data.tid["5"]&&b._cevent!="purchase")||b._cevent==="prodview"){e="ProductviewTag_";u.data[e+"pr"]=u.data[e+"pr"]||u.data.product_id;u.data[e+"pm"]=u.data[e+"pm"]||u.data.product_name;u.data[e+"cg"]=u.data[e+"cg"]||u.data.product_category;u.data.pr_a=u.concat_attr("pr_a",e,50);if(u.data[e+"pr"]instanceof Array&&u.data[e+"pr"].length>1){for(f=0;f<u.data[e+"pr"].length;f++){u.data.pr_a=u.concat_attr("pr_a",e,50,f);cmCreateProductviewTag(u.data[e+"pr"][f],u.data[e+"pm"][f],u.data[e+"cg"][f],u.data.pr_a);}}else{cmCreateProductviewTag(u.data[e+"pr"]+'',u.data[e+"pm"]+'',u.data[e+"cg"]+'',u.data.pr_a,u.data[e+"cm_vc"]);}}
if(u.data.tid["14"]||u.data["ConversionEventTag_cid"]||b._cevent==="conversion"){e="ConversionEventTag_";u.data[e+"cid"]=u.data[e+"cid"]||"conversion";u.data[e+"cat"]=u.data[e+"cat"]||"2";u.data.c_a=u.concat_attr("c_a",e,50);u.data.cx=u.concat_attr("cx",e,5);cmCreateConversionEventTag(u.data[e+"cid"],u.data[e+"cat"],u.data[e+"ccid"],u.data[e+"cpt"],u.data.c_a,u.data.cx);u.data[e+"cid"]="";}
if(u.data.tid["15"]||u.data["ElementTag_eid"]){e="ElementTag_";u.data.e_a=u.concat_attr("e_a",e,50);cmCreateElementTag(u.data[e+"eid"],u.data[e+"ecat"],u.data.e_a);u.data[e+"eid"]="";}};u.callBack=function(){var data={};while(data=u.queue.shift()){u.data=data.data;u.loader_cb(data.b);}};if(u.initialized){u.loader_cb(b);}else{u.queue.push({"data":u.data,"b":b});if(!u.scriptrequested){u.scriptrequested=true;u.loader({"type":"script","src":u.data.base_url,"cb":u.callBack,"loc":"script","id":'tealium_cormetrics7'});}}
}};utag.o[loader].loader.LOAD(id);}('7','ieeexplore.main'));}catch(error){utag.DB(error);}
