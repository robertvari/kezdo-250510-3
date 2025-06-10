## Osztályok definiálása
A python nyelvben az osztályokat a class paranccsal definiáljuk és a függvényekkel ellentétben az osztályok nevei mindig nagybetűvel kezdődnek. A legegyszerűbb forma:
```python
class MyClass:
    pass
```

## Attribútumok
Az osztályokban felírhatunk változókat úgy mint a függvényekben. Ezeket a változók egy osztályon belül attribútumoknak nevezzük.

```python
 class MyClass:
    	name="robert"
```

A fenti példában létrehoztam egy name attribútumot melyet kívülről is elérek ha az osztályt példányosítottam. 

## A példány
Az osztályok hívása eltér a függvényekétől. Ebben az esetben már nem beszélünk hívásról, hiszen egy osztály nem hajt végre feladatokat abban a pillanatban mikor meghívjuk. Ebben az esetben példányosításról beszélünk. Egy osztályban lévő attribútumokat és függvényeket (amiket itt már metódusoknak hívunk) csak a példány létrehozása után érhetünk el:

```python
class MyClass:
    name = "Robert"
```

c = MyClass() # egy példány a MyClass osztályból
print(c.name)


## Access Levels
Egy osztályban definiált attribútum minden esetben “public”. Ez annyit jelent, hogy az attribútum értéke kintről printelhető és meg is tudod változtatni ha akarod:

```python
c.name = "Zoltan"
print(c.name)
```

Ez a szabadság viszont veszélyekkel is jár. Gondolj arra, hogy mi történhet ha egy korábban string attributum egyszercsak int lesz… Annak érdekében hogy egy belső attribútumot elrejtsünk kétféle módszer létezik. Az első módszer csak egy egyszerű változtatás az attribútum nevében. Ettől persze ugyanúgy elérhető kivülről de jeleztük, hogy ezt az attribútumot az osztály belsőleg használja és nem kéne hozzányúlni. 

```python
class MyClass:
    name = "Robert"
    _myProtectedName = "Csaba"
```

A `_myProtectedName` kapott egy aláhúzást a név előtt. Ezzel jelöltük, hogy ez a név protected hozzáférési szinten van és belső használatra lett létrehozva.

A következő használatával tényleg elrejthető egy az osztályban definiált attribútum. Ilyenkor használjuk a két aláhúzást a név előtt:

```python
class MyClass:
    name = "Robert"
    _myProtectedName = "Csaba"
    __my_private_name = "Csilla"
```

Ha megpróbálod printelni a `_my_private_name` attribútomot akkor ezt kapod:
```python
c = MyClass()
print(c._my_private_name)
>>> AttributeError: 'MyClass' object has no attribute '_my_private_name'
```

A python nyelvben nincsenek privát attribútumok. Ez a nyelv sajátossága. A fenti példában mégis elértük, hogy egy attribútum eltűnt kivülről. Ha egy attribútum előtt két aláhúzás van, a Python átnevezi ezt az attribútumot és hozzácsapja az osztály nevét is. Ha ezt tudod akkor meg is találod így:
```python
print(c._MyClass_my_private_name)
```

## Metódusok
Metódusról akkor beszélünk ha egy függvény egy osztályon belül van definiálva és megkapja a speciális `self` paramétert. Ezek a metódusok elérhetők az osztály példányosítása után:

```python
class MyClass:
    def my_function(self):
        print("Hello there!")

c = MyClass()
c.my_function()
```

A `self` paraméter minden osztályban írt függvény első paramétere. Ez a paraméter lényegében az osztályra mutató hivatkozás amely a példányosítás után kap értéket. Segítségével a függvény belsejéből elérjük az osztályban definiált többi metódust és attribútumot:

```python
class MyClass:
    def my_function(self):
        print("Hello there!")

    def call_my_function(self):
        self.my_function()

c = MyClass()
c.call_my_function()
```

Gondolj úgy a `self`-re mint egy belső hivatkozás rendszerre.

Az osztály metódusain belül már kétféleképpen definiálhatunk változót. Ha nem írjuk ki a `self` prefixet, akkor az a változó csak a metóduson belül használható és nem lesz az osztály attribútuma. Az alábbi példa bemutatja az osztály attribútum és a lokális változó felírását:
```python
class MyClass:
    def my_function(self):
        self.class_attributum = "Hello"
        local_variable = "This can be used only in my_function()"
```

## A constructor
Az osztályon belül van néhány speciális metódus melyek közül a leggyakoribb a konstruktor metódus `__init__()`:
```python
class MyClass:
    def __init__(self):
        print("My Class inited!")

c = MyClass()
```

