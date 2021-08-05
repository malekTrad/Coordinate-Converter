import utm
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import re


def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd

def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]
	
def decdeg2dms(dd):
	mnt,sec = divmod(dd*3600,60)
	deg,mnt = divmod(mnt,60)
	return deg,mnt,sec

def parse_dms(dms):
    parts = re.split('[^\d\w]+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    lng = dms2dd(parts[4], parts[5], parts[6], parts[7])

    return (lat, lng)



form = tk.Tk()
form.title("CONVERTER")
form.geometry("600x280")

tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="DEC to UTM")
tab_parent.add(tab2, text="DEGREE to UTM")
tab_parent.add(tab3, text="UTM to DEC")

# === WIDGETS FOR TAB ONE
latLabelOne = tk.Label(tab1, text="LATITUDE:")
lonLabelOne = tk.Label(tab1, text="LONGITUDE:")
utmLabelOne = tk.Label(tab1, text="UTM:")

latTabOne = tk.Entry(tab1)
lonTabOne = tk.Entry(tab1)
utmTabOne = tk.Entry(tab1, width="50")

def show_utm():
    lat = latTabOne.get()
    lon = lonTabOne.get()
    utmTabOne.insert(1,utm.from_latlon(float(lat), float(lon)))

def clearAllOne():
	latTabOne.delete(0, tk.END)
	lonTabOne.delete(0, tk.END)
	utmTabOne.delete(0, tk.END)

def clear_entry(event, entry):
    entry.delete(0, tk.END)

# latTabOne.insert(0,"LAT")
# latTabOne.bind("<Button-1>", lambda event: clear_entry(event, latTabOne))

# lonTabOne.insert(0,"LON")
# lonTabOne.bind("<Button-1>", lambda event: clear_entry(event, lonTabOne))

buttonClearOne = tk.Button(tab1, text="Clear",command=clearAllOne)
buttonConvertOne = tk.Button(tab1, text="Convert", command=show_utm)


# === ADD WIDGETS TO GRID ON TAB ONE
latLabelOne.grid(row=0, column=0, padx=15, pady=15)
latTabOne.grid(row=0, column=1, padx=15, pady=15)

lonLabelOne.grid(row=1, column=0, padx=15, pady=15)
lonTabOne.grid(row=1, column=1, padx=15, pady=15)

utmLabelOne.grid(row=2, column=0, padx=15, pady=15)
utmTabOne.grid(row=2, column=1,columnspan=3, padx=15, pady=15)

buttonClearOne.grid(row=4, column=1, padx=15, pady=15)
buttonConvertOne.grid(row=4, column=2, padx=15, pady=15)

# === WIDGETS FOR TAB TWO
latDegLabTab = tk.Label(tab2, text="LATITUDE DEGREE:")
lonDegLabTab = tk.Label(tab2, text="LONGITUDE DEGREE:")
utmLabTab = tk.Label(tab2, text="UTM:")

labDeg = tk.Label(tab2, text="Degrés")
labMin = tk.Label(tab2, text="Minutes")
labSec = tk.Label(tab2, text="Secondes")
labDir = tk.Label(tab2, text="Direction")
labRes = tk.Label(tab2, text="Decimal")


latTabDeg = tk.Entry(tab2,width="5")
latTabMin = tk.Entry(tab2,width="5")
latTabSec = tk.Entry(tab2,width="10")

#dropdown for Lat
tkvarLat = tk.StringVar()
choicesLat = { 'S','N'}
tkvarLat.set('N') # set the default option
popupMenuLat = tk.OptionMenu(tab2, tkvarLat, *choicesLat)

ddLatTab=tk.Entry(tab2,width="10")

lonTabDeg = tk.Entry(tab2,width="5")
lonTabMin = tk.Entry(tab2,width="5")
lonTabSec = tk.Entry(tab2,width="10")

