class Actividad:
  def __init__(self, nombre, tipo, presupuesto, gasto_real):
    self.nombre      = nombre
    self.tipo        = tipo
    self.presupuesto = presupuesto
    self.gasto_real  = gasto_real

  def esta_en_presupuesto(self):
    if self.gasto_real <= self.presupuesto:
      return True
    else:
      return False

  def mostrar_info(self):
    return {
        "nombre": self.nombre,
        "tipo": self.tipo,
        "presupuesto": round(self.presupuesto,2),
        "gasto_real": round(self.gasto_real,2),
        "esta_en_presupuesto": self.esta_en_presupuesto()
    }