Ha egy osztályban definiálsz egy konstruktort, annak tartalma azonnal lefut a példányosításnál. Ezt láthatod is ha kipróbálod a fenti kódrészletet. A konstruktor szerepe az, hogy a példásnyosításnál létrehozzunk attributumokat és segítségével be is kérhetsz adatokat pont úgy ahogy azt a függvényeknél tanultuk. A konstruktor paraméterein keresztül:

```python
class MyClass:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

c = MyClass("Robert", "Budapest", 42)
print(c.name)
print(c.address)
print(c.age)
```

Ha létezik egy konstruktor melynek paraméterei vannak, akkor az osztályt már nem lehet példányosítani ezen paraméterek megadása nélkül. Természetesen itt is felírhatsz default paramétereket pont úgy mint a függvényeknél. A konstruktort használhatod belső metódusok elindítására vagy más osztályok példányosítására is:

```python
class MyClass:
    def __init__(self):
        other = My_Other_Class()

class My_Other_Class:
    def __init__(self):
        print("I'm the other one!")

c = MyClass()
```

## class reprezentációk
Vannak egyéb speciális metódusok amiket szintén gyakran fogsz használni és érdemes róluk ejteni pár szót. Az egyik ilyen a `__str__()`. Ennek abban van szerepe, hogy egy osztály példányát printelve értelmes szöveget kapjunk és ne csak érthetetlen, a fordító által visszaadott adatokat. Alaphelyzetben ezt látod:

```python
class MyClass:
    def __init__(self):
        self.name = "Robert"

c = MyClass()
print(c)
>>><__main__.MyClass object at 0x002F8630>
```

Most írjuk meg az `__str__()` metódust ahol eldönthetjük hogy nézzen ki az osztályunk printelve:

```python
class MyClass:
    def __init__(self):
        self.name = "Robert"

    def __str__(self):
        return f"Hello there! Here is what I have for you: {self.name}"

c = MyClass()
print(c)
>>>Hello there! Here is what I have for you: Robert
```

A `__repr__()` metódus is használható arra, hogy egy példány string-ként jelenjen meg pontosan úgy mint a `__str__()` a printekben, viszont akkor is reprezentálja az osztályt ha a példányok listában vannak:

```python
class Person:
    # Constructor of my class
    def __init__(self, name):
        self.name = name
    
    # You need this if you print your class in a list
    def __repr__(self):
        return self.name

kriszta = Person("Kriszta")
tamas = Person("Tamás")
csaba = Person("Csaba")
adam = Person("Ádám")

my_driends = [kriszta, tamas, csaba, adam]

print(my_driends)
>>> [Kriszta, Tamás, Csaba, Ádám]
```
## Setter és Getter metódusok
Korábban említettem, hogy az osztályok attribútumai elég könnyen elérhetők és kívülről átírhatók. Ez azt a veszélyt vonja maga után, hogy egy attribútum értéke a program futása közben olyan értéket kap amit a belső metódusok nem tudnak kezelni. Pl. Egy attributum korábban `str` típusról átvált `int` típusra. Már van annyi tapasztalatod hogy tudd, ez nem túl szerencsés.
Ilyen helyzetek elkerülésére használjuk az ún. `setter` és `getter` metódusokat. Az attribútumok értékeit ezeken keresztül állítjuk át és kérdezzük le. Így lehetőségünk van vizsgálni a bejövő új adatot és csak akkor írjuk át az attribútumot ha az megfelel az elvárásainknak. Lássunk egy egyszerű példát:

```python
class MyClass:
    def __init__(self):
        self.__name = "Robert"

    def set_name(self, name):
        assert isinstance(name, str), "Name must be a type of string."
        self.__name = name

c = MyClass()
c.set_name(10)
>>> AssertionError: Name must be a type of string.
```

Láthatod, hogy megpróbáltam egy int értéket adni a name attributumnak a `set_name()` metóduson keresztül. Ebben a függvényben viszont ellenőriztük a bejövő paramétert és mivel az nem felelt meg a típusnak dobtunk egy `assert` hibát. Egy `setter` metódus csak annyiban tér el bármely más metódustól, hogy a neve a `set_` prefixel kezdődik. 

A `getter` metódus ugyanezen az elven működik csak visszafelé. Ha kérsz egy paramétert és az még nincs set-elve akkor visszaad neked egy olyan típust amilyen a paraméter lesz. Erre a legjobb példa egy még nem létező string lekérdezése:

```python
class MyClass:
    def __init__(self):
        self.__name = None

    def get_names(self):
        if self.__name:
            return self.__name
        return ""
```