#dropdown for Lon
tkvarLon = tk.StringVar()
choicesLon = { 'E','W'}
tkvarLon.set('E') # set the default option
popupMenuLon = tk.OptionMenu(tab2, tkvarLon, *choicesLon)

ddLonTab=tk.Entry(tab2,width="10")

utmTabTwo = tk.Entry(tab2,width="50")


def getLatDec():
	deg=latTabDeg.get()
	min=latTabMin.get()
	sec=latTabSec.get()
	dir=tkvarLat.get()
	degLon=lonTabDeg.get()
	minLon=lonTabMin.get()
	secLon=lonTabSec.get()
	dirLon=tkvarLon.get()
	ddLat=dms2dd(deg,min,sec,dir)
	ddLon=dms2dd(degLon,minLon,secLon,dirLon)
	ddLatTab.insert(1,round(ddLat,6))
	ddLonTab.insert(1,round(ddLon,6))
	utmTabTwo.insert(1,utm.from_latlon(float(ddLat), float(ddLon)))
	
def clearAll():
	latTabDeg.delete(0, tk.END)
	latTabMin.delete(0, tk.END)
	latTabMin.delete(0, tk.END)
	latTabSec.delete(0, tk.END)
	ddLatTab.delete(0, tk.END)
	lonTabDeg.delete(0, tk.END)
	lonTabMin.delete(0, tk.END)
	lonTabMin.delete(0, tk.END)
	lonTabSec.delete(0, tk.END)
	ddLonTab.delete(0, tk.END)
	utmTabTwo.delete(0, tk.END)
	
buttonCancel = tk.Button(tab2, text="Clear",command=clearAll)
buttonConvert = tk.Button(tab2, text="Convert",command=getLatDec)

# === ADD WIDGETS TO GRID ON TAB TWO

labDeg.grid(row=0, column=1, padx=10)
labMin.grid(row=0, column=2, padx=10)
labSec.grid(row=0, column=3, padx=10)
labDir.grid(row=0, column=4, padx=10)
labRes.grid(row=0, column=5, padx=10)

latDegLabTab.grid(row=1, column=0, padx=15, pady=15)
latTabDeg.grid(row=1, column=1, padx=15, pady=15)
latTabMin.grid(row=1, column=2, padx=15, pady=15)
latTabSec.grid(row=1, column=3, padx=15, pady=15)
popupMenuLat.grid(row=1, column=4, padx=15, pady=15)
ddLatTab.grid(row=1, column=5, padx=15, pady=15)

lonDegLabTab.grid(row=2, column=0, padx=15, pady=15)
lonTabDeg.grid(row=2, column=1, padx=15, pady=15)
lonTabMin.grid(row=2, column=2, padx=15, pady=15)
lonTabSec.grid(row=2, column=3, padx=15, pady=15)
popupMenuLon.grid(row=2, column=4, padx=15, pady=15)
ddLonTab.grid(row=2, column=5, padx=15, pady=15)


utmLabTab.grid(row=3, column=0, padx=15, pady=15)
utmTabTwo.grid(row=3, column = 1,columnspan = 5, padx=15, pady=15)

buttonCancel.grid(row=5, column=1, padx=15, pady=15)
buttonConvert.grid(row=5, column=2, padx=15, pady=15)

# === WIDGETS FOR TAB 3
latDegLabTab3 = tk.Label(tab3, text="UTM:")
latLabTab3 = tk.Label(tab3, text="Decimal")
lonLabTab3 = tk.Label(tab3, text="Degree")


labEsting = tk.Label(tab3, text="Easting")
labNorthing = tk.Label(tab3, text="Northing")
labZoneNum = tk.Label(tab3, text="Zone Number")
labZoneLet = tk.Label(tab3, text="Zone Lettre")

labDecimal = tk.Label(tab3, text="LATITUDE")
labDegree = tk.Label(tab3, text="LONGITUDE")

