a=input('Какой уровень сейчас или сколько опыта у вас имеется? ')
b=input('Какой уровень хотите? ')
x={'1':900,'2':2150,'3':3700,'4':5550,'5':7750,'6':10350,'7':13350,
   '8':16850,'9':20850,'10':25450,'11':30051,'12':34662,'13':39299,
   '14':43986,'15':48757,'16':53652,'17':58720,'18':64019,'19':69614,
   '20':75579,'21':81996,'22':88955,'23':96555,'24':104902,'25':114110,
   '26':124303,'27':135611,'28':148174,'29':162139,'30':177662,'31':194907,
   '32':214046,'33':235259,'34':258735,'35':284670,'36':313269,'37':344745,
   '38':379319,'39':417221,'40':458688,'41':503966,'42':553308,'43':606978,
   '44':665245,'45':729388,'46':796694,'47':870457,'48':949981,'49':1035577,
   '50':1127565,'51':1226272,'52':1332034,'53':1445195,'54':1566108,
   '55':1695133,'56':1832639,'57':1979002,'58':2134608,'59':2299850,
   '60':2475123,'61':2660855,'62':2857446,'63':3065327,'64':3284933,
   '65':3516707,'66':3761099,'67':4018567,'68':4289579,'69':4574610,
   '70':4874143,'71':5188670,'72':5518691,'73':5864713,'74':6227253,
   '75':6606835,'76':7003991,'77':7419262,'78':7853198,'79':8306355,
   '80':8779298,'81':9786846,'82':10322622,'83':10322622,'84':10880528,
   '85':11461170,'86':12065162,'87':12693127,'88':13345696,'89':14023507,
   '90':14727208,'91':15457455,'92':16214911,'93':1700247,'94':17814144,
   '95':18657290,'96':19530381,'97':20434122,'98':21369226,'99':22336413,
   '100':23336413}
if int(a)>100:
    print (x[b]-int(a))
else:
    print(x[b]-x[a]) 
k=input("press close to exit") 
