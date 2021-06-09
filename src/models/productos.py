#---------------------------------------
# Integrantes:
# Maicol Jossa Campaña
# Henry David Rosero
#---------------------------------------

from src.config.db import DB

class DatosModel():
    #------------------------------------------ mostrar estudiantes -----------------------------------
    def estudiantesGet(self):
        cursor = DB.cursor()
        cursor.execute('select * from estudiantes')
        estudiantes = cursor.fetchall()
        cursor.close()
        return estudiantes
    
    def estudianteGet(self,id):
        cursor = DB.cursor()
        cursor.execute('select * from estudiantes where id = ?', (id,))
        estudiante = cursor.fetchone()
        cursor.close()
        return estudiante

    #------------------------------------------ crear estudiantes  -----------------------------------
    def EstudiantesPost(self, identificacion, nombre, apellido, celular, correo, semestre):
        cursor = DB.cursor()
        cursor.execute('insert into estudiantes(identificacion, nombre, apellido, celular, correo, semestre) values(?,?,?,?,?,?)', 
        (identificacion, nombre, apellido, celular, correo, semestre,))
        cursor.close()
    #------------------------------------------ editar estudiantes  -----------------------------------
    def EstudiantesPut(self, id, identificacion, nombre, apellido, celular, correo, semestre):
        cursor = DB.cursor()
        cursor.execute('update estudiantes set identificacion = ?, nombre = ?, apellido = ?, celular = ?, correo = ?, semestre = ? where id = ?',
        (identificacion, nombre, apellido, celular, correo, semestre, id,))
        cursor.close()
    #------------------------------------------ eliminar estudiantes  -----------------------------------
    def EstudiantesDelete(self, id):
        cursor = DB.cursor()
        cursor.execute('delete from estudiantes where id = ?', (id,))
        cursor.close()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------ mostrar materias -----------------------------------
    def materiasGet(self):
        cursor = DB.cursor()
        cursor.execute('select * from materias')
        materias = cursor.fetchall()
        cursor.close()
        return materias
    
    def materiaGet(self,id):
        cursor = DB.cursor()
        cursor.execute('select * from materias where id = ?', (id,))
        estudiante = cursor.fetchone()
        cursor.close()
        return estudiante

    #------------------------------------------ crear materias  -----------------------------------
    def materiasPost(self, nombre, semestre):
        cursor = DB.cursor()
        cursor.execute('insert into materias(nombre, semestre) values(?,?)',(nombre, semestre,))
        cursor.close()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------ asignar materia -----------------------------------
    def llenarEstu_mat(self, materia_id, estudiante_id):
        cursor = DB.cursor()
        cursor.execute('insert into estudiate_materia(materia_id, estudiante_id) values(?,?)', (materia_id, estudiante_id,))
        cursor.close()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------ mostrar sesion -----------------------------------
    def sesionesGet(self):
        cursor = DB.cursor()
        cursor.execute('select * from sesiones')
        sesion = cursor.fetchall()
        cursor.close()
        return sesion
    #------------------------------------------ Crear sesion -----------------------------------
    def sesionesPost(self, materia_id, fecha, hora_inicio, hora_final):
        cursor = DB.cursor()
        cursor.execute('insert into sesiones(materia_id, fecha, hora_inicio, hora_final) values(?,?,?,?)', (materia_id, fecha, hora_inicio, hora_final,))
        cursor.close()
    #-----------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------ mostrar asistencia -----------------------------------
    def asistenciaGet(self):
        cursor = DB.cursor()
        cursor.execute('SELECT estudiantes.nombre,sesiones.fecha, sesiones.hora_inicio, sesiones.hora_final, materias.nombre AS Materia, asistencia.asistencia FROM asistencia INNER JOIN sesiones ON asistencia.sesion_id = sesiones.id INNER JOIN estudiantes ON asistencia.estudiante_id = estudiantes.id INNER JOIN materias ON sesiones.materia_id = materias.id')
        asistencia = cursor.fetchall()
        cursor.close()
        return asistencia
        print(asis)
    #------------------------------------------ Crear asistencia -----------------------------------
    def asistenciaPost(self, sesion_id, estudiante_id, asistencia):
        cursor = DB.cursor()
        cursor.execute('insert into asistencia(sesion_id, estudiante_id, asistencia) values(?,?,?)', (sesion_id, estudiante_id, asistencia,))
        cursor.close()