labDeg3 = tk.Label(tab3, text="Deg")
labMin3 = tk.Label(tab3, text="Min")
labsec3 = tk.Label(tab3, text="Sec")

TabEasting = tk.Entry(tab3,width="10")
TabNorthing = tk.Entry(tab3,width="10")
TabZoneNum = tk.Entry(tab3,width="5")
TabZoneLet = tk.Entry(tab3,width="5")
TabLatDecimal = tk.Entry(tab3,width="15")
TabLonDecimal = tk.Entry(tab3,width="15")
TabLatDegree = tk.Entry(tab3,width="15")
TabLonDegree = tk.Entry(tab3,width="15")


def show_latLon():
	easting = TabEasting.get()
	northing = TabNorthing.get()
	zoneNum = TabZoneNum.get()
	zoneLetter = TabZoneLet.get()
	out=utm.to_latlon(float(easting), float(northing), float(zoneNum), zoneLetter)
	result=re.sub('[() ]','', str(out))
	resultF=re.split('[,]', result)
	print()
	TabLatDecimal.insert(1,round(float(resultF[0]),6))
	TabLonDecimal.insert(1,round(float(resultF[1]),6))
	latDegree=decdeg2dms(float(round(float(resultF[0]),6)))
	lonDegree=decdeg2dms(float(round(float(resultF[1]),6)))
	resultLat=re.sub('[() ]','', str(latDegree))
	resultFLat=re.split('[,]', resultLat)
	TabLatDegree.insert(1,(resultFLat[0]+'°'+resultFLat[1]+"'"+str(round(float(resultFLat[2]),4))+'"'))
	resultLon=re.sub('[() ]','', str(lonDegree))
	resultFLon=re.split('[,]', resultLon)
	TabLonDegree.insert(1,(resultFLon[0]+'°'+resultFLon[1]+"'"+str(round(float(resultFLon[2]),4))+'"'))
	
def clearAll3():
	TabEasting.delete(0, tk.END)
	TabNorthing.delete(0, tk.END)
	TabZoneNum.delete(0, tk.END)
	TabZoneLet.delete(0, tk.END)
	TabLatDecimal.delete(0, tk.END)
	TabLonDecimal.delete(0, tk.END)
	TabLatDegree.delete(0, tk.END)
	TabLonDegree.delete(0, tk.END)
	
buttonCancel = tk.Button(tab3, text="Clear",command=clearAll3)
buttonConvert = tk.Button(tab3, text="Convert",command=show_latLon)

# === ADD WIDGETS TO GRID ON TAB 3

labEsting.grid(row=0, column=1, padx=10)
labNorthing.grid(row=0, column=2, padx=10)
labZoneNum.grid(row=0, column=3, padx=10)
labZoneLet.grid(row=0, column=4, padx=10)

latDegLabTab3.grid(row=1, column=0, padx=15, pady=15)
TabEasting.grid(row=1, column=1, padx=15, pady=15)
TabNorthing.grid(row=1, column=2, padx=15, pady=15)
TabZoneNum.grid(row=1, column=3, padx=15, pady=15)
TabZoneLet.grid(row=1, column=4, padx=15, pady=15)

labDecimal.grid(row=2, column=1, padx=0.1)
labDegree.grid(row=2, column=2, padx=0.1)

latLabTab3.grid(row=3, column=0, padx=15, pady=15)
TabLatDecimal.grid(row=3, column=1, padx=15, pady=15)
TabLonDecimal.grid(row=3, column=2, padx=15, pady=15)

lonLabTab3.grid(row=4, column=0, padx=0.1)
TabLatDegree.grid(row=4, column=1, padx=0.1)
TabLonDegree.grid(row=4, column=2, padx=0.1)


buttonCancel.grid(row=5, column=2, padx=25, pady=25)
buttonConvert.grid(row=5, column=3, padx=25, pady=25)


#packing
tab_parent.pack(expand=1, fill='both')


form.mainloop()
