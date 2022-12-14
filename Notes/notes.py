import conection as conection

connect = conection.connect()



class Note:
    def __init__(self,Id="", Nombre="", AM="", AP="", RFC="", Sueldo="",Sexo="", Materias="", TelC="", 
                    TelCasa="", Pasatiempos="", NombreCreador="", TesisAM="", TesisNombre=""):
        self.Id = Id
        self.Nombre = Nombre
        self.AP = AP
        self.AM = AM
        self.AP = AP
        self.RFC = RFC
        self.Sueldo = Sueldo
        self.Sexo = Sexo
        self.Materias = Materias
        self.TelC = TelC
        self.TelCasa = TelCasa
        self.Pasatiempos = Pasatiempos
        self.NombreCreador = NombreCreador
        self.TesisAM = TesisAM
        self.TesisNombre = TesisNombre
        
    def save(self):

        x = connect.find().sort('_id', -1)[0]

        x = int(x['_id'])+1

        x = str(x)

        # db.micoleccion.find().sort({$natural:-1}).limit(1);
        mydict ={
                    "_id": x,
                    "Nombre": {
                        "pila": self.Nombre,
                        "AP": self.AP,
                        "AM": self.AM
                    },
                    "RFC": self.RFC,
                    "Sueldo": self.Sueldo,
                    "Sexo": self.Sexo,
                    "Materias": self.Materias,
                    "Telefonos": {
                        "celular": self.TelC,
                        "casa": self.TelCasa
                    },
                    "Pasatiempos": self.Pasatiempos,
                    "Tesistas": {
                        "nombre": {
                            "pila": self.NombreCreador,
                            "AP": self.TesisAM
                        },
                        "Tesis": self.TesisNombre
                    }
                }

        
        print(mydict)
        # # sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        #note = (self.Nombre, self.AP, self.AM)

        connect.insert_one(mydict)

    def show(self):
        # print("hola")
        result = connect.find()
        # sql = f"SELECT * FROM notas WHERE usuario_id ={self.usuario_id}"

        # cursor.execute(sql)
        # database.commit()

        # result = cursor.fetchall()
        return result
    
    def showNameSelector(self,NombreGet):
        result = connect.find({"Nombre.pila":f"{NombreGet}"})
        # print(f"Nombre.pila:{NombreGet}")
        return result

    def showMatterSelector(self,MateriaGet):
        
        result = connect.find({"Materias":f"{MateriaGet}"})
        # print(f"Nombre.pila:{NombreGet}")
        return result

    def showSalarySelector(self):
        sueldoM=0
        sueldoF=0
        for x in connect.find({"Sexo":"M"}):
            
            sueldoM = int(x["Sueldo"])+sueldoM
        # print(sueldoM)
        vM=sueldoM
        for x in connect.find({"Sexo":"F"}):
            
            sueldoF = int(x["Sueldo"])+sueldoF
        # print(sueldoF)
        vF = sueldoF
        result = connect.find()
        # print(result)
        return result, vF, vM

    def showIdSelector(self,idGet):
        result = connect.find_one({"_id":f"{idGet}"})
        return result

    def delete(self,idGet):
        result = connect.delete_one({"_id":f"{idGet}"})
        #print(f"_id{idGet}")
        return result

    def update(self):
        myquery = {"_id":self.Id}
        newvalues = {"$set":{"Nombre": {
                                "pila": self.Nombre,
                                "AP": self.AP,
                                "AM": self.AM
                            },
                            "RFC": self.RFC,
                            "Sueldo": self.Sueldo,
                            "Sexo": self.Sexo,
                            "Materias": self.Materias,
                            "Telefonos": {
                                "celular": self.TelC,
                                "casa": self.TelCasa
                            },
                            "Pasatiempos": self.Pasatiempos,
                            "Tesistas": {
                                "nombre": {
                                    "pila": self.NombreCreador,
                                    "AP": self.TesisAM
                                },
                                "Tesis": self.TesisNombre
                            }}}
        result = connect.update_one(myquery,newvalues)
        return result