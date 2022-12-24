import darfuncs
import EnemyTypes
import PhantonFX
import LevelFuncs


expected_player_lvl_min= 9
expected_player_lvl_max= 16

lvl_control= LevelFuncs.EnemyLevelControl (expected_player_lvl_min, expected_player_lvl_max)

#skeketo magico

#1
espada=Bladex.CreateEntity("DESERTCimitarra2","Espadafilo",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(espada)

escudo=Bladex.CreateEntity("DESERTEscudo2c","Escudo7",0,0,0,"Weapon")
ItemTypes.ItemDefaultFuncs(escudo)

pers=Bladex.CreateEntity("CaballeroLlave","Dark_Knight",-24896.780, -2017.02, 16121.63)
pers.Person=1
pers.Level=lvl_control.GiveLevel(13,15)
pers.Angle=3.14000499744
pers.Alpha = 0.0
Actions.TakeObject(pers.Name,"DESERTCimitarra2")
Actions.TakeObject(pers.Name,"DESERTEscudo2c")

pers.ActionAreaMin=pow(2,0)
pers.ActionAreaMax=pow(2,1)

#Actions.TakeObject("CaballeroLlave", "llave4")

EnemyTypes.EnemyDefaultFuncs(pers)
pers.SetOnFloor()

darfuncs.HideBadGuy("CaballeroLlave")

