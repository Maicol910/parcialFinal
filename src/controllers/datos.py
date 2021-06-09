from flask import request, Flask
from flask.json import jsonify
from src import app
from src.models.productos import DatosModel

datosModel = DatosModel()

# ---------------------------- Motrar estudiantes metodo GET ---------------------------------------
@app.route('/estudiantes')
def estudiantesGet():
    estudiantes = datosModel.estudiantesGet()
    print(estudiantes)
    array = []

    for estudiante in estudiantes:
        array.append({'id':estudiante[0],'identificacion':estudiante[1],'nombre':estudiante[2],'apellido':estudiante[3],
        'celular':estudiante[4], 'correo':estudiante[5], 'semestre':estudiante[6]})
    
    if len(estudiantes) == 0:
        return jsonify ({'message':'No hay estudiantes registrados...'})
    return jsonify({'message': ' Estudiantes registrados.','estudiantes':array})

# ---------------------------- crear estudiantes metodo POST ---------------------------------------
@app.route('/estudiantes', methods=['POST'])
def estudiantesPost():
    
    identificacion = request.json['identificacion']
    nombre = request.json['nombre']
    apellido =request.json['apellido']
    celular =request.json['celular']
    correo =request.json['correo']
    semestre = request.json['semestre']

    try:
        datosModel.EstudiantesPost(identificacion, nombre, apellido, celular, correo, semestre)
    except:
        return jsonify({'message':'Error'})
    
    return jsonify ({'message':'Estudiante guardado correctamente...', 'estudiantes':{
        'identificacion' : identificacion,
        'nombre' :         nombre,
        'apellido' :       apellido,
        'celular' :        celular,
        'correo' :         correo,
        'semestre' :       semestre
    }})

# ---------------------------- Editar estudiantes metodo PUT ---------------------------------------
@app.route('/estudiantes/<id>', methods=['PUT'])
def estudiantesPut(id):

    estudiante = datosModel.estudianteGet(id)
    print(estudiante)
    
    identificacion = request.json['identificacion']
    nombre = request.json['nombre']
    apellido =request.json['apellido']
    celular =request.json['celular']
    correo =request.json['correo']
    semestre = request.json['semestre']

    if identificacion == '':
        identificacion = estudiante[1]
    if nombre == '':
        nombre = estudiante[2] 
    if apellido == '':
        apellido = estudiante[3] 
    if celular == '':
        celular = estudiante[4] 
    if correo == '':
        correo = estudiante[5] 
    if semestre == '':
        semestre = estudiante[6] 
    
    try:
        datosModel.EstudiantesPut(id,identificacion, nombre, apellido, celular, correo, semestre)
    except:
        return jsonify({'message':'Error'})

    return jsonify({'message':'Estudiante editado correctamente ...', 'estudiante':{
            'identificacion' : identificacion,
            'nombre' :         nombre,
            'apellido' :       apellido,
            'celular' :        celular,
            'correo' :         correo,
            'semestre' :       semestre
        }})
# ---------------------------- Eliminar estudiantes metodo DELETE ---------------------------------------
@app.route('/estudiantes/<id>', methods=['DELETE'])
def estudiantesDelete(id):
    datosModel.EstudiantesDelete(id)
    return jsonify({'message':'Estudiante eliminado correctamente...'})

#-------------------------------------------------------------------------------------------------------------------------------------------    
# ---------------------------- Motrar materias metodo GET ---------------------------------------
@app.route('/materias')
def materiasGet():
    materias = datosModel.materiasGet()
    print(materias)
    arrayMat = []

    for materia in materias:
        arrayMat.append({'id':materia[0],'nombre':materia[1],'semestre':materia[2]})
    
    if len(materias) == 0:
        return jsonify ({'message':'No hay materias registradas...'})
    return jsonify({'message': ' Materias registradas.','Materias':arrayMat})

