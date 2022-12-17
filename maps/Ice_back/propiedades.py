import Sparks
import Torchs
import Breakings
import Bladex

############
#####REJAS#####
########




#######################
#####ANTORCHAS en pared################
###########
Torchs.SetUsable("lamp1",3,3,-1)
Torchs.SetUsable("antp1",3,3,-1)
Torchs.SetUsable("antp2",3,3,-1)
Torchs.SetUsable("antp3",3,3,-1)

Torchs.SetUsable("antp5",3,3,-1)
Torchs.SetUsable("antp6",3,3,-1)
Torchs.SetUsable("antp7",3,3,-1)
Torchs.SetUsable("antp8",3,3,-1)
Torchs.SetUsable("antp9",3,3,-1)
Torchs.SetUsable("antp10",3,3,-1)
Torchs.SetUsable("antp11",3,3,-1)
Torchs.SetUsable("antcrip1",3,3,-1)
Torchs.SetUsable("antcrip2",3,3,-1)

Torchs.SetUsable("antpj1",3,3,-1)





#####ANTORCHAS##############
Torchs.SetUsable("ant1",3,3,100)
Torchs.SetUsable("antj21",3,3,90)
Torchs.SetUsable("antj22",3,3,-1)

#EN LA SALA DE LAS TABLILLAS
Torchs.SetUsable("antjj21",3,3,-1)
Torchs.SetUsable("antjj22",3,3,-1)
Torchs.SetUsable("antjj23",3,3,-1)

##############

Apagala2Sec = Bladex.GetSector(37936.4048732, -1015.74449635, 22526.03)
Apagala2Sec.OnEnter = Apagala2

##############

Apagala22Sec = Bladex.GetSector(45208.2002094, -2496.04455027, 29286.756)
Apagala22Sec.OnEnter = Apagala22
##############

Apagala3Sec = Bladex.GetSector(31041.3221702, -12994.13188594, 6671.867)
Apagala3Sec.OnEnter = Apagala3
###########Mesasssssssss



############## candelabros
##########################

o=Bladex.CreateEntity("cand3","Candelabro",13578.934000,-8857.134000,-33234.944000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.582745,0.582745,0.400510,-0.400510
o.FiresIntensity=[ 16 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("cand4","Candelabro",13801.043000,-8874.140000,-34443.163000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.281958,0.281958,-0.648459,0.648459
o.FiresIntensity=[ 14 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("cand6","Candelabro",15197.844000,-8868.519000,-28287.953000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.593030,0.593030,0.385118,-0.385118
o.FiresIntensity=[ 16 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("cand7","Candelabro",14202.004000,-8859.485000,-27725.894000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.698401,0.698401,0.110616,-0.110616
o.FiresIntensity=[ 21 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("cand5","Candelabro",15001.325000,-8860.234000,-29414.957000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.430459,0.430459,-0.560986,0.560986
o.FiresIntensity=[ 18 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("cand8","Candelabro",23493.731000,-8856.308000,-27660.171000)
o.Static=0
o.Scale=1.000000
o.Orientation=0.668583,0.668583,0.230211,-0.230211
o.FiresIntensity=[ 17 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("cand9","Candelabro",24252.087000,-9000.192000,-28455.354000)
o.Static=0
o.Scale=1.138093
o.Orientation=0.230211,0.230211,-0.668583,0.668583
o.FiresIntensity=[ 20 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]


o=Bladex.CreateEntity("cand10","Candelabro",24881.392000,-9187.617000,-27674.714000)
o.Static=0
o.Scale=1.295256
o.Orientation=0.395409,0.395409,0.586218,-0.586218
o.FiresIntensity=[ 14 ]
o.Lights=[ (0.000000,0.031250,(255,196,128)) ]

Sparks.SetMetalSparkling("cand1")
Sparks.SetMetalSparkling("cand2")
Sparks.SetMetalSparkling("cand3")
Sparks.SetMetalSparkling("cand4")
Sparks.SetMetalSparkling("cand5")
Sparks.SetMetalSparkling("cand6")
Sparks.SetMetalSparkling("cand7")
Sparks.SetMetalSparkling("cand8")
Sparks.SetMetalSparkling("cand9")
Sparks.SetMetalSparkling("cand10")



#########braseros aranya

Sparks.SetMetalSparkling("bra1")
Sparks.SetMetalSparkling("bra2")
#Sparks.SetMetalSparkling("bra3")
#Sparks.SetMetalSparkling("bra4")