Láthatod hogy a name a konstruktorban None-al jött létre, viszont ez az érték hibát dobna ha iterálni akarsz ezen az attributumon. Éppen ezért létezik a get_names() metódus. Ezen keresztül akkor is egy string-et kapunk ha ez az attributum még nem áll készen.

## A property
A `setter` és `getter` metódusok előnyeit már megismerted, de használatuk körülményes lehet. Itt jön a képbe a `@property`. Ennek használatával a kérdéses attributumok már nem is érhetők el máshogy, csak a mi metódusainkon keresztül. Lássunk egy egyszerű példát a `fullname` attributum átírására, majd lekérésére a property segítségével:

```python
class MyClass:
    def __init__(self):
        self.__first_name = None
        self.__last_name = None
 
    @property
    def fullname(self):
        return f'{self.__first_name} {self.__last_name}'
 
    @fullname.setter
    def fullname(self, fullname):
        self.__first_name, self.__last_name = fullname.split()

c = MyClass()
c.fullname = 'Vari Robert'
print(c.fullname)
```

A fenti példában megfigyelheted, hogy a `fullname` egy class metódus de kintről attribútumként használod. Ha szeretnénk látni a `fullname` értékét akkor egyszerűen c.fullname amely a `@property` dekorátornak köszönhetően rögtön a mi metódusunkat hívja meg és visszaadja a teljes nevet.
Ennek megfelelően a `c.fullname = ‘Your Name’` a `@fullname.setter` metódusát fogja indítani és átadja a beírt nevet. Így maximálisan kontolláljuk hogyan lesznek beállítva a `__first_name` és `__last_name` attribútumok. 

## Örökítés
Az osztályok örökítése az a folyamat amikor egy ősosztály attribútumait és metódusait szeretnénk tovább örökíteni más osztályokba. Ezt akkor használjuk, ha olyan új osztályt szeretnénk létrehozni, ami nagyban hasonlít az ős osztályhoz, viszont kisebb dolgokban különbözik tőle. Ez a módszer nagyon hatékonnyá teszi az új funkciók fejlesztését és a hibák javítását is, hiszen minden az ős osztályban végrehajtott módosítás automatikusan öröklődik a child osztályokba. A következőkben bemutatom az örökítést egy életszerű példán keresztül:

```python
class Vehicle:
    def __init__(self, type, max_speed, color):
        self.type = type
        self.max_speed = max_speed
        self.color = color

    def get_max_speed(self):
        return self.max_speed

class Car(Vehicle):
    pass

c = Car("BMW", 180, "red")
print( c.get_max_speed() )
>>>180
```
A fenti példa szemlélteti hogyan írtam fel egy Vehicle ős osztályt. Ott létrehoztam néhány attribútumot ami egy járműre jellemző. Figyeld meg, hogy kapja meg a Car osztály a Vehicle osztályt. Ezek után már meghívhatom a get_max_speed() metódust amit az ős osztályban definiáltam. Láthatod hogy örökölte az attribútumokat és a metódust a Car.
Ez a mechanizmus lehetővé teszi számunkra, hogy egy helyen írjuk meg a szükséges attribútumokat és függvényeket melyeket más osztályok átvehetnek és ezeken keresztül használnak. Ha javítani és fejleszteni kell a kódon akkor elegendő az ős osztályban dolgoznunk. Minden változtatás öröklődik az alosztályokba is. 

## super()
Az örökítés után lehetőséged van arra hogy a gyermek osztályban teljesen, vagy részlegesen felülírd az ős metódusait. Itt használjuk a `supert()`-t. 

```python
class Vehicle:
    def __init__(self, speed, weight, name):
        self.speed = speed
        self.weight = weight
        self.name = name

class Car(Vehicle):
    # override parent class __init__
    def __init__(self, speed, weight, name, wheels):
        # call parent class's __init__ to fill out the base attributes
        super().__init__(speed, weight, name)
        self.wheels = wheels
```

A fenti példa azt mutatja meg, hogy a Car felülírja az ős konstrukturát és hozzáad egy új attribútumot a `wheels`-t.
Itt a `super().__init__(speed, weight, name)` feladata az, hogy az ősben lévő konstruktor is lefusson és létrehozza az eredeti attribútumokat. Ez után mi hozzáadjuk a sajátunkat. Ez a részleges felülírás (partial override).

Teljes felülírásról akkor beszélünk ha kihagyjuk a super() sort. Ebben az esetben a car saját, az őstől teljesen eltésrő konstruktort kap ahol nekünk kell létrehozni az osztály attribútumati.

```python
class Car(Vehicle):
    def __init__(self, speed, weight, name, wheels):
        ...
``` 