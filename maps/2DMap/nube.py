# Item configuration script
# Script generated by LED: May 17 1999 15:40:27
import whrandom



def MueveNube(e_name, time):
	for o in Nubes:
		o.Move(o.Data,0,0)
		if o.Position[0] < -161921.112873:
			o.Position = 133678.887127, 12742.333308, whrandom.randint(-45752,54247)
			o.Data        = whrandom.randint(-500,-50)
			o.Alpha       = whrandom.random()/0.6
			o.Scale=10.467530 - whrandom.random()*3.5
			
			
	
#  whrandom.randint(-45752.780836,54247.219164)


# Script with 1 Items.
def CreaNuve():
	o=Bladex.CreateEntity("NoName0","Nube",whrandom.randint(-45752,161921), 12742.333308, whrandom.randint(-45752,54247))
	o.Static = 1
	o.Scale=10.467530 - whrandom.random()*3.5
	o.Orientation=0.707107,0.707107,0.000000,0.000000
	o.RasterMode  ="AdditiveAlpha"
	o.RasterMode  ="Read"
	o.CastShadows = 0
	o.SelfIlum    = 1
	o.Alpha       = whrandom.random()/0.6
	o.Data        = whrandom.randint(-500,-100)
	return o

#Nubes = [CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve(),CreaNuve()]
Nubes = [CreaNuve(),CreaNuve(),CreaNuve()]
def BorraNubes():
	global Nubes
	for o in Nubes:
		o.SubscribeToList("Pin")
	Nubes = []
	

char.SubscribeToList("Timer30")
char.TimerFunc=MueveNube