# ---------------------------- crear materias metodo POST ---------------------------------------
@app.route('/materias', methods=['POST'])
def materiasPost():
    nombre = request.json['nombre']
    semestre = request.json['semestre']

    try:
        datosModel.materiasPost(nombre, semestre)
    except:
        return jsonify({'message':'Error'})
    
    return jsonify ({'message':'Materia guardada correctamente...', 'Materia':{
        'nombre' :    nombre,
        'semestre' :  semestre
    }})

#-------------------------------------------------------------------------------------------------------------------------------------------    
# ---------------------------- Asignar materia metodo POST ---------------------------------------
@app.route('/asignar', methods=['POST'])
def asignarMat():
    materia_id = request.json['materia_id']
    estudiante_id = request.json['estudiante_id']

    try:
        datosModel.llenarEstu_mat(materia_id, estudiante_id)
    except:
        return jsonify({'message':'Error'})
    
    return jsonify ({'message':'Materia asignada correctamente...', 'Materia - Estudiante':{
        'materia_id' :    materia_id,
        'estudiante_id' : estudiante_id
    }})

#-------------------------------------------------------------------------------------------------------------------------------------------    
# ---------------------------- Motrar sesiones metodo GET ---------------------------------------
@app.route('/sesiones')
def sesionesGet():
    sesion = datosModel.sesionesGet()
    print(sesion)
    arraySesi = []

    for sesiones in sesion:
        arraySesi.append({'id':sesiones[0],'materia_id':sesiones[1],'fecha':sesiones[2],'hora_inicio':sesiones[3],'hora_final':sesiones[4]})
    
    if len(sesion) == 0:
        return jsonify ({'message':'No hay sesiones registradas...'})
    return jsonify({'message': ' Sesiones registradas.','Sesiones':arraySesi})

# ---------------------------- Crear sesiones metodo POST ---------------------------------------
@app.route('/sesiones', methods=['POST'])
def sesionesPOST():
    materia_id = request.json['materia_id']
    fecha = request.json['fecha']
    hora_inicio = request.json['hora_inicio']
    hora_final = request.json['hora_final']

    try:
        datosModel.sesionesPost(materia_id, fecha, hora_inicio, hora_final)
    except:
        return jsonify({'message':'Error'})
    
    return jsonify ({'message':'Sesion guardada correctamente...', 'Sesiones':{
        'materia_id' :    materia_id,
        'fecha' :         fecha,
        'hora_inicio' :   hora_inicio,
        'hora_final' :    hora_final
    }})

#-------------------------------------------------------------------------------------------------------------------------------------------    
# ---------------------------- Motrar asistencias metodo GET ---------------------------------------
@app.route('/asistencia')
def asistenciaGet():
    asistencia = datosModel.asistenciaGet()
    print(asistencia)
    arrayAsis = []

    for aistencias in asistencia:
        arrayAsis.append({'Nombre':aistencias[0],'Fecha de sesion':aistencias[1],
        'Hora inicio':aistencias[2],'Hora final':aistencias[3],'Materia':aistencias[4],'Asistencia':aistencias[5]})
    
    if len(asistencia) == 0:
        return jsonify ({'message':'No hay asistencias registradas...'})
    return jsonify({'message': ' Asistencias registradas.','Asistencias':arrayAsis})

# ---------------------------- Crear asistencias metodo POST ---------------------------------------
@app.route('/asistencia', methods=['POST'])
def asistenciaPOST():
    sesion_id = request.json['sesion_id']
    estudiante_id = request.json['estudiante_id']
    asistencia = request.json['asistencia']

    try:
        datosModel.asistenciaPost(sesion_id, estudiante_id, asistencia)
    except:
        return jsonify({'message':'Error'})
    
    return jsonify ({'message':'Asistencia guardada correctamente...', 'Asistencia':{
        'sesion_id' :     sesion_id,
        'estudiante_id' : estudiante_id,
        'asistencia' :    asistencia
    }})