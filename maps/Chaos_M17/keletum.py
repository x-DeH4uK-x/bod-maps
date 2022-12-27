import Bladex
import Enm_Gen
import ReadGSFile
import B3DLib



######################
#     Particulas     #
######################

Bladex.AddParticleGType("Tierra2","SmokeParticle",B_PARTICLE_GTYPE_BLEND,64)

for i in range(64):
	aux=(64.0-i)/64.0
	r=0
	g=0
	b=0
	a=255.0*(1.0-aux)**0.5
	size=80.0+aux*400.0
	Bladex.SetParticleGVal("Tierra2",i,r,g,b,a,size)


Bladex.AddParticleGType("Tierra3","GenericParticle",B_PARTICLE_GTYPE_BLEND,60)

for i in range(60):
	aux=(60-i)/60
	r=0
	g=0
	b=0
	a=255*(1.0-aux/2.0)
	size=60.0*(1.0-aux)
	Bladex.SetParticleGVal("Tierra3",i,r,g,b,a,size)


Rres = ReadGSFile.ReadGhostSectorFile("esqueletos.sf")

for igs in Rres:
   Bladex.AddTriggerSector(igs["Name"],igs["Grupo"],igs["FloorHeight"],igs["RoofHeight"],igs["Vertex"])

	
#######################
#     Generadores     #
#######################

generador1=Enm_Gen.CreateEnemiesGenerator(284106, 43900, -545, "generador1", 2, ("Gen1Skl", "Skeleton", "Hacha3", 0, "Escudo1", 1, 20), "Skl_appears1")
generador1.InitGenFunc=SaltaTierraGen
generador1.InitGenArgs=(generador1,)
generador1.Activate()

generador2=Enm_Gen.CreateEnemiesGenerator(282043, 43900, 5062, "generador2", 2, ("Gen2Skl", "Skeleton", "Hacha3", 0, "Escudo1", 1, 20), "Skl_appears1")
generador2.InitGenFunc=SaltaTierraGen
generador2.InitGenArgs=(generador2,)
generador2.Activate()

generador3=Enm_Gen.CreateEnemiesGenerator(284682, 44900, 17808, "generador3", 2, ("Gen3Skl", "Skeleton", "Hacha3", 0, "Escudo1", 1, 20), "Skl_appears1")
generador3.InitGenFunc=SaltaTierraGen
generador3.InitGenArgs=(generador3,)
generador3.Activate()

generador4=Enm_Gen.CreateEnemiesGenerator(284180, 45900, 26001, "generador4", 2, ("Gen4Skl", "Skeleton", "Hacha3", 0, "Escudo1", 1, 20), "Skl_appears1")
generador4.InitGenFunc=SaltaTierraGen
generador4.InitGenArgs=(generador4,)
generador4.Activate()

generador5=Enm_Gen.CreateEnemiesGenerator(301657, 45900, 32707, "generador5", 2, ("Gen5Skl", "Skeleton", "Hacha3", 0, "Escudo1", 1, 20), "Skl_appears1")
generador5.InitGenFunc=SaltaTierraGen
generador5.InitGenArgs=(generador5,)
generador5.Activate()




generador6=Enm_Gen.CreateEnemiesGenerator(306000, 40900, -44000, "generador6", 2, ("Gen6Skl", "Skeleton", "Hacha3", 0, "Escudo1", 1, 20), "Skl_appears1")
generador6.InitGenFunc=SaltaTierraGen
generador6.InitGenArgs=(generador6,)
generador6.Activate()


generador7=Enm_Gen.CreateEnemiesGenerator(308000, 40900, -36000, "generador7", 2, ("Gen7Skl", "Skeleton", "Hacha3", 0, "Escudo1", 1, 20), "Skl_appears1")
generador7.InitGenFunc=SaltaTierraGen
generador7.InitGenArgs=(generador7,)
generador7.Activate()


generador8=Enm_Gen.CreateEnemiesGenerator(320000, 40900, -32000, "generador8", 2, ("Gen8Skl", "Skeleton", "Hacha3", 0, "Escudo1", 1, 20), "Skl_appears1")
generador8.InitGenFunc=SaltaTierraGen
generador8.InitGenArgs=(generador8,)
generador8.Activate()


char = Bladex.GetEntity("Player1")
char.SendTriggerSectorMsgs = 1
