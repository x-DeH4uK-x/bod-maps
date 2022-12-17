import darfuncs
import AuxFuncs
import Sounds
import GameText
import OnInitTake
import Scorer

libro2 = Bladex.CreateEntity("LibroFin2","Libroabierto2",0,0,0)
#libro2.Static = 0


libro1 = Bladex.CreateEntity("LibroFin1","LibroPulsador",-276333.5,-27630,58503.797)
libro1.Orientation=0.500000,0.500000,0.500000,-0.500000
libro1.UseFunc = UseMagicBook

darfuncs.SetHint(libro1,"Chronicles of the Ancient Kingdom")

OnInitTake.AddOnInitTakeEvent("LibroFin1",TakeMagicBook)

sTakeBook=Sounds.CreateEntitySound('../../Sounds/coger-libro.wav', 'TakeBook')
sTakeBook.Volume=1.0
sTakeBook.MinDistance=10000
sTakeBook.MaxDistance=20000

sReadBook=Sounds.CreateEntitySound('../../Sounds/lee-libro.wav', 'ReadBook')
sReadBook.Volume=1.0
sReadBook.MinDistance=10000
sReadBook.MaxDistance=20000

#OnInitTake.AddOnInitTakeEvent("LibroFin1",UseMagicBook